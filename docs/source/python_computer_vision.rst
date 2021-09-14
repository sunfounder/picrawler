Computer Vision
=======================

This project will officially enter the field of computer vision!

**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picrawler/examples
    sudo python3 display.py

**View the Image**

After the code runs, the terminal will display the following prompt:

.. code-block::

    No desktop !
    * Serving Flask app "vilib.vilib" (lazy loading)
    * Environment: production
    WARNING: Do not use the development server in a production environment.
    Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)

Then you can enter ``http://<your IP>:9000/mjpg`` in the browser to view the video screen. such as:  ``https://192.168.18.113:9000/mjpg``

.. image:: image/display.png

**Call the Function**

After the program runs, you will see the following information in the final:


.. code-block::

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


Please follow the prompts to activate the corresponding functions.

    #. **Take Photo**

        Type ``q`` in the terminal and press Enter. The picture currently seen by the camera will be saved (if the color detection function is turned on, the mark box will also appear in the saved picture). You can see these photos from the ``/home/pi/Pictures/PiCrawler/`` directory of the Raspberry Pi.
        You can use tools such as :ref:`Filezilla Software` to transfer photos to your PC.
        

    #. **Color Detect**

        Entering a number between ``1~6`` will detect one of the colors in "red, orange, yellow, green, blue, purple". Enter ``0`` to turn off color detection.

        .. note:: You can download and print the :download:`PDF Color Cards <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>` for color detection.


    #. **Face Detect**

        Type ``f`` to turn on face detection.

    #. **QR Code Detect**

        Enter ``r`` to open the QR code recognition. No other operations can be performed before the QR code is recognized. The decoding information of the QR code will be printed in the terminal.

    #. **Display Information**

        Entering ``s`` will print the information of the face detection (and color detection) target in the terminal. Including the center coordinates (X, Y) and size (Weight, height) of the measured object.


**Code** 

.. code-block:: python

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



**How it works?**

The first thing you need to pay attention to here is the following function. These two functions allow you to start the camera.

.. code-block:: python

    Vilib.camera_start()
    Vilib.display()

Functions related to "object detection":

* ``Vilib.face_detect_switch(True)`` : Switch ON/OFF face detection
* ``Vilib.color_detect(color)`` : For color detection, only one color detection can be performed at the same time. The parameters that can be input are: ``"red"``, ``"orange"``, ``"yellow"``, ``"green"``, ``"blue"``, ``"purple"``
* ``Vilib.color_detect_switch(False)`` : Switch OFF color detection
* ``color_detect_switch(False)`` : Switch ON/OFF QR code detection, Returns the decoded data of the QR code.
* ``gesture_detect_switch(False)`` : Switch ON/OFF gesture detection
* ``traffic_sign_detect_switch(False)`` : Switch ON/OFF traffic sign detection

The information detected by the target will be stored in the ``detect_obj_parameter = Manager().dict()`` dictionary.

In the main program, you can use it like this:

.. code-block:: python

    Vilib.detect_obj_parameter['color_x']

The keys of the dictionary and their uses are shown in the following list:

* ``color_x``: the x value of the center coordinate of the detected color block, the range is 0~320
* ``color_y``: the y value of the center coordinate of the detected color block, the range is 0~240
* ``color_w``: the width of the detected color block, the range is 0~320
* ``color_h``: the height of the detected color block, the range is 0~240
* ``color_n``: the number of detected color patches
* ``human_x``: the x value of the center coordinate of the detected human face, the range is 0~320
* ``human_y``: the y value of the center coordinate of the detected face, the range is 0~240
* ``human_w``: the width of the detected human face, the range is 0~320
* ``human_h``: the height of the detected face, the range is 0~240
* ``human_n``: the number of detected faces
* ``traffic_sign_x``: the center coordinate x value of the detected traffic sign, the range is 0~320
* ``traffic_sign_y``: the center coordinate y value of the detected traffic sign, the range is 0~240
* ``traffic_sign_w``: the width of the detected traffic sign, the range is 0~320
* ``traffic_sign_h``: the height of the detected traffic sign, the range is 0~240
* ``traffic_sign_t``: the content of the detected traffic sign, the value list is `['stop','right','left','forward']`
* ``gesture_x``: The center coordinate x value of the detected gesture, the range is 0~320
* ``gesture_y``: The center coordinate y value of the detected gesture, the range is 0~240
* ``gesture_w``: The width of the detected gesture, the range is 0~320
* ``gesture_h``: The height of the detected gesture, the range is 0~240
* ``gesture_t``: The content of the detected gesture, the value list is `["paper","scissor","rock"]`
* ``qr_date``: the content of the QR code being detected
* ``qr_x``: the center coordinate x value of the QR code to be detected, the range is 0~320
* ``qr_y``: the center coordinate y value of the QR code to be detected, the range is 0~240
* ``qr_w``: the width of the QR code to be detected, the range is 0~320
* ``qr_h``: the height of the QR code to be detected, the range is 0~320


