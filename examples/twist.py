
from picrawler import Picrawler
from time import sleep
from robot_hat import Music

music = Music()
crawler = Picrawler()


def twist(speed):
    new_step=[[50, 50, -80], [50, 50, -80],[50, 50, -80], [50, 50, -80]]
    for i in range(4):
        for inc in range(30, 50, 5): 
            rise = [50,50,(-80+inc*0.5)]
            drop = [50,50,(-80-inc)]

            new_step[i]=rise
            new_step[(i+2)%4] = drop
            new_step[(i+1)%4] = rise
            new_step[(i-1)%4] = drop
            crawler.do_step(new_step,speed)


def main():  

    music.music_play('./musics/sports-Ahjay_Stelino.mp3')
    music.music_set_volume(20)

    while True:
        twist(speed=100) 
            
 
if __name__ == "__main__":
    main()