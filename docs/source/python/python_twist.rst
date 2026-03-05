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

程序启动后，机器人会先缓慢站立起来，以达到稳定的姿态。

站立完成后，背景音乐开始播放。同时，机器人会持续执行扭动式的舞蹈动作。在这个动作过程中，四条腿会交替抬起和放下，形成有节奏的扭动效果。四条腿会以协调的方式成对运动，使机器人身体看起来像左右摆动。

每一步之间都会加入短暂的延时，使动作更加平滑和稳定，而不会显得突兀或过快。

机器人会在音乐播放的同时持续跳舞。当按下 **Ctrl+C** 时，程序会停止运行，机器人会在退出前安全地回到坐下的姿态。

**代码**

.. note::
    你可以对下面的代码进行 **Modify/Reset/Copy/Run/Stop** 操作。但在此之前，需要先进入源码路径，例如 ``picrawler\examples``。修改代码后，可以直接运行并查看效果。


.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from robot_hat import Music
    from time import sleep

    music = Music()
    crawler = Picrawler()

    def twist(speed):
        new_step = [[50, 50, -80], [50, 50, -80], [50, 50, -80], [50, 50, -80]]

        for i in range(4):
            for inc in range(30, 60, 5):
                rise = [50, 50, (-80 + inc * 0.5)]
                drop = [50, 50, (-80 - inc)]

                new_step[i] = rise
                new_step[(i + 2) % 4] = drop
                new_step[(i + 1) % 4] = rise
                new_step[(i - 1) % 4] = drop

                crawler.do_step(new_step, speed)
                sleep(0.03)  # small delay to make motion smoother and less "crazy"

    def main():
        try:
            # Stand up slowly first
            crawler.do_step('stand', 40)
            sleep(1.0)

            # Start music
            music.music_play('./musics/sports-Ahjay_Stelino.mp3')
            music.music_set_volume(20)

            while True:
                twist(speed=100)

        except KeyboardInterrupt:
            print("\nCtrl+C detected, exiting...")

        finally:
            # Sit down safely before exit
            try:
                crawler.do_step('sit', 40)
                sleep(1.0)
            except Exception:
                pass

    if __name__ == "__main__":
        main()

**它是如何工作的？**

在这段代码中，需要特别注意以下部分：

.. code-block:: python

    def twist(speed):
        new_step = [[50, 50, -80], [50, 50, -80], [50, 50, -80], [50, 50, -80]]

        for i in range(4):
            for inc in range(30, 60, 5):
                rise = [50, 50, (-80 + inc * 0.5)]
                drop = [50, 50, (-80 - inc)]

                new_step[i] = rise
                new_step[(i + 2) % 4] = drop
                new_step[(i + 1) % 4] = rise
                new_step[(i - 1) % 4] = drop

                crawler.do_step(new_step, speed)
                sleep(0.03)  # small delay to make motion smoother and less "crazy"

简单来说，这段代码使用两层 ``for`` 循环，使 ``new_step`` 数组持续产生规律变化，同时通过 ``crawler.do_step()`` 执行姿态，从而形成连续的动作。

你可以通过 :ref:`py_posture` 直观地查看每个姿态对应的坐标数组。

此外，该示例还播放了背景音乐，具体实现方法如下。

通过导入以下库来播放音乐：

.. code-block:: python

    from robot_hat import Music

声明一个 Music 对象：

.. code-block:: python

    music = Music()

播放 ``picrawler/examples/musics`` 目录中的背景音乐，并将音量设置为 20。你也可以通过 :ref:`filezilla` 向 ``musics`` 文件夹中添加自己的音乐。

.. code-block:: python

    music.music_play('./musics/sports-Ahjay_Stelino.mp3')
    music.music_set_volume(20)