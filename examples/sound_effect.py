
'''
    Sorry, currently there is only sound when running with sudo
'''

from time import sleep
from robot_hat import Music,TTS

music = Music()
tts = TTS()

manual = '''
Input key to call the function!
    q: Play background music
    1: Play sound effect
    2: Play sound effect with threads
    t: Text to speak
'''

def main():  
    print(manual)

    flag_bgm = False
    music.music_set_volume(20)
    tts.lang("en-US")
    

    while True:
        key = input() 
        key = key.lower() 
        if key == "q":
            flag_bgm = not flag_bgm
            if flag_bgm is True:
                music.background_music('./musics/sports-Ahjay_Stelino.mp3')
            else:
                music.music_stop()

        elif key == "1":
            music.sound_effect_play('./sounds/talk1.wav')
            sleep(0.05)
            music.sound_effect_play('./sounds/talk3.wav')
            sleep(0.05)
            music.sound_effect_play('./sounds/sign.wav')
            sleep(0.5)

        elif key =="2":
            music.sound_effect_threading('./sounds/talk1.wav')
            sleep(0.05)
            music.sound_effect_threading('./sounds/talk3.wav')
            sleep(0.05)
            music.sound_effect_threading('./sounds/sign.wav')
            sleep(0.5)

        elif key == "t":
            words = "Hello"
            tts.say(words)
        
if __name__ == "__main__":
    main()

