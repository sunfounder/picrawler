Do Single Leg
=====================

在这个示例中，我们用键盘来对PiCrawler的逐个脚进行控制，摆出想要的姿势。

你可以按下空格键将当前的坐标值打印出来，这些坐标值在你为PiCrawler创造独特的行为时派上用场。


**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picrawler/examples
    sudo python3 do_step.py

代码运行后，请根据terminal中弹出的提示进行操作。

**Code**

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
    Press keys on keyboard to control PiSloth!
        W: Y++
        A: X--
        S: Y--
        D: X++
        R: Z++
        F: Z--
        1: Select right front leg
        2: Select left front leg
        3: Select left rear leg
        4: Select right rear leg
        Space: Print all leg coodinate
        ESC: Quit
    '''

    def main():  

        speed = 80
        print(manual)
        crawler.do_step('stand',speed)
        leg = 0 
        coodinate=crawler.current_step_leg_value(leg)   
        while True:
            key = readchar()
            print(key)
            if 'w' == key:
                coodinate[1]=coodinate[1]+5    
            elif 's' == key:
                coodinate[1]=coodinate[1]-5           
            elif 'a' == key:
                coodinate[0]=coodinate[0]-5         
            elif 'd' == key:
                coodinate[0]=coodinate[0]+5   
            elif 'r' == key:
                coodinate[2]=coodinate[2]+5         
            elif 'f' == key:
                coodinate[2]=coodinate[2]-5       
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
                print("[[right front], [left front], [left read], [left rear]]")
                print(crawler.current_step_all_leg_value())

            elif chr(27) == key:# 27 for ESC
                break    

            sleep(0.05)
            crawler.do_single_leg(leg,coodinate,speed)          
        print("\n q Quit")  
            
    if __name__ == "__main__":
        main()

**How it works?**

在该项目中你需要注意的是以下三个函数：

.. code-block:: python

    current_step_leg_value(leg)
    current_step_all_leg_value()
    do_single_leg(leg,coodinate,speed) 

* ``current_step_leg_value(leg)`` : 返回对应脚的坐标值。参数 ``leg`` 可以为 ``0``, ``1``, ``2``, ``3`` 四个值，分别对应right front, left front, left rear, left rear 四个leg。
* ``current_step_all_leg_value()`` : 返回所有脚的坐标值。
* ``do_single_leg(leg,coodinate,speed)`` : 单独修改某一个脚的坐标值。