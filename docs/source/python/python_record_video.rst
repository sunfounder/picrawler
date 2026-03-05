.. _py_video:

录制视频
==================

本示例将演示如何使用视频录制功能。

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 record_video.py


代码运行后，可以在浏览器中输入 ``http://<your IP>:9000/mjpg`` 来查看实时画面，例如： ``http://192.168.18.113:9000/mjpg``

.. image:: img/display.png

通过键盘按键可以开始或停止录制。

* 按下 ``q`` 开始录制，或实现暂停/继续；按下 ``e`` 停止录制并保存视频。  
* 若要退出程序，请按 ``Ctrl+C``   。


**代码** 

.. code-block:: python

    from time import sleep, strftime, localtime
    from vilib import Vilib
    import readchar
    from os import getlogin
    import os

    USERNAME = getlogin()
    VIDEO_PATH = f"/home/{USERNAME}/Videos/"

    MANUAL = '''
    Press keys on keyboard to control recording:
        Q: record/pause/continue
        E: stop
        Ctrl+C: Quit
    '''

    def print_overwrite(msg, end='', flush=True):
        """Overwrite the current terminal line."""
        print('\r\033[2K', end='', flush=True)
        print(msg, end=end, flush=True)

    def safe_stop_recording():
        """Stop recording safely (avoid exceptions during exit)."""
        try:
            Vilib.rec_video_stop()
        except Exception:
            pass

    def safe_close_camera():
        """Close camera safely (avoid exceptions during exit)."""
        try:
            Vilib.camera_close()
        except Exception:
            pass

    def main():
        rec_flag = 'stop'  # Possible states: start, pause, stop
        vname = None

        # Ensure the video directory exists
        os.makedirs(VIDEO_PATH, exist_ok=True)

        # Set save path for recorded videos
        Vilib.rec_video_set["path"] = VIDEO_PATH

        # Start camera and preview
        Vilib.camera_start(vflip=False, hflip=False)
        Vilib.display(local=False, web=True)
        sleep(0.8)  # Wait for camera startup

        print(MANUAL)

        try:
            while True:
                # Read keyboard input (no Enter needed)
                key = readchar.readkey().lower()

                # Q: start / pause / continue
                if key == 'q':
                    if rec_flag == 'stop':
                        rec_flag = 'start'

                        # Generate filename based on timestamp
                        vname = strftime("%Y-%m-%d-%H.%M.%S", localtime())
                        Vilib.rec_video_set["name"] = vname

                        # Start recording
                        Vilib.rec_video_run()
                        Vilib.rec_video_start()
                        print_overwrite('rec start ...')

                    elif rec_flag == 'start':
                        rec_flag = 'pause'
                        Vilib.rec_video_pause()
                        print_overwrite('pause')

                    elif rec_flag == 'pause':
                        rec_flag = 'start'
                        Vilib.rec_video_start()
                        print_overwrite('continue')

                # E: stop recording
                elif key == 'e' and rec_flag != 'stop':
                    rec_flag = 'stop'
                    safe_stop_recording()
                    print_overwrite(
                        "The video saved as %s%s.avi" % (Vilib.rec_video_set["path"], vname),
                        end='\n'
                    )

                # Ctrl+C (readchar special key): quit
                elif key == readchar.key.CTRL_C:
                    print('\nquit')
                    break

                sleep(0.1)

        except KeyboardInterrupt:
            # Handle Ctrl+C from terminal as well
            print('\nquit')

        finally:
            # If recording is still active, stop it before closing camera
            if rec_flag != 'stop':
                safe_stop_recording()
            safe_close_camera()
            sleep(0.1)

    if __name__ == "__main__":
        main()

**它是如何工作的？**

#. 程序功能

   该程序允许你使用键盘控制视频录制。

   • Q → 开始 / 暂停 / 继续录制  
   • E → 停止录制  
   • Ctrl+C → 退出程序  

   录制的视频将保存在 ``Videos`` 文件夹中。

#. 准备视频保存文件夹

   .. code-block:: python

      USERNAME = getlogin()
      VIDEO_PATH = f"/home/{USERNAME}/Videos/"
      os.makedirs(VIDEO_PATH, exist_ok=True)

   程序会获取当前系统用户名，
   如果 ``Videos`` 文件夹不存在，则会自动创建。

   所有录制的视频都会保存到该目录。

#. 启动摄像头

   .. code-block:: python

      Vilib.camera_start(vflip=False, hflip=False)
      Vilib.display(local=False, web=True)
      sleep(0.8)

   启动摄像头。

   同时启用网页预览功能，
   你可以在浏览器中观看实时视频流。

   短暂延时用于确保摄像头正常启动。

#. 录制状态设置

   .. code-block:: python

      rec_flag = 'stop'
      vname = None

   程序使用变量 ``rec_flag`` 来记录当前的录制状态：

   • stop  → 未录制  
   • start → 正在录制  
   • pause → 暂停录制  

#. 等待键盘输入

   .. code-block:: python

      key = readchar.readkey().lower()

   程序会等待用户按下一个键。

#. 按 Q 开始录制

   .. code-block:: python

      if rec_flag == 'stop':
          vname = strftime("%Y-%m-%d-%H.%M.%S", localtime())
          Vilib.rec_video_set["name"] = vname
          Vilib.rec_video_run()
          Vilib.rec_video_start()

   当你第一次按下 Q 时：

   • 程序会根据当前日期和时间生成文件名  
   • 视频录制会立即开始  

   示例文件名：

   2026-03-03-15.30.21.avi

#. 再次按 Q 暂停录制

   .. code-block:: python

      elif rec_flag == 'start':
          Vilib.rec_video_pause()

   如果当前正在录制，
   再次按下 Q 会暂停录制。

#. 再次按 Q 继续录制

   .. code-block:: python

      elif rec_flag == 'pause':
          Vilib.rec_video_start()

   如果当前处于暂停状态，
   再次按下 Q 会继续录制。

#. 按 E 停止录制

   .. code-block:: python

      elif key == 'e' and rec_flag != 'stop':
          Vilib.rec_video_stop()

   按下 E 会完全停止录制。

   视频文件会保存到：

   ``/home/your_username/Videos/``

#. 安全退出程序

   .. code-block:: python

      finally:
          if rec_flag != 'stop':
              Vilib.rec_video_stop()
          Vilib.camera_close()

   当程序退出时：

   • 如果仍在录制，会先停止录制  
   • 然后安全关闭摄像头  

   这样可以避免视频文件损坏或摄像头异常。