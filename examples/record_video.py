from os import pardir
from time import sleep
from vilib import Vilib

def main():
    Vilib.camera_start()
    Vilib.display()

    Vilib.rec_video_set["path"] = "/home/pi/video/test/"
    vname = "vtest"
    Vilib.rec_video_run(vname)
    print('start rec ...')
    while True:
        if input() == 'q':
            Vilib.rec_video_start()
            print('continue')
        if input() == 'w':
            Vilib.rec_video_pause()
            print('pause')                                                       
        if input() == 'e':
            Vilib.rec_video_stop()
            print('stop')
            print("The video saved as",Vilib.rec_video_set["path"],vname)

if __name__ == "__main__":
    main()