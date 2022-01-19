避障
=====================

在这个项目中，picrawler 将使用超声波模块来检测前方的障碍物。当 PiCrawler 检测到障碍物时，它会发出信号并寻找另一个方向前进。

.. image:: img/avoid1.png

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picrawler/examples
    sudo python3 avoid.py

代码运行后，PiCrawler 会向前走。如果检测到前方障碍物的距离小于10cm，就会停下并发出警告，然后左转并继续检测。如果左转之后没有障碍物或障碍物距离大于10，则继续向前移动。


**代码**

.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from robot_hat import TTS, Music
    from robot_hat import Ultrasonic
    from robot_hat import Pin
    import time
    import os

    tts = TTS()
    music = Music()

    crawler = Picrawler([10,11,12,4,5,6,1,2,3,7,8,9]) 
    #crawler.set_offset([0,0,0,0,0,0,0,0,0,0,0,0])
    sonar = Ultrasonic(Pin("D2") ,Pin("D3"))

    alert_distance = 15

    speed = 100

    def main():
        distance = sonar.read()
        print(distance)
        if distance < 0:
            pass
        elif distance <= alert_distance:
            try:
                music.sound_effect_threading('./sounds/sign.wav')
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

**这个怎么运作?**

您可以通过导入 ``Ultrasonic`` 类来帮助你检测障碍物。

.. code-block:: python

    from robot_hat import Ultrasonic

然后初始化超声波引脚。

.. code-block:: python

    sonar = Ultrasonic(Pin("D2") ,Pin("D3"))


如下是主程序的逻辑。

* 读取超声波模块检测到的 ``distance`` 值，过滤掉小于0的值（当超声波模块距离障碍物太远或无法正确读取数据时，会出现 ``distance<0`` 的情况）。
  
* 当 ``distance`` 小于等于 ``alert_distance`` （之前设置的阈值，数值为10）时，播放音效 ``sign.wav``。并让 PiCrawler 执行 ``turn left angle`` 动作。

* 当 ``distance`` 大于 ``alert_distance`` 时，让 PiCrawler 执行 ``forward`` 动作。



.. code-block:: python

    distance = sonar.read()
    print(distance)
    if distance < 0:
        pass
    elif distance <= alert_distance:
        try:
            music.sound_effect_threading('./sounds/sign.wav')
        except Exception as e:
            print(e)
        crawler.do_action('turn left angle',3,speed)
        time.sleep(0.2)
    else :
        crawler.do_action('forward', 1,speed)
        time.sleep(0.2)


.. note::

    你可以通过 :ref:`Filezilla` 给 ``musics`` or ``sounds`` 文件夹添加不同的音乐或者音效。