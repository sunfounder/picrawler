from time import sleep
import readchar
from robot_hat import Music, TTS

music = Music()
tts = TTS()

manual = '''
Press a key to trigger actions (no Enter needed):
    q: Play/Stop background music
    1: Play sound effect (blocking)
    2: Play sound effect (threading)
    t: Text to speak

    Ctrl^C: quit
'''

def main():
    print(manual)

    flag_bgm = False
    music.music_set_volume(20)
    tts.lang("en-US")

    try:
        while True:
            # Real-time key input (no Enter required)
            key = readchar.readkey().lower()

            if key == "q":
                flag_bgm = not flag_bgm
                if flag_bgm:
                    music.music_play('./musics/sports-Ahjay_Stelino.mp3')
                else:
                    music.music_stop()

            elif key == "1":
                music.sound_play('./sounds/talk1.wav')
                sleep(0.05)
                music.sound_play('./sounds/talk3.wav')
                sleep(0.05)
                music.sound_play('./sounds/sign.wav')
                sleep(0.5)

            elif key == "2":
                music.sound_play_threading('./sounds/talk1.wav')
                sleep(0.05)
                music.sound_play_threading('./sounds/talk3.wav')
                sleep(0.05)
                music.sound_play_threading('./sounds/sign.wav')
                sleep(0.5)

            elif key == "t":
                tts.say("Hello")

    except KeyboardInterrupt:
        print("\nquit")

    finally:
        # Stop music before exit to reduce error messages
        try:
            music.music_stop()
        except Exception:
            pass

if __name__ == "__main__":
    main()