键盘控制
=======================

在这个项目中，我们将学习如何使用键盘远程控制 PiCrawler。您可以控制 PiCrawler 向前、向后、向左和向右移动。

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picrawler/examples
    sudo python3 keyboard_control.py

代码运行后，请根据终端弹出的提示进行操作。

* 按下 ``w``，让PiCrawler前进。
* 按下 ``a``，让PiCrawler左转。
* 按下 ``s``，让PiCrawler后退。
* 按下 ``d``，让PiCrawler右转。

**代码**

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep
    import sys
    import tty
    import termios



    crawler = Picrawler([10,11,12,4,5,6,1,2,3,7,8,9]) 
    #crawler.set_offset([0,0,0,0,0,0,0,0,0,0,0,0])
    speed = 90

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
        w: Forward
        a: Turn left
        s: Backward
        d: Turn right
    '''

    def main():  
        
        print(manual)
            
        while True:
            key = readchar()
            print(key)
            if 'w' == key or 'W' == key:
                crawler.do_action('forward',1,speed)     
            elif 's' == key or 'S' == key:
                crawler.do_action('backward',1,speed)          
            elif 'a' == key or 'A' == key:
                crawler.do_action('turn left',1,speed)           
            elif 'd' == key or 'D' == key:
                crawler.do_action('turn right',1,speed)
            elif chr(27) == key:# 27 for ESC
                break    

            sleep(0.05)          
        print("\n q Quit")  
                
    
    if __name__ == "__main__":
        main()



**这个怎么运作?**

下面这个函数引用标准输入流并返回读取的数据流的第一个字符。

* ``tty.setraw(sys.stdin.fileno)`` 就是将标准输入流改为raw模式，即传输过程中所有字符都不会被转义，包括特殊字符。更改模式前，请备份原模式，更改后恢复。
* ``old_settings = termios.tcgetattr(fd)`` 和 ``termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)`` 起到备份和恢复的作用。
        
.. code-block:: python

    def readchar():
		fd = sys.stdin.fileno() 
		old_settings = termios.tcgetattr(fd) 
		try:
			tty.setraw(sys.stdin.fileno())  
			ch = sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)  
		return ch

最后，根据读取的键盘字符，让PiCrawler做我们设置的动作。

.. code-block:: python

    while True:
        key = readchar()
        print(key)
        if 'w' == key or 'W' == key:
            crawler.do_action('forward',1,speed)     
        elif 's' == key or 'S' == key:
            crawler.do_action('backward',1,speed)          
        elif 'a' == key or 'A' == key:
            crawler.do_action('turn left',1,speed)           
        elif 'd' == key or 'D' == key:
            crawler.do_action('turn right',1,speed)
        elif chr(27) == key:# 27 for ESC
            break 

