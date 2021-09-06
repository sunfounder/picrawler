from vilib import Vilib
from time import sleep
import time

flag_face = False
flag_color = False

manual = '''
Input key to call the function!
    q: Take photo
    1: Color detect : red
    2: Color detect : orange
    3: Color detect : yellow
    4: Color detect : green
    5: Color detect : blue
    6: Color detect : purple
    0: Switch off Color detect
    r：Scan the QR code
    f: Switch ON/OFF face detect
    s: Display detected object information
'''

def face_detect(flag):
    print("Face Detect:" + str(flag))
    Vilib.face_detect_switch(flag)

def color_detect(color):
    print("detecting color :" + color)
    Vilib.color_detect(color)



def qrcode_detect():
    Vilib.qrcode_detect_switch(True)
    print("Waitting for QR code")
    while True:
        text = Vilib.detect_obj_parameter['qr_data']  
        if text != "None":
            break
        sleep(0.5)
    print(text)
    sleep(0.5)  
    Vilib.qrcode_detect_switch(False)

def take_photo():
    now = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
    path = "/home/pi/Pictures/PiCrawler/"
    Vilib.take_photo('photo'+now,path)
    sleep(0.1)

def object_show():
    global flag_face,flag_color
    if flag_color is True and Vilib.detect_obj_parameter['color_n']!=0:
        color_coodinate = (Vilib.detect_obj_parameter['color_x'],Vilib.detect_obj_parameter['color_y'])
        color_size = (Vilib.detect_obj_parameter['color_w'],Vilib.detect_obj_parameter['color_h'])
        print("[Color Detect] ","Coordinate:",color_coodinate,"Size",color_size)
    if flag_face is True and Vilib.detect_obj_parameter['human_n']!=0:
        human_coodinate = (Vilib.detect_obj_parameter['human_x'],Vilib.detect_obj_parameter['human_y'])
        human_size = (Vilib.detect_obj_parameter['human_w'],Vilib.detect_obj_parameter['human_h'])
        print("[Human Detect] ","Coordinate:",human_coodinate,"Size",human_size)

def main():
    Vilib.camera_start()
    Vilib.display()
    print(manual)

    global flag_face,flag_color

    while True:
        key = input()  
        if key == "q":
            take_photo()
        elif key == "1":
            color_detect("red")
            flag_color = True
        elif key == "2":
            color_detect("orange")
            flag_color = True
        elif key == "3":
            color_detect("yellow")
            flag_color = True
        elif key == "4":
            color_detect("green")
            flag_color = True
        elif key == "5":
            color_detect("blue")
            flag_color = True
        elif key == "6":
            color_detect("purple")
            flag_color = True
        elif key =="0":
            Vilib.color_detect_switch(False)
            flag_color = False
        elif key =="f":
            flag_face = not flag_face
            face_detect(flag_face)
        elif key =="r":
            qrcode_detect()
        elif key == "s":
            object_show()

if __name__ == "__main__":
    main()

