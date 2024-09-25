#!/usr/bin/env python3
from picrawler import Picrawler
import readchar 
from time import sleep


# init picrawler
# ======================================
crawler = Picrawler()
crawler.do_step([[60, 0, -30]]*4, 80)

# print(f'current_angles: {[round(x, 2) for x in crawler.servo_positions]}')
# print(f'OFFSET_ZERO: {[round(x, 2) for x in OFFSET_ZERO]}')
# print(f'offset: {offset}')


# global variables
# ======================================
manual = '''
------------------- Spider Calibration Helper -------------------

                   .......          .......
                <=|   2   |┌-┌┐┌┐-┐|   1   |=>
                   ``````` ├      ┤ ```````
                   ....... ├      ┤ .......
                <=|   3   |└------┘|   4   |=>
                   ```````          ```````
  [1~4]: select leg                     [SPACE]: confirm calibration
  [A/D]: adjust x coordinate
  [W/S]: adjust ycoordinate
  [R/F]: adjust z coordinate            [Crtl^C]: quit
'''

key_dict = {
    'w': 'up', 
    's': 'down', 
    'a': 'left', 
    'd': 'right', 
    'r': 'high', 
    'f': 'low', 
}

OFFSET_ZERO = crawler.coord2polar([60, 0, -30])
COORD_OFFSET_STEP = 0.2
ANGLE_LIMIT = 20

POSITIVE_LIST = [
    [1, 1, -1],
    [1, 1, 1],
    [1, 1, -1],
    [1, 1, 1],
]

leg_num = 1
coord_offset = [[0, 0, 0]]*4
offset = list.copy(crawler.offset)
angle_offset = offset

# ======================================

def show_info():
    global leg_num, coord_offset, angle_offset

    print("\033[H\033[J", end='')  # clear terminal windows
    print(manual)   
    print(f'leg_num: \033[0;33m{leg_num}\033[0m')

    colors = ['0']*4
    colors[leg_num-1] = '0;33'
    print(f"coord_offset: "\
        f"\033[{colors[0]}m{coord_offset[0]}\033[0m, "
        f"\033[{colors[1]}m{coord_offset[1]}\033[0m, "
        f"\033[{colors[2]}m{coord_offset[2]}\033[0m, "
        f"\033[{colors[3]}m{coord_offset[3]}\033[0m"
        )

    print(f"coord_offset: ["\
        f"\033[{colors[0]}m{angle_offset[0]}, {angle_offset[1]}, {angle_offset[2]}\033[0m, "
        f"\033[{colors[1]}m{angle_offset[3]}, {angle_offset[4]}, {angle_offset[5]}\033[0m, "
        f"\033[{colors[2]}m{angle_offset[6]}, {angle_offset[7]}, {angle_offset[8]}\033[0m, "
        f"\033[{colors[3]}m{angle_offset[9]}, {angle_offset[10]}, {angle_offset[11]}\033[0m"
        f"]")

def cali_helper(): 
    global leg_num, coord_offset, angle_offset

    x = 0; y=0; z=0
    pos = None

    show_info()

    while True:
        # --- readkey ---
        key = readchar.readkey()
        key = key.lower()

        # --- select the leg ---
        if key in ('1234'):
            leg_num = int(key)
            show_info()

        # move
        elif key in ('wsadrf'):
            _index = leg_num -1
            _coord_offset = list.copy(coord_offset[_index])

            if key == 'w':
                _coord_offset[1] += COORD_OFFSET_STEP
            elif key == 's':
                _coord_offset[1] -= COORD_OFFSET_STEP
            elif key == 'a':
                _coord_offset[0] += COORD_OFFSET_STEP
            elif key == 'd':
                _coord_offset[0] -= COORD_OFFSET_STEP
            elif key == 'r':
                _coord_offset[2] += COORD_OFFSET_STEP
            elif key == 'f':
                _coord_offset[2] -= COORD_OFFSET_STEP

            _coord = [60, 0, -30]
            _coord[0] += _coord_offset[0]
            _coord[1] += _coord_offset[1]
            _coord[2] += _coord_offset[2]
            _angles = crawler.coord2polar(_coord)
            _angles = [round(x, 2) for x in _angles]

            _alpha_offset = round(_angles[0] - OFFSET_ZERO[0], 2)
            _beta_offset = round(_angles[1] - OFFSET_ZERO[1], 2)
            _gamma_offset = round(_angles[2] - OFFSET_ZERO[2], 2)

            if (_alpha_offset > ANGLE_LIMIT) or (_alpha_offset < -ANGLE_LIMIT):
                continue
            elif (_beta_offset > ANGLE_LIMIT) or (_beta_offset < -ANGLE_LIMIT):
                continue
            elif (_gamma_offset > ANGLE_LIMIT) or (_gamma_offset < -ANGLE_LIMIT):
                continue
            else:
                coord_offset[_index] = [round(x, 2) for x in _coord_offset]
                offset[_index*3 + 0] = _beta_offset
                offset[_index*3 + 1] = _alpha_offset
                offset[_index*3 + 2] = _gamma_offset

                crawler.servo_list[_index*3 + 0].angle(_angles[1]*POSITIVE_LIST[_index][0])
                crawler.servo_list[_index*3 + 1].angle(_angles[0]*POSITIVE_LIST[_index][1])
                crawler.servo_list[_index*3 + 2].angle(_angles[2]*POSITIVE_LIST[_index][2])
                show_info()
        elif key == readchar.key.SPACE:
            print('Confirm save ?(y/n)')
            while True:
                key = readchar.readkey()
                key = key.lower()
                if key == 'y':
                    crawler.set_offset(offset)
                    sleep(0.2)
                    crawler.do_step([[60, 0, -30]]*4, 80)
                    show_info()
                    print('The calibration value has been saved.')
                    break
                elif key == 'n':
                    show_info()
                    break
                sleep(0.01) 
        sleep(0.01)

if __name__ == "__main__":
    cali_helper()
