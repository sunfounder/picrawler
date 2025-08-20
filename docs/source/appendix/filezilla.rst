.. _filezilla: 

Filezilla 软件
==========================

.. image:: img/filezilla_icon.png

文件传输协议（FTP）是一种标准通信协议，用于在计算机网络中将文件从服务器传输到客户端。

Filezilla 是一款开源软件，不仅支持 FTP，还支持基于 TLS 的 FTP（FTPS）以及 SFTP。通过 Filezilla，我们可以将本地文件（如图片、音频等）上传到树莓派，或将树莓派中的文件下载到本地。

**Step 1**: 下载 Filezilla。

可从 `Filezilla 官方网站 <https://filezilla-project.org/>`_ 下载客户端。Filezilla 提供了非常完善的使用教程，请参考： `Documentation - Filezilla <https://wiki.filezilla-project.org/Documentation>`_ 。

**Step 2**: 连接树莓派

完成快速安装后，打开软件并 `连接到 FTP 服务器 <https://wiki.filezilla-project.org/Using#Connecting_to_an_FTP_server>`_。它提供了三种连接方式，这里我们使用 **Quick Connect** 工具栏。输入 **hostname/IP** 、 **username** 、 **password** 以及 **port (22)**，然后点击 **Quick Connect** 或按 **Enter** 键即可连接到服务器。

.. image:: img/filezilla_connect.png

.. note::

    Quick Connect 是测试登录信息的便捷方式。如果你希望创建一个永久条目，在成功连接后，可以选择 **File** -> **Copy Current Connection to Site Manager** ，输入名称并点击 **OK** 。下次即可在 **File** -> **Site Manager** 中选择已保存的站点进行连接。
    
    .. image:: img/ftp_site.png

**Step 3**: 上传/下载文件。

你可以通过拖拽的方式将本地文件上传到树莓派，或者将树莓派中的文件下载到本地。

.. image:: img/upload_ftp.png
