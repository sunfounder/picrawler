.. _ezb_twist:

Twist 
==================

We already know how to make PiCrawler assume a specific pose, the next step is to combine the poses to form a continuous action.

Here, PiCrawler's four feet are up and down in twos, jumping with the music.

**Program**

.. note::

    * You can write the program according to the following picture, please refer to the tutorial: :ref:`ezblock:create_project_latest`.
    * Or find the code with the same name on the **Examples** page of the EzBlock Studio and click **Run** or **Edit** directly.

.. image:: img/twist.png
    :width: 800

**How it works?**

It uses two layers of for loops to make the ``new_step`` array produce continuous and regular changes, and at the same time, **do step** executes the posture to form a continuous action.

You can intuitively get the coordinate value array corresponding to each pose from :ref:`ezb_posture`.

One thing you need to pay attention to is this coordinate matrix block:

.. image:: img/sp210928_154257.png
    
It is essentially a two-dimensional array, which can be processed by blocks in the **List** category. Its structure is ``[[right front],[left front],[left rear],[right rear]]``.
In other words, in this example, ``new_step#1`` corresponds to the right front; ``new_step#2`` corresponds to the left front; ``new_step#3`` corresponds to the left rear; and ``new_step#4`` corresponds to right rear.