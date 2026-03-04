from picrawler import Picrawler
from time import sleep
import readchar

crawler = Picrawler()

SPEED_MIN = 20
SPEED_MAX = 70
speed = 60

STEP = 1            # Number of action steps per key press
ACTION_GAP = 0.25   # Delay after each action to reduce current spikes

manual = """
Keyboard Control - PiCrawler

Movement:
  W: Forward
  A: Turn left
  S: Backward
  D: Turn right

Speed Control:
  + / ] : Increase speed
  - / [ : Decrease speed

Other:
  Space  : Stop (no action)
  Ctrl+C : Quit (auto sit)
"""

def clamp(value, min_value, max_value):
    """Limit value within a specified range."""
    return max(min_value, min(max_value, value))

def show_info():
    """Clear terminal and display control instructions."""
    print("\033[H\033[J", end="")  # Clear terminal screen
    print(manual)
    print(f"Current speed: {speed}  (range {SPEED_MIN}-{SPEED_MAX})")
    print(f"Action gap: {ACTION_GAP:.2f}s")

def do_move(action_name):
    """Execute movement action with safety delay."""
    crawler.do_action(action_name, STEP, speed)
    sleep(ACTION_GAP)

def safe_sit():
    """Safely sit down before program exit."""
    try:
        crawler.do_step("sit", clamp(speed, 20, 40))
        sleep(1.0)
    except Exception:
        pass

def main():
    show_info()

    try:
        while True:
            key = readchar.readkey()
            k = key.lower()

            if k == "w":
                do_move("forward")
            elif k == "s":
                do_move("backward")
            elif k == "a":
                do_move("turn left")
            elif k == "d":
                do_move("turn right")

            # Speed increase
            elif k in ("+", "]"):
                global speed
                speed = clamp(speed + 5, SPEED_MIN, SPEED_MAX)

            # Speed decrease
            elif k in ("-", "["):
                speed = clamp(speed - 5, SPEED_MIN, SPEED_MAX)

            # Stop (no movement)
            elif k == " ":
                pass

            # Quit using readchar special key
            elif key == readchar.key.CTRL_C:
                print("\nQuit.")
                break

            show_info()
            sleep(0.02)

    except KeyboardInterrupt:
        print("\nQuit (KeyboardInterrupt).")

    finally:
        safe_sit()

if __name__ == "__main__":
    main()