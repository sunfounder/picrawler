避障
=============================


在这个项目中，picrawler 将使用超声波模块来检测前方的障碍物。当 PiCrawler 检测到障碍物时，它会发出信号并寻找另一个方向前进。

.. image:: img/avoid1.png


**程序**

.. note::

  你可以直接打开我们提供的示例或者是按照下图来编写程序，详细教程请参考 :ref:`open_create`。

.. image:: img/avoid.png

程序运行后，picrawler 将使用超声波模块来检测前方的障碍物。当 PiCrawler 检测到障碍物时，它会发出信号并寻找另一个方向前进。

**这个如何运作?**

您可以在 **模块** 类别中找到以下块来实现距离检测：

.. image:: img/sp210928_103046.png
    :width: 350

需要注意的是，此积木块的两个引脚要对应实际接线，即trig-D2，echo-D3。

主程序逻辑如下：

* 读取超声波模块检测到的 ``distance`` 值，会过滤掉小于0的值（当超声波模块距离障碍物太远或无法正确读取数据时，会出现 ``distance<0`` 的情况）。
* 当 ``distance`` 小于 ``alert_distance`` （之前设置的阈值，数值为10）时，播放音效 ``sign.wav`` 并让 PiCrawler 执行左转的动作。
* 当 ``distance`` 大于 ``alert_distance`` 时，让 PiCrawler 执行前进的动作。