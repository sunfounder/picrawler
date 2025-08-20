.. _py_sound: 

音效功能
=====================

在本示例中，我们将使用 PiCrawler（更准确地说，是 Robot HAT）的音效功能。它分为三个部分： **Muisc** 、 **Sound** 、 **Text to Speech** 。

.. .. image:: img/tts.png

**安装i2samp**

在使用这些功能之前，需要先启用扬声器，使其能够发声。

运行 ``i2samp.sh`` 脚本，该脚本会安装使用 i2s 放大器所需的所有依赖。

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/
    sudo bash i2samp.sh 

运行过程中会出现多次提示，要求确认操作。请全部输入 **Y** 确认。完成系统修改后，需要重启树莓派才能使更改生效。

重启后，请再次运行 ``i2samp.sh`` 脚本来测试放大器。如果扬声器能够正常播放声音，说明配置完成。


**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 sound_effect.py

程序运行后，请根据终端打印的提示进行操作。

输入按键即可调用相应功能：
* ``q``: 播放背景音乐
* ``1``: 播放音效
* ``2``: 多线程播放音效
* ``t``: 文本转语音
* 若要退出程序，请按 ``Ctrl+C``


**代码** 

.. code-block:: python

    '''
        Sorry, currently there is only sound when running with sudo
    '''

    from time import sleep
    from robot_hat import Music,TTS

    music = Music()
    tts = TTS()

    manual = '''
    Input key to call the function!
        q: Play background music
        1: Play sound effect
        2: Play sound effect with threads
        t: Text to speak

        Ctrl^C: quit
    '''

    def main():  
        print(manual)

        flag_bgm = False
        music.music_set_volume(20)
        tts.lang("en-US")


        while True:
            key = input() 
            key = key.lower() 
            if key == "q":
                flag_bgm = not flag_bgm
                if flag_bgm is True:
                    music.music_play('./musics/sports-Ahjay_Stelino.mp3')
                else:
                    music.music_stop()

            elif key == "1":
                music.sound_play('./sounds/talk1.wav')
                sleep(0.05)
                music.sound_play('./sounds/talk3.wav')
                sleep(0.05)
                music.sound_play('./sounds/sign.wav')
                sleep(0.5)

            elif key =="2":
                music.sound_play_threading('./sounds/talk1.wav')
                sleep(0.05)
                music.sound_play_threading('./sounds/talk3.wav')
                sleep(0.05)
                music.sound_play_threading('./sounds/sign.wav')
                sleep(0.5)

            elif key == "t":
                words = "Hello"
                tts.say(words)

    if __name__ == "__main__":
        main()


**它是如何工作的？**

与背景音乐相关的函数包括：

* ``music = Music()`` : 声明对象  
* ``music.music_set_volume(20)`` : 设置音量，范围为 0~100  
* ``music.music_play(./musics/sports-Ahjay_Stelino.mp3)`` : 播放音乐文件，此处播放的是 ``./musics`` 路径下的 **sports-Ahjay_Stelino.mp3** 文件  
* ``music.music_stop()`` : 停止播放背景音乐  

.. note::

    你可以通过 :ref:`filezilla` 将不同的音效或音乐文件添加到 ``musics`` 或 ``sounds`` 文件夹中。


与音效相关的函数包括：

* ``music = Music()``  
* ``music.sound_play('./sounds/talk1.wav')``: 播放音效文件，此处为 ``./musics`` 路径下的 **talk1.wav**  
* ``music.sound_play_threading('./sounds/talk1.wav')``: 以多线程模式播放音效，不会阻塞主线程

与文本转语音相关的函数包括：

* ``tts = TTS()``  
* ``tts.say(words)`` : 将文本转换为语音  
* ``tts.lang("en-US")`` : 设置语言  

.. note:: 

    可以通过设置 ``lang("")`` 的参数来指定语言，支持以下选项：

.. list-table:: Language
    :widths: 15 50

    *   - zh-CN 
        - 普通话（中文）
    *   - en-US 
        - 英语-美国
    *   - en-GB     
        - 英语-英国
    *   - de-DE     
        - 德语-德国
    *   - es-ES     
        - 西班牙语-西班牙
    *   - fr-FR  
        - 法语-法国
    *   - it-IT  
        - 意大利语-意大利