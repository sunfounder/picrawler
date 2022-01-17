计算机视觉
=======================

本项目将正式进入计算机视觉领域！

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picrawler/examples
    sudo python3 display.py

**查看图像**

代码运行后，在浏览器中输入 ``http://<your IP>:9000/mjpg`` 来查看视频画面。如:  ``https://192.168.18.113:9000/mjpg``

.. image:: image/display.png

按照根据终端的信息提示，按下键盘上的按键来查看相应的功能。

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


*  **拍照**

        在终端中输入 ``q`` 并按下回车。 相机当前看到的图片会被保存（如果开启颜色检测功能，保存的图片中也会出现标记框）。你可以从目录 ``/home/pi/Pictures/PiCrawler/`` 看到这些照片。
        然后用 :ref:`Filezilla Software` 之类的工具将照片发送到你的电脑上。
        

*  **颜色检测**

        在 ``1~6`` 之间输入一个数字，将会检测 "红色、橙色、黄色、绿色、蓝色、紫色" 中的一种颜色。 输入 ``0`` 以关闭颜色检测。

        .. image:: image/DTC2.png

        .. note:: 
            
            你可以下载并打印 :download:`PDF 颜色卡片 <https://gitee.com/sunfounder/sf-pdf/raw/master/%E5%8D%A1%E7%89%87/%E7%9B%AE%E6%A0%87%E8%AF%86%E5%88%AB/%E9%A2%9C%E8%89%B2%E5%8D%A1.pdf>` 来用于颜色检测。


*  **人脸检测**

        输入 ``f`` 来打开人脸检测。

        .. image:: image/DTC5.png

*  **二维码检测**

        输入 ``r`` 来打开二维码检测。在识别二维码之前，不能进行其他操作。二维码的解码信息将打印在终端中。

        .. image:: image/DTC4.png

*  **显示信息**

        输入 ``s`` 会在终端打印人脸检测（和颜色检测）目标的信息。包括被测物体的中心坐标（X，Y）和尺寸（重量，高度）。


**代码** 

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
            if key == "q" or key == "Q":
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
            elif key =="f" or key == "F":
                flag_face = not flag_face
                face_detect(flag_face)
            elif key =="r" or key == "R":
                qrcode_detect()
            elif key == "s" or key == "S":
                object_show()

    if __name__ == "__main__":
        main()



**这个怎么运作?**

这里首先需要注意的是下面的函数。这两个函数可以帮助您启动相机。

.. code-block:: python

    Vilib.camera_start()
    Vilib.display()

与"物体检测"相关的函数:

* ``Vilib.face_detect_switch(True)`` : 开启/关闭人脸检测
* ``Vilib.color_detect(color)`` : 对于颜色检测，只能同时检测一种颜色。可以输入的参数有: ``"red"``, ``"orange"``, ``"yellow"``, ``"green"``, ``"blue"``, ``"purple"``
* ``Vilib.color_detect_switch(False)`` : 关闭颜色检测
* ``Vilib.qrcode_detect_switch(False)`` : 开启/关闭二维码检测，返回二维码的解码数据
* ``Vilib.gesture_detect_switch(False)`` : 打开/关闭手势检测
* ``Vilib.traffic_sign_detect_switch(False)`` :  开启/关闭交通标志检测

目标检测到的信息将存储在 ``detect_obj_parameter = Manager().dict()`` 字典中。

在主程序中，您可以像这样使用它:

.. code-block:: python

    Vilib.detect_obj_parameter['color_x']

字典的键及其用途如下表所示:

* ``color_x``：检测到的色块中心坐标的x值，范围0~320
* ``color_y``：检测到的色块中心坐标的y值，范围0~240
* ``color_w``：检测色块的宽度，范围0~320
* ``color_h``：检测到的色块高度，范围0~240
* ``color_n``: 检测到的色块数量
* ``human_x``：检测到的人脸中心坐标的x值，范围0~320
* ``human_y``：检测人脸中心坐标的y值，范围0~240
* ``human_w``：检测到的人脸宽度，范围0~320
* ``human_h``：检测到的人脸高度，范围0~240
* ``human_n``：检测到的人脸数量
* ``traffic_sign_x``：检测到的交通标志的中心坐标x值，范围0~320
* ``traffic_sign_y``：检测到的交通标志的中心坐标y值，范围0~240
* ``traffic_sign_w``：检测到的交通标志的宽度，范围0~320
* ``traffic_sign_h``：检测到的交通标志的高度，范围0~240
* ``traffic_sign_t``: 检测到的交通标志的内容，取值列表为 `['stop','right','left','forward']`
* ``gesture_x``：检测到的手势的中心坐标x值，范围0~320
* ``gesture_y``：检测到的手势的中心坐标y值，范围0~240
* ``gesture_w``：检测到的手势宽度，范围0~320
* ``gesture_h``：检测到的手势高度，范围0~240
* ``gesture_t``：检测到的手势内容，值列表为 `["paper","scissor","rock"]`
* ``qr_date``: 正在检测的二维码内容
* ``qr_x``：待检测二维码的中心坐标x值，范围0~320
* ``qr_y``：待检测二维码的中心坐标y值，范围0~240
* ``qr_w``：要检测的二维码宽度，范围0~320
* ``qr_h``：要检测的二维码高度，范围0~320

