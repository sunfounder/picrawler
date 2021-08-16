from picrawler import Picrawler
from time import sleep



crawler = Picrawler([10,11,12,4,5,6,1,2,3,7,8,9]) 
#crawler.set_offset([0,0,0,0,0,0,0,0,0,0,0,0])
speed = 80

# mix_step
def my_mix_step():

    crawler.do_step(crawler.step_list["stand"],speed=100)
    sleep(0.5)
    basic_step = []
    basic_step = crawler.step_list.get("stand")
    print(basic_step)
    left_hand  = crawler.mix_step(basic_step,0,[0,50,80])
    right_hand  = crawler.mix_step(basic_step,1,[0,50,80])
    print('left_hand:',left_hand)
    print('right_hand:',right_hand)

    speed = 100
    while True:
        
        crawler.do_step(left_hand,speed)
        sleep(0.6)
        crawler.do_step(right_hand,speed)
        sleep(0.6)


# main
def main():
    my_mix_step()
    sleep(0.05)

if __name__ == "__main__":
    main()