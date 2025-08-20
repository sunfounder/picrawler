.. _ezb_remote: 

远程控制
=========================


在本项目中，我们将学习如何远程控制 PiCrawler。  
你可以操控 PiCrawler 向前、向后、向左或向右移动。

.. note:: 

    你可以参考 :ref:`ezblock:remote_control_latest`，以便更顺利地完成本项目。

**Program**

.. note::

    * 你可以根据下图编写程序，详细操作请参考教程：:ref:`ezblock:create_project_latest`。
    * 或者在 EzBlock Studio 的 **Examples** 页面找到同名示例代码，直接点击 **Run** 或 **Edit** 运行或修改。

.. image:: img/remote.png

切换到远程控制界面后，你将看到如下组件。

.. image:: img/remote_B.png

程序运行后，你可以通过 D-Pad 激活并控制 PiCrawler。

**工作原理**

当你在远程控制界面拖出组件后，编程界面的模块分类栏中会新增一个名为 **Remote** 的类别。

这里我们添加了 D-Pad 控件，因此会出现 **D-Pad get value** 模块。

.. image:: img/sp210927_180739.png

D-Pad 可以理解为四合一的按键。你可以在模块的第二个槽位中选择要读取的具体按键。

当按键被按下时，返回值为 "1"；当按键未按下时，返回值为 "0"。


.. image:: img/sp210927_182447.png
    :width: 200

我们使用了一个 **if** 模块（可在左侧 **Logic** 分类中找到），使得当 D-Pad 的 **UP** 按键被按下时，PiCrawler 执行一次前进动作。

.. image:: img/sp210927_182828.png
    :width: 600

你可以点击模块左上角的齿轮图标，修改 **if** 模块的结构，从而实现多条件分支判断。


.. image:: img/sp210927_183237.png
    :width: 300

**if** 模块通常与 **=** 模块搭配使用。通过下拉菜单， **=** 模块可以修改为 **>** 、 **<** 等条件，请根据需要灵活使用。
