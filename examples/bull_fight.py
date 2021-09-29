from picrawler import Picrawler
from time import sleep
from robot_hat import Music
from vilib import Vilib


crawler = Picrawler([10,11,12,4,5,6,1,2,3,7,8,9]) 
#crawler.set_offset([0,0,0,0,0,0,0,0,0,0,0,0])

music = Music()

def main():
    Vilib.camera_start()
    Vilib.display()
    Vilib.color_detect("red") 
    speed = 100

    while True:
        if Vilib.detect_obj_parameter['color_n']!=0:
            coordinate_x = Vilib.detect_obj_parameter['color_x']
            music.sound_effect_threading('./sounds/talk1.wav')

            if coordinate_x == -1:
                crawler.do_action('turn left',1,speed)
                sleep(0.05) 
            elif coordinate_x == 1:
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
