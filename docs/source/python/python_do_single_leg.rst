.. _py_do_leg:

调整姿势
=====================

在这个例子中，我们使用键盘来控制 PiCrawler 的脚来摆出我们想要的姿势。

您可以按空格键打印出当前坐标值。当您为 PiCrawler 创建独特的动作时，这些坐标值会派上用场。

.. image:: img/1cood.A.png

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picrawler/examples
    sudo python3 do_single_leg.py

代码运行后，请根据终端弹出的提示进行操作。

* 按下1234来分别选择脚， ``1``：右前脚， ``2``：左前脚， ``3``：左后脚， ``4``：右后脚
* 按下 ``w``， ``a``， ``s``， ``d``， ``r``，和 ``f`` 来慢慢控制PiCrawler的坐标值。
* 按下 ``空格键`` 来打印所有的坐标值。
* 按下 ``esc`` 来退出。

**代码**

.. code-block:: python
 
    from picrawler import Picrawler
    from time import sleep
    import readchar

    crawler = Picrawler([10,11,12,4,5,6,1,2,3,7,8,9]) 
    speed = 80


    manual = '''
    -------- PiCrawler Controller --------- 
        .......          .......
        <=|   2   |┌-┌┐┌┐-┐|   1   |=>
        ``````` ├      ┤ ```````
        ....... ├      ┤ .......
        <=|   3   |└------┘|   4   |=>
        ```````          ```````
        1: Select right front leg
        2: Select left front leg
        3: Select left rear leg
        4: Select right rear leg

        W: Y++          R: Z++             
        A: X--          F: Z--
        S: Y--
        D: X++          Esc: Quit
    '''
    legs_list = ['right front', 'left front', 'left rear', 'right rear']

    def main():  
        leg = 0
        speed = 80
        step = 2
        print(manual)
        crawler.do_step('stand',speed)
        sleep(0.2)
        coordinate=crawler.current_step_all_leg_value()  

        def show_info():
            print("\033[H\033[J",end='')  # clear terminal windows
            print(manual)   
            print('%s : %s'%(leg+1, legs_list[leg])) 
            print('coordinate: %s'%(coordinate))  
        
        show_info()

        while True:
            # readkey
            key = readchar.readkey()
            key = key.lower()
            # select the leg 
            if key in ('1234'):
                leg = int(key) - 1
                show_info()
            # move
            elif key in ('wsadrf'):         
                if 'w' == key:
                    coordinate[leg][1]=coordinate[leg][1] + step    
                elif 's' == key:
                    coordinate[leg][1]=coordinate[leg][1] - step           
                elif 'a' == key:
                    coordinate[leg][0]=coordinate[leg][0] - step         
                elif 'd' == key:
                    coordinate[leg][0]=coordinate[leg][0] + step   
                elif 'r' == key:
                    coordinate[leg][2]=coordinate[leg][2] + step         
                elif 'f' == key:
                    coordinate[leg][2]=coordinate[leg][2] - step 

                crawler.do_single_leg(leg,coordinate[leg],speed) 
                sleep(0.1)  
                # coordinate=crawler.current_step_all_leg_value()
                show_info()
            # quit 
            elif key == readchar.key.CTRL_C or key in readchar.key.ESCAPE_SEQUENCES:
                print("\n Quit")  
                break    

            sleep(0.05)
                
    
    if __name__ == "__main__":
        main()

**这个怎么运作?**

在这个项目中需要注意的是以下三个函数：

.. code-block:: python

    do_single_leg(leg,coordinate,speed) 

.. * ``current_step_leg_value(leg)`` : 返回对应腿的坐标值。参数 ``leg`` 可以是 ``0``, ``1``, ``2``, ``3`` 四个值, 分别对应右前，左前，左后，左后四条腿。
.. * ``current_step_all_leg_value()`` : 返回所有腿的坐标值。

``do_single_leg(leg,coordinate,speed)``: 单独修改某条腿的坐标值。