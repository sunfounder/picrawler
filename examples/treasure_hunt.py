from picrawler import Picrawler
from time import sleep
from robot_hat import Music,TTS
from vilib import Vilib
import sys
import tty
import termios
import random


crawler = Picrawler([10,11,12,4,5,6,1,2,3,7,8,9]) 
#crawler.set_offset([0,0,0,0,0,0,0,0,0,0,0,0])

music = Music()
tts = TTS()

def readchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


manual = '''
Press keys on keyboard to control Picrawler!
    W: Forward
    A: Turn left
    S: Backward
    D: Turn right
    Space: Say the target again
    ESC: Quit
'''

color = "red"
color_list=["red","orange","yellow","green","blue","purple"]


def renew_color_detect():
    global color
    color = random.choice(color_list)
    Vilib.color_detect(color)
    tts.say("Look for " + color)


def main():
    Vilib.camera_start()
    Vilib.display()
    speed = 100
    print(manual)

    tts.say("game start")
    sleep(0.05)   
    renew_color_detect()

    while True:
        if Vilib.detect_obj_parameter['color_n']!=0 and Vilib.detect_obj_parameter['color_w']>100:
            tts.say("will done")
            sleep(0.05)   
            renew_color_detect()
            
        key = readchar()
        if 'w' == key:
            crawler.do_action('forward',1,speed)     
        elif 's' == key:
            crawler.do_action('backward',1,speed)          
        elif 'a' == key:
            crawler.do_action('turn left',1,speed)           
        elif 'd' == key:
            crawler.do_action('turn right',1,speed)
        elif chr(32) == key:
            tts.say("Look for " + color)
        elif chr(27) == key:# 27 for ESC
            break    

        sleep(0.05)          
    print("\n q Quit")  

if __name__ == "__main__":
    main()
