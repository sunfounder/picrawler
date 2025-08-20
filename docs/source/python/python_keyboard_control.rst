.. _py_keyboard:

键盘控制
=======================

在本项目中，我们将学习如何使用键盘远程控制 PiCrawler。你可以通过键盘操作让 PiCrawler 前进、后退、左转或右转。


**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 keyboard_control.py

通过键盘按键来控制 PiCrawler！

* ``w``: 前进
* ``a``: 左转
* ``s``: 后退
* ``d``: 右转
* ``Ctrl+C``: 退出


**代码**

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep
    import readchar

    crawler = Picrawler() 
    speed = 90

    manual = '''
    Press keys on keyboard to control PiCrawler!
        W: Forward
        A: Turn left
        S: Backward
        D: Turn right

        Ctrl^C: Quit
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
            elif key == readchar.key.CTRL_C:
                print("\n Quit") 
                break    

            sleep(0.02)          

    
    if __name__ == "__main__":
        main()

**它是如何工作的？**

PiCrawler 会根据读取到的键盘按键执行相应的动作。 ``lower()`` 函数用于将大写字母转换为小写字母，这样无论输入大小写，都能保持按键有效。

.. code-block:: python

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
            elif key == readchar.key.CTRL_C:
                print("\n Quit") 
                break    
            
            sleep(0.02)  
