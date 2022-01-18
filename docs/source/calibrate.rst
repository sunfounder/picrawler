PiCrawler 校准
===============

因为 PiCrawler 安装过程中可能存在偏差或舵机本身的限制，
使一些舵机角度略有倾斜，因此您可以对其进行校准。

当然如果你认为组装很完美，不需要校准，你也可以跳过这一章。

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picrawler/examples/calibration
    sudo python3 calibration.py
	
运行上面的代码之后，你会看见终端显示如下界面。

.. image:: image/calibration1.png

* 按下1234来分别选择脚， ``1``：右前脚， ``2``：左前脚， ``3``：左后脚， ``4``：右后脚
* 按下 ``w``， ``a``， ``s``， ``d``， ``r``，和 ``f`` 来慢慢控制PiCrawler的坐标值。
* 按空格保存校准。

具体的步骤如下：

1.拿出组装折页，将它翻到最后一页，平整的放桌上。然后将PiCrawler如下图放置，需要将它的底部与校准图上的轮廓线对齐。

.. image:: image/calibration2.png

2.先选择2和3将左侧两条腿移动到校准点。

.. image:: image/calibration3.png

3.然后将校准纸换到右边，选择1和4将右侧2条腿移动到校准点。   

.. image:: image/calibration4.png

4.校准完毕后按 ``空格键`` 进行保存，会提示输入 ``Y`` 确认，然后 ``ctrl+c`` 退出程序完成校准。

.. image:: image/calibration5.png


