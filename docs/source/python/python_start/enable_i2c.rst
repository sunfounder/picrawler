.. _i2c_spi_config:

6. 检查 I2C 接口
========================================

我们将使用树莓派的 I2C 接口。在之前安装 ``robot-hat`` 模块时，该接口应已被启用。为确保一切正常，让我们来检查一下是否确实开启了它。

#. 输入以下命令：

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. 使用键盘方向键选择 **Interfacing Options** ，然后按下 **Enter** 键。

    .. image:: img/image282.png
        :align: center

#. 接着选择 **I2C** 。

    .. image:: img/image283.png
        :align: center

#. 使用键盘方向键选择 **<Yes>** -> **<OK>**，即可完成 I2C 接口的配置。

    .. image:: img/image284.png
        :align: center