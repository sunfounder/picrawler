.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_twist:

Twist
==============

We already know how to make PiCrawler assume a specific pose, the next step is to combine the poses to form a continuous action.

Here, PiCrawler's four feet are up and down in twos, jumping with the music.

**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 twist.py


**Code**

.. note::
    You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you need to go to source code path like ``picrawler\examples``. After modifying the code, you can run it directly to see the effect.


.. raw:: html

    <run></run>

.. code-block:: python


    from picrawler import Picrawler
    from robot_hat import Music

    music = Music()
    crawler = Picrawler()


    def twist(speed):
        new_step=[[50, 50, -80], [50, 50, -80],[50, 50, -80], [50, 50, -80]]
        for i in range(4):
            for inc in range(30, 60, 5): 
                rise = [50,50,(-80+inc*0.5)]
                drop = [50,50,(-80-inc)]

                new_step[i]=rise
                new_step[(i+2)%4] = drop
                new_step[(i+1)%4] = rise
                new_step[(i-1)%4] = drop
                # print(new_step)
                crawler.do_step(new_step,speed)


    def main():  

        music.music_play('./musics/sports-Ahjay_Stelino.mp3')
        music.music_set_volume(20)

        while True:
            twist(speed=100) 
                
    
    if __name__ == "__main__":
        main()

**How it works?**

In this code, you need to pay attention to this part:

.. code-block:: python

    def twist(speed):
        ## [right front],[left front],[left rear],[right rear]
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

Simply put, it uses two layers of for loops to make the ``new_step`` array produce continuous and regular changes, and at the same time, ``crawler.do_step()`` executes the posture to form a continuous action.

You can intuitively get the coordinate value array corresponding to each pose from :ref:`py_posture`.


In addition, the example also played background music. The implementation method is as follows.

Play music by importing the following libraries.

.. code-block:: python

    from robot_hat import Music

Declare a Music object.

.. code-block:: python

    music = Music()

Play the background music in the ``picrawler/examples/musics`` directory and set the volume to 20. You can also add music to the ``musics`` folder via :ref:`filezilla`.

.. code-block:: python

    music.music_play('./musics/sports-Ahjay_Stelino.mp3')
    music.music_set_volume(20)


.. note::

    You can add different sound effects or music to ``musics`` or ``sounds`` folder via :ref:`filezilla`.