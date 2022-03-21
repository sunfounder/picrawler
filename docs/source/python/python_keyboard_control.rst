.. _py_remote_control:

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
* 按下 ``esc`` 退出程序。

**代码**

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep
    import readchar

    crawler = Picrawler([10,11,12,4,5,6,1,2,3,7,8,9]) 
    speed = 90

    manual = '''
    Press keys on keyboard to control PiCrawler!
        w: Forward
        a: Turn left
        s: Backward
        d: Turn right
        esc: Quit
    '''

    def show_info():
        print("\033[H\033[J",end='')  # clear terminal windows 
        print(manual)


    def main(): 
        show_info()   
        while True:
            key = readchar.readkey()
            key = key.lower()
            if key in('wsad'):
                if 'w' == key:
                    crawler.do_action('forward',1,speed)     
                elif 's' == key:
                    crawler.do_action('backward',1,speed)          
                elif 'a' == key:
                    crawler.do_action('turn left',1,speed)           
                elif 'd' == key:
                    crawler.do_action('turn right',1,speed)
                sleep(0.05)
                show_info()  
            elif key == readchar.key.CTRL_C or key in readchar.key.ESCAPE_SEQUENCES:
                print("\n Quit") 
                break    
            
            sleep(0.02)          
        
    
    if __name__ == "__main__":
        main()



**这个怎么运作?**

根据读取的键盘字符，让PiCrawler做我们设置的动作。 ``lower()`` 是将读取的按键字符转化成小写字符，这样无论读取了该字母的大小写，都是有效的。

.. code-block:: python

    while True:
        key = readchar.readkey()
        key = key.lower()
        if key in('wsad'):
        if 'w' == key:
            crawler.do_action('forward',1,speed)     
        elif 's' == key:
            crawler.do_action('backward',1,speed)     
        elif 'a' == key:
            crawler.do_action('turn left',1,speed)     
        elif 'd' == key:
            crawler.do_action('turn right',1,speed)
        sleep(0.05)
        show_info()  
        elif key == readchar.key.CTRL_C or key in readchar.key.ESCAPE_SEQUENCES:
        print("\n Quit") 
            break 

