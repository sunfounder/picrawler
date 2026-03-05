.. _py_avoid:

避障功能
=====================

在本项目中，PiCrawler 将使用超声波模块检测前方的障碍物。  
当检测到障碍物时，PiCrawler 会发送信号，并寻找其他方向继续前进。  


**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 avoid.py

当程序启动时，PiCrawler 会站立起来。

它会持续使用超声波传感器测量距离，
并在终端中打印测量到的数值。

如果在 15 cm 范围内检测到障碍物：
- 会播放警告声音。
- 机器人会进行一次小幅度左转。

如果前方路径是畅通的：
- 机器人会向前移动。

机器人会持续自动避障运行，直到你按下 Ctrl+C。

在程序退出之前，机器人会安全地坐下。

**代码**

.. note::  
    你可以对下面的代码进行 **Modify/Reset/Copy/Run/Stop** 操作。但在此之前，需要先进入源码路径，如 ``picrawler\examples``。修改代码后，可以直接运行查看效果。  

.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from robot_hat import Music, Ultrasonic, Pin
    import time
    import signal

    music = Music()
    crawler = Picrawler()
    sonar = Ultrasonic(Pin("D2"), Pin("D3"))  # Ultrasonic trigger/echo pins

    music.music_set_volume(100)  # Set speaker volume

    alert_distance = 15  # Obstacle warning distance (cm)
    speed = 80           # Movement speed

    # ----------------------------
    # Add hardware timeout to sonar.read()
    # Prevent program from freezing
    # ----------------------------
    class Timeout(Exception):
        pass

    def _alarm_handler(signum, frame):
        raise Timeout()

    signal.signal(signal.SIGALRM, _alarm_handler)

    # Read distance once with timeout protection
    def safe_read_once(timeout_s=1):
        try:
            signal.alarm(timeout_s)
            d = sonar.read()
            signal.alarm(0)
            return d
        except Timeout:
            signal.alarm(0)
            return None
        except Exception:
            signal.alarm(0)
            return None

    # Read multiple times and return median value (anti-noise)
    def read_distance_filtered(n=5, gap=0.03, timeout_s=1):
        vals = []
        for _ in range(n):
            d = safe_read_once(timeout_s=timeout_s)
            if d is not None and d > 0:
                vals.append(d)
            time.sleep(gap)

        if not vals:
            return None

        vals.sort()
        return vals[len(vals)//2]  # Median filter

    def main():
        distance = read_distance_filtered(n=5, gap=0.03, timeout_s=1)
        print("distance:", distance)

        if distance is None:
            time.sleep(0.15)  # Wait if read failed
            return

        if distance <= alert_distance:
            # Obstacle detected → play sound and turn
            try:
                music.sound_play_threading('./sounds/sign.wav', volume=100)
            except Exception as e:
                print("sound error:", e)

            crawler.do_action('turn left angle', 1, speed)
            time.sleep(0.5)  # Quiet window after movement
        else:
            # Path clear → move forward
            crawler.do_action('forward', 1, speed)
            time.sleep(0.4)

    if __name__ == "__main__":
        try:
            crawler.do_step('stand', 40)  # Stand before starting
            time.sleep(1.0)

            while True:
                main()

        except KeyboardInterrupt:
            print("\nStop.")
        finally:
            try:
                crawler.do_step('sit', 40)  # Sit before exit
                time.sleep(1.0)
            except Exception:
                pass

**工作原理**

#. 初始化模块

   .. code-block:: python

      music = Music()
      crawler = Picrawler()
      sonar = Ultrasonic(Pin("D2"), Pin("D3"))

      music.music_set_volume(100)
      alert_distance = 15
      speed = 80

   该代码块初始化三个主要模块：
   - ``music``：用于控制声音播放。
   - ``crawler``：用于控制 PiCrawler 的运动。
   - ``sonar``：通过超声波传感器读取距离。

   同时还设置了扬声器音量、障碍物检测阈值（单位：厘米），
   以及机器人的运动速度。

#. 超时保护模块（防止 sonar.read() 卡死）

   .. code-block:: python

      class Timeout(Exception):
          pass

      def _alarm_handler(signum, frame):
          raise Timeout()

      signal.signal(signal.SIGALRM, _alarm_handler)

   超声波驱动在等待回波信号时可能会阻塞程序。
   该代码块安装了一个信号处理器，使程序可以中断
   卡住的 ``sonar.read()`` 调用，从而保证程序继续运行。

#. 函数：safe_read_once()

   .. code-block:: python

      def safe_read_once(timeout_s=1):
          try:
              signal.alarm(timeout_s)
              d = sonar.read()
              signal.alarm(0)
              return d
          except Timeout:
              signal.alarm(0)
              return None
          except Exception:
              signal.alarm(0)
              return None

   该函数在带有超时保护的情况下读取一次超声波距离。

   - 如果读取成功，则返回距离值。
   - 如果读取超时或发生错误，则返回 ``None``，避免程序卡死。

#. 函数：read_distance_filtered()

   .. code-block:: python

      def read_distance_filtered(n=5, gap=0.03, timeout_s=1):
          vals = []
          for _ in range(n):
              d = safe_read_once(timeout_s=timeout_s)
              if d is not None and d > 0:
                  vals.append(d)
              time.sleep(gap)

          if not vals:
              return None

          vals.sort()
          return vals[len(vals)//2]

   该函数通过多次采样来提高测量可靠性：

   - 无效数据（``None`` 或 ``<= 0``）会被忽略。
   - 将剩余的有效数据排序。
   - 返回中位数作为最终距离值，从而减少噪声影响。

#. 函数：main()（核心决策与动作）

   .. code-block:: python

      def main():
          distance = read_distance_filtered(...)
          if distance is None:
              return

          if distance <= alert_distance:
              music.sound_play_threading(...)
              crawler.do_action('turn left angle', 1, speed)
          else:
              crawler.do_action('forward', 1, speed)

   这是主要的控制逻辑：

   - 读取经过过滤的距离值。
   - 如果读取失败，则跳过本次循环。
   - 如果检测到的障碍物距离小于 ``alert_distance``，
     则播放警告声音并向左转。
   - 否则机器人向前移动。

#. 程序入口模块（循环运行 + 安全退出）

   .. code-block:: python

      if __name__ == "__main__":
          try:
              crawler.do_step('stand', 40)
              while True:
                  main()
          except KeyboardInterrupt:
              print("\nStop.")
          finally:
              crawler.do_step('sit', 40)

   该代码块控制程序的整体运行流程：

   - 程序开始前，机器人先站立。
   - 在无限循环中不断执行 ``main()``。
   - 按下 Ctrl+C 可以终止程序。
   - 程序退出前，机器人会安全地坐下。