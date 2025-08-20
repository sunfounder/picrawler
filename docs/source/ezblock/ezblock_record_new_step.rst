.. _ezb_record:

记录新动作
==============================

我们通过远程控制功能让 PiCrawler 依次摆出多个姿态，并将这些姿态记录下来，之后可以进行回放。


**Program**

.. note::

    * 你可以根据下图编写程序，详细操作请参考教程：:ref:`ezblock:create_project_latest`。
    * 或者在 EzBlock Studio 的 **Examples** 页面找到同名示例代码，直接点击 **Run** 或 **Edit** 运行或修改。

.. image:: img/record.png
    :width: 800

切换到远程控制界面后，你将看到如下组件。

.. image:: img/sp210928_164343-1.png
    :width: 600

**工作原理**


本项目源自 :ref:`ezb_posture`，在其基础上新增了记录和回放功能。

以下代码实现了动作记录功能：

.. image:: img/sp210928_164449.png

以下代码实现了动作回放功能：

.. image:: img/sp210928_164500.png