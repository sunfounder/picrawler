适用于 Windows 用户
=======================

对于 Windows 10 或更高版本的用户，可以通过以下步骤远程登录到 Raspberry Pi：

#. 在 Windows 搜索框中输入 ``powershell``。右键点击 ``Windows PowerShell``，选择 **以管理员身份运行** 。

    .. image:: img/powershell_ssh.png
        :align: center

#. 在 PowerShell 中输入 ``ping -4 <hostname>.local`` 来获取 Raspberry Pi 的 IP 地址。

    .. code-block::

        ping -4 raspberrypi.local

    .. image:: img/sp221221_145225.png
        :width: 550
        :align: center

    当 Raspberry Pi 成功连接到网络后，其 IP 地址将会显示出来。

    * 如果终端提示 ``Ping request could not find host pi.local. Please check the name and try again.``，请检查输入的主机名是否正确。
    * 如果依然无法获取 IP 地址，请检查 Raspberry Pi 的网络或 WiFi 设置。

#. 确认 IP 地址后，使用 ``ssh <username>@<hostname>.local`` 或 ``ssh <username>@<IP address>`` 登录到 Raspberry Pi。

    .. code-block::

        ssh pi@raspberrypi.local

    .. warning::

        如果出现错误提示 ``The term 'ssh' is not recognized as the name of a cmdlet...``，说明系统未预装 SSH 工具。此时你需要按照 :ref:`openssh_powershell` 手动安装 OpenSSH，或者使用第三方工具（如 PuTTY）。

#. 首次登录时会出现一条安全提示，请输入 ``yes`` 继续。

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. 输入之前设置的密码。请注意，出于安全考虑，输入时密码不会显示在屏幕上。

    .. note::
        输入密码时没有字符显示是正常现象，请确保输入正确的密码。

#. 连接成功后，你的 Raspberry Pi 就可以进行远程操作了。

    .. image:: img/sp221221_140628.png
        :width: 550
        :align: center
