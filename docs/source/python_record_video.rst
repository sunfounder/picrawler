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

    from os import pardir
    from time import sleep
    from vilib import Vilib

    def main():
        Vilib.camera_start()
        Vilib.display()

        Vilib.rec_video_set["path"] = "/home/pi/video/test/"
        vname = "vtest"
        Vilib.rec_video_run(vname)
        print('start rec ...')
        while True:
            if input() == 'q':
                Vilib.rec_video_start()
                print('continue')
            if input() == 'w':
                Vilib.rec_video_pause()
                print('pause')                                                       
            if input() == 'e':
                Vilib.rec_video_stop()
                print('stop')
                print("The video saved as",Vilib.rec_video_set["path"],vname)

    if __name__ == "__main__":
        main()


**这个怎么运作?**

与录像相关的功能包括:

* ``Vilib.rec_video_run(video_name)`` : 启动线程来录制视频。 ``video_name`` 是一个字符串，表示视频文件的名称。
* ``Vilib.rec_video_start()`` : 开始或继续视频录制。
* ``Vilib.rec_video_pause()`` : 暂停录像。
* ``Vilib.rec_video_stop()`` : 停止录像。

``Vilib.rec_video_set["path"] = "/home/pi/video/test/"`` 设置视频文件的存储位置。