适用于 Linux/Unix 用户 
==========================

#. 在 Linux/Unix 系统中找到并打开 **Terminal** 终端。

#. 确保 Raspberry Pi 已连接到同一网络。你可以通过输入 ``ping <hostname>.local`` 来验证。例如：

    .. code-block::

        ping raspberrypi.local

    如果 Raspberry Pi 已成功连接网络，你会看到其对应的 IP 地址。

    * 如果终端提示 ``Ping request could not find host pi.local. Please check the name and try again.`` ，请检查你输入的主机名是否正确。
    * 如果仍无法获取 IP 地址，请检查 Raspberry Pi 的网络或 WiFi 设置。

#. 通过输入 ``ssh <username>@<hostname>.local`` 或 ``ssh <username>@<IP address>`` 来建立 SSH 连接。例如：

    .. code-block::

        ssh pi@raspberrypi.local

#. 第一次登录时，你会看到一条安全提示信息。请输入 ``yes`` 继续。

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. 输入你之前设置的密码。请注意，出于安全考虑，输入时密码不会显示。

    .. note::
        在终端中看不到密码字符是正常的，只需确保输入正确即可。

#. 登录成功后，你的 Raspberry Pi 就已连接，现在可以继续进行下一步操作。
