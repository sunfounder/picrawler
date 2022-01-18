
from picrawler import Picrawler
from time import sleep
import sys
import tty
import termios



crawler = Picrawler([10,11,12,4,5,6,1,2,3,7,8,9]) 
#crawler.set_offset([0,0,0,0,0,0,0,0,0,0,0,0])
speed = 80





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
    space: Print all leg coordinate
    esc: Quit
'''



def main():  

    speed = 80
    print(manual)
    crawler.do_step('stand',speed)
    leg = 0 
    coordinate=crawler.current_step_leg_value(leg)   
    while True:
        key = readchar()
        print(key)
        if 'w' == key or 'W' == key:
            coordinate[1]=coordinate[1]+2    
        elif 's' == key or 'S' == key:
            coordinate[1]=coordinate[1]-2           
        elif 'a' == key or 'A' == key:
            coordinate[0]=coordinate[0]-2         
        elif 'd' == key or 'D' == key:
            coordinate[0]=coordinate[0]+2   
        elif 'r' == key or 'R' == key:
            coordinate[2]=coordinate[2]+2         
        elif 'f' == key or 'F' == key:
            coordinate[2]=coordinate[2]-2       
        elif '1' == key:
            leg=0
            coordinate=crawler.current_step_leg_value(leg)           
        elif '2' == key:
            leg=1   
            coordinate=crawler.current_step_leg_value(leg)              
        elif '3' == key:
            leg=2  
            coordinate=crawler.current_step_leg_value(leg)     
        elif '4' == key:
            leg=3     
            coordinate=crawler.current_step_leg_value(leg)  
        elif chr(32) == key:
            print("[[right front], [left front], [left rear], [right rear]]")
            print(crawler.current_step_all_leg_value())

        elif chr(27) == key:# 27 for ESC
            break    

        sleep(0.05)
        crawler.do_single_leg(leg,coordinate,speed)          
    print("\n q Quit")  
            
 
if __name__ == "__main__":
    main()