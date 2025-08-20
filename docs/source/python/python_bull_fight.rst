.. _py_bull:

斗牛
==========

让 PiCrawler 变身愤怒的公牛！利用摄像头锁定红布并发起冲击！


**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 bull_fight.py


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

然后在浏览器中输入 ``http://<your IP>:9000/mjpg`` 即可查看视频画面，例如： ``https://192.168.18.113:9000/mjpg``  

.. image:: img/display.png

**代码**

.. note::  
    你可以对以下代码进行 **Modify/Reset/Copy/Run/Stop** 操作。但在此之前，需要进入源码路径，如 ``picrawler\examples``。修改后可直接运行查看效果。  


.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep
    from robot_hat import Music
    from vilib import Vilib
    
    
    crawler = Picrawler() 
    
    music = Music()
    
    def main():
        Vilib.camera_start()
        Vilib.display()
        Vilib.color_detect("red") 
        speed = 80
    
        while True:
            if Vilib.detect_obj_parameter['color_n']!=0:
                coordinate_x = Vilib.detect_obj_parameter['color_x']
                music.sound_play_threading('./sounds/talk1.wav')
    
                if coordinate_x < 100:
                    crawler.do_action('turn left',1,speed)
                    sleep(0.05) 
                elif coordinate_x > 220:
                    crawler.do_action('turn right',1,speed)
                    sleep(0.05) 
                else :
                    crawler.do_action('forward',2,speed)
                    sleep(0.05)    
            else :
                crawler.do_step('stand',speed)
                sleep(0.05)
    
    
    if __name__ == "__main__":
        main()


**工作原理**

总体而言，本项目结合了 :ref:`py_move`、:ref:`py_vision` 与 :ref:`py_sound` 的相关知识点。  

其流程如下图所示：  

.. image:: img/bull_fight-f.png

