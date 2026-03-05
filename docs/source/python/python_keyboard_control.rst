.. _py_keyboard:

键盘控制
=======================

在本项目中，我们将学习如何使用键盘远程控制 PiCrawler。你可以通过键盘操作让 PiCrawler 前进、后退、左转或右转。

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 keyboard_control.py

当程序启动时，PiCrawler 会完成初始化，并在终端中显示一个键盘控制界面。

按下键盘按键即可控制 PiCrawler！

* ``w``：向前移动
* ``a``：向左转
* ``s``：向后移动
* ``d``：向右转
* ``Ctrl+C``：退出程序

当前速度会显示在终端中，并且可以通过以下按键进行调整：

- + / ] ：提高速度
- - / [ ：降低速度

每次执行动作后，程序都会加入一个短暂的延时，以保证动作的稳定性。

按下 Ctrl+C 可以退出程序。
在程序关闭之前，机器人会执行一次安全的“坐下”动作。

**代码**

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep
    import readchar

    crawler = Picrawler()

    SPEED_MIN = 20
    SPEED_MAX = 70
    speed = 60

    STEP = 1            # Number of action steps per key press
    ACTION_GAP = 0.25   # Delay after each action to reduce current spikes

    manual = """
    Keyboard Control - PiCrawler

    Movement:
    W: Forward
    A: Turn left
    S: Backward
    D: Turn right

    Speed Control:
    + / ] : Increase speed
    - / [ : Decrease speed

    Other:
    Space  : Stop (no action)
    Ctrl+C : Quit (auto sit)
    """

    def clamp(value, min_value, max_value):
        """Limit value within a specified range."""
        return max(min_value, min(max_value, value))

    def show_info():
        """Clear terminal and display control instructions."""
        print("\033[H\033[J", end="")  # Clear terminal screen
        print(manual)
        print(f"Current speed: {speed}  (range {SPEED_MIN}-{SPEED_MAX})")
        print(f"Action gap: {ACTION_GAP:.2f}s")

    def do_move(action_name):
        """Execute movement action with safety delay."""
        crawler.do_action(action_name, STEP, speed)
        sleep(ACTION_GAP)

    def safe_sit():
        """Safely sit down before program exit."""
        try:
            crawler.do_step("sit", clamp(speed, 20, 40))
            sleep(1.0)
        except Exception:
            pass

    def main():
        show_info()

        try:
            while True:
                key = readchar.readkey()
                k = key.lower()

                if k == "w":
                    do_move("forward")
                elif k == "s":
                    do_move("backward")
                elif k == "a":
                    do_move("turn left")
                elif k == "d":
                    do_move("turn right")

                # Speed increase
                elif k in ("+", "]"):
                    global speed
                    speed = clamp(speed + 5, SPEED_MIN, SPEED_MAX)

                # Speed decrease
                elif k in ("-", "["):
                    speed = clamp(speed - 5, SPEED_MIN, SPEED_MAX)

                # Stop (no movement)
                elif k == " ":
                    pass

                # Quit using readchar special key
                elif key == readchar.key.CTRL_C:
                    print("\nQuit.")
                    break

                show_info()
                sleep(0.02)

        except KeyboardInterrupt:
            print("\nQuit (KeyboardInterrupt).")

        finally:
            safe_sit()

    if __name__ == "__main__":
        main()

**它是如何工作的？**

#. 创建机器人对象

   .. code-block:: python

      crawler = Picrawler()

   这一行代码创建了一个 ``Picrawler`` 对象，
   使程序能够控制机器人的运动。

#. 定义安全速度范围

   .. code-block:: python

      SPEED_MIN = 20
      SPEED_MAX = 70
      speed = 60

   这些变量定义了允许的速度范围。
   ``speed`` 用于存储当前的运动速度。
   机器人不会超过设定的最大速度运行。

#. 使用 clamp() 限制速度

   .. code-block:: python

      def clamp(value, min_value, max_value):
          return max(min_value, min(max_value, value))

   该函数用于确保速度保持在安全范围内，
   从而避免由于极端速度值导致的不稳定运动。

#. 执行运动动作

   .. code-block:: python

      def do_move(action_name):
          crawler.do_action(action_name, STEP, speed)
          sleep(ACTION_GAP)

   该函数向机器人发送运动指令。
   ``ACTION_GAP`` 会加入一个短暂延时，以提高动作稳定性。

#. 读取键盘输入

   .. code-block:: python

      key = readchar.readkey()
      k = key.lower()

   程序会等待用户按下一个按键。
   按键会被转换为小写，以保持输入的一致性。

#. 运动控制逻辑

   .. code-block:: python

      if k == "w":
          do_move("forward")
      elif k == "s":
          do_move("backward")

   当按下对应按键时，
   机器人会立即执行相应的运动动作，
   无需按下 Enter 键。

#. 安全退出

   .. code-block:: python

      finally:
          safe_sit()

   在程序退出之前，
   机器人会执行一次安全的“坐下”动作，
   以防止姿态不稳定或突然断电导致的问题。