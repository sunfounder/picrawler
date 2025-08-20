.. _py_move:

移动
==============

这是 PiCrawler 的第一个项目，用来展示它最基本的功能 —— 移动。


**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 move.py

代码执行后，PiCrawler 将依次完成以下动作：前进、后退、左转、右转、站立。

**代码**

.. note::
    你可以对下面的代码进行 **Modify/Reset/Copy/Run/Stop** 操作。但在此之前，需要进入源码路径，例如 ``pisloth\examples``。修改代码后可直接运行并查看效果。

.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep
    
    crawler = Picrawler() 
    
    def main():  
        
        speed = 80
              
        while True:
           
            crawler.do_action('forward',2,speed)
            sleep(0.05)     
            crawler.do_action('backward',2,speed)
            sleep(0.05)          
            crawler.do_action('turn left',2,speed)
            sleep(0.05)           
            crawler.do_action('turn right',2,speed)
            sleep(0.05)  
            crawler.do_action('turn left angle',2,speed)
            sleep(0.05)  
            crawler.do_action('turn right angle',2,speed)
            sleep(0.05) 
            crawler.do_step('stand',speed)
            sleep(1)
    
    if __name__ == "__main__":
        main()


**它是如何工作的？**

首先，从已安装的 ``picrawler`` 库中导入 ``Picrawler`` 类，该类包含了 PiCrawler 的全部动作以及实现这些动作的函数。

.. code-block:: python

    from picrawler import Picrawler

然后实例化 ``crawler`` 类。

.. code-block:: python

    crawler = Picrawler() 

最后，通过 ``crawler.do_action()`` 函数来控制 PiCrawler 移动。

.. code-block:: python
    
    crawler.do_action('forward',2,speed)    
    crawler.do_action('backward',2,speed)         
    crawler.do_action('turn left',2,speed)          
    crawler.do_action('turn right',2,speed) 
    crawler.do_action('turn left angle',2,speed) 
    crawler.do_action('turn right angle',2,speed)

总体而言，PiCrawler 的所有移动动作都可以通过 ``do_action()`` 函数实现。它包含 3 个参数：

* ``motion_name`` 表示具体的动作名称，包括： ``forward`` 、 ``turn right`` 、 ``turn left`` 、 ``backward`` 、 ``turn left angle`` 、 ``turn right angle`` 。
* ``step`` 表示动作执行的次数，默认值为 1。
* ``speed`` 表示动作执行的速度，默认值为 50，取值范围为 0~100。

此外，这里还使用了 ``crawler.do_step('stand',speed)`` 来让 PiCrawler 保持站立状态。该函数的用法将在后续示例中进一步说明。