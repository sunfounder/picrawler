.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

Calibrate the PiCrawler
=============================

Due to possible deviations during PiCrawler installation or limitations of the servos themselves, some servo angles may be slightly tilted, so you can calibrate them.

Of course you can skip this chapter if you think the assembly is perfect and doesn't require calibration.

.. raw:: html

    <iframe width="600" height="400" src="https://www.youtube.com/embed/48FLHB_cw3k?si=Zla7BApIt0o6tq73" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


The specific steps are as follows:

1. Take out the assembly leaflet, turn it to the last page, and lay it flat on the table. Then place the PiCrawler as shown below, aligning its bottom with the outline on the calibration chart.

    .. image:: img/calibration2.png

#. Run the ``calibration.py``.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/picrawler/examples/calibration
        sudo python3 calibration.py
        
    After running the above code, you will see the following interface displayed in the terminal.

    .. image:: img/calibration1.png


#. Press ``2`` and ``3`` keys respectively to choose left 2 legs，then press ``w``, ``a``, ``s``, ``d``, ``r``, and ``f`` keys to move them to the calibration point.

    .. image:: img/calibration3.png

#. Now, change the calibration paper to the right and press the ``1`` and ``4`` keys to choose right 2 legs, then press ``w``, ``a``, ``s``, ``d``, ``r``, and ``f`` keys to move them to the calibration point.

    .. image:: img/calibration4.png

#. After the calibration is completed, press the ``space`` key to save, you will be prompted to enter ``Y`` to confirm, and then ``ctrl+c`` to exit the program to complete the calibration.

    .. image:: img/calibration5.png



