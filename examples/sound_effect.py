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
        if key == "q" or key == "Q":
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

        elif key == "t" or key == "T":
            words = "Hello"
            tts.say(words)
        
if __name__ == "__main__":
    main()

