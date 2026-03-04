from time import sleep, strftime, localtime
from vilib import Vilib
import readchar
from os import getlogin
import os

USERNAME = getlogin()
VIDEO_PATH = f"/home/{USERNAME}/Videos/"

MANUAL = '''
Press keys on keyboard to control recording:
    Q: record/pause/continue
    E: stop
    Ctrl+C: Quit
'''

def print_overwrite(msg, end='', flush=True):
    """Overwrite the current terminal line."""
    print('\r\033[2K', end='', flush=True)
    print(msg, end=end, flush=True)

def safe_stop_recording():
    """Stop recording safely (avoid exceptions during exit)."""
    try:
        Vilib.rec_video_stop()
    except Exception:
        pass

def safe_close_camera():
    """Close camera safely (avoid exceptions during exit)."""
    try:
        Vilib.camera_close()
    except Exception:
        pass

def main():
    rec_flag = 'stop'  # Possible states: start, pause, stop
    vname = None

    # Ensure the video directory exists
    os.makedirs(VIDEO_PATH, exist_ok=True)

    # Set save path for recorded videos
    Vilib.rec_video_set["path"] = VIDEO_PATH

    # Start camera and preview
    Vilib.camera_start(vflip=False, hflip=False)
    Vilib.display(local=False, web=True)
    sleep(0.8)  # Wait for camera startup

    print(MANUAL)

    try:
        while True:
            # Read keyboard input (no Enter needed)
            key = readchar.readkey().lower()

            # Q: start / pause / continue
            if key == 'q':
                if rec_flag == 'stop':
                    rec_flag = 'start'

                    # Generate filename based on timestamp
                    vname = strftime("%Y-%m-%d-%H.%M.%S", localtime())
                    Vilib.rec_video_set["name"] = vname

                    # Start recording
                    Vilib.rec_video_run()
                    Vilib.rec_video_start()
                    print_overwrite('rec start ...')

                elif rec_flag == 'start':
                    rec_flag = 'pause'
                    Vilib.rec_video_pause()
                    print_overwrite('pause')

                elif rec_flag == 'pause':
                    rec_flag = 'start'
                    Vilib.rec_video_start()
                    print_overwrite('continue')

            # E: stop recording
            elif key == 'e' and rec_flag != 'stop':
                rec_flag = 'stop'
                safe_stop_recording()
                print_overwrite(
                    "The video saved as %s%s.avi" % (Vilib.rec_video_set["path"], vname),
                    end='\n'
                )

            # Ctrl+C (readchar special key): quit
            elif key == readchar.key.CTRL_C:
                print('\nquit')
                break

            sleep(0.1)

    except KeyboardInterrupt:
        # Handle Ctrl+C from terminal as well
        print('\nquit')

    finally:
        # If recording is still active, stop it before closing camera
        if rec_flag != 'stop':
            safe_stop_recording()
        safe_close_camera()
        sleep(0.1)

if __name__ == "__main__":
    main()