.. _py_pose:

姿态
=============

PiCrawler 可以通过编写坐标数组来摆出特定的姿态。这里演示的是抬起右后腿的姿势。

.. image:: img/4cood.A.png

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 do_step.py

运行程序后，机器人首先会缓慢站立起来，以达到稳定的姿态。

站立完成后，机器人会在循环中重复执行两个动作。它首先进入一个站立步态姿势，并保持该姿势几秒钟，然后切换到一个自定义步态，使四条腿移动到不同的坐标位置。这样就形成了一个重复的姿态变化动作。

机器人会持续在这两种姿态之间交替运行，直到程序被停止。如果按下 **Ctrl+C**，程序会安全退出，机器人也会回到坐下的姿态。

**代码**

.. raw:: html

    <run></run>

.. code-block:: python

    #!/usr/bin/env python3
    from picrawler import Picrawler
    from time import sleep

    # Create Picrawler instance
    crawler = Picrawler()

    # Leg order:
    # [right front], [left front], [left rear], [right rear]
    new_step = [[45, 45, -75], [45, 0, -75], [45, 0, -30], [45, 45, -75]]

    # Get the default stand step from the move list
    stand_step = crawler.move_list['stand'][0]


    def main():
        action_speed = 80  # Speed for movement actions

        try:
            # Stand up slowly at 40% speed to reduce current spikes
            crawler.do_step('stand', 40)
            sleep(1.0)

            # Continuous action loop
            while True:
                crawler.do_step(stand_step, action_speed)
                sleep(3)

                crawler.do_step(new_step, action_speed)
                sleep(3)

        except KeyboardInterrupt:
            # Handle Ctrl+C for safe exit
            print("\nExiting safely...")

        finally:
            # Return to sitting position before shutting down
            try:
                crawler.do_step('sit', 40)
                sleep(1.0)
            except Exception:
                pass


    if __name__ == "__main__":
        main()

**它是如何工作的？**

在这段代码中，你需要特别关注的是 ``crawler.do_step()`` 。

与 ``do_action()`` 类似， ``do_step()`` 也能控制 PiCrawler 的动作。  
不同之处在于：前者用于执行连续动作，例如 ``move forward`` ；而后者则用来实现 ``stand`` 、 ``sit`` 等独立的姿态。


它有两种用法：


第一种：可以直接传入字符串，调用 ``picrawler`` 库中的 ``step_list`` 字典。

.. code-block:: python

    crawler.do_step('stand',speed) 
    # "speed" 表示动作速度，范围为 0~100。


第二种：也可以直接传入包含 4 组坐标值的数组。

.. code-block:: python

    new_step=[[45, 45, -75], [45, 0, -75], [45, 0, -30], [45, 45, -75]]
    # 这四组坐标分别用于控制右前腿、左前腿、左后腿和右后腿。

每条腿都有独立的坐标系，如下图所示：

.. image:: img/4cood.png

你需要分别测量每个足端的坐标，如下图所示：

.. image:: img/1cood.png


顺带一提：第一种方法中调用的 ``step_list`` 其实也是由 4 组坐标值数组组成的。

.. code-block:: python

    step_list = {

        "stand":[
            [45, 45, -50], 
            [45, 45, -50], 
            [45, 45, -50], 
            [45, 45, -50]
        ],
        "sit":[
            [45, 45, -30], 
            [45, 45, -30], 
            [45, 45, -30], 
            [45, 45, -30]
        ],
              
    }
    




