Keyboard Control
=======================

In this project, we will learn how to use the keyboard to remotely control the PiCrawler. You can control the PiCrawler to move forward, backward, left, and right.


**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picrawler/examples
    sudo python3 keyboard_control.py

**Code**

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
    Press keys on keyboard to control PiSloth!
        W: Forward
        A: Turn left
        S: Backward
        D: Turn right
    '''

    def main():  
        
        print(manual)
            
        while True:
            key = readchar()
            print(key)
            if 'w' == key:
                crawler.do_action('forward',1,speed)     
            elif 's' == key:
                crawler.do_action('backward',1,speed)          
            elif 'a' == key:
                crawler.do_action('turn left',1,speed)           
            elif 'd' == key:
                crawler.do_action('turn right',1,speed)
            elif chr(27) == key:# 27 for ESC
                break    

            sleep(0.05)          
        print("\n q Quit")  
                
    
    if __name__ == "__main__":
        main()



**How it works?**

This function refers to the standard input stream and returns the first character of the data stream read. 

* ``tty.setraw(sys.stdin.fileno)`` is to change the standard input stream to raw mode, that is, all characters will not be escaped during transmission, including special characters. Before changing the mode, back up the original mode, and restore it after the change. 
* ``old_settings = termios.tcgetattr(fd)`` and ``termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)`` plays the role of backup and restore.
        
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

Finally, according to the read keyboard characters, let PiCrawler do the actions we set.

.. code-block:: python

    key = readchar()
    print(key)
    if 'w' == key:
        crawler.do_action('forward',1,speed)     
    elif 's' == key:
        crawler.do_action('backward',1,speed)          
    elif 'a' == key:
        crawler.do_action('turn left',1,speed)           
    elif 'd' == key:
        crawler.do_action('turn right',1,speed)
    elif chr(27) == key:# 27 for ESC
        break  

