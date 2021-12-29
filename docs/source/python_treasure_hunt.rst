寻宝
============================

在你的房间里布置一个迷宫，在六个角落放置六张不同颜色的卡片。然后控制PiCrawler一一搜索这些色卡吧！

.. note:: 
    
    您可以下载并打印文件 :download:`PDF 颜色卡片 <https://gitee.com/sunfounder/sf-pdf/raw/master/%E5%8D%A1%E7%89%87/%E7%9B%AE%E6%A0%87%E8%AF%86%E5%88%AB/%E9%A2%9C%E8%89%B2%E5%8D%A1.pdf>` 用于颜色检测。


**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picrawler/examples
    sudo python3 treasure_hunt.py


**查看图像**

代码运行后，在浏览器中进入 ``http://<your IP>:9000/mjpg`` 来查看视频画面。 比如:  ``https://192.168.18.113:9000/mjpg``

.. image:: image/display.png

然后按照终端打印的提示进行操作。

* 注意要将键盘切换为小写的英文输入。
* 按下 ``w``，让PiCrawler前进。
* 按下 ``a``，让PiCrawler左转。
* 按下 ``s``，让PiCrawler后退。
* 按下 ``d``，让PiCrawler右转。
* 按下 ``空格键`` 来让PiCrawler说一种颜色。
* 按下 ``esc`` 退出游戏。


**代码**

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep
    from robot_hat import Music,TTS
    from vilib import Vilib
    import sys
    import tty
    import termios
    import random


    crawler = Picrawler([10,11,12,4,5,6,1,2,3,7,8,9]) 
    #crawler.set_offset([0,0,0,0,0,0,0,0,0,0,0,0])

    music = Music()
    tts = TTS()

    def readchar():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


    manual = '''
    Press keys on keyboard to control Picrawler!
        w: Forward
        a: Turn left
        s: Backward
        s: Turn right
        space: Say the target again
        esc: Quit
    '''

    color = "red"
    color_list=["red","orange","yellow","green","blue","purple"]


    def renew_color_detect():
        global color
        color = random.choice(color_list)
        Vilib.color_detect(color)
        tts.say("Look for " + color)


    def main():
        Vilib.camera_start()
        Vilib.display()
        speed = 100
        print(manual)

        tts.say("game start")
        sleep(0.05)   
        renew_color_detect()

        while True:
            if Vilib.detect_obj_parameter['color_n']!=0 and Vilib.detect_obj_parameter['color_w']>100:
                tts.say("will done")
                sleep(0.05)   
                renew_color_detect()
                
            key = readchar()
            if 'w' == key:
                crawler.do_action('forward',1,speed)     
            elif 's' == key:
                crawler.do_action('backward',1,speed)          
            elif 'a' == key:
                crawler.do_action('turn left',1,speed)           
            elif 'd' == key:
                crawler.do_action('turn right',1,speed)
            elif chr(32) == key:
                tts.say("Look for " + color)
            elif chr(27) == key:# 27 for ESC
                break    

            sleep(0.05)          
        print("\n q Quit")  

    if __name__ == "__main__":
        main()


**怎么运行的?**

总的来说，这个项目结合了 :ref:`键盘控制`, :ref:`计算机视觉` 和 :ref:`音效`。

其流程如下图所示:

.. image:: image/treasure_hunt-f.png

