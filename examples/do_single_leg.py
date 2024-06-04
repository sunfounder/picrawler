
from picrawler import Picrawler
from time import sleep
import readchar

crawler = Picrawler()
speed = 80


manual = '''
-------- PiCrawler Controller --------- 
       .......          .......
    <=|   2   |┌-┌┐┌┐-┐|   1   |=>
       ``````` ├      ┤ ```````
       ....... ├      ┤ .......
    <=|   3   |└------┘|   4   |=>
       ```````          ```````
    1: Select right front leg
    2: Select left front leg
    3: Select left rear leg
    4: Select right rear leg

    W: Y++          R: Z++             
    A: X--          F: Z--
    S: Y--
    D: X++          Ctrl+C: Quit
'''
legs_list = ['right front', 'left front', 'left rear', 'right rear']

def main():  
    leg = 0
    speed = 80
    step = 2
    print(manual)
    crawler.do_step('stand', speed)
    sleep(0.2)
    coordinate=crawler.current_step_all_leg_value()  

    def show_info():
        print("\033[H\033[J", end='')  # clear terminal windows
        print(manual)   
        print('%s : %s'%(leg+1, legs_list[leg])) 
        print('coordinate: %s'%(coordinate))  
    
    show_info()

    while True:
        # readkey
        key = readchar.readkey()
        key = key.lower()
        # select the leg 
        if key in ('1234'):
            leg = int(key) - 1
            show_info()
        # move
        elif key in ('wsadrf'):         
            if 'w' == key:
                coordinate[leg][1]=coordinate[leg][1] + step    
            elif 's' == key:
                coordinate[leg][1]=coordinate[leg][1] - step           
            elif 'a' == key:
                coordinate[leg][0]=coordinate[leg][0] - step         
            elif 'd' == key:
                coordinate[leg][0]=coordinate[leg][0] + step   
            elif 'r' == key:
                coordinate[leg][2]=coordinate[leg][2] + step         
            elif 'f' == key:
                coordinate[leg][2]=coordinate[leg][2] - step 

            crawler.do_single_leg(leg,coordinate[leg],speed) 
            sleep(0.1)  
            # coordinate=crawler.current_step_all_leg_value()
            show_info()

        sleep(0.05)
               
   
if __name__ == "__main__":
    main()