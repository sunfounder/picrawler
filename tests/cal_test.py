# import sys
# from types import coroutine
# sys.path.append('/home/pi/picrawler/picrawler')

from robot_hat import Servo,PWM,Joystick,ADC,Pin
from robot_hat.utils import reset_mcu

from picrawler import Picrawler
from time import sleep

reset_mcu()
sleep(0.01)

crawler = Picrawler([10,11,12,4,5,6,1,2,3,7,8,9])

def _cal_test():
    # arm.do_by_coord([-90,80,80])
    # print(arm.current_coord,arm.servo_positions)
    reset_mcu()
    sleep(0.01)

    angles = crawler.coord2polar([111 ,0, 48])
    print(angles)
    
    coord = crawler.polar2coord(angles)
    print(coord)

if __name__ == "__main__":
    _cal_test()