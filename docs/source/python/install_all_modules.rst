.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _install_all_modules:


Install All the Modules (Important)
=========================================

#. **Prepare the system**

   Make sure your Raspberry Pi is connected to the Internet, then update the system:

   .. raw:: html

      <run></run>

   .. code-block::

      sudo apt update
      sudo apt upgrade

   .. note::
      
      If you are using Raspberry Pi OS Lite, install the required Python 3 packages first:

   .. raw:: html

      <run></run>

   .. code-block::

         sudo apt install git python3-pip python3-setuptools python3-smbus

#. **Install robot-hat**

   Download and install the ``robot-hat`` module:

   .. raw:: html

      <run></run>

   .. code-block::

      cd ~/
      git clone -b v2.0 https://github.com/sunfounder/robot-hat.git --depth 1
      cd robot-hat
      sudo python3 install.py

#. **Install vilib**

   Download and install the ``vilib`` module:

   .. raw:: html

      <run></run>

   .. code-block::

      cd ~/
      git clone https://github.com/sunfounder/vilib.git --depth 1
      cd vilib
      sudo python3 install.py


#. **Install picrawler**

   Then download the code and install ``picrawler`` module.
   
   .. raw:: html
   
       <run></run>
   
   .. code-block::
   
       cd ~/
       git clone https://github.com/sunfounder/picrawler.git --depth 1
       cd picrawler
       sudo python3 setup.py install
   
   This step will take a little time, so please be patient.

#. **Enable sound (I2S amplifier)**

   To enable audio output, run the ``i2samp.sh`` script to install the required I2S amplifier components:

   .. raw:: html

      <run></run>

   .. code-block::

      cd ~/robot-hat
      sudo bash i2samp.sh

   Follow the on-screen prompts by typing ``y`` and pressing Enter to continue, run ``/dev/zero`` in the background, and restart the Picar-X.

   .. note::
      If there is no sound after restarting, try running the ``i2samp.sh`` script several times.
