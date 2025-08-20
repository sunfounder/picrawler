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


**代码**

.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep

    crawler = Picrawler() 

    ## [右前腿],[左前腿],[左后腿],[右后腿]
    new_step=[[45, 45, -75], [45, 0, -75], [45, 0, -30], [45, 45, -75]]
    stand_step = crawler.move_list['stand'][0]

    def main():  
        while True:
            speed = 80

            print(f"stand step: {stand_step}")
            crawler.do_step(stand_step, speed)
            sleep(3)
            print(f"new step: {new_step}")
            crawler.do_step(new_step,speed)
            sleep(3)

    
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
    




