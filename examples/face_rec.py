from vilib import Vilib
from vilib import Face
import cv2
from os import getlogin

username = getlogin()

def main():
    Vilib.camera_start()
    Vilib.display()
    Face.load_model(model_path=f'/home/{username}/trainer/encodings.pickle')
    Vilib.face_recognition_switch(True)

# def main():
#     Face.load_model(model_path=f'/home/{username}/trainer/encodings.{username}ckle')
#     img = cv2.imread(f"/home/{username}/trainer/test8.jpg")     
#     img = Face.recognition2img(img)
#     cv2.imwirte(img,f"/home/{username}/trainer/testout,jpg")

            
if __name__ == "__main__":
    main()