from picrawler import Picrawler
from time import sleep

crawler = Picrawler()


def get_sit_step():
    # Get a valid sit step used as the base pose for hand actions
    try:
        return crawler.move_list['sit'][0]
    except Exception:
        return None


def handwork(speed):
    base = get_sit_step()

    # If a valid sit step cannot be retrieved, just perform a sit action
    if not base or len(base) < 4:
        crawler.do_step('sit', speed)
        sleep(0.6)
        return

    # Generate hand poses by modifying the sit step
    left_hand = crawler.mix_step(base, 0, [0, 50, 80])
    right_hand = crawler.mix_step(base, 1, [0, 50, 80])
    two_hand = crawler.mix_step(left_hand, 1, [0, 50, 80])

    crawler.do_step('sit', speed)
    sleep(0.6)

    crawler.do_step(left_hand, speed)
    sleep(0.6)

    crawler.do_step(two_hand, speed)
    sleep(0.6)

    crawler.do_step(right_hand, speed)
    sleep(0.6)

    crawler.do_step('sit', speed)
    sleep(0.6)


def twist(speed):
    # Initialize the base position for all four legs
    new_step = [[50, 50, -80], [50, 50, -80], [50, 50, -80], [50, 50, -80]]

    # Create a twisting motion by alternating rise and drop movements
    for i in range(4):
        for inc in range(30, 60, 5):
            rise = [50, 50, (-80 + inc * 0.5)]
            drop = [50, 50, (-80 - inc)]

            new_step[i] = rise
            new_step[(i + 2) % 4] = drop
            new_step[(i + 1) % 4] = rise
            new_step[(i - 1) % 4] = drop

            crawler.do_step(new_step, speed)
            sleep(0.02)


def pushup(speed):
    # Two poses used to simulate a push-up motion
    up = [[80, 0, -100], [80, 0, -100], [0, 120, -60], [0, 120, -60]]
    down = [[80, 0, -30], [80, 0, -30], [0, 120, -60], [0, 120, -60]]

    crawler.do_step(up, speed)
    sleep(0.6)

    crawler.do_step(down, speed)
    sleep(0.6)


def swimming(speed, loops=100):
    # Simulate a swimming-like motion by gradually adjusting leg coordinates
    for i in range(loops):
        crawler.do_step(
            [
                [100 - i, i, 0],
                [100 - i, i, 0],
                [0, 120, -60 + i / 5],
                [0, 100, -40 - i / 5]
            ],
            speed
        )
        sleep(0.01)


def main():
    speed = 100

    try:
        # Stand up slowly before performing actions
        crawler.do_step('stand', 40)
        sleep(1.0)

        swimming(speed)
        pushup(speed)
        handwork(speed)
        twist(speed)

    except KeyboardInterrupt:
        print("\nCtrl+C detected, exiting...")

    finally:
        # Return to a sitting posture before exiting
        try:
            crawler.do_step('sit', 40)
            sleep(1.0)
        except Exception:
            pass


if __name__ == "__main__":
    main()