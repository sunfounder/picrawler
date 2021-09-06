Move
==============

这是第一个项目，我们让PiCrawler进行它最基础的功能——移动。

**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picrawler/examples
    sudo python3 move.py

在代码执行后，PiCrawler会依次执行以下动作：move forward, move backward, turn left, turn right, turn left angle, turn right angle, stand

**Code**

.. note::
    You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you need to go to  source code path like ``pisloth\examples``. After modifying the code, you can run it directly to see the effect.

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

**How it works?**

First, import the ``Picrawler`` class from the ``picrawler`` library you have installed, which contains all of PiCrawler's actions and the functions that implement them.

.. code-block:: python

    from picrawler import Picrawler

Then instantiate the ``crawler`` class.

.. code-block:: python

    crawler = Picrawler([10,11,12,4,5,6,1,2,3,7,8,9]) 

Finally use the ``crawler.do_action()`` function to make Pisloth move.

.. code-block:: python
    
    crawler.do_action('forward',2,speed)    
    crawler.do_action('backward',2,speed)         
    crawler.do_action('turn left',2,speed)          
    crawler.do_action('turn right',2,speed) 
    crawler.do_action('turn left angle',2,speed) 
    crawler.do_action('turn right angle',2,speed)

In general, all movement of PiCrawler can be implemented with the ``do_action()`` function. It has 3 parameters:

* ``motion_name`` is the name of specific actions, including: ``forward``, ``turn right``, ``turn left``, ``backward``, ``turn left angle``, ``turn right angle``.
* ``step`` represents the number of each action is done, the default is 1.
* ``speed`` indicates the speed of the action, the default is 50 and the range is 0~100.

除此之外，这里还用到了 ``crawler.do_step('stand',speed)`` 来让PiCrawler站立。该函数的用法将在后面的示例中详细解答。