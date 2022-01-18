Adjust Posture — Ezblock
==========================

In this example, we use the remote function to control the PiCrawler foot by foot and assume the desired posture.

You can tap the button to print out the current coordinate values. These coordinate values come in handy when you create unique actions for PiCrawler.

.. image:: ../python/img/1cood.A.png


**Program**

After opening the example, you can see the following code block.

.. image:: img/do_single_leg.png
    :width: 800

Switch to the Remote Control interface, and you will see the following widgets.

.. image:: img/do_single_leg_B-1.png
    :width: 600

**How it works?**

What you need to pay attention to in this project are the following three blocks:

.. image:: img/sp210928_115847.png

Modify the coordinate value of a certain leg individually.

.. image:: img/sp210928_115908.png

Returns the coordinate value of the corresponding leg.

.. image:: img/sp210928_115958.png


You may want to simplify the program with Functions, especially when you perform the same operation multiple times. Putting these operations into a newly declared function can greatly facilitate your 
use.

.. image:: img/sp210928_135733.png
    :width: 500