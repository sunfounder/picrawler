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

    from time import sleep,strftime,localtime
    from vilib import Vilib
    import readchar 
    from os import getlogin
    
    USERNAME = getlogin()
    VIDEO_PATH = f"/home/{USERNAME}/Videos/"
    
    MANUAL = '''
    Press keys on keyboard to control recording:
        Q: record/pause/continue
        E: stop
        Ctrl^C: Quit
    '''
    
    def print_overwrite(msg,  end='', flush=True):
        print('\r\033[2K', end='',flush=True)
        print(msg, end=end, flush=True)
    
    def main():
        rec_flag = 'stop' # start,pause,stop
        vname = None
        Vilib.rec_video_set["path"] = VIDEO_PATH
    
        Vilib.camera_start(vflip=False,hflip=False) 
        Vilib.display(local=True,web=True)
        sleep(0.8)  # 等待启动完成
    
        print(MANUAL)
        while True:
            # 读取键盘输入
            key = readchar.readkey()
            key = key.lower()
            # 开始/暂停
            if key == 'q':
                key = None
                if rec_flag == 'stop':            
                    rec_flag = 'start'
                    # 设置文件名
                    vname = strftime("%Y-%m-%d-%H.%M.%S", localtime())
                    Vilib.rec_video_set["name"] = vname
                    # 开始录制
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
            # stop       
            elif key == 'e' and rec_flag != 'stop':
                key = None
                rec_flag = 'stop'
                Vilib.rec_video_stop()
                print_overwrite("The video saved as %s%s.avi"%(Vilib.rec_video_set["path"],vname),end='\n')  
            # quit
            elif key == readchar.key.CTRL_C:
                Vilib.camera_close()
                print('\nquit')
                break 
    
            sleep(0.1)
    
    if __name__ == "__main__":
        main()

**它是如何工作的？**

与录制相关的函数包括以下几项：

* ``Vilib.rec_video_run(video_name)`` ：启动视频录制线程。 ``video_name`` 为视频文件名，需为字符串  
* ``Vilib.rec_video_start()`` ：开始或继续录制视频  
* ``Vilib.rec_video_pause()`` ：暂停录制  
* ``Vilib.rec_video_stop()`` ：停止录制  

另外， ``Vilib.rec_video_set["path"] = "~/video/test/"`` 用于设置视频文件的保存路径。