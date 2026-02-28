from picrawler import Picrawler
from robot_hat import Music, Ultrasonic, Pin
import time
import signal

music = Music()
crawler = Picrawler()
sonar = Ultrasonic(Pin("D2"), Pin("D3"))  # Ultrasonic trigger/echo pins

music.music_set_volume(100)  # Set speaker volume

alert_distance = 15  # Obstacle warning distance (cm)
speed = 80           # Movement speed

# ----------------------------
# Add hardware timeout to sonar.read()
# Prevent program from freezing
# ----------------------------
class Timeout(Exception):
    pass

def _alarm_handler(signum, frame):
    raise Timeout()

signal.signal(signal.SIGALRM, _alarm_handler)

# Read distance once with timeout protection
def safe_read_once(timeout_s=1):
    try:
        signal.alarm(timeout_s)
        d = sonar.read()
        signal.alarm(0)
        return d
    except Timeout:
        signal.alarm(0)
        return None
    except Exception:
        signal.alarm(0)
        return None

# Read multiple times and return median value (anti-noise)
def read_distance_filtered(n=5, gap=0.03, timeout_s=1):
    vals = []
    for _ in range(n):
        d = safe_read_once(timeout_s=timeout_s)
        if d is not None and d > 0:
            vals.append(d)
        time.sleep(gap)

    if not vals:
        return None

    vals.sort()
    return vals[len(vals)//2]  # Median filter

def main():
    distance = read_distance_filtered(n=5, gap=0.03, timeout_s=1)
    print("distance:", distance)

    if distance is None:
        time.sleep(0.15)  # Wait if read failed
        return

    if distance <= alert_distance:
        # Obstacle detected → play sound and turn
        try:
            music.sound_play_threading('./sounds/sign.wav', volume=100)
        except Exception as e:
            print("sound error:", e)

        crawler.do_action('turn left angle', 1, speed)
        time.sleep(0.5)  # Quiet window after movement
    else:
        # Path clear → move forward
        crawler.do_action('forward', 1, speed)
        time.sleep(0.4)

if __name__ == "__main__":
    try:
        crawler.do_step('stand', 40)  # Stand before starting
        time.sleep(1.0)

        while True:
            main()

    except KeyboardInterrupt:
        print("\nStop.")
    finally:
        try:
            crawler.do_step('sit', 40)  # Sit before exit
            time.sleep(1.0)
        except Exception:
            pass