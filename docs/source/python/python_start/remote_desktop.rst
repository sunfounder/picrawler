.. _remote_desktop: 

远程桌面访问 Raspberry Pi
==================================================

如果你更习惯使用图形用户界面（GUI）而非命令行，Raspberry Pi 同样支持远程桌面功能。本指南将带你完成配置和使用 VNC（Virtual Network Computing）进行远程访问的步骤。

我们推荐使用 `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ 作为远程桌面客户端。

**在 Raspberry Pi 上启用 VNC 服务**

Raspberry Pi OS 已预装 VNC 服务，但默认处于禁用状态。请按照以下步骤启用：

#. 在 Raspberry Pi 终端输入以下命令：

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. 使用方向键选择 **Interfacing Options**，然后按 **Enter** 。

    .. image:: img/config_interface.png
        :align: center

#. 从选项中选择 **VNC** 。

    .. image:: img/vnc.png
        :align: center

#. 使用方向键依次选择 **<Yes>** -> **<OK>** -> **<Finish>** ，完成 VNC 服务的启用。

    .. image:: img/vnc_yes.png
        :align: center

**通过 VNC Viewer 登录**

#. 在个人电脑上下载并安装 `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ 。

#. 安装完成后，启动 VNC Viewer，输入 Raspberry Pi 的主机名或 IP 地址，然后按 Enter。

    .. image:: img/vnc_viewer1.png
        :align: center

#. 当系统提示时，输入 Raspberry Pi 的用户名和密码，然后点击 **OK** 。

    .. image:: img/vnc_viewer2.png
        :align: center

#. 几秒钟后，你将看到 Raspberry Pi OS 桌面。此时你可以打开终端并开始输入命令。

    .. image:: img/bookwarm.png
        :align: center
