.. _ezb_pose:

姿态
===============


通过编写坐标数组，PiCrawler 可以摆出特定的姿态。这里展示的是抬起右后脚的姿势。

.. image:: ../python/img/4cood.A.png



**Program**

.. note::

    * 你可以根据下图编写程序，详细操作请参考教程：:ref:`ezblock:create_project_latest`。
    * 或者在 EzBlock Studio 的 **Examples** 页面找到同名示例代码，直接点击 **Run** 或 **Edit** 运行或修改。

.. image:: img/dostep.png


**工作原理**

在本代码中，需要特别注意的是 **do step**。

它有两种用法：

1. 可以直接调用 **stand** 或 **sit**。

2. 也可以编写包含 4 个坐标值的数组。

每只脚都有独立的坐标系，如下图所示：


.. image:: ../python/img/4cood.png

你需要分别测量每个脚趾的坐标，如下图所示：

.. image:: ../python/img/1cood.png
