Mix Step
=================

如果你对反复测量多个坐标感到厌倦，可以尝试在现有的Step中快速生成新的一个.



**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picrawler/examples
    sudo python3 mix_step.py



**Code**

.. code-block:: python


    from picrawler import Picrawler
    from time import sleep

    crawler = Picrawler([10,11,12,4,5,6,1,2,3,7,8,9]) 
    #crawler.set_offset([0,0,0,0,0,0,0,0,0,0,0,0])
    speed = 80

    # mix_step
    def my_mix_step():

        crawler.do_step('sit',speed=100)
        sleep(0.5)
        basic_step = []
        basic_step = crawler.step_list.get("sit")
        print(basic_step)
        left_hand  = crawler.mix_step(basic_step,0,[0,50,80])
        right_hand  = crawler.mix_step(basic_step,1,[0,50,80])
        two_hand = crawler.mix_step(left_hand,1,[0,50,80])

        speed = 100
        while True:
            
            crawler.do_step(left_hand,speed)
            sleep(0.6)
            crawler.do_step(two_hand,speed)
            sleep(0.6)
            crawler.do_step(right_hand,speed)
            sleep(0.6)
            crawler.do_step('sit',speed)
            sleep(0.6)

    # main
    def main():
        my_mix_step()
        sleep(0.05)

    if __name__ == "__main__":
        main()

**How it works?**

首先，我们获取 ``step_list`` 现成的 ``'sit'`` step，赋值到 ``basic_step`` 。

.. code-block:: python

    basic_step = []
    basic_step = crawler.step_list.get("sit")

然后，用 ``mix_step(step_list_value,leg,coordinate)`` 替换掉原步态的某一个脚的坐标值。

.. code-block:: python

    left_hand  = crawler.mix_step(basic_step,0,[0,50,80])
    right_hand  = crawler.mix_step(basic_step,1,[0,50,80])
    two_hand = crawler.mix_step(left_hand,1,[0,50,80])

就这样，我们生成了三个新的step。