from picrawler import Picrawler
from time import sleep, time
from robot_hat import Music
from vilib import Vilib

# Create robot and audio controller objects
crawler = Picrawler()
music = Music()

def main():
    # Start camera and enable preview window
    Vilib.camera_start(vflip=False, hflip=False)
    Vilib.display(local=False, web=True)

    # Enable red color detection
    Vilib.color_detect("red")

    speed = 70                  # Movement speed
    last_seen = False           # Indicates whether the red target was detected in previous loop
    last_beep = 0               # Timestamp of last sound playback
    BEEP_COOLDOWN = 1.0         # Minimum interval between sound effects (seconds)

    # Stand once before starting tracking
    crawler.do_step('stand', 40)
    sleep(1.0)

    try:
        while True:
            # Read detection result
            if Vilib.detect_obj_parameter.get('color_n', 0) != 0:

                # Get horizontal coordinate of detected red object
                coordinate_x = Vilib.detect_obj_parameter.get('color_x', 0)

                # Play sound effect with cooldown to avoid spamming
                now = time()
                if now - last_beep >= BEEP_COOLDOWN:
                    try:
                        music.sound_play_threading('./sounds/talk1.wav')
                    except Exception:
                        pass
                    last_beep = now

                # Steering logic based on horizontal position
                # Left side of image
                if coordinate_x < 100:
                    crawler.do_action('turn left', 1, speed)

                # Right side of image
                elif coordinate_x > 220:
                    crawler.do_action('turn right', 1, speed)

                # Center area → move forward
                else:
                    crawler.do_action('forward', 2, speed)

                last_seen = True
                sleep(0.05)

            else:
                # No red target detected

                # Stop movement only once when target is lost
                # This prevents repeated stand() calls that cause "push-up" effect
                if last_seen:
                    crawler.do_step('stand', 40)
                    last_seen = False

                sleep(0.15)

    except KeyboardInterrupt:
        # Stop program safely when Ctrl+C is pressed
        print("\nStop.")

    finally:
        # Cleanup section to avoid exit errors

        # Disable color detection
        try:
            Vilib.color_detect("close")
        except Exception:
            pass

        # Close camera safely
        try:
            Vilib.camera_close()
        except Exception:
            pass

        # Make the robot sit before exit
        try:
            crawler.do_step('sit', 40)
            sleep(1.0)
        except Exception:
            pass

if __name__ == "__main__":
    main()