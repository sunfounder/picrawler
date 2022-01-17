记录新的动作
=================

我们用键盘控制PiCrawler依次摆出几个动作，并记录下这些动作。然后让PiCrawler重复这些动作。

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picrawler/examples
    sudo python3 record_new_step_by_keyboard.py

代码运行后，请根据终端弹出的提示进行操作。

* 按下1234来分别选择脚， ``1``：右前脚， ``2``：左前脚， ``3``：左后脚， ``4``：右后脚
* 按下 ``w``， ``a``， ``s``， ``d``， ``r``，和 ``f`` 来慢慢控制PiCrawler的坐标值。
* 按下 ``空格键`` 来打印所有的坐标值并且保存这一动作。
* 按下 ``p`` 来让PiCrawler来复现记录的动作。
* 按下 ``esc`` 来退出。

**代码**

.. code-block:: python


    from picrawler import Picrawler
    from time import sleep
    import sys
    import tty
    import termios
    import copy

    crawler = Picrawler([10,11,12,4,5,6,1,2,3,7,8,9]) 
    #crawler.set_offset([0,0,0,0,0,0,0,0,0,0,0,0])
    speed = 80

    def readchar():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


    manual = '''
    Press keys on keyboard to control PiCrawler!
        w: Y++
        a: X--
        s: Y--
        d: X++
        r: Z++
        f: Z--
        1: Select right front leg
        2: Select left front leg
        3: Select left rear leg
        4: Select right rear leg
        space: Print all leg coodinate & Save this step
        p: Play all saved step
        esc: Quit
    '''


    new_step=[]

    def save_new_step():
        new_step.append(copy.deepcopy(crawler.current_step_all_leg_value()))
        print(new_step)

    def play_all_new_step():
        for step in new_step:
            crawler.do_step(step,speed)
            sleep(0.6)

    def main():  

        speed = 80
        print(manual)
        crawler.do_step('sit',speed)
        leg = 0 
        coodinate=crawler.current_step_leg_value(leg)   
        while True:
            key = readchar()
            print(key)
            if 'w' == key or 'W' == key:
                coodinate[1]=coodinate[1]+2    
            elif 's' == key or 'S' == key:
                coodinate[1]=coodinate[1]-2           
            elif 'a' == key or 'A' == key:
                coodinate[0]=coodinate[0]-2         
            elif 'd' == key or 'D' == key:
                coodinate[0]=coodinate[0]+2   
            elif 'r' == key or 'R' == key:
                coodinate[2]=coodinate[2]+2         
            elif 'f' == key or 'F' == key:
                coodinate[2]=coodinate[2]-2       
            elif '1' == key:
                leg=0
                coodinate=crawler.current_step_leg_value(leg)           
            elif '2' == key:
                leg=1   
                coodinate=crawler.current_step_leg_value(leg)              
            elif '3' == key:
                leg=2  
                coodinate=crawler.current_step_leg_value(leg)     
            elif '4' == key:
                leg=3     
                coodinate=crawler.current_step_leg_value(leg)  
            elif chr(32) == key:
                print("[[right front],[left front],[left rear],[right rear]]")
                print("saved new step")
                print(crawler.current_step_all_leg_value())
                save_new_step()
            elif 'p' == key or 'P' == key:
                play_all_new_step()
            elif chr(27) == key:# 27 for ESC
                break    

            sleep(0.05)
            crawler.do_single_leg(leg,coodinate,speed)          
        print("\n q Quit")  
                
    
    if __name__ == "__main__":
        main()


**这个怎么运作?**

这个项目参考自 :ref:`调整姿势` 。 我们增加了记录和回放功能。

记录功能由以下代码实现。

.. code-block:: python

    new_step=[]

    def save_new_step():
        new_step.append(copy.deepcopy(crawler.current_step_all_leg_value()))
        print(new_step)

.. note:: 
    这里的赋值需要用到 `Deep Copy <https://docs.python.org/3/library/copy.html>`_ 函数, 否则赋值的时候 ``new_step`` 将不会被分配新的数组对象。


回放功能由以下代码实现。

.. code-block:: python

    def play_all_new_step():
        for step in new_step:
            crawler.do_step(step,speed)
            sleep(0.6)