.. _install_all_modules:

5. 安装所有模块（重要）
===============================================

请确保树莓派已连接至互联网，并先更新系统：

.. raw:: html

    <run></run>

.. code-block::

    sudo apt update
    sudo apt upgrade

.. note::

    如果你安装的是 Lite 版本的系统，则必须额外安装与 Python3 相关的依赖包。

    .. raw:: html

        <run></run>

    .. code-block::
    
        sudo apt install git python3-pip python3-setuptools python3-smbus


安装 ``robot-hat`` 模块。

.. raw:: html

    <run></run>

.. code-block::

    cd ~/
    git clone -b v2.0 https://github.com/sunfounder/robot-hat.git
    cd robot-hat
    sudo python3 setup.py install

接着下载代码并安装 ``vilib`` 模块。

.. raw:: html

    <run></run>

.. code-block::

    cd ~/
    git clone -b picamera2 https://github.com/sunfounder/vilib.git
    cd vilib
    sudo python3 install.py

然后下载代码并安装 ``picrawler`` 模块。

.. raw:: html

    <run></run>

.. code-block::

    cd ~/
    git clone https://github.com/sunfounder/picrawler.git --depth 1
    cd picrawler
    sudo python3 setup.py install

此过程可能需要一些时间，请耐心等待。

最后，你需要运行脚本 ``i2samp.sh`` 来安装 i2s 放大器所需的组件，否则 pislot 将无法发声。

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler
    sudo bash i2samp.sh
	
.. image:: img/i2s.png

输入 ``y`` 并按下 ``Enter`` 键以继续运行脚本。

.. image:: img/i2s2.png

输入 ``y`` 并按下 ``Enter`` 键以在后台运行 ``/dev/zero``。

.. image:: img/i2s3.png

输入 ``y`` 并按下 ``Enter`` 键以重启设备。

.. note::
    如果重启后依旧没有声音，可能需要多次运行 ``i2samp.sh`` 脚本。
