情感机器人
===============

这个例子展示了 PiCrawler 的几个有趣的自定义动作。

.. image:: image/emotional.png

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picrawler/examples
    sudo python3 emotional_robot.py

代码运行后，你会看到PiCrawler做一些有趣的动作，比如游泳，俯卧撑，摆手和摇摆。

**代码**

.. raw:: html

    <run></run>


.. code-block:: python

    from picrawler import Picrawler
    from time import sleep

    crawler = Picrawler([10,11,12,4,5,6,1,2,3,7,8,9]) 
    #crawler.set_offset([0,0,0,0,0,0,0,0,0,0,0,0])

    def handwork(speed):

        basic_step = []
        basic_step = crawler.step_list.get("sit")
        left_hand  = crawler.mix_step(basic_step,0,[0,50,80])
        right_hand  = crawler.mix_step(basic_step,1,[0,50,80])
        two_hand = crawler.mix_step(left_hand,1,[0,50,80])

        crawler.do_step('sit',speed)
        sleep(0.6)    
        crawler.do_step(left_hand,speed)
        sleep(0.6)
        crawler.do_step(two_hand,speed)
        sleep(0.6)
        crawler.do_step(right_hand,speed)
        sleep(0.6)
        crawler.do_step('sit',speed)
        sleep(0.6)

    def twist(speed):

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

    ##"[[right front], [left front], [left rear], [left rear]]")

    def pushup(speed):
        up=[[80, 0, -100], [80, 0, -100],[0, 120, -60], [0, 120, -60]]
        down=[[80, 0, -30], [80, 0, -30],[0, 120, -60], [0, 120, -60]]
        crawler.do_step(up,speed)
        sleep(0.6)
        crawler.do_step(down,speed)
        sleep(0.6)

    def swimming(speed):
        for i in range(100):
            crawler.do_step([[100-i,i,0],[100-i,i,0],[0,120,-60+i/5],[0,100,-40-i/5]],speed)

    # main
    def main():
        speed = 100
        
        swimming(speed)
        pushup(speed)
        handwork(speed)
        twist(speed)

        sleep(0.05)

    if __name__ == "__main__":
        main()
    
    