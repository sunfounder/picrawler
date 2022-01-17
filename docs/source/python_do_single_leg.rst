调整姿势
=====================

在这个例子中，我们使用键盘来控制 PiCrawler 的脚来摆出我们想要的姿势。

您可以按空格键打印出当前坐标值。当您为 PiCrawler 创建独特的动作时，这些坐标值会派上用场。

.. image:: image/1cood.A.png

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picrawler/examples
    sudo python3 do_single_leg.py

代码运行后，请根据终端弹出的提示进行操作。

* 按下1234来分别选择脚， ``1``：右前脚， ``2``：左前脚， ``3``：左后脚， ``4``：右后脚
* 按下 ``w``， ``a``， ``s``， ``d``， ``r``，和 ``f`` 来慢慢控制PiCrawler的坐标值。
* 按下 ``空格键`` 来打印所有的坐标值。
* 按下 ``esc`` 来退出。

**代码**

.. code-block:: python
 
    from picrawler import Picrawler
    from time import sleep
    import sys
    import tty
    import termios

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
        space: Print all leg coordinate
        esc: Quit
    '''

    def main():  

        speed = 80
        print(manual)
        crawler.do_step('stand',speed)
        leg = 0 
        coordinate=crawler.current_step_leg_value(leg)   
        while True:
            key = readchar()
            print(key)
            if 'w' == key or 'W' == key:
                coordinate[1]=coordinate[1]+5    
            elif 's' == key or 'S' == key:
                coordinate[1]=coordinate[1]-5           
            elif 'a' == key or 'A' == key:
                coordinate[0]=coordinate[0]-5         
            elif 'd' == key or 'D' == key:
                coordinate[0]=coordinate[0]+5   
            elif 'r' == key or 'R' == key:
                coordinate[2]=coordinate[2]+5         
            elif 'f' == key or 'F' == key:
                coordinate[2]=coordinate[2]-5       
            elif '1' == key:
                leg=0
                coordinate=crawler.current_step_leg_value(leg)           
            elif '2' == key:
                leg=1   
                coordinate=crawler.current_step_leg_value(leg)              
            elif '3' == key:
                leg=2  
                coordinate=crawler.current_step_leg_value(leg)     
            elif '4' == key:
                leg=3     
                coordinate=crawler.current_step_leg_value(leg)  
            elif chr(32) == key:
                print("[[right front],[left front],[left rear],[right rear]]")
                print(crawler.current_step_all_leg_value())

            elif chr(27) == key:# 27 for ESC
                break    

            sleep(0.05)
            crawler.do_single_leg(leg,coordinate,speed)          
        print("\n q Quit")  
            
    if __name__ == "__main__":
        main()

**这个怎么运作?**

在这个项目中需要注意的是以下三个函数：

.. code-block:: python

    current_step_leg_value(leg)
    current_step_all_leg_value()
    do_single_leg(leg,coordinate,speed) 

* ``current_step_leg_value(leg)`` : 返回对应腿的坐标值。参数 ``leg`` 可以是 ``0``, ``1``, ``2``, ``3`` 四个值, 分别对应右前，左前，左后，左后四条腿。
* ``current_step_all_leg_value()`` : 返回所有腿的坐标值。
* ``do_single_leg(leg,coordinate,speed)`` : 单独修改某条腿的坐标值。