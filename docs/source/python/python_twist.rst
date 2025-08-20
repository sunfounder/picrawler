.. _py_twist:

扭动舞
==============

我们已经学会了如何让 PiCrawler 定格在某个特定姿势，下一步就是将这些姿势组合起来，形成连续的动作。

在这个示例中，PiCrawler 的四条腿两两抬起和落下，伴随音乐节奏跳动。

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 twist.py


**代码**

.. note::
    你可以对下面的代码进行 **Modify/Reset/Copy/Run/Stop** 操作。但在此之前，需要先进入源码路径，例如 ``picrawler\examples``。修改代码后，可以直接运行并查看效果。


.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from robot_hat import Music

    music = Music()
    crawler = Picrawler()


    def twist(speed):
        new_step=[[50, 50, -80], [50, 50, -80],[50, 50, -80], [50, 50, -80]]
        for i in range(4):
            for inc in range(30, 60, 5): 
                rise = [50,50,(-80+inc*0.5)]
                drop = [50,50,(-80-inc)]

                new_step[i]=rise
                new_step[(i+2)%4] = drop
                new_step[(i+1)%4] = rise
                new_step[(i-1)%4] = drop
                # print(new_step)
                crawler.do_step(new_step,speed)


    def main():  

        music.music_play('./musics/sports-Ahjay_Stelino.mp3')
        music.music_set_volume(20)

        while True:
            twist(speed=100) 

    
    if __name__ == "__main__":
        main()

**它是如何工作的？**

在这段代码中，需要特别注意以下部分：

.. code-block:: python

    def twist(speed):
        ## [右前腿],[左前腿],[左后腿],[右后腿]
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

简而言之，它通过两层 for 循环让 ``new_step`` 数组产生连续且有规律的变化，同时调用 ``crawler.do_step()`` 执行这些姿态，从而形成连贯的动作。

你可以从 :ref:`py_posture` 直观地获取每个姿态对应的坐标数组。


此外，该示例还播放了背景音乐，实现方法如下。

通过导入以下库来播放音乐：

.. code-block:: python

    from robot_hat import Music

声明一个 Music 对象：

.. code-block:: python

    music = Music()

播放 ``picrawler/examples/musics`` 目录下的背景音乐，并将音量设置为 20。你也可以通过 :ref:`filezilla` 向 ``musics`` 文件夹添加新的音乐文件。

.. code-block:: python

    music.music_play('./musics/sports-Ahjay_Stelino.mp3')
    music.music_set_volume(20)


.. note::

    你可以通过 :ref:`filezilla` 向 ``musics`` 或 ``sounds`` 文件夹添加不同的音效或音乐。