.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ezb_vision:

Computer Vision
=============================

This project will officially enter the field of computer vision!


.. note:: 
    
    You can read :ref:`ezblock:video_latest`. Come and carry out this project smoothly.


**Program**

.. note::

    * You can write the program according to the following picture, please refer to the tutorial: :ref:`ezblock:create_project_latest`.
    * Or find the code with the same name on the **Examples** page of the EzBlock Studio and click **Run** or **Edit** directly.


.. image:: img/sp210928_165255.png
    :width: 800

Switch to the Remote Control interface, and you will see the following widgets.

.. image:: img/sp210928_165642.png

After the program is running, you can switch the slider widget to turn on/off the face detection; click the D-Pad to select the color of the detection; click the button to print the detection result.

**How it works?**

.. image:: img/sp210928_170920.png

This block is used to enable the camera module.

.. image:: img/sp210928_171021.png
    :width: 400

These two blocks are used to enable the face detection/color detection function.

.. image:: img/sp210928_171125.png
    :width: 400

These two blocks are used to output information. The detection result has five output values, namely coordinate x value, coordinate y value, width, height, and number.

