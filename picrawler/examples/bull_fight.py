from picrawler import Picrawler
from time import sleep
from robot_hat import Music
from vilib import Vilib


crawler = Picrawler() 

music = Music()

def main():
    Vilib.camera_start()
    Vilib.display()
    Vilib.color_detect("red") 
    speed = 80

    while True:
        if Vilib.detect_obj_parameter['color_n']!=0:
            coordinate_x = Vilib.detect_obj_parameter['color_x']
            music.sound_play_threading('./sounds/talk1.wav')

            if coordinate_x < 100:
                crawler.do_action('turn left',1,speed)
                sleep(0.05) 
            elif coordinate_x > 220:
                crawler.do_action('turn right',1,speed)
                sleep(0.05) 
            else :
                crawler.do_action('forward',2,speed)
                sleep(0.05)    
        else :
            crawler.do_step('stand',speed)
            sleep(0.05)


if __name__ == "__main__":
    main()
