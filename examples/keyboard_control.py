
from picrawler import Picrawler
from time import sleep
import sys
import tty
import termios



crawler = Picrawler([10,11,12,4,5,6,1,2,3,7,8,9]) 
#crawler.set_offset([0,0,0,0,0,0,0,0,0,0,0,0])
speed = 90

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
Press keys on keyboard to control PiCrawler!
    W: Forward
    A: Turn left
    S: Backward
    D: Turn right
    ESC: Quit
'''

def main():  
    
    print(manual)
          
    while True:
        key = readchar()
        print(key)
        if 'w' == key:
            crawler.do_action('forward',1,speed)     
        elif 's' == key:
            crawler.do_action('backward',1,speed)          
        elif 'a' == key:
            crawler.do_action('turn left',1,speed)           
        elif 'd' == key:
            crawler.do_action('turn right',1,speed)
        elif chr(27) == key:# 27 for ESC
            break    

        sleep(0.05)          
    print("\n q Quit")  
            
 
if __name__ == "__main__":
    main()