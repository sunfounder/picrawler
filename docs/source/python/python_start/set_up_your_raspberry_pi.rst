4. 设置你的 Raspberry Pi
============================

如果你有显示屏
-------------------------

如果你有一台显示屏，操作 Raspberry Pi 将会非常方便。

**所需组件**

* 任意型号的 Raspberry Pi   
* 1 * 电源适配器  
* 1 * Micro SD 卡  
* 1 * 显示屏电源适配器  
* 1 * HDMI 线缆  
* 1 * 显示屏  
* 1 * 鼠标  
* 1 * 键盘  

1. 将已写入 Raspberry Pi OS 的 SD 卡插入 Raspberry Pi 底部的 Micro SD 卡槽。  

#. 插入鼠标和键盘。  

#. 使用 HDMI 线缆将显示屏连接到 Raspberry Pi，并确保显示屏已接通电源并开启。  

    .. note::

        如果你使用的是 Raspberry Pi 4，需要将显示屏连接到 HDMI0 接口（靠近电源接口的那个）。  

#. 使用电源适配器为 Raspberry Pi 供电。  

#. 几秒钟后，你将看到 Raspberry Pi OS 的桌面界面。此时你就可以打开终端，开始输入命令。  

    .. image:: img/bookwarm.png
        :align: center

如果你没有显示屏
--------------------------

如果你没有显示器，可以通过远程方式登录 Raspberry Pi。  

你可以使用 SSH 命令打开 Raspberry Pi 的 Bash shell。Bash 是 Linux 的默认标准 shell。在 Unix/Linux 环境下，shell 就是用户执行命令（指令）的接口。大部分操作都可以通过 shell 来完成。  

如果你不习惯只用命令窗口访问 Raspberry Pi，还可以使用远程桌面功能，通过图形界面（GUI）轻松管理 Raspberry Pi 上的文件。  

不同系统的详细教程请参考以下内容：  


.. toctree::

    remote_macosx
    remote_windows
    remote_linux
    remote_desktop

