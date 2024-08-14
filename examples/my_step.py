
from picrawler import Picrawler
from time import sleep

crawler = Picrawler() 

## [right front],[left front],[left rear],[right rear]
new_step=[[45, 45, -75], [45, 0, -75], [45, 0, -30], [45, 45, -75]]
stand_step = crawler.move_list['stand'][0]
sit_step = crawler.move_list['sit'][0]

def main():  
    while True:
        speed = 80
            
        print(f"stand step: {stand_step}")
        crawler.do_step(stand_step, speed)
        sleep(3)
        print(f"sit step: {sit_step}")
        crawler.do_step(sit_step, speed)
        sleep(3)
            
 
if __name__ == "__main__":
    main()
