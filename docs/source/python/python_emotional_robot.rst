.. _py_emotional:

情感机器人
===============

这个示例展示了 PiCrawler 的一些有趣自定义动作。

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 emotional_robot.py

运行程序后，机器人首先会缓慢站立起来，以达到稳定的姿态。

随后，机器人会依次执行一系列动作，包括类似游泳的动作、俯卧撑、用前腿挥动打招呼的动作，以及扭动身体的舞蹈。这些动作按顺序执行，使机器人表现出动态且富有表现力的行为。

如果按下 **Ctrl+C**，程序会安全退出，机器人也会回到坐下的姿态。

**代码**

.. note::
    你可以对下面的代码进行 **Modify/Reset/Copy/Run/Stop** 操作。但在此之前，请先进入源码路径，如 ``picrawler\examples`` 。修改完成后，可以直接运行查看效果。

.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep

    crawler = Picrawler()


    def get_sit_step():
        # Get a valid sit step used as the base pose for hand actions
        try:
            return crawler.move_list['sit'][0]
        except Exception:
            return None


    def handwork(speed):
        base = get_sit_step()

        # If a valid sit step cannot be retrieved, just perform a sit action
        if not base or len(base) < 4:
            crawler.do_step('sit', speed)
            sleep(0.6)
            return

        # Generate hand poses by modifying the sit step
        left_hand = crawler.mix_step(base, 0, [0, 50, 80])
        right_hand = crawler.mix_step(base, 1, [0, 50, 80])
        two_hand = crawler.mix_step(left_hand, 1, [0, 50, 80])

        crawler.do_step('sit', speed)
        sleep(0.6)

        crawler.do_step(left_hand, speed)
        sleep(0.6)

        crawler.do_step(two_hand, speed)
        sleep(0.6)

        crawler.do_step(right_hand, speed)
        sleep(0.6)

        crawler.do_step('sit', speed)
        sleep(0.6)

    def twist(speed):
        # Initialize the base position for all four legs
        new_step = [[50, 50, -80], [50, 50, -80], [50, 50, -80], [50, 50, -80]]

        # Create a twisting motion by alternating rise and drop movements
        for i in range(4):
            for inc in range(30, 60, 5):
                rise = [50, 50, (-80 + inc * 0.5)]
                drop = [50, 50, (-80 - inc)]

                new_step[i] = rise
                new_step[(i + 2) % 4] = drop
                new_step[(i + 1) % 4] = rise
                new_step[(i - 1) % 4] = drop

                crawler.do_step(new_step, speed)
                sleep(0.02)

    def pushup(speed):
        # Two poses used to simulate a push-up motion
        up = [[80, 0, -100], [80, 0, -100], [0, 120, -60], [0, 120, -60]]
        down = [[80, 0, -30], [80, 0, -30], [0, 120, -60], [0, 120, -60]]

        crawler.do_step(up, speed)
        sleep(0.6)

        crawler.do_step(down, speed)
        sleep(0.6)

    def swimming(speed, loops=100):
        # Simulate a swimming-like motion by gradually adjusting leg coordinates
        for i in range(loops):
            crawler.do_step(
                [
                    [100 - i, i, 0],
                    [100 - i, i, 0],
                    [0, 120, -60 + i / 5],
                    [0, 100, -40 - i / 5]
                ],
                speed
            )
            sleep(0.01)

    def main():
        speed = 100

        try:
            # Stand up slowly before performing actions
            crawler.do_step('stand', 40)
            sleep(1.0)

            swimming(speed)
            pushup(speed)
            handwork(speed)
            twist(speed)

        except KeyboardInterrupt:
            print("\nCtrl+C detected, exiting...")

        finally:
            # Return to a sitting posture before exiting
            try:
                crawler.do_step('sit', 40)
                sleep(1.0)
            except Exception:
                pass

    if __name__ == "__main__":
        main()

**工作原理**

#. 当程序启动时，机器人首先会缓慢站立起来，以达到稳定的姿态。

   .. code-block:: python
   
      crawler.do_step('stand', 40)
      sleep(1.0)

   站立完成后，程序会按顺序执行多个预定义动作。

#. 游泳动作

   机器人通过逐渐改变四条腿的坐标，模拟类似游泳的运动。

   .. code-block:: python

      for i in range(loops):
          crawler.do_step([
              [100-i, i, 0],
              [100-i, i, 0],
              [0,120,-60+i/5],
              [0,100,-40-i/5]
          ], speed)

#. 俯卧撑动作

   定义两个姿态来模拟俯卧撑的上下运动。

   .. code-block:: python

      up = [[80,0,-100],[80,0,-100],[0,120,-60],[0,120,-60]]
      down = [[80,0,-30],[80,0,-30],[0,120,-60],[0,120,-60]]

      crawler.do_step(up, speed)
      crawler.do_step(down, speed)

#. 挥手动作

   程序使用 ``mix_step()`` 修改前腿的坐标，
   从而实现挥手的动作效果。

   .. code-block:: python

      left_hand = crawler.mix_step(base,0,[0,50,80])
      right_hand = crawler.mix_step(base,1,[0,50,80])

#. 扭动动作

   机器人通过抬起和降低对角线的腿来扭动身体。

   .. code-block:: python

      rise = [50,50,(-80+inc*0.5)]
      drop = [50,50,(-80-inc)]
      crawler.do_step(new_step, speed)

#. 如果按下 **Ctrl+C**，程序会安全退出，机器人会回到坐下的姿态。

   .. code-block:: python
   
      crawler.do_step('sit', 40)

