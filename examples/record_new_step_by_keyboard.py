from picrawler import Picrawler
from time import sleep
import readchar
import copy

# Initialize PiCrawler
crawler = Picrawler()

# Movement speed used for single-leg movement and step playback
speed = 50

# Coordinate increment for each key press
step_size = 2

# Keyboard control instructions
manual = '''
Press keys on keyboard to control!
    w: Y++
    a: X--
    s: Y--
    d: X++
    r: Z++
    f: Z--
    1: Select right front leg
    2: Select left front leg
    3: Select left rear leg
    4: Select right rear leg
    Space: Save this step
    p: Play all saved step
    Ctrl+C: Quit
'''

# Leg order:
# 0 = right front
# 1 = left front
# 2 = left rear
# 3 = right rear
legs_list = ['right front', 'left front', 'left rear', 'right rear']

# Store all recorded steps
new_step = []

# Key-to-axis mapping:
# 0 = X axis, 1 = Y axis, 2 = Z axis
move_map = {
    'w': (1, +step_size),  # Y++
    's': (1, -step_size),  # Y--
    'a': (0, -step_size),  # X--
    'd': (0, +step_size),  # X++
    'r': (2, +step_size),  # Z++
    'f': (2, -step_size),  # Z--
}


def print_current_step(selected_leg, coordinate):
    """Print the currently selected leg and full step data."""
    print(f"\nSelected leg: {selected_leg + 1} - {legs_list[selected_leg]}")
    print("Current step:")
    print(coordinate)


def save_new_step(coordinate):
    """Save the current full-leg coordinate as a new step."""
    step = copy.deepcopy(coordinate)
    new_step.append(step)
    print(f"\nSaved step {len(new_step)}:")
    print(step)


def play_all_new_step():
    """Play all saved steps in sequence."""
    for step in new_step:
        crawler.do_step(step, speed)
        sleep(0.6)


def main():
    # Default selected leg is the right front leg
    selected_leg = 0

    try:
        # Show control guide
        print(manual)

        # Read the current coordinate of all four legs
        coordinate = crawler.current_step_all_leg_value()
        print_current_step(selected_leg, coordinate)

        while True:
            # Read one key and convert it to lowercase
            key = readchar.readkey().lower()

            # Select leg
            if key in ('1', '2', '3', '4'):
                selected_leg = int(key) - 1
                coordinate = crawler.current_step_all_leg_value()
                print_current_step(selected_leg, coordinate)

            # Adjust the selected leg position
            elif key in move_map:
                axis, delta = move_map[key]
                coordinate[selected_leg][axis] += delta

                # Move only the selected leg
                crawler.do_single_leg(selected_leg, coordinate[selected_leg], speed)
                sleep(0.05)

            # Save the current step
            elif key == ' ':
                coordinate = crawler.current_step_all_leg_value()
                save_new_step(coordinate)

            # Play all saved steps
            elif key == 'p':
                play_all_new_step()
                coordinate = crawler.current_step_all_leg_value()
                print_current_step(selected_leg, coordinate)

    except KeyboardInterrupt:
        print("\nExiting safely...")

    finally:
        # Return to sitting position before exit
        try:
            crawler.do_step('sit', 40)
            sleep(1)
        except Exception:
            pass

        print("Robot is now sitting. Program ended.")


if __name__ == "__main__":
    main()