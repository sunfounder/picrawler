.. _control_by_app:

Controlled by the APP
=======================

The SunFounder controller is used to control Raspberry Pi/Pico based robots.

The APP integrates Button, Switch, Joystick, D-pad, Slider and Throttle Slider widgets; Digital Display, Ultrasonic Radar, Grayscale Detection and Speedometer input widgets.

There are 17 areas A-Q , where you can place different widgets to customize your own controller.

In addition, this application provides a live video streaming service.

Let's customize a PiCar-X controller using this app.

**How to do?**

#. Install the ``sunfounder-controller`` module.

    The ``robot-hat``, ``vilib``, and ``picrawler`` modules need to be installed first, for details see: :ref:`install_all_modules`.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~
        git clone https://github.com/sunfounder/sunfounder-controller.git
        cd ~/sunfounder-controller
        sudo python3 setup.py install

#. Run the code.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/sunfounder-controller/examples
        sudo python3 picrawler_control.py

#. Install `SunFounder Controller <https://docs.sunfounder.com/projects/sf-controller/en/latest/>`_ from **APP Store(iOS)** or **Google Play(Android)**.


#. Open and create a new controller.

    Create a new controller by clicking on the + sign in the SunFounder Controller APP.

    .. image:: img/app1.PNG

    There are preset controllers for some products in the Preset section, 这里我们选择PiCrawler.

    .. image:: img/app_control1.jpg

    Give it a name and select the Controller type. 

    .. image:: img/app_control2.jpg

    进入到这个预设的控制器之后，你会发现已经有一些小部件了。如果你没有其他要修改的，点击 |app_save|按键。

    .. image:: img/app_control3.jpg

#. Connect to PiCrawler.

    When you click the **Connect** button, it will automatically search for robots nearby. Its name is defined in ``picrawler_control.py`` and it must be running at all times.

    .. image:: img/app_control6.jpg
    
    Once you click on the product name, the message "Connected Successfully" will appear and the product name will appear in the upper right corner.

    .. image:: img/app_control7.jpg

    .. note::

        * You need to make sure that your mobile device is connected to the same LAN as PiCrawler.
        * If it doesn't search automatically, you can also manually enter the IP to connect.

        .. image:: img/app11.PNG

#. Run this controller.

    Click the **Run** button to start the controller, you will see the footage of the car shooting, and now you can control your PiCrawler with these widgets.

    .. image:: img/app_control8.jpg
    
    Here are the functions of the widgets.

    * **A**: Set the power of the Picrawler.
    * **B**: Show the move speed of the robot.
    * **C**: The same function as the B widget.
    * **D**: Show the detected obstacles in red points.
    * **G**: voice recognition, press and hold this widget to start speaking, and it will show the recognized voice when you release it. We have set ``forward``, ``backard``, ``left`` and ``right`` 4 commands in the code to control the car.
    * **K**: Control forward, backward, left, and right motions of the car.
    * **Q**: turn the head(Camera) up, down, left and right.
    * **N**: Turn on the color recognition function.
    * **O**: Turn on the face recognition function.
    * **P**: Turn on the object recognition function, it can recognize nearly 90 kinds of objects, for the list of models, please refer to: https://github.com/sunfounder/vilib/blob/master/workspace/coco_labels.txt.


