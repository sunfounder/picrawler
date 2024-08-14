from picrawler import Picrawler
from time import sleep
from robot_hat import Music,TTS
from vilib import Vilib
import readchar
import random
import threading
import board
import busio
import adafruit_ssd1306


# Initialize I2C and the OLED display
i2c = busio.I2C(board.SCL, board.SDA)

# Try to initialize the OLED display
try:
    display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
    oled_present = True
except Exception as e:
    print("OLED display not detected or initialization failed.")
    oled_present = False

# If OLED is present, clear the display
if oled_present:
    display.fill(0)  # 0 is black
    display.show()


crawler = Picrawler()


music = Music()
tts = TTS()

manual = '''
Press keys on keyboard to control Picrawler!
    w: Forward
    a: Turn left
    s: Backward
    d: Turn right
    space: Say the target again
    Ctrl^C: Quit
'''

color = "red"
color_list=["red","orange","yellow","green","blue","purple"]
#color_list=["red"]
key_dict = {
    'w': 'forward',
    's': 'backward',
    'a': 'turn_left',
    'd': 'turn_right',
}
def renew_color_detect():
    global color
    color = random.choice(color_list)
    Vilib.color_detect(color)
    music.sound_play_threading('./sounds/hoot.wav')
    sleep(0.05)   
    tts.say("Hoot says find  " + color)
    if oled_present:
            # Update the OLED display with the current servo being reset
            display.fill(0)  # Clear the display
            display.text("Hoot says find  " + color, 0, 20, 1)  # Display which color
            display.show()


key = None
lock = threading.Lock()
def key_scan_thread():
    global key
    while True:
        key_temp = readchar.readkey()
        print('\r',end='')
        with lock:
            key = key_temp.lower()
            if key == readchar.key.SPACE:
                key = 'space'
            elif key == readchar.key.CTRL_C:
                key = 'quit'
                break
        sleep(0.01)

def main():
    global key
    action = None
    Vilib.camera_start(vflip=False,hflip=False)
    Vilib.display(local=True,web=True)
    Vilib.qrcode_detect_switch(True)
    sleep(0.8)
    speed = 80
    print(manual)

    sleep(1)
    _key_t = threading.Thread(target=key_scan_thread)
    _key_t.setDaemon(True)
    _key_t.start()


    tts.say("Lets play find the color")
    if oled_present:
        display.fill(0)  # Clear the display
        display.text("Find the color.", 0, 0, 1)
        display.show()
    sleep(0.05)   
    renew_color_detect()
    last_qr_data = ""  # Track the last detected QR code


    while True:


        if Vilib.detect_obj_parameter['color_n']!=0 and Vilib.detect_obj_parameter['color_w']>100:
            tts.say("awesome!")
            if oled_present:
                display.fill(0)  # Clear the display
                display.text("You found it.", 0, 0, 1)
                display.show()
            sleep(0.05)   
            tts.say("you found " + color)
            sleep(0.05)   
            renew_color_detect()

        with lock:
            if key != None and key in ('wsad'):
                action = key_dict[str(key)]
                key =  None
            elif key == 'space':
                music.sound_play_threading('./sounds/hoot.wav')
                sleep(0.05)   
                tts.say("Try to find " + color)
                key =  None
            elif key == 'quit':
                _key_t.join()
                Vilib.camera_close()
                print("\n\rQuit") 
                break 
            elif key == '6':
                # QR code detection and announcement
                current_qr_data = Vilib.detect_obj_parameter['qr_data']

                if current_qr_data == None and Vilib.detect_obj_parameter['color_n'] == 0:
                    print("Nothing to see here: ", current_qr_data)
                else:
                    if current_qr_data != last_qr_data:
                        last_qr_data = current_qr_data
                        music.sound_play_threading('./sounds/hoot.wav')
                        print("QR Code detected:", current_qr_data)
                        tts.say("I found a QR code that says: " + current_qr_data)       

                key = None  # Reset key after processing

        if action != None:
            crawler.do_action(action,1,speed)  
            action = None
        sleep(0.05)          
     

if __name__ == "__main__":
    main()

