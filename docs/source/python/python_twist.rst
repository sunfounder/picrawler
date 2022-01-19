组合动作
==============

我们已经知道如何让 PiCrawler 摆出一个特定的姿势，下一步就是将这些姿势组合起来形成一个连续的动作。

这个项目中，我们让 PiCrawler 的四只脚上下摆动，随着音乐跳跃。

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picrawler/examples
    sudo python3 twist.py

代码运行后，PiCrawler 的四只脚上下摆动，随着音乐跳跃。

**代码**

.. raw:: html

    <run></run>

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


**这个怎么运作?**

在这段代码中，需要注意下面这个部分:

.. code-block:: python

    def twist(speed):
        ## [right front],[left front],[left rear],[right rear]
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

简单的说，就是使用两层for循环，让 ``new_step`` 数组产生连续有规律的变化，同时用 ``crawler.do_step()`` 函数执行姿势，形成连续动作。

你可以从 :ref:`调整姿势` 课程中直观的获得每个动作对应的坐标值数组。

除此以外，该示例还可以播放背景音乐。实现方法如下。

通过导入以下库来播放音乐。

.. code-block:: python

    from robot_hat import Music

声明一个 Music 对象。

.. code-block:: python

    music = Music()

播放 ``picrawler/examples/musics`` 目录中的背景音乐，音量设置为20。 您也可以通过 :ref:`Filezilla` 软件将音乐添加到 ``musics`` 文件夹中。

.. code-block:: python

    music.background_music('./musics/sports-Ahjay_Stelino.mp3')
    music.music_set_volume(20)


.. note::

    您可以通过 :ref:`Filezilla` 软件向 ``musics`` 或 ``sounds`` 文件夹添加不同的音效或音乐。 