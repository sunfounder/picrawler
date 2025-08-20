.. _py_posture:

调整姿态
=====================

在本示例中，我们将通过键盘逐条腿地控制 PiCrawler，并调整到所需的姿态。

你可以按下空格键打印出当前的坐标值。在为 PiCrawler 创建独特的动作时，这些坐标值将非常有用。

.. image:: img/1cood.A.png

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 do_single_leg.py

代码运行后，请根据终端中出现的提示进行操作。

* 按下 ``1234`` 分别选择腿部， ``1``：右前腿， ``2`` ：左前腿， ``3`` ：左后腿， ``4`` ：右后腿  
* 按下 ``w`` 、 ``a`` 、 ``s`` 、 ``d`` 、 ``r``、 ``f`` 可逐步调整 PiCrawler 的坐标值  
* 按下 ``Ctrl+C`` 退出程序  


**代码**

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep
    import readchar

    crawler = Picrawler()
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
        D: X++          Ctrl+C: Quit
    '''
    legs_list = ['right front', 'left front', 'left rear', 'right rear']

    def main():  
        leg = 0
        speed = 80
        step = 2
        print(manual)
        crawler.do_step('stand', speed)
        sleep(0.2)
        coordinate=crawler.current_step_all_leg_value()  

        def show_info():
            print("\033[H\033[J", end='')  # clear terminal windows
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

            sleep(0.05)

    
    if __name__ == "__main__":
        main()

* ``current_step_all_leg_value()``：返回所有腿部的坐标值  
* ``do_single_leg(leg,coordinate[leg],speed)``：单独修改某条腿的坐标值  