.. _py_move:

移动
==============

这是 PiCrawler 的第一个项目，用来展示它最基本的功能 —— 移动。


**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 move.py

当程序启动时，PiCrawler 会先站立起来，并短暂等待。

随后它会持续执行一个循环动作：
向前移动、向后移动、向左转、向右转、
小幅左转以及小幅右转。

每个动作之间都会加入短暂的延时，使运动更加平稳。

按下 Ctrl+C 可以停止程序。
在程序退出之前，机器人会安全地坐下。

**代码**

.. note::
    你可以对下面的代码进行 **Modify/Reset/Copy/Run/Stop** 操作。但在此之前，需要进入源码路径，例如 ``pisloth\examples``。修改代码后可直接运行并查看效果。

.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep

    crawler = Picrawler()  # Create PiCrawler object

    def main():
        speed = 80  # Movement speed

        try:
            crawler.do_step('stand', 40)  # Stand up
            sleep(1.0)

            while True:
                crawler.do_action('forward', 1, speed)   # Move forward
                sleep(0.25)

                crawler.do_action('backward', 1, speed)  # Move backward
                sleep(0.25)

                crawler.do_action('turn left', 1, speed)  # Turn left
                sleep(0.25)

                crawler.do_action('turn right', 1, speed)  # Turn right
                sleep(0.25)

                crawler.do_action('turn left angle', 1, speed)  # Small left turn
                sleep(0.3)

                crawler.do_action('turn right angle', 1, speed)  # Small right turn
                sleep(0.3)

                sleep(0.5)

        except KeyboardInterrupt:
            print("\nCtrl+C pressed...")

        finally:
            crawler.do_step('sit', 40)  # Sit down before exit
            sleep(1.0)

    if __name__ == "__main__":
        main()


**它是如何工作的？**

#. 导入与初始化

   .. code-block:: python

      from picrawler import Picrawler
      from time import sleep

      crawler = Picrawler()

   该脚本导入所需的模块，并创建一个
   ``Picrawler`` 对象，用于控制机器人的所有运动。

#. 主函数与初始化设置

   .. code-block:: python

      def main():
          speed = 80
          crawler.do_step('stand', 40)
          sleep(1.0)

   ``main()`` 函数中定义了机器人的运动速度。
   在进入循环之前，机器人会先站立起来并保持稳定。

#. 持续运动循环

   .. code-block:: python

      while True:
          crawler.do_action('forward', 1, speed)
          crawler.do_action('backward', 1, speed)
          crawler.do_action('turn left', 1, speed)
          crawler.do_action('turn right', 1, speed)
          crawler.do_action('turn left angle', 1, speed)
          crawler.do_action('turn right angle', 1, speed)

   机器人会在无限循环中持续执行一组预定义的
   运动动作。

   每个动作之间加入短暂延时，可以让动作更加平滑。

#. 安全退出处理

   .. code-block:: python

      except KeyboardInterrupt:
          print("\nCtrl+C pressed...")
      finally:
          crawler.do_step('sit', 40)

   ``try / except / finally`` 结构确保：

   - 按下 Ctrl+C 时可以安全地停止循环。
   - 程序退出前，机器人会先执行坐下动作。

#. 程序入口

   .. code-block:: python

      if __name__ == "__main__":
          main()

   该结构确保只有在脚本被直接运行时，
   才会执行 ``main()`` 函数。