
from picrawler import Picrawler
from time import sleep


crawler = Picrawler([10,11,12,4,5,6,1,2,3,7,8,9]) 
#crawler.set_offset([0,0,0,0])
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
    print(crawler.current_step_leg_value(0))
    sleep(0.1)
    crawler.do_step(mystep2,speed)
    print(crawler.current_step_leg_value(0))
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
        crawler.do_action('turn right',3,speed)
    else:
        crawler.do_action('turn left',3,speed)






def main():
        
    for _ in range(1):
       pushup()   
     
          
    while True:
        if input() == 'w':
            print('forward')
            crawler.do_action('forward',2,90)     
        if input() == 's':
            print('backward')
            crawler.do_action('backward',2,90)          
        if input() == 'a':
            print('turn left')
            crawler.do_action('turn left',2,90)           
        if input() == 'd':
            print('turn right')
            crawler.do_action('turn right',2,90)
            

        if input() == 'q':
            print('wave') 
            wave(0)
            
        if input() == 'e':
            print('swing')  
            swing()           
        if input() == 'r':
            print('rotate') 
            rotate(True)
                   
        
            
 
if __name__ == "__main__":
    main()