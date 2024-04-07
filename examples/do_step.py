
from picrawler import Picrawler
from time import sleep

crawler = Picrawler() 

## [right front],[left front],[left rear],[right rear]
new_step=[[50, 50, -75], [50, 50, -75], [75, 75, 0], [50, 50, -75]]

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