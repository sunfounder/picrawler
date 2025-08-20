.. _control_by_app: 

通过 APP 控制
=======================

SunFounder 控制器可用于操控基于 Raspberry Pi/Pico 的机器人。  

该 APP 集成了 Button、Switch、Joystick、D-pad、Slider 和 Throttle Slider 等控件；同时还支持 Digital Display、Ultrasonic Radar、Grayscale Detection 和 Speedometer 等输入组件。  

界面上共有 17 个区域（A-Q），你可以在这些区域中放置不同的控件，来自定义专属的控制器。  

此外，该应用还提供实时视频流功能。  

下面我们通过此 APP 来定制一个 PiCrawler 控制器。  

**具体操作步骤**  

#. 安装 ``sunfounder-controller`` 模块。  

    在此之前需先安装 ``robot-hat``、 ``vilib`` 和 ``picrawler`` 模块，详情请参考：:ref:`install_all_modules`。  

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~
        git clone https://github.com/sunfounder/sunfounder-controller.git
        cd ~/sunfounder-controller
        sudo python3 setup.py install

#. 运行示例代码。  

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/sunfounder-controller/examples
        sudo python3 picrawler_control.py

#. 从 **APP Store(iOS)** 或 **Google Play(Android)** 安装 `SunFounder Controller <https://docs.sunfounder.com/projects/sf-controller/en/latest/>`_。  


#. 打开并创建新控制器。  

    在 SunFounder Controller APP 中点击 “+” 号来新建一个控制器。  

    .. image:: img/app1.PNG

    在 Preset 区域中已经为部分产品预设了控制器，这里我们选择 PiCrawler。  

    .. image:: img/app_control1.jpg

    为该控制器命名，并选择 Controller 类型。  

    .. image:: img/app_control2.jpg

    进入该预设控制器后，可以看到已经存在一些默认控件。如果无需修改，直接点击 ``app_save`` 按钮即可。  

    .. image:: img/app_control3.jpg

#. 连接 PiCrawler。  

    点击 **Connect** 按钮后，系统会自动搜索附近的机器人。其名称在 ``picrawler_control.py`` 中定义，并且必须保持运行。  

    .. image:: img/app_control6.jpg
    
    点击产品名称后，会提示 “Connected Successfully”，同时设备名称会显示在右上角。  

    .. image:: img/app_control7.jpg

    .. note::

        * 请确保移动设备与 PiCrawler 处于同一局域网内。  
        * 如果未能自动搜索到，也可以手动输入 IP 地址进行连接。  

        .. image:: img/app11.PNG

#. 运行控制器。  

    点击 **Run** 按钮即可启动控制器，此时你将看到小车的实时画面，并可以通过各个控件来操控 PiCrawler。  

    .. image:: img/app_control8.jpg
    
    以下是各控件的功能说明：  

    * **A**: 设置 PiCrawler 的供电功率。  
    * **B**: 显示机器人的运动速度。  
    * **C**: 与 B 控件功能相同。  
    * **D**: 以红点形式显示检测到的障碍物。  
    * **G**: 语音识别功能，长按开始说话，松开后显示识别结果。代码中已设置 ``forward`` 、 ``backard`` 、 ``left`` 和 ``right`` 四个语音指令来控制小车移动。  
    * **K**: 控制小车前进、后退、左转和右转。  
    * **Q**: 控制摄像头（头部）上下左右转动。  
    * **N**: 开启颜色识别功能。  
    * **O**: 开启人脸识别功能。  
    * **P**: 开启物体识别功能，可识别约 90 种物体，完整模型列表请参考：https://github.com/sunfounder/vilib/blob/master/workspace/coco_labels.txt。  


