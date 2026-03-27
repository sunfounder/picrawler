#!/usr/bin/env python3
from picrawler import Picrawler
from time import sleep

# Create Picrawler instance
crawler = Picrawler()

# Leg order:
# [right front], [left front], [left rear], [right rear]
new_step = [[45, 45, -75], [45, 0, -75], [45, 0, -30], [45, 45, -75]]

# Get the default stand step from the move list
stand_step = crawler.move_list['stand'][-1]


def main():
    action_speed = 50  # Speed for movement actions

    try:

        # Continuous action loop
        while True:
            crawler.do_step(stand_step, action_speed)
            sleep(3)

            crawler.do_step(new_step, action_speed)
            sleep(3)

    except KeyboardInterrupt:
        # Handle Ctrl+C for safe exit
        print("\nExiting safely...")

    finally:
        # Return to sitting position before shutting down
        try:
            crawler.do_step('sit', 40)
            sleep(1.0)
        except Exception:
            pass


if __name__ == "__main__":
    main()