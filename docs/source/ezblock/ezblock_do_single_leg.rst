.. _ezb_posture: 

姿态调整
==========================

在本示例中，我们通过远程控制功能逐步操控 PiCrawler 的每条腿，从而让其摆出所需的姿态。

你可以点击按钮打印出当前的坐标值。在为 PiCrawler 创建独特动作时，这些坐标值会非常有用。

.. image:: ../python/img/1cood.A.png


**Program**

.. note::

    * 你可以根据下图编写程序，具体操作请参考教程：:ref:`ezblock:create_project_latest`。
    * 或者在 EzBlock Studio 的 **Examples** 页面找到同名示例代码，直接点击 **Run** 或 **Edit** 运行或修改。


.. image:: img/do_single_leg.png
    :width: 800

切换到远程控制界面后，你将看到如下组件。

.. image:: img/do_single_leg_B-1.png
    :width: 600

**工作原理**

在本项目中，你需要重点关注以下三个模块：

.. image:: img/sp210928_115847.png

用于单独修改某条腿的坐标值。

.. image:: img/sp210928_115908.png

用于返回对应腿的坐标值。

.. image:: img/sp210928_115958.png


在编程时，你可能希望通过 **Functions** 来简化程序，尤其是在需要多次执行相同操作的情况下。将这些操作封装到一个新声明的函数中，可以大大提高使用效率。

.. image:: img/sp210928_135733.png
    :width: 500