下载并运行代码
============================

下载代码并安装3个库
--------------------------------------

我们可以在命令行中通过 ``git clone`` 命令下载文件。

首先安装 ``robot-hat`` 库。

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/
    git clone https://gitee.com/sunfounder/robot-hat.git
    cd robot-hat
    sudo python3 setup.py install

.. note::
    运行 ``setup.py`` 将下载一些必要的组件。 由于网络问题，您可能无法下载成功。您可能需要重新下载。 在这种情况下，输入 ``Y`` 并按 Enter.
	
	.. image:: img/dowload_code.png

然后下载代码并安装 ``vilib`` 库。

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/
    git clone https://gitee.com/sunfounder/vilib.git
    cd vilib
    sudo python3 install.py

然后下载代码并安装 ``picrawler`` 库。

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/
    git clone -b v2.0 https://gitee.com/sunfounder/picrawler.git
    cd picrawler
    sudo python3 setup.py install

这一步需要一点时间，所以请耐心等待。

最后需要运行脚本 ``i2samp.sh`` 安装i2s功放所需的组件，否则它可能会没有声音。

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picrawler
    sudo bash i2samp.sh
	
.. image:: img/i2s.png

输入 y 并按 Enter 继续运行脚本。

.. image:: img/i2s2.png

输入 y 并按 Enter 让 ``/dev/zero`` 在后台运行。

.. image:: img/i2s3.png

输入 y 并按 Enter 重新启动机器。

.. note::
    如果重启后没有声音，可能需要多次运行 i2samp.sh 脚本。

运行 ``servo_zeroing.py``
--------------------------

因为舵机是靠Robot HAT上的电源供电的，当你只给树莓派供电时，舵机是不会工作的。您需要确保电池已放置在电池盒中且 Robot HAT 已通电。

.. image:: img/slide_to_power.png
    :width: 400
    :align: center

在运行任何代码之前，请启用 Raspberry Pi 的 I2C 端口，请参阅: :ref:`I2C 配置`。

现在，运行 ``examples/`` 文件夹中的 ``servo_zeroing.py`` 。

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picrawler/examples
    sudo python3 servo_zeroing.py

为确保您可以看到舵机已设置为0°，您可以先在舵机轴中插入摇臂，然后将舵机偏转一个任意角度。

.. image:: img/servo_arm.png
    :align: center

现在按照下图将舵机插入 P11 位置。

.. image:: img/pin11_connect.png
    :width: 400
    :align: center

如果伺服臂偏转并固定在一个角度，则说明该功能生效。如果不是，请检查伺服电缆的插入方向或重新运行代码。

.. note::

    在组装每个舵机之前，您需要将舵机引脚插入 P11 并保持通电。    