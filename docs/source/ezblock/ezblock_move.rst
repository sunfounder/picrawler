.. _ezb_move:

移动
=================

这是 PiCrawler 的第一个项目，实现它最基础的功能 —— 移动。

**Program**

.. note::

    * 你可以根据下图编写程序，详细操作请参考教程：:ref:`ezblock:create_project_latest`。
    * 或者在 EzBlock Studio 的 **Examples** 页面找到同名示例代码，直接点击 **Run** 或 **Edit** 运行或修改。

.. image:: img/move.png

点击屏幕右下角的 **Upload & Run** 按钮后，PiCrawler 将依次执行 “forward” 和 “backward” 动作。

**工作原理**

首先，你需要了解 Ezblock 的程序框架，如下图所示：

.. image:: img/sp210927_162828.png
    :width: 200

所有 Ezblock 项目都包含这两个模块。 **Start** 模块在程序启动时运行，仅执行一次，通常用于设置变量； **Forever** 模块在 **Start** 之后运行，会被循环执行，通常用于实现主要功能。  
如果不小心删除了这两个模块，可以从左侧的 **Basic** 分类中拖拽回来。

接下来需要了解以下模块：

.. image:: img/sp210927_165133.png

**do action** 模块让 PiCrawler 执行基础动作。  
你可以修改第一个槽位的选项，例如选择“Turn Left”“Back”等。  
第二个槽位用于设置该动作执行的次数，只能填写大于 0 的整数。  
第三个槽位用于设置动作的速度，只能填写 0~100 之间的整数。

.. image:: img/sp210927_170717.png
    :width: 500

**do step** 与 **do action** 类似，但它不是动作，而是静态姿态，例如 “stand” “sit”。

这两个模块都可以从左侧的 **PiCrawler** 分类中拖拽获取。
