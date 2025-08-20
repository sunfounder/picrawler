.. _py_record:

记录新动作
=================

我们使用键盘依次控制 PiCrawler 做出几个姿态，并将这些姿态记录下来，之后可以进行回放。


**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 record_new_step_by_keyboard.py

代码运行后，请根据终端中弹出的提示进行操作。

* 按下 ``1234`` 分别选择不同的脚， ``1`` : 右前脚， ``2``: 左前脚， ``3``: 左后脚， ``4`` : 右后脚  
* 按下 ``w`` 、 ``a`` 、 ``s`` 、 ``d`` 、 ``r`` 、 ``f`` 来逐步控制 PiCrawler 的坐标值  
* 按下 ``space`` 打印所有坐标值  
* 按下 ``p`` 回放已记录的动作  
* 按下 ``esc`` 退出程序  


**代码**

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep
    import sys
    import tty
    import termios
    import copy

    crawler = Picrawler() 
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
    Press keys on keyboard to control!
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
        Space: Print all leg coodinate & Save this step
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
            key = key.lower()
            # print(key)
            if 'w' == key:
                coodinate[1]=coodinate[1]+2    
            elif 's' == key:
                coodinate[1]=coodinate[1]-2           
            elif 'a' == key:
                coodinate[0]=coodinate[0]-2         
            elif 'd' == key:
                coodinate[0]=coodinate[0]+2   
            elif 'r' == key:
                coodinate[2]=coodinate[2]+2         
            elif 'f' == key:
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
            elif 'p' == key:
                play_all_new_step()
            elif chr(27) == key:# 27 for ESC
                break    

            sleep(0.05)
            crawler.do_single_leg(leg,coodinate,speed)          
        print("\n q Quit")  

    
    if __name__ == "__main__":
        main()

**它是如何工作的？**

该项目基于 :ref:`py_posture` 开发，并新增了动作记录与回放功能。

动作记录功能由以下代码实现：

.. code-block:: python

    new_step=[]

    def save_new_step():
        new_step.append(copy.deepcopy(crawler.current_step_all_leg_value()))
        print(new_step)

.. note:: 
    这里必须使用 `Deep Copy <https://docs.python.org/3/library/copy.html>`_ ，否则在 ``append`` 时 ``new_step`` 不会得到一个新的数组对象。


动作回放功能由以下代码实现：

.. code-block:: python

    def play_all_new_step():
        for step in new_step:
            crawler.do_step(step,speed)
            sleep(0.6)