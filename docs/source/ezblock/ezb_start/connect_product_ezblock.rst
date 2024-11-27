.. _connect_product_ezblock_latest:

连接产品与 EzBlock
=====================================================

#. 将机器人 HAT 的电源开关切换到 ON 位置。稍等片刻，您会听到开机提示音，这表明树莓派已成功启动。

    .. image:: img/slide_to_power1.png
            :align: center

#. 将您的移动设备（手机/平板）连接到 WiFi，并打开蓝牙。

    .. image:: img/open_wif_bluetooth.jpg
        :align: center

#. 现在打开 APP - EzBlock Studio，系统会提示您允许 EzBlock Studio 访问以下两个权限：
    
    * 访问设备上的照片、媒体和文件：如果您已登录并需要更改头像，APP 需要访问设备照片；当使用产品的拍照功能时，APP 需要此权限以保存照片。
    * 访问设备位置：此权限必须选择 **允许**，否则 APP 无法通过蓝牙连接到产品。

    .. image:: img/allow_access.png
        :align: center

#. 点击左上角的连接图标。

    .. image:: img/sp221115_1435251.png
        :align: center

#. 在弹出页面中，点击连接。

    .. image:: img/click_connect.png
        :align: center

#. 进入蓝牙连接页面，系统会自动搜索对应的蓝牙设备，通常产品名称为 ezb-Raspberry，但不同产品的 MAC 地址不同。如果您有多个产品，可以通过 MAC 地址区分。此外，蓝牙名称可以在后续步骤中更改。

    .. image:: img/connect_bluetooth1.jpg
        :align: center

#. 当连接成功时，您的产品会发出“叮咚”声，APP 会提示连接成功。

    .. image:: img/connect_success.png
        :align: center

#. 如果这是您第一次使用该产品，系统会提示您进行快速配置。

    .. image:: img/imgIMG_0395.png
        :align: center

#. 输入您的 Wi-Fi 账号和密码。

    .. Note::

        * 如果您已经在 **Raspberry Pi Imager** 中配置了 Wi-Fi，此步骤将不会出现，并会直接进入下一步。
        * 该步骤用于为树莓派配置 Wi-Fi，需与您的移动设备（手机/平板）使用相同的 Wi-Fi 网络。

    .. image:: img/imgIMG_0396.png
        :align: center

#. 选择匹配的产品。

    .. image:: img/imgIMG_0398.png
        :align: center

#. 为您的产品设置一个唯一的名称，该名称将成为您的蓝牙名称（重新启动产品和 APP 后生效），也可以作为主机名在浏览器中使用 EzBlock 时使用。

    .. image:: img/imgIMG_0399.png
        :align: center

#. 如果您的产品需要校准，系统会提示您点击 **立即校准** 进入校准页面。如果不需要校准，弹窗会消失并返回主页。

    .. image:: img/imgIMG_0401.png
        :align: center

#. 每个产品的校准页面不同，但页面上会提示需要校准的部件。您可以点击相应部件，并参考 **校准帮助** 进行校准。校准完成后，点击 **确认**。

    .. image:: img/imgIMG_0403.png
        :align: center

.. note::
    如果您在使用过程中需要重新校准机器人，请按照以下步骤操作：
    
    点击左上角的连接图标，进入产品详情页面。

    .. image:: img/calibrate0.png

    点击 **设置** 按钮。

    .. image:: img/calibrate01.png

    在该页面中，您可以更改产品名称、产品类型，查看 APP 版本，或重新校准机器人。点击 **校准** 后即可进入校准页面。

    .. image:: img/calibrate02.png
