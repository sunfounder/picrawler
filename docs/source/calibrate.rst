PiCrawler 校准
===============

因为 PiCrawler 安装过程中可能存在偏差或舵机本身的限制，
使一些舵机角度略有倾斜，因此您可以对其进行校准。

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picrawler/examples/calibration
    sudo python3 calibration.py
	
运行上面的代码之后，你会看见终端显示如下界面。

.. image:: image/calibration1.png

数字1，2，3，4分别选择四条腿，长按A/D，W/S，R/F进行校准，按空格保存校准。

实物可以根据折页辅助校准，步骤如下：

1.拿出组装折页，将它翻到最后一页，平整的放桌上。然后将PiCrawler如下图放置，需要将它的底部与校准图上的轮廓线对齐。

.. image:: image/calibration2.png

2.先选择2和3将左侧两条腿校准正确

.. image:: image/calibration3.png

3.然后将校准纸换到右边，选择1和4校准右侧两只脚    

.. image:: image/calibration4.png

4.校准完毕后按空格进行保存，会提示输入Y确认，然后ctrl+c退出程序完成校准。

.. image:: image/calibration5.png

当然如果你认为组装很完美，不需要校准，你也可以跳过这一章。

