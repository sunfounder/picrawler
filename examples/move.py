from picrawler import Picrawler
from time import sleep

crawler = Picrawler()  # Create PiCrawler object

def main():
    speed = 70  # Movement speed

    try:

        while True:
            crawler.do_action('forward', 1, speed)   # Move forward
            sleep(0.25)

            crawler.do_action('backward', 1, speed)  # Move backward
            sleep(0.25)

            crawler.do_action('turn left', 1, speed)  # Turn left
            sleep(0.25)

            crawler.do_action('turn right', 1, speed)  # Turn right
            sleep(0.25)

            crawler.do_action('turn left angle', 1, speed)  # Small left turn
            sleep(0.3)

            crawler.do_action('turn right angle', 1, speed)  # Small right turn
            sleep(1)

    except KeyboardInterrupt:
        print("\nCtrl+C pressed...")

    finally:
        crawler.do_step('sit', 40)  # Sit down before exit
        sleep(1.0)

if __name__ == "__main__":
    main()