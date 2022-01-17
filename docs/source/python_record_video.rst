录制视频
==================

本示例将指导您如何使用录制视频功能。

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picrawler/examples
    sudo python3 record_video.py


代码运行后，在浏览器中输入 ``http://<your IP>:9000/mjpg`` 来查看视频画面。 比如:  ``https://192.168.18.113:9000/mjpg``

.. image:: image/display.png

然后按下键盘上的按键来录像或停止录像。

* 注意要将键盘切换为小写的英文输入。
* 按下 ``w`` 来暂停录像, 按下 ``q`` 键开始/继续录像，按下 ``e`` 停止录像。
* 注意每按下一个按键，都需要按下 ``Enter`` 来确认。



**代码** 

.. code-block:: python

    from time import sleep,strftime,localtime
    from vilib import Vilib
    import readchar

    manual = '''
    Press keys on keyboard to control recording:
            Q: record/pause/continue
            E: stop
            ESC: Quit
    '''

    def print_overwrite(msg,  end='', flush=True):
            print('\r\033[2K', end='',flush=True)
            print(msg, end=end, flush=True)

    def main():
            rec_flag = 'stop' # start,pause,stop
            vname = None
            Vilib.rec_video_set["path"] = "/home/pi/Videos/" # set path

            Vilib.camera_start(vflip=False,hflip=False)
            Vilib.display(local=True,web=True)
            sleep(0.8)  # wait for startup

            print(manual)
            while True:
                    # read keyboard
                    key = readchar.readkey()
                    key = key.lower()
                    # start,pause
                    if key == 'q':
                            key = None
                            if rec_flag == 'stop':
                                    rec_flag = 'start'
                                    # set name
                                    vname = strftime("%Y-%m-%d-%H.%M.%S", localtime())
                                    Vilib.rec_video_set["name"] = vname
                                    # start record
                                    Vilib.rec_video_run()
                                    print_overwrite('rec start ...')
                            elif rec_flag == 'start':
                                    rec_flag = 'pause'
                                    Vilib.rec_video_pause()
                                    print_overwrite('pause')
                            elif rec_flag == 'pause':
                                    rec_flag = 'start'
                                    Vilib.rec_video_start()
                                    print_overwrite('continue')
                    # stop
                    elif key == 'e' and rec_flag != 'stop':
                            key = None
                            rec_flag = 'stop'
                            Vilib.rec_video_stop()
                            print_overwrite("The video saved as %s%s.avi"%(Vilib.rec_video_set["path"],vname),end='\n')
                    # quit
                    elif key == readchar.key.CTRL_C or key in readchar.key.ESCAPE_SEQUENCES:
                            Vilib.camera_close()
                            print('\nquit')
                            break

                    sleep(0.1)

    if __name__ == "__main__":
            main()


**这个怎么运作?**

与录像相关的功能包括:

* ``Vilib.rec_video_run(video_name)`` : 启动线程来录制视频。 ``video_name`` 是一个字符串，表示视频文件的名称。
* ``Vilib.rec_video_start()`` : 开始或继续视频录制。
* ``Vilib.rec_video_pause()`` : 暂停录像。
* ``Vilib.rec_video_stop()`` : 停止录像。

``Vilib.rec_video_set["path"] = "/home/pi/video/test/"`` 设置视频文件的存储位置。