
from picrawler import Picrawler
from time import sleep
import sys
import tty
import termios



crawler = Picrawler([10,11,12,4,5,6,1,2,3,7,8,9]) 
#crawler.set_offset([0,0,0,0,0,0,0,0,0,0,0,0])
speed = 80

#俯卧撑
def pushup():

    crawler.do_step(crawler.step_list["stand"],speed = 80)
    sleep(0.01)
    crawler.do_step(crawler.step_list["sit"],speed=100)
    sleep(0.01)
    
#左右摇摆
def swing():
    crawlereed = 100
    crawler.do_step(crawler.step_list["sit"],speed)
    # crawler.do_single_leg(leg=1,coodinate=[80,0,-20])
    mystep1 = [[50,50,-30],[50,50,-30],[50,50,-80],[50,50,-80]]
    mystep2 = [[50,50,-80],[50,50,-80],[50,50,-30],[50,50,-30]]
    # crawler.do_step(mystep,speed=100)
    
    crawler.do_step(mystep1,speed)
    #print(crawler.current_step_leg_value(0))
    sleep(0.1)
    crawler.do_step(mystep2,speed)
    #print(crawler.current_step_leg_value(0))
    sleep(0.1)
 
#挥手
def wave(leg):
    crawler.do_single_leg(leg,coodinate=[0,50,80],speed=100)
    sleep(0.1)
    crawler.do_single_leg(leg,coodinate=[50,0,80],speed=100)
    sleep(0.1)
 
 
# 旋转

def rotate(clockwise):
    if True ==  clockwise:
        crawler.do_action('turn right',1,speed)
    else:
        crawler.do_action('turn left',1,speed)


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
Press keys on keyboard to control PiSloth!
    W: Forward
    A: Turn left
    S: Backward
    D: Turn right
    Q: Wave
    E: Swing
    R: Rotate
'''





def main():  

    for _ in range(1):
       speed = 100
       pushup()   
    
    print(manual)

          
    while True:
        key = readchar()
        print(key)
        if 'w' == key:
            crawler.do_action('forward',1,90)     
        elif 's' == key:
            crawler.do_action('backward',1,90)          
        elif 'a' == key:
            crawler.do_action('turn left',1,90)           
        elif 'd' == key:
            crawler.do_action('turn right',1,90)
        elif 'q' == key:
            wave(0)           
        elif 'e' == key:
            swing()           
        elif 'r' == key:
            rotate(True)
        elif chr(27) == key:# 27 for ESC
            break    

        sleep(0.05)          
    print("\nQuit")  
            
 
if __name__ == "__main__":
    main()