#!/usr/bin/env python3
from picrawler import Picrawler
from time import sleep, time
from robot_hat import Music, TTS
from vilib import Vilib
import readchar
import random
import threading

crawler = Picrawler()
music = Music()   # kept for compatibility (not used here)
tts = TTS()

MANUAL = '''
Press keys on keyboard to control Picrawler!
        w: Forward
        a: Turn left
        s: Backward
        d: Turn right
        space: Say the target again
        Ctrl+C: Quit
'''

color = "red"
color_list = ["red", "orange", "yellow", "green", "blue", "purple"]

key_dict = {
        'w': 'forward',
        's': 'backward',
        'a': 'turn_left',
        'd': 'turn_right',
}

# ----------------------------
# Thread-safe key handling
# ----------------------------
lock = threading.Lock()
key_state = None               # last key event
stop_event = threading.Event() # signal to exit cleanly

def set_key(k):
        global key_state
        with lock:
                key_state = k

def pop_key():
        """Read and clear the last key event."""
        global key_state
        with lock:
                k = key_state
                key_state = None
        return k

def key_scan_thread():
        """Keyboard input thread (quiet exit on Ctrl+C)."""
        while not stop_event.is_set():
                try:
                        k = readchar.readkey()
                except KeyboardInterrupt:
                        # Ctrl+C may raise KeyboardInterrupt inside this thread
                        stop_event.set()
                        break
                except Exception:
                        sleep(0.02)
                        continue

                if k == readchar.key.SPACE:
                        set_key('space')
                elif k == readchar.key.CTRL_C:
                        set_key('quit')
                        stop_event.set()
                        break
                else:
                        try:
                                set_key(str(k).lower())
                        except Exception:
                                pass

                sleep(0.01)

# ----------------------------
# Game logic
# ----------------------------
def renew_color_detect():
        global color
        color = random.choice(color_list)
        try:
                Vilib.color_detect(color)
        except Exception:
                pass
        try:
                tts.say("Look for " + color)
        except Exception:
                pass

def safe_camera_close():
        try:
                Vilib.color_detect("close")
        except Exception:
                pass
        try:
                Vilib.camera_close()
        except Exception:
                pass

def safe_sit():
        try:
                crawler.do_step('sit', 40)
                sleep(0.5)
        except Exception:
                pass

def main():
        speed = 70
        action = None

        # Start camera + web preview
        Vilib.camera_start(vflip=False, hflip=False)
        Vilib.display(local=False, web=True)
        sleep(0.8)

        print(MANUAL)

        # Start keyboard thread (daemon, so it won't block process exit)
        t = threading.Thread(target=key_scan_thread, daemon=True)
        t.start()

        # Announce and stand up to 40
        try:
                tts.say("game start")
        except Exception:
                pass
        sleep(0.05)

        renew_color_detect()

        try:
                while not stop_event.is_set():
                        # If target detected and large enough -> renew target
                        try:
                                n = Vilib.detect_obj_parameter.get('color_n', 0)
                                w = Vilib.detect_obj_parameter.get('color_w', 0)
                        except Exception:
                                n, w = 0, 0

                        if n != 0 and w > 100:
                                try:
                                        tts.say("well done")
                                except Exception:
                                        pass
                                sleep(0.05)
                                renew_color_detect()

                        # Handle key event
                        k = pop_key()

                        if k in key_dict:
                                action = key_dict[k]

                        elif k == 'space':
                                try:
                                        tts.say("Look for " + color)
                                except Exception:
                                        pass

                        elif k == 'quit':
                                stop_event.set()

                        # Move only after receiving a WASD action
                        if action is not None:
                                try:
                                        crawler.do_action(action, 1, speed)
                                except Exception:
                                        pass
                                action = None

                        sleep(0.05)

        except KeyboardInterrupt:
                stop_event.set()

        finally:
                # Clean exit
                stop_event.set()
                safe_camera_close()
                safe_sit()
                print("\nQuit")

if __name__ == "__main__":
        main()