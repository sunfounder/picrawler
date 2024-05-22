.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_keyboard:

Keyboard Control
=======================

In this project, we will learn how to use the keyboard to remotely control the PiCrawler. You can control the PiCrawler to move forward, backward, left, and right.


**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picrawler/examples
    sudo python3 keyboard_control.py

Press keys on keyboard to control PiCrawler!
* w: Forward
* a: Turn left
* s: Backward
* d: Turn right
* esc: Quit


**Code**

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



**How it works?**

PiCrawler should take appropriate action based on the keyboard characters read. The ``lower()`` function converts upper case characters into lower case characters, so that the letter remains valid regardless of case.

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

