.. _ezb_avoid:

Obstacle Avoidance
=============================


In this project, picrawler will use an ultrasonic module to detect obstacles in front. 
When PiCrawler detects an obstacle, it will send a signal and look for another direction to move forward.

.. image:: ../python/img/avoid1.png

**Program**

.. note::

    * You can write the program according to the following picture, please refer to the tutorial: :ref:`ezblock:create_project_latest`.
    * Or find the code with the same name on the **Examples** page of the EzBlock Studio and click **Run** or **Edit** directly.

.. image:: img/avoid.png


**How it works?**

You can find the following blocks in the **Module** category to achieve distance detection:

.. image:: img/sp210928_103046.png
    :width: 600

It should be noted that the two pins of the block should correspond to the actual wiring, that is, trig-D2, echo-D3.

Here is the main program.

* Read the ``distance`` detected by ultrasonic module and filter out the values less than 0 (When the ultrasonic module is too far from the obstacle or cannot read the data correctly, ``distance<0`` will appear).
* When the ``distance`` is less than ``alert_distance`` (the threshold value set earlier, which is 10), play the sound effect ``sign.wav``. PiCrawler does ``turn left`` .
* When the ``distance`` is greater than ``alert_distance``, PiCrawler will move ``forward``.
