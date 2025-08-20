适用于 Mac OS X 用户
==========================

对于 Mac OS X 用户来说，SSH（Secure Shell，安全外壳协议）提供了一种安全且高效的方式来远程访问和控制 Raspberry Pi。无论是在远程操作还是在没有显示器的情况下，这都是一种非常实用的方法。通过 Mac 上的 Terminal 终端应用，你可以建立这种安全连接。其过程是通过一条包含 Raspberry Pi 用户名和主机名的 SSH 命令来实现的。在首次连接时，系统会弹出安全提示，要求你确认 Raspberry Pi 的身份。

#. 要连接到 Raspberry Pi，请输入以下 SSH 命令：

    .. code-block::

        ssh pi@raspberrypi.local

    .. image:: img/mac-ping.png

#. 第一次登录时会出现一条安全提示信息，请输入 **yes** 继续。

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. 输入 Raspberry Pi 的密码。请注意，出于安全考虑，输入时密码不会显示，这是正常现象。

    .. code-block::

        pi@raspberrypi.local's password: 
        Linux raspberrypi 5.15.61-v8+ #1579 SMP PREEMPT Fri Aug 26 11:16:44 BST 2022 aarch64

        The programs included with the Debian GNU/Linux system are free software;
        the exact distribution terms for each program are described in the
        individual files in /usr/share/doc/*/copyright.

        Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
        permitted by applicable law.
        Last login: Thu Sep 22 12:18:22 2022
        pi@raspberrypi:~ $ 

