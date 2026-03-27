from picrawler import Picrawler
from time import sleep

crawler = Picrawler()

def main():
    speed = 70  # Movement speed

    try:

        while True:
            crawler.do_action('forward', 1, speed)
            sleep(0.25)

            crawler.do_action('backward', 1, speed)
            sleep(0.25)

            crawler.do_action('turn left', 1, speed)
            sleep(0.25)

            crawler.do_action('turn right', 1, speed)
            sleep(0.25)

            crawler.do_action('turn left angle', 1, speed)
            sleep(0.3)

            crawler.do_action('turn right angle', 1, speed)  # Small right turn
            sleep(1)

    except KeyboardInterrupt:
        print("\nCtrl+C pressed, sitting down...")
    finally:

        try:
            crawler.do_step('sit', 40)
            sleep(1.0)
        except Exception as e:
            print("Failed to sit:", e)

if __name__ == "__main__":
    main()