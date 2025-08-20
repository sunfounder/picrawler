.. _install_os_sd:

2. 安装操作系统
============================================================

**所需组件**

* 一台个人电脑
* 一张 Micro SD 卡及读卡器

1. 安装 Raspberry Pi Imager
----------------------------------

#. 访问树莓派软件官方下载页面： `Raspberry Pi Imager <https://www.raspberrypi.org/software/>`_ 。根据你的操作系统选择对应版本的 Imager。下载并打开安装文件，开始安装程序。

    .. image:: img/os_install_imager.png
        :align: center

#. 在安装过程中，可能会弹出系统安全提示。例如，在 Windows 上可能会出现警告信息。此时请选择 **More info**，然后点击 **Run anyway**，并按照屏幕提示完成安装。

    .. image:: img/os_info.png
        :align: center

#. 安装完成后，可通过点击图标启动 Raspberry Pi Imager，或在终端输入 ``rpi-imager`` 运行。

    .. image:: img/os_open_imager.png
        :align: center

2. 将操作系统写入 Micro SD 卡
--------------------------------

#. 使用读卡器将 SD 卡插入电脑或笔记本。

#. 在 Imager 中点击 **Raspberry Pi Device** ，并在下拉列表中选择对应的树莓派型号。

    .. image:: img/os_choose_device.png
        :align: center

#. 选择 **Operating System** ，并选用推荐的操作系统版本。

    .. image:: img/os_choose_os.png
        :align: center

#. 点击 **Choose Storage** ，选择目标存储设备。

    .. note::

        请务必选择正确的存储设备。若电脑连接了多个存储设备，建议先拔掉无关设备以避免误操作。

    .. image:: img/os_choose_sd.png
        :align: center

#. 点击 **NEXT** ，然后选择 **EDIT SETTINGS** ，对操作系统进行自定义设置。 

    .. note::

        如果你已为树莓派准备了显示器，可以跳过以下步骤，直接点击 "Yes" 开始安装，并在显示器上进行后续设置。

    .. image:: img/os_enter_setting.png
        :align: center

#. 设置树莓派的 **主机名（hostname）** 。

    .. note::

        主机名是树莓派在网络中的标识。你可以通过 ``<hostname>.local`` 或 ``<hostname>.lan`` 来访问。

    .. image:: img/os_set_hostname.png
        :align: center

#. 创建树莓派管理员账户的 **用户名（Username）** 和 **密码（Password）** 。

    .. note::

        树莓派默认没有预设密码，因此为其设置唯一的用户名和密码是保障安全的重要步骤。

    .. image:: img/os_set_username.png
        :align: center

#. 配置无线网络，输入 Wi-Fi 的 **SSID** 和 **密码** 。

    .. note::

        请根据所在国家或地区设置 ``Wireless LAN country`` ，输入对应的两位字母 `ISO/IEC alpha2 代码 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ 。

    .. image:: img/os_set_wifi.png
        :align: center


#. 若需远程连接树莓派，可在服务选项卡中启用 SSH。

    * 若选择 **密码认证** ，则需使用常规的用户名和密码登录。
    * 若选择 **公钥认证** ，则启用 "Allow public-key authentication only"。系统会自动使用已有的 RSA 密钥；如无密钥，可点击 "Run SSH-keygen" 生成新的密钥对。

    .. image:: img/os_enable_ssh.png
        :align: center

#. 通过 **Options** 菜单可配置写入后的操作行为，例如完成后播放提示音、弹出介质或启用数据回传等。

    .. image:: img/os_options.png
        :align: center

#. 完成操作系统自定义设置后，点击 **Save** 保存配置，并在写入镜像时点击 **Yes** 以应用设置。

    .. image:: img/os_click_yes.png
        :align: center

#. 如果 SD 卡中已有数据，请先进行备份，以免丢失。若无需备份，可直接点击 **Yes** 继续。

    .. image:: img/os_continue.png
        :align: center

#. 当弹出 “Write Successful” 提示时，说明镜像已成功写入并校验完成。此时你就可以使用该 SD 卡启动树莓派了！

    .. image:: img/os_finish.png
        :align: center

#. 将已写入操作系统的 SD 卡插入树莓派底部的 microSD 卡槽中，即可完成安装准备。

    .. image:: img/insert_sd_card.png
        :width: 500
        :align: center