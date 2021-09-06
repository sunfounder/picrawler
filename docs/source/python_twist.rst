Twist
==============

我们已经知道了如何让PiCrawler摆出特定的姿势，接下来就是将姿势组合起来，形成连续的动作。

在这里让PiCrawler的四只脚两两起伏，随着音乐蹦跶。

**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picrawler/examples
    sudo python3 twist.py


**Code**

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep
    from robot_hat import Music

    music = Music()
    crawler = Picrawler([10,11,12,4,5,6,1,2,3,7,8,9]) 
    #crawler.set_offset([0,0,0,0,0,0,0,0,0,0,0,0])


    def twist(speed):
         ## [right front],[left front],[left rear],[left rear]
        new_step=[[50, 50, -80], [50, 50, -80],[50, 50, -80], [50, 50, -80]]
        for i in range(4):
            for inc in range(30,60,5): 
                rise = [50,50,(-80+inc*0.5)]
                drop = [50,50,(-80-inc)]

                new_step[i]=rise
                new_step[(i+2)%4] = drop
                new_step[(i+1)%4] = rise
                new_step[(i-1)%4] = drop
                crawler.do_step(new_step,speed)

    def main():  

        music.background_music('./musics/sports-Ahjay_Stelino.mp3')
        music.music_set_volume(20)

        while True:
            twist(speed=100) 
                
    
    if __name__ == "__main__":
        main()


**How it works?**

在这个代码中，你需要注意的是这一部分：

.. code-block:: python

    def twist(speed):
        ## [right front],[left front],[left rear],[left rear]
        new_step=[[50, 50, -80], [50, 50, -80],[50, 50, -80], [50, 50, -80]]
        for i in range(4):
            for inc in range(30,60,5): 
                rise = [50,50,(-80+inc*0.5)]
                drop = [50,50,(-80-inc)]

                new_step[i]=rise
                new_step[(i+2)%4] = drop
                new_step[(i+1)%4] = rise
                new_step[(i-1)%4] = drop
                crawler.do_step(new_step,speed)

简单的说，它就是使用了两层for循环来让 ``new_step`` 数组产生持续且规律的变化，同时由 ``crawler.do_step()`` 把姿势执行出来，形成连续动作。

您可以从 :ref:`Do Single Leg` 中直观的获取到每个姿势所对应的坐标值数组。


除此之外，该示例还播放了背景音乐。其实现方法如下。

Play music by importing the following libraries.

.. code-block:: python

    from robot_hat import Music

声明一个 Music 对象

.. code-block:: python

    music = Music()

Play the background music in the ``picrawler/examples/musics`` directory and set the volume to 20. You can also add music to the ``musics`` folder via :ref:`Filezilla Software`.

.. code-block:: python

    music.background_music('./musics/sports-Ahjay_Stelino.mp3')
    music.music_set_volume(20)


.. note::

    You can add different sound effects or music to ``musics`` or ``sounds`` folder via :ref:`Filezilla Software`.