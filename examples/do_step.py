
from picrawler import Picrawler
from time import sleep

crawler = Picrawler([10,11,12,4,5,6,1,2,3,7,8,9]) 
#crawler.set_offset([0,0,0,0,0,0,0,0,0,0,0,0])

## [right front],[left front],[left rear],[right rear]
new_step=[[50, 50, -80], [50, 50, -80], [80, 80, 0], [50, 50, -80]]

def main():  
    
    speed = 100
          
    while True:
        
        crawler.do_step('stand',speed)
        print(crawler.step_list.get('stand'))
        sleep(3)
        crawler.do_step(new_step,speed)
        print(new_step)
        sleep(3)

            
 
if __name__ == "__main__":
    main()