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

代码运行后，terminal会显示以下提示：

.. code-block::

    No desktop !
    * Serving Flask app "vilib.vilib" (lazy loading)
    * Environment: production
    WARNING: Do not use the development server in a production environment.
    Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)

随后你可以在浏览器中输入 ``http://<your IP>:9000/mjpg`` 来查看视频画面。

如： "https://192.168.18.113:9000/mjpg"

.. image:: image/display.png

**Call the Function**

程序运行后，你将在teriminal看到以下信息：


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


请根据提示启动相应的功能。

    #. **Take Photo**

        在terminal中输入 ``q`` ，并敲击回车键。摄像头当前看到的画面将会被保存（如果打开了颜色检测等功能，标记框也将出现在被保存的图片里）。你可以从树莓派的 ``/home/pi/Pictures/PiCrawler/`` 目录下看到这些照片。
        你可以使用 :ref:`Filezilla Software` 等工具将照片转移到你的PC。
        

    #. **Color Detect**

        输入 ``1~6`` 之间的一个数字，将会对red, orange, yellow, green, blue, purple中的一种颜色。输入 ``0`` ，则关闭颜色检测。

        .. note:: You can download and print the :download:`PDF Color Cards <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>` for color detection.


    #. **Face Detect**

        输入 ``f`` 打开人脸检测。

    #. **QR Code Detect**

        输入 ``r`` 打开二维码识别，在识别到二维码之前无法进行其他操作。二维码的解码信息将会打印在terminal中。

    #. **Display Information**

        输入 ``s`` 将会把人脸检测（和颜色检测）目标的信息打印在terminal中。包括被测物体的中心坐标（X,Y）和尺寸（Weight,height）。


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

在这里你首先需要注意的是以下函数。这两个函数可以让你启动摄像头。

.. code-block:: python

    Vilib.camera_start()
    Vilib.display()



目标检测相关的函数包括以下：

* ``Vilib.face_detect_switch(True)`` : Switch ON/OFF face detection
* ``Vilib.color_detect(color)`` : 进行颜色检测，同一时间只能进行一种颜色检测，可以输入的参数有 ``"red"``, ``"orange"``, ``"yellow"``, ``"green"``, ``"blue"``, ``"purple"``
* ``Vilib.color_detect_switch(False)`` : Switch OFF color detection
* ``color_detect_switch(False)`` : Switch ON/OFF QR code detection, 返回二维码解码数据。
* ``gesture_detect_switch(False)`` : Switch ON/OFF gesture detection
* ``traffic_sign_detect_switch(False)`` : Switch ON/OFF traffic sign detection

目标检测到的信息将储存在 ``detect_obj_parameter = Manager().dict()`` 字典中。

在主程序中，你可以如下使用它：

.. code-block:: python

    Vilib.detect_obj_parameter['color_x']

该字典的key及其用途如下列表所示:

* ``color_x`` : 被检测色块的中心坐标的x值，范围为0~320
* ``color_y`` : 被检测色块的中心坐标的y值，范围为0~240
* ``color_w`` : 被检测色块的宽度，范围为0~320
* ``color_h`` : 被检测色块的高度，范围为0~240
* ``color_n`` : 被检测色块的数量
* ``human_x`` : 被检测人脸的中心坐标的x值，范围为0~320 
* ``human_y`` : 被检测人脸的中心坐标的y值，范围为0~240
* ``human_w`` : 被检测人脸的宽度，范围为0~320
* ``human_h`` : 被检测人脸的高度，范围为0~240
* ``human_n`` : 被检测人脸的数量
* ``traffic_sign_x`` : 被检测交通标志的中心坐标x值，范围为0~320 
* ``traffic_sign_y`` : 被检测交通标志的中心坐标y值，范围为0~240
* ``traffic_sign_w`` : 被检测交通标志的宽度，范围为0~320
* ``traffic_sign_h`` : 被检测交通标志的高度，范围为0~240
* ``traffic_sign_t`` : 被检测交通标志的内容，其值列表为 `['stop','right','left','forward']`
* ``gesture_x`` : 被检测手势的中心坐标x值，范围为0~320 
* ``gesture_y`` : 被检测手势的中心坐标y值，范围为0~240
* ``gesture_w`` : 被检测手势的宽度，范围为0~320
* ``gesture_h`` : 被检测手势的高度，范围为0~240
* ``gesture_t`` : 被检测手势的内容，其值列表为 `["paper","scissor","rock"]`
* ``qr_date``  : 被检测二维码的内容
* ``qr_x``  : 被检测二维码的中心坐标x值，范围为0~320
* ``qr_y`` : 被检测二维码的中心坐标y值，范围为0~240
* ``qr_w`` : 被检测二维码的宽度，范围为0~320
* ``qr_h`` : 被检测二维码的高度，范围为0~320


