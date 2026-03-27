#!/usr/bin/env python3
from picrawler import Picrawler
from time import sleep

# Create Picrawler instance
crawler = Picrawler()


def get_sit_step():
    """
    Get the first built-in sit pose.

    This pose is used as the base pose for hand gestures.
    If it cannot be read, return None.
    """
    try:
        return crawler.move_list['sit'][0]
    except Exception:
        return None


def handwork(speed=50, repeat=2):
    """
    Perform hand gestures.

    Compared with the original version, the motion range is reduced
    to avoid a large sudden jump that may cause the Pi to freeze.

    Args:
        speed: action speed
        repeat: how many times to repeat the hand gesture sequence
    """
    base = get_sit_step()

    # If no valid sit pose is available, skip this action safely
    if not base or len(base) < 4:
        return

    # Create gesture poses based on the built-in sit pose
    # Original offset was [0, 50, 80], which was too aggressive
    # Reduced to [0, 28, 45] to keep it expressive but safer
    left_hand = crawler.mix_step(base, 0, [0, 28, 45])
    right_hand = crawler.mix_step(base, 1, [0, 28, 45])
    two_hand = crawler.mix_step(left_hand, 1, [0, 28, 45])

    # Repeat the gesture sequence for better stage/show effect
    for _ in range(repeat):
        crawler.do_step(left_hand, speed)
        sleep(0.35)

        crawler.do_step(two_hand, speed)
        sleep(0.35)

        crawler.do_step(right_hand, speed)
        sleep(0.35)


def twist(speed=80, repeat=2):
    """
    Perform a body twisting motion.

    This version keeps the visual effect close to the original,
    but uses a cleaner base-step construction to avoid shared-list issues.

    Args:
        speed: action speed
        repeat: how many times to repeat the full twist sequence
    """
    # Use independent lists for each leg
    base = [[50, 50, -80] for _ in range(4)]

    for _ in range(repeat):
        for i in range(4):
            for inc in range(30, 60, 10):
                # Raise and lower part of the body to simulate twisting
                rise = [50, 50, (-80 + inc * 0.5)]
                drop = [50, 50, (-80 - inc)]

                # Copy base pose for this frame
                step = [p[:] for p in base]

                # Apply mirrored rise/drop pattern
                step[i] = rise
                step[(i + 2) % 4] = drop
                step[(i + 1) % 4] = rise
                step[(i - 1) % 4] = drop

                crawler.do_step(step, speed)
                sleep(0.04)


def pushup(speed=50, repeat=2):
    """
    Simulate a push-up motion.

    Main optimization:
    The original front-leg z movement was too large (-100 -> -30),
    which could cause a sudden load spike.
    This version reduces that range to make it safer while still visible.

    Args:
        speed: action speed
        repeat: how many push-up cycles to perform
    """
    # Reduced motion range for front legs
    up = [[80, 0, -90], [80, 0, -90], [0, 120, -60], [0, 120, -60]]
    down = [[80, 0, -50], [80, 0, -50], [0, 120, -60], [0, 120, -60]]

    for _ in range(repeat):
        crawler.do_step(up, speed)
        sleep(0.35)

        crawler.do_step(down, speed)
        sleep(0.35)


def swimming(speed=100, loops=100):
    """
    Perform a swimming-like motion.

    This action is intentionally kept fast because you confirmed
    that speed 100 looks best and is relatively stable on your setup.

    Note:
        The robot is expected to perform this motion while lying down.

    Args:
        speed: action speed
        loops: number of frames in the swimming sequence
    """
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
    """
    Main routine.

    Sequence design:
    1. Swimming once
    2. Push-up twice
    3. Handwork twice
    4. Twist twice

    Short pauses are added between actions to improve presentation rhythm,
    but the robot does not sit down between actions.
    """
    try:
        # Action 1: swimming
        swimming(100)
        sleep(0.2)

        # Action 2: push-up
        pushup(50, repeat=2)
        sleep(0.2)

        # Action 3: hand gestures
        handwork(50, repeat=2)
        sleep(0.2)

        # Action 4: twist
        twist(80, repeat=2)

    except KeyboardInterrupt:
        print("\nCtrl+C detected, exiting...")

    finally:
        # Return to sitting posture before exiting
        try:
            crawler.do_step('sit', 40)
            sleep(1.0)
        except Exception:
            pass


if __name__ == "__main__":
    main()