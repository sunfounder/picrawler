from picrawler import Picrawler
from time import sleep

crawler = Picrawler([10,11,12,4,5,6,1,2,3,7,8,9]) 
#crawler.set_offset([0,0,0,0,0,0,0,0,0,0,0,0])

def main():  
    
    speed = 100
          
    while True:
       
        crawler.do_action('forward',2,speed)
        sleep(0.05)     
        crawler.do_action('backward',2,speed)
        sleep(0.05)          
        crawler.do_action('turn left',2,speed)
        sleep(0.05)           
        crawler.do_action('turn right',2,speed)
        sleep(0.05)  
        crawler.do_action('turn left angle',2,speed)
        sleep(0.05)  
        crawler.do_action('turn right angle',2,speed)
        sleep(0.05) 
        crawler.do_step('stand',speed)
        sleep(1)

if __name__ == "__main__":
    main()