from vilib import Vilib
from vilib import Face
import vilib
import cv2


def main():
    Vilib.camera_start()
    Vilib.display()
    Face.load_model(model_path='/home/pi/trainer/encodings.pickle')
    Vilib.face_recognition_switch(True)

# def main():
#     Face.load_model(model_path='/home/pi/trainer/encodings.pickle')
#     img = cv2.imread("/home/pi/trainer/test8.jpg")     
#     img = Face.recognition2img(img)
#     cv2.imwirte(img,"/home/pi/trainer/testout,jpg")

            
if __name__ == "__main__":
    main()