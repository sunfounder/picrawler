
from picrawler import Picrawler
from robot_hat import TTS, Music
from robot_hat import Ultrasonic
from robot_hat import Pin
import time

tts = TTS()
music = Music()

crawler = Picrawler() 
sonar = Ultrasonic(Pin("D2") ,Pin("D3"))
music.music_set_volume(100)

alert_distance = 15
speed = 80

def main():
    distance = sonar.read()
    print(distance)
    if distance < 0:
        pass
    elif distance <= alert_distance:
        try:
            music.sound_play_threading('./sounds/sign.wav', volume=100)
        except Exception as e:
            print(e)
        crawler.do_action('turn left angle',3,speed)
        time.sleep(0.2)
    else :
        crawler.do_action('forward', 1,speed)
        time.sleep(0.2)

if __name__ == "__main__":
    while True:
        main()
