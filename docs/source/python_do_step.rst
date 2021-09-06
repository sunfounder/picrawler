Do Step
=============

在这个示例中，我们让PiCrawler摆出特定的Postion。


**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picrawler/examples
    sudo python3 do_step.py


**Code**

.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep

    crawler = Picrawler([10,11,12,4,5,6,1,2,3,7,8,9]) 
    #crawler.set_offset([0,0,0,0,0,0,0,0,0,0,0,0])

    ## [right front],[left front],[left rear],[left rear]
    new_step=[[50, 50, -80], [50, 50, -80],[80, 80, 0], [50, 50, -80]]

    def main():  
        
        speed = 100
            
        while True:
            
            crawler.do_step('stand',speed)
            print(crawler.step_list.get('stand'))
            sleep(3)
            crawler.do_step(new_step,speed)
            print(new_step)
            sleep(3)

if __name__ == "__main__":
    main()


**How it works?**

在这个代码中，你需要关注的代码是这个 ``crawler.do_step()`` 。 

与 ``do_action()`` 相似， ``do_step()`` 也可以操控PiCrawler的行为。
不同的是，前者可以做出 ``move forward`` 这种连续的行为，而后者则是用于做出 ``stand`` 与 ``sit`` 这种单独的姿势。


它有两种用法:


其一：它可以写入字符串，直接使用 ``picrawler`` 库中的 ``step_list`` 字典.

.. code-block:: python

    crawler.do_step('stand',speed) 
    # "speed" indicates the speed of the step, the range is 0~100.


其二：它也可以写入一组记录了4个坐标值的数组.

.. code-block:: python

    crawler.do_step([[50, 50, -80], [50, 50, -80],[80, 80, 0], [50, 50, -80]],speed)
    # 这四个坐标分别用于控制 right front, left front, left rear, left rear 四个leg。

每个脚各自拥有一个独立的坐标系。如下图所示：

.. image:: image/

你需要单独测量每一个脚尖的坐标值。如下图所示：

.. image:: image/


顺带一提：第一种方法中调用的 ``step_list`` 同样由包含4个坐标值的数组组成。

.. code-block:: python

    step_list = {
        "stand":[
            [50, 50, -80],
            [50, 50, -80],
            [50, 50, -80],
            [50, 50, -80]
        ],
        "sit":[
            [50, 50, -33],
            [50, 50, -33],
            [50, 50, -33],
            [50, 50, -33]
        ],
    }





