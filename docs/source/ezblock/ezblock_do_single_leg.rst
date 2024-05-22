.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ezb_posture:

Adjust Posture
==========================

In this example, we use the remote function to control the PiCrawler foot by foot and assume the desired posture.

You can tap the button to print out the current coordinate values. These coordinate values come in handy when you create unique actions for PiCrawler.

.. image:: ../python/img/1cood.A.png


**Program**

.. note::

    * You can write the program according to the following picture, please refer to the tutorial: :ref:`ezblock:create_project_latest`.
    * Or find the code with the same name on the **Examples** page of the EzBlock Studio and click **Run** or **Edit** directly.


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