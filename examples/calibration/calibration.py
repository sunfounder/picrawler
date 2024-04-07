#!/usr/bin/env python3
from picrawler import Picrawler
import readchar 
from robot_hat.utils import reset_mcu
from time import sleep

reset_mcu()
sleep(0.01)

manual = '''
----- Spider Calibration Helper -------      
                                      
       .......          .......
    <=|   2   |┌-┌┐┌┐-┐|   1   |=>
       ``````` ├      ┤ ```````
       ....... ├      ┤ .......
    <=|   3   |└------┘|   4   |=>
       ```````          ```````
    1~4: select leg 
    A/D: adjust x coordinate              
    W/S: adjust ycoordinate
    R/F: adjust z coordinate
    SPACE: confirm calibration

'''    

key_dict = {
    'w': 'up', 
    's': 'down', 
    'a': 'left', 
    'd': 'right', 
    'r': 'high', 
    'f': 'low', 
}

crawler = Picrawler()

def cali_helper(): 
    leg_num = 1
    cali_coord = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    x = 0; y=0; z=0
    pos = None
    step = 0.2
    crawler.do_step([[60, 0, -30]]*4, 100)
    sleep(0.2)
    current_coord = list.copy(crawler.current_coord)
    offset = list.copy(crawler.offset)
    # current_angles = list.copy(crawler.current_angles)
    # cali_position = crawler.do_step(current_coord,  speed=100)
    sleep(0.2)

    def show_info():
        print("\033[H\033[J", end='')  # clear terminal windows
        print(manual)   
        print('leg_num: %s'%leg_num) 
        print('calibration_xyz: %s'%([round(i, 2) for i in cali_coord[leg_num-1]]))  
        print('offset: %s'%offset)

    show_info()
    while True:
        # readkey
        key = readchar.readkey()
        key = key.lower()
        # select the leg 
        if key in ('1234'):
            leg_num = int(key)
            x=0; y=0; z=0
            show_info()
        # move
        elif key in ('wsadrf'):  
            _leg_num = leg_num -1  
            if key == 'w' and cali_coord[_leg_num][1] <= 40:
                cali_coord[_leg_num][1] += step
            elif key == 's' and cali_coord[_leg_num][1] >= -40:
                cali_coord[_leg_num][1] -= step
            elif key == 'a' and cali_coord[_leg_num][0] <= 40:
                cali_coord[_leg_num][0] += step
            elif key == 'd' and cali_coord[_leg_num][0] >= -40:
                cali_coord[_leg_num][0] -= step
            elif key == 'r' and cali_coord[_leg_num][2] <= 40:
                cali_coord[_leg_num][2] += step   
            elif key == 'f' and cali_coord[_leg_num][2] >= -40:
                cali_coord[_leg_num][2] -= step 
            else:
                continue
            pos = key_dict[str(key)]
            crawler.cali_helper_web(leg_num,  pos,  0)
            show_info()
        elif key == readchar.key.SPACE:
            print('Confirm save ?(y/n)')
            while True:
                key = readchar.readkey()
                key = key.lower()
                if key == 'y':
                    crawler.cali_helper_web(leg_num,  ' ',  1)
                    sleep(0.2)
                    # current_coord = list.copy(crawler.current_coord)
                    # offset = list.copy(crawler.offset)
                    show_info()
                    print('The calibration value has been saved.')
                    break
                elif key == 'n':
                    show_info()
                    break   
                sleep(0.01) 
        elif key == readchar.key.CTRL_C or key in readchar.key.ESCAPE_SEQUENCES:
            print('quit')
            break 
        sleep(0.01)

if __name__ == "__main__":
    cali_helper()
