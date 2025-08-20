.. _ezb_avoid:

避障功能
=============================

在本项目中，PiCrawler 将使用超声波模块来检测前方障碍物。  
当 PiCrawler 检测到障碍物时，会发出信号，并寻找其他方向继续前进。


**Program**

.. note::

    * 你可以按照下图编写程序，详细操作请参考教程：:ref:`ezblock:create_project_latest` 。
    * 或者在 EzBlock Studio 的 **Examples** 页面找到同名示例代码，直接点击 **Run** 或 **Edit** 运行或修改。

.. image:: img/avoid.png


**工作原理**

你可以在 **Module** 分类中找到以下模块，用于实现距离检测：

.. image:: img/sp210928_103046.png
    :width: 600

需要注意的是，模块的两个引脚必须与实际接线对应，即 trig-D2，echo-D3。

以下是主程序逻辑：

* 读取超声波模块检测到的 ``distance`` ，并过滤掉小于 0 的数值（当超声波模块距离障碍物过远或无法正确读取数据时，会出现 ``distance<0`` 的情况）。
* 当 ``distance`` 小于 ``alert_distance``（预设阈值，这里设为 10）时，播放音效 ``sign.wav`` ，PiCrawler 执行 ``turn left`` 。
* 当 ``distance`` 大于 ``alert_distance`` 时，PiCrawler 执行 ``forward`` 。
