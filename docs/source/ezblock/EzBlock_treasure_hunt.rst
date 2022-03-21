寻宝 
============================


在你的房间里布置一个迷宫，在六个角落放置六张不同颜色的卡片。然后控制PiCrawler一一搜索这些卡纸吧！


.. note:: 
    
    您可以下载并打印文件 :download:`PDF 颜色卡纸 <https://gitee.com/sunfounder/sf-pdf/raw/master/%E5%8D%A1%E7%89%87/%E7%9B%AE%E6%A0%87%E8%AF%86%E5%88%AB/%E9%A2%9C%E8%89%B2%E5%8D%A1.pdf>` 来用于颜色检测。

**程序**

.. note::

  你可以直接打开我们提供的示例或者是按照下图来编写程序，详细教程请参考 :ref:`open_create`。


.. image:: img/sp210928_181036.png
    :width: 800

程序运行后，切换到远程控制界面，您将看到以下小部件。你可以点击方向盘A来让PiCrawler移动，它会将设定的卡片颜色框选出来。
你可以按下按键来生成新的颜色指令。

.. image:: img/sp210928_181134.png
    :width: 800


**这个如何运作?**

总的来说，这个项目结合了 :ref:`ezb_remote_control`, :ref:`ezb_computer_vision` 和 :ref:`ezb_sound_effect` 的知识点。

其流程图如下所示:

.. image:: img/treasure_hunt-f.png
    :width: 600