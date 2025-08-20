.. _openssh_powershell:

通过 Powershell 安装 OpenSSH
==================================

当你使用 ``ssh <username>@<hostname>.local``（或 ``ssh <username>@<IP address>``）连接树莓派时，如果出现如下错误提示：

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.


这意味着你的电脑系统版本过旧，未预装 `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_，需要按照以下步骤手动安装。

#. 在 Windows 桌面的搜索框中输入 ``powershell``，右键点击 ``Windows PowerShell`` ，并在弹出菜单中选择 **以管理员身份运行** 。

    .. image:: img/powershell_ssh.png
        :align: center

#. 输入以下命令安装 ``OpenSSH.Client`` 。

    .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. 安装完成后，将显示如下输出。

    .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. 使用以下命令验证安装结果。

    .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. 系统将提示 ``OpenSSH.Client`` 已成功安装。

    .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

    .. warning:: 
        如果没有出现上述提示，说明你的 Windows 系统版本仍然过旧，建议安装第三方 SSH 工具，如 PuTTY。

#. 重新启动 PowerShell，并继续以管理员身份运行。此时，你就可以使用 ``ssh`` 命令登录树莓派，系统会提示输入你之前设置的密码。

    .. image:: img/powershell_login.png