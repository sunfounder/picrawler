.. _py_pose:

Pose
=============

PiCrawler can assume a specific posture by writing a coordinate array. Here it assumes a raised right rear foot posture.

.. image:: img/4cood.A.png

**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picrawler/examples
    sudo python3 do_step.py


**Code**

.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep

    crawler = Picrawler([10,11,12,4,5,6,1,2,3,7,8,9]) 
    #crawler.set_offset([0,0,0,0,0,0,0,0,0,0,0,0])

    ## [right front],[left front],[left rear],[right rear]
    new_step=[[50, 50, -80], [50, 50, -80],[80, 80, 0], [50, 50, -80]]

    def main():  
        
        speed = 100
            
        while True:
            
            crawler.do_step('stand',speed)
            print(crawler.step_list.get('stand'))
            sleep(3)
            crawler.do_step(new_step,speed)
            print(new_step)
            sleep(3)

    if __name__ == "__main__":
        main()


**How it works?**

In this code, the code you need to pay attention to is this ``crawler.do_step()``.

Similar to ``do_action()``, ``do_step()`` can also manipulate PiCrawler's behavior.
The difference is that the former can perform the continuous behavior of ``move forward``, while the latter can be used to make separate gestures of ``stand`` and ``sit``.


It has two uses:


One: It can write strings, directly use the ``step_list`` dictionary in the ``picrawler`` library.

.. code-block:: python

    crawler.do_step('stand',speed) 
    # "speed" indicates the speed of the step, the range is 0~100.


Second: It can also write an array of 4 coordinate values.

.. code-block:: python

    crawler.do_step([[50, 50, -80], [50, 50, -80],[80, 80, 0], [50, 50, -80]],speed)
    # These four coordinates are used to control the four legs of right front, left front, left rear, and left rear respectively.

Each foot has an independent coordinate system. As shown below:

.. image:: img/4cood.png

You need to measure the coordinates of each toe individually. As shown below:

.. image:: img/1cood.png


By the way: the ``step_list`` called in the first method also consists of an array containing 4 coordinate values.

.. code-block:: python

    step_list = {
        "stand":[
            [50, 50, -80],
            [50, 50, -80],
            [50, 50, -80],
            [50, 50, -80]
        ],
        "sit":[
            [50, 50, -33],
            [50, 50, -33],
            [50, 50, -33],
            [50, 50, -33]
        ],
    }





