.. _py_avoid:

避障功能
=====================

在本项目中，PiCrawler 将使用超声波模块检测前方的障碍物。  
当检测到障碍物时，PiCrawler 会发送信号，并寻找其他方向继续前进。  


**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 avoid.py

代码运行后，PiCrawler 会开始向前行走。如果检测到前方障碍物距离小于 10cm，它会停止并发出提示音，然后左转并暂停。若左转方向无障碍物，或障碍物距离大于 10cm，它将继续向前移动。  



**代码**

.. note::  
    你可以对下面的代码进行 **Modify/Reset/Copy/Run/Stop** 操作。但在此之前，需要先进入源码路径，如 ``picrawler\examples``。修改代码后，可以直接运行查看效果。  

.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from robot_hat import TTS, Music
    from robot_hat import Ultrasonic
    from robot_hat import Pin
    import time

    tts = TTS()
    music = Music()

    crawler = Picrawler() 
    sonar = Ultrasonic(Pin("D2") ,Pin("D3"))
    music.music_set_volume(100)

    alert_distance = 15
    speed = 80

    def main():
        distance = sonar.read()
        print(distance)
        if distance < 0:
            pass
        elif distance <= alert_distance:
            try:
                music.sound_play_threading('./sounds/sign.wav', volume=100)
            except Exception as e:
                print(e)
            crawler.do_action('turn left angle',3,speed)
            time.sleep(0.2)
        else :
            crawler.do_action('forward', 1,speed)
            time.sleep(0.2)

    if __name__ == "__main__":
        while True:
            main()

**工作原理**

你可以通过导入 ``Ultrasonic`` 类来获取测距功能。  

.. code-block:: python

    from robot_hat import Ultrasonic

接着初始化超声波引脚。  

.. code-block:: python

    sonar = Ultrasonic(Pin("D2") ,Pin("D3"))


以下是主程序逻辑：  

* 读取超声波模块检测到的 ``distance``，并过滤掉小于 0 的值（当超声波模块距离障碍物过远或数据读取异常时，可能会返回 ``distance < 0`` ）。  
* 当 ``distance`` 小于或等于 ``alert_distance``（之前设置的阈值，这里为 10）时，播放提示音 ``sign.wav`` ，并执行 ``turn left angle`` 动作。  
* 当 ``distance`` 大于 ``alert_distance`` 时，PiCrawler 将执行 ``forward`` 前进动作。  

.. code-block:: python

    distance = sonar.read()
    print(distance)
    if distance < 0:
        pass
    elif distance <= alert_distance:
        try:
            music.sound_play_threading('./sounds/sign.wav', volume=100)
        except Exception as e:
            print(e)
        crawler.do_action('turn left angle',3,speed)
        time.sleep(0.2)
    else :
        crawler.do_action('forward', 1,speed)
        time.sleep(0.2)


.. note::  

    你可以通过 :ref:`filezilla` 将不同的音效或音乐添加到 ``musics`` 或 ``sounds`` 文件夹中。  