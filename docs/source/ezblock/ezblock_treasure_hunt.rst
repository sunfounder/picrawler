.. _ezb_treasure: 

寻宝游戏
============================


在房间里摆放一个迷宫，并在六个角落分别放置六张不同颜色的色卡。然后控制 PiCrawler 逐一寻找这些色卡！

.. note:: 你可以下载并打印用于颜色检测的 :download:`PDF 色卡 <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>` 。

**Program**

.. note::

    * 你可以根据下图编写程序，详细操作请参考教程：:ref:`ezblock:create_project_latest`。
    * 或者在 EzBlock Studio 的 **Examples** 页面找到同名示例代码，直接点击 **Run** 或 **Edit** 运行或修改。

.. image:: img/sp210928_181036.png
    :width: 800

切换到远程控制界面后，你将看到如下组件。

.. image:: img/sp210928_181134.png
    :width: 800


**工作原理**

总体而言，本项目结合了 :ref:`ezb_remote`、:ref:`ezb_vision` 和 :ref:`ezb_sound` 的相关知识点。

其运行流程如下图所示：

.. image:: ../python/img/treasure_hunt-f.png
    :width: 600