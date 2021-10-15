Mix Step
=================

If you are tired of repeatedly measuring multiple coordinates, you can try to quickly generate a new one in the existing step.


**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picrawler/examples
    sudo python3 mix_step.py



**Code**

.. note::
    You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you need to go to source code path like ``picrawler\examples``. After modifying the code, you can run it directly to see the effect.


.. raw:: html

    <run></run>

.. code-block:: python


    from picrawler import Picrawler
    from time import sleep

    crawler = Picrawler([10,11,12,4,5,6,1,2,3,7,8,9]) 
    #crawler.set_offset([0,0,0,0,0,0,0,0,0,0,0,0])
    speed = 80

    # mix_step
    def my_mix_step():

        crawler.do_step('sit',speed=100)
        sleep(0.5)
        basic_step = []
        basic_step = crawler.step_list.get("sit")
        print(basic_step)
        left_hand  = crawler.mix_step(basic_step,0,[0,50,80])
        right_hand  = crawler.mix_step(basic_step,1,[0,50,80])
        two_hand = crawler.mix_step(left_hand,1,[0,50,80])

        speed = 100
        while True:
            
            crawler.do_step(left_hand,speed)
            sleep(0.6)
            crawler.do_step(two_hand,speed)
            sleep(0.6)
            crawler.do_step(right_hand,speed)
            sleep(0.6)
            crawler.do_step('sit',speed)
            sleep(0.6)

    # main
    def main():
        my_mix_step()
        sleep(0.05)

    if __name__ == "__main__":
        main()

**How it works?**

First, we get the ready-made ``'sit'`` step of ``step_list`` and assign it to ``basic_step``.

.. code-block:: python

    basic_step = []
    basic_step = crawler.step_list.get("sit")

Then, use ``mix_step(step_list_value,leg,coordinate)`` to replace the coordinate value of a certain foot of the original gait.

.. code-block:: python

    left_hand  = crawler.mix_step(basic_step,0,[0,50,80])
    right_hand  = crawler.mix_step(basic_step,1,[0,50,80])
    two_hand = crawler.mix_step(left_hand,1,[0,50,80])

In this way, we have generated three new steps.