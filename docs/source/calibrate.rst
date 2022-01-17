PiCrawler calibration
===============

Due to possible deviations during PiCrawler installation or limitations of the servos themselves, some servo angles may be slightly tilted, so you can calibrate them.

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picrawler/examples/calibration
    sudo python3 calibration.py
	
After running the above code, you will see the following interface displayed in the terminal.

.. image:: image/calibration1.png

Numbers 1, 2, 3, and 4 are used to select four legs respectively, long press A/D, W/S, R/F to calibrate, and press space to save calibration.

The real object can be calibrated according to the folding assistance, and the steps are as follows:

1. Take out the assembly folder, turn it to the last page, and place it flat on the table. Then place the PiCrawler as shown below, aligning its bottom with the outline on the calibration chart.

.. image:: image/calibration2.png

2. First select 2 and 3 to calibrate the two left legs correctly.

.. image:: image/calibration3.png

3.Then change the calibration paper to the right, select 1 and 4 to calibrate the two feet on the right.   

.. image:: image/calibration4.png

4.After the calibration is completed, press the space to save, you will be prompted to enter Y to confirm, and then ctrl+c to exit the program to complete the calibration.

.. image:: image/calibration5.png

Of course you can skip this chapter if you think the assembly is perfect and doesn't require calibration.

