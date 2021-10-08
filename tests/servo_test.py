# from math import e
# import sys
# from types import coroutine
# sys.path.append('/home/pi/picrawler/picrawler')

from robot_hat import Joystick,ADC,Pin
from robot_hat.utils import reset_mcu

from picrawler import Picrawler
from time import sleep

reset_mcu()
sleep(0.01)

leftJoystick = Joystick(ADC('A0'),ADC('A1'),Pin('D0'))
rightJoystick = Joystick(ADC('A2'),ADC('A3'),Pin('D1'))

crawler = Picrawler([10,11,12,4,5,6,1,2,3,7,8,9])
crawler.set_offset([0,0,0,0,0,0,0,0,0,0,0,0])

def _angles_control():
    crawler.speed = 100
    flag = False
    angle1,angle2,angle3 = crawler.servo_positions[:3]

    if leftJoystick.read_status() == "up":
        angle1 -= 1
        flag = True
    elif leftJoystick.read_status() == "down":
        angle1+= 1
        flag = True
    if rightJoystick.read_status() == "left":
        angle2 -= 1
        flag = True
    elif rightJoystick.read_status() == "right":
        angle2 += 1
        flag = True
    if leftJoystick.read_status() == "left":
        angle3 -= 1
        flag = True
    elif leftJoystick.read_status() == "right":
        angle3 += 1
        flag = True
    
    # angle1,angle2,angle3 = angles
    if flag == True:
        # crawler.set_angle([[angle1,angle2,angle3],[0,0,0],[0,0,0],[0,0,0]],100)
        crawler.set_angle([[angle1,angle2,angle3],[angle1,angle2,angle3],[angle1,angle2,angle3],[angle1,angle2,angle3]],100)
        print('servo angles: %s'%(crawler.servo_positions[:3]))

def _coord_control():
    flag = False
    coord = list(crawler.current_coord)
    x,y,z = coord[0]

    if leftJoystick.read_status() == "up":
        x -= 1
        flag = True
    elif leftJoystick.read_status() == "down":
        x+= 1
        flag = True
    if rightJoystick.read_status() == "left":
        y -= 1
        flag = True
    elif rightJoystick.read_status() == "right":
        y += 1
        flag = True
    if leftJoystick.read_status() == "left":
        z -= 1
        flag = True
    elif leftJoystick.read_status() == "right":
        z += 1
        flag = True

    if flag == True:
        coord[0] = [x,y,z]
        coord[1] = [x,y,z]
        coord[2] = [x,y,z]
        coord[3] = [x,y,z]
        crawler.do_step(coord,80,False)
        print('coord: %s \nservo angles: %s\n'%(crawler.current_coord,crawler.servo_positions[:3]))

def test():
    crawler.servo_move([90,90,-45,90,90,-45,90,90,-45,90,90,-45])
    # crawler.do_step([[78.4888 ,78.4888, 48],[60, 0, -30],[60, 0, -30],[60, 0, -30]])
    # print(crawler.current_coord)
    print(crawler.servo_positions)

def angles_test():
    while True:
        _angles_control()
        sleep(0.01)

def coords_test():
    while True:
        _coord_control()
        sleep(0.01)

if __name__ == "__main__":

    print('Hello !')
    # test()
    # angles_test()
    coords_test()
