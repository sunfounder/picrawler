移动
==============

这是 PiCrawler's 的第一个项目， 让它移动起来。

.. image:: img/move.png
    :align: center

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picrawler/examples
    sudo python3 move.py

执行代码之后，PiCrawler 会依次执行以下动作：前进、后退、左转、右转、站立。

**代码**

.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep
    
    crawler = Picrawler([10,11,12,4,5,6,1,2,3,7,8,9]) 
    #crawler.set_offset([0,0,0,0,0,0,0,0,0,0,0,0])
    
    def main():  
        
        speed = 100
              
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

**这个怎么运作?**

首先从您安装的 ``Picrawler`` 库中导入 ``picrawler`` 类, 这个类包含了 PiCrawler 的所有操作和实现它们的函数。

.. code-block:: python

    from picrawler import Picrawler

然后示例化 ``Picrawler`` 类，创建一个它的对象 ``crawler``.

.. code-block:: python

    crawler = Picrawler([10,11,12,4,5,6,1,2,3,7,8,9]) 

最后用 ``crawler.do_action()`` 函数来使Picrawler移动。

.. code-block:: python
    
    crawler.do_action('forward',2,speed)    
    crawler.do_action('backward',2,speed)         
    crawler.do_action('turn left',2,speed)          
    crawler.do_action('turn right',2,speed) 
    crawler.do_action('turn left angle',2,speed) 
    crawler.do_action('turn right angle',2,speed)

一般情况下，PiCrawler 的所有动作都可以通过 ``do_action()`` 函数来实现。它有3个参数：

* ``motion_name`` 是具体动作的名字, 包括: ``forward``, ``turn right``, ``turn left``, ``backward``, ``turn left angle``, ``turn right angle``.
* ``step`` 表示每个动作执行的次数，默认为1次。
* ``speed`` 表示动作执行的速度，默认为50，范围为0~100。

此外, ``crawler.do_step('stand',speed)`` 在这里也是用于使PiCrawler 站立。 它的用法将在下面的例子中说明。