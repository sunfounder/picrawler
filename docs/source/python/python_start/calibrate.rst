校准 PiCrawler
=============================

由于在安装 PiCrawler 过程中可能存在偏差，或伺服舵机本身存在一定的限制，部分舵机的角度可能会出现轻微偏移，因此需要进行校准。

当然，如果你认为装配已经非常精准，无需调整，可以跳过本章节。


具体步骤如下：

1. 取出装配说明书，翻到最后一页并平放在桌面上。然后将 PiCrawler 按下图所示放置，使其底部与校准图上的轮廓对齐。

    .. image:: img/calibration2.png

#. 运行 ``calibration.py``。

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/picrawler/examples/calibration
        sudo python3 calibration.py
        
    运行上述代码后，你将在终端中看到如下界面。

    .. image:: img/calibration1.png


#. 分别按下 ``2`` 和 ``3`` 键选择左侧两条腿，然后使用 ``w`` 、 ``a`` 、 ``s`` 、 ``d`` 、 ``r`` 和 ``f`` 键将它们移动到校准点。

    .. image:: img/calibration3.png

#. 接着，将校准纸移到右侧，并按下 ``1`` 和 ``4`` 键选择右侧两条腿，再使用 ``w`` 、 ``a`` 、 ``s`` 、 ``d`` 、 ``r`` 和 ``f`` 键将它们移动到校准点。

    .. image:: img/calibration4.png

#. 校准完成后，按下 ``space`` 键保存，此时会提示输入 ``Y`` 进行确认，然后按 ``ctrl+c`` 退出程序，即完成校准。

    .. image:: img/calibration5.png



