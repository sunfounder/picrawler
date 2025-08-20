.. _py_vision:

计算机视觉
=======================

本项目将正式进入计算机视觉领域！

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 display.py

**查看画面**

代码运行后，终端会显示如下提示：  

.. code-block::

    No desktop !
    * Serving Flask app "vilib.vilib" (lazy loading)
    * Environment: production
    WARNING: Do not use the development server in a production environment.
    Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)

随后，在浏览器中输入 ``http://<your IP>:9000/mjpg`` 即可查看视频画面，例如： ``https://192.168.18.113:9000/mjpg``  

.. image:: img/display.png


程序运行后，最后你会在终端看到以下提示信息：  


* 输入按键以调用对应功能！
* ``q``: 拍照
* ``1``: 颜色识别：红色
* ``2``: 颜色识别：橙色
* ``3``: 颜色识别：黄色
* ``4``: 颜色识别：绿色
* ``5``: 颜色识别：蓝色
* ``6``: 颜色识别：紫色
* ``0``: 关闭颜色识别
* ``r``: 扫描二维码
* ``f``: 开/关人脸识别
* ``s``: 显示检测到的对象信息

请根据提示操作以启用对应功能。  

    *  **拍照**

        在终端输入 ``q`` 并按回车，摄像头当前画面将被保存（若颜色识别已开启，保存的照片中也会显示标记框）。照片会保存在树莓派的 ``~/Pictures/PiCrawler/`` 目录下。  
        你可以使用 :ref:`filezilla` 等工具将照片传输到电脑。  

    *  **颜色识别**

        输入 ``1~6`` 中的任意数字，即可识别“红、橙、黄、绿、蓝、紫”中的一种颜色；输入 ``0`` 可关闭颜色识别。  

        .. image:: img/DTC2.png

        .. note:: 你可以下载并打印 :download:`PDF 色卡 <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>` 以进行颜色识别。  


    *  **人脸识别**

        输入 ``f`` 开启人脸检测。  

        .. image:: img/DTC5.png

    *  **二维码识别**

        输入 ``r`` 开启二维码识别。在二维码识别完成前，无法执行其他操作。二维码的解码信息会打印在终端中。  

        .. image:: img/DTC4.png

    *  **显示信息**

        输入 ``s`` 将在终端打印人脸检测（以及颜色检测）的目标信息，包括目标的中心坐标 (X, Y) 以及大小 (宽度、高度)。  


**代码** 

.. code-block:: python

    from vilib import Vilib
    from time import sleep, time, strftime, localtime
    import threading
    from os import getlogin
    
    USERNAME = getlogin()
    PICTURE_PATH = f"/home/{USERNAME}/Pictures/"
    
    
    flag_face = False
    flag_color = False
    qr_code_flag = False
    
    MANUAL = '''
    Input key to call the function!
        q: Take photo
        1: Color detect : red
        2: Color detect : orange
        3: Color detect : yellow
        4: Color detect : green
        5: Color detect : blue
        6: Color detect : purple
        0: Switch off Color detect
        r: Scan the QR code
        f: Switch ON/OFF face detect
        s: Display detected object information
    '''
    
    color_list = ['close', 'red', 'orange', 'yellow', 
            'green', 'blue', 'purple',
    ]
    
    def face_detect(flag):
        print("Face Detect:" + str(flag))
        Vilib.face_detect_switch(flag)
    
    
    def qrcode_detect():
        global qr_code_flag
        if qr_code_flag == True:
            Vilib.qrcode_detect_switch(True)
            print("Waitting for QR code")
    
        text = None
        while True:
            temp = Vilib.detect_obj_parameter['qr_data']
            if temp != "None" and temp != text: 
                text = temp         
                print('QR code:%s'%text)
            if qr_code_flag == False:          
                break
            sleep(0.5)
        Vilib.qrcode_detect_switch(False)
    
    
    def take_photo():
        _time = strftime('%Y-%m-%d-%H-%M-%S',localtime(time()))
        name = 'photo_%s'%_time
        Vilib.take_photo(name, PICTURE_PATH)
        print('photo save as %s%s.jpg'%(PICTURE_PATH, name))
    
    
    def object_show():
        global flag_color, flag_face
    
        if flag_color is True:
            if Vilib.detect_obj_parameter['color_n'] == 0:
                print('Color Detect: None')
            else:
                color_coodinate = (Vilib.detect_obj_parameter['color_x'],Vilib.detect_obj_parameter['color_y'])
                color_size = (Vilib.detect_obj_parameter['color_w'],Vilib.detect_obj_parameter['color_h'])
                print("[Color Detect] ","Coordinate:",color_coodinate,"Size",color_size)
    
        if flag_face is True:
            if Vilib.detect_obj_parameter['human_n'] == 0:
                print('Face Detect: None')
            else:
                human_coodinate = (Vilib.detect_obj_parameter['human_x'],Vilib.detect_obj_parameter['human_y'])
                human_size = (Vilib.detect_obj_parameter['human_w'],Vilib.detect_obj_parameter['human_h'])
                print("[Face Detect] ","Coordinate:",human_coodinate,"Size",human_size)
    
    
    def main():
        global flag_face, flag_color, qr_code_flag
        qrcode_thread = None
    
        Vilib.camera_start(vflip=False,hflip=False)
        Vilib.display(local=True,web=True)
        print(MANUAL)
    
        while True:
            # readkey
            key = input()
            key = key.lower()
            # take photo
            if key == 'q':
                take_photo()
            # color detect         
            elif key != '' and key in ('0123456'):  # '' in ('0123') -> True
                index = int(key)
                if index == 0:
                    flag_color = False
                    Vilib.color_detect('close')
                else:
                    flag_color = True
                    Vilib.color_detect(color_list[index]) # color_detect(color:str -> color_name/close)
                print('Color detect : %s'%color_list[index])  
            # face detection
            elif key =="f":
                flag_face = not flag_face
                face_detect(flag_face)
            # qrcode detection
            elif key =="r":
                qr_code_flag = not qr_code_flag
                if qr_code_flag == True:
                    if qrcode_thread == None or not qrcode_thread.is_alive():
                        qrcode_thread = threading.Thread(target=qrcode_detect)
                        qrcode_thread.setDaemon(True)
                        qrcode_thread.start()
                else:
                    if qrcode_thread != None and qrcode_thread.is_alive(): 
                       # wait for thread to end 
                        qrcode_thread.join()
                        print('QRcode Detect: close')
            # show detected object information
            elif key == "s":
                object_show()
    
            sleep(0.5)
    
    
    if __name__ == "__main__":
        main()

**工作原理**

首先需要注意以下函数，这两个函数可以启动摄像头：  

.. code-block:: python

    Vilib.camera_start()
    Vilib.display()

与“目标检测”相关的函数有：  

* ``Vilib.face_detect_switch(True)`` : 开/关人脸检测  
* ``Vilib.color_detect(color)`` : 进行颜色检测，同一时间只能检测一种颜色。可输入的参数有： ``"red"`` 、 ``"orange"`` 、 ``"yellow"`` 、 ``"green"`` 、 ``"blue"`` 、 ``"purple"``  
* ``Vilib.color_detect_switch(False)`` : 关闭颜色检测  
* ``Vilib.qrcode_detect_switch(False)`` : 开/关二维码检测，并返回二维码的解码数据  
* ``Vilib.gesture_detect_switch(False)`` : 开/关手势检测  
* ``Vilib.traffic_sign_detect_switch(False)`` : 开/关交通标志检测  

目标检测到的信息会存储在 ``detect_obj_parameter = Manager().dict()`` 字典中。  

在主程序中，可以这样调用：  

.. code-block:: python

    Vilib.detect_obj_parameter['color_x']

字典中的键及其含义如下：  

* ``color_x``: 检测到的颜色块中心点 x 坐标，范围 0~320  
* ``color_y``: 检测到的颜色块中心点 y 坐标，范围 0~240  
* ``color_w``: 检测到的颜色块宽度，范围 0~320  
* ``color_h``: 检测到的颜色块高度，范围 0~240  
* ``color_n``: 检测到的颜色块数量  
* ``human_x``: 检测到的人脸中心点 x 坐标，范围 0~320  
* ``human_y``: 检测到的人脸中心点 y 坐标，范围 0~240  
* ``human_w``: 检测到的人脸宽度，范围 0~320  
* ``human_h``: 检测到的人脸高度，范围 0~240  
* ``human_n``: 检测到的人脸数量  
* ``traffic_sign_x``: 检测到的交通标志中心点 x 坐标，范围 0~320  
* ``traffic_sign_y``: 检测到的交通标志中心点 y 坐标，范围 0~240  
* ``traffic_sign_w``: 检测到的交通标志宽度，范围 0~320  
* ``traffic_sign_h``: 检测到的交通标志高度，范围 0~320  
* ``traffic_sign_t``: 检测到的交通标志内容，可选值为 `['stop','right','left','forward']`  
* ``gesture_x``: 检测到的手势中心点 x 坐标，范围 0~320  
* ``gesture_y``: 检测到的手势中心点 y 坐标，范围 0~240  
* ``gesture_w``: 检测到的手势宽度，范围 0~320  
* ``gesture_h``: 检测到的手势高度，范围 0~320  
* ``gesture_t``: 检测到的手势内容，可选值为 `["paper","scissor","rock"]`  
* ``qr_date``: 检测到的二维码内容  
* ``qr_x``: 检测到的二维码中心点 x 坐标，范围 0~320  
* ``qr_y``: 检测到的二维码中心点 y 坐标，范围 0~240  
* ``qr_w``: 检测到的二维码宽度，范围 0~320  
* ``qr_h``: 检测到的二维码高度，范围 0~240  


