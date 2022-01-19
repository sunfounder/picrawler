音效
=====================

在本例中，我们使用 PiCrawler（准确地说是 Robot HAT）的音效。它由三部分组成，分别是 **Muisc**, **Sound**, **Text to Speech**.

.. image:: img/tts.png


**安装 i2samp**

在使用该功能之前，请先激活扬声器，使其启用并可以发出声音。

运行 ``i2samp.sh`` ， 此脚本将安装使用 i2s 放大器所需的一切依赖。

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picrawler/
    sudo bash i2samp.sh 

过程中会有提示请求确认，全部输入 **Y** 即可。对 Raspberry Pi 系统进行更改后，需要重新启动计算机才能使这些更改生效。

重新启动后，再次运行脚本 ``i2samp.sh`` 以测试放大器。如果扬声器成功播放声音，则配置完成。

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picrawler/examples
    sudo python3 sound_effect.py

代码运行后，请按照终端打印的提示进行操作。

* 按下 ``q`` 来播放背景音乐
* 按下 ``1`` 来播放音效
* 按下 ``2`` 来以单独的线程播放音效
* 按下 ``t`` 来让PiCrawler说 ``Hello``。


**代码** 

.. code-block:: python

    from time import sleep
    from robot_hat import Music,TTS

    music = Music()
    tts = TTS()

    manual = '''
    Input key to call the function!
        q: Play background music
        1: Play sound effect
        2: Play sound effect with threads
        t: Text to Speech
    '''

    def main():  
        print(manual)

        flag_bgm = False
        music.music_set_volume(20)
        tts.lang("en-US")
        

        while True:
            key = input()  
            if key == "q" or key == "Q":
                flag_bgm = not flag_bgm
                if flag_bgm is True:
                    music.background_music('./musics/sports-Ahjay_Stelino.mp3')
                else:
                    music.music_stop()

            elif key == "1":
                music.sound_effect_play('./sounds/talk1.wav')
                sleep(0.05)
                music.sound_effect_play('./sounds/talk3.wav')
                sleep(0.05)
                music.sound_effect_play('./sounds/sign.wav')
                sleep(0.5)

            elif key =="2":
                music.sound_effect_threading('./sounds/talk1.wav')
                sleep(0.05)
                music.sound_effect_threading('./sounds/talk3.wav')
                sleep(0.05)
                music.sound_effect_threading('./sounds/sign.wav')
                sleep(0.5)

            elif key == "t" or key == "T":
                words = "Hello"
                tts.say(words)
            
    if __name__ == "__main__":
        main()

**这个怎么运作?**

与背景音乐相关的功能包括:

* ``music = Music()`` : 声明对象。
* ``music.music_set_volume(20)`` : 设置音量，范围为 0~100。
* ``music.background_music(./musics/sports-Ahjay_Stelino.mp3)`` : 播放音乐文件, 参数为文件所在路径，比如 ``./musics`` 路径下的 **sports-Ahjay_Stelino.mp3** 文件。
* ``music.music_stop()`` : 停止播放背景音乐。

.. note::

    你可以通过 :ref:`Filezilla` 给 ``musics`` or ``sounds`` 文件夹添加不同的音乐或者音效。


与音效相关的功能包括:

* ``music = Music()``
* ``music.sound_effect_play('./sounds/talk1.wav')`` : 播放音效文件, 参数为文件所在路径，比如 ``./sounds`` 路径下的 **talk1.wav** 文件。
* ``muisc.sound_effect_threading('./sounds/talk1.wav')`` : 开辟一个新的线程来播放音效文件，无需挂起主线程。

与文本到语音相关的功能包括:

* ``tts = TTS()``
* ``tts.say(words)`` : 文字音频。
* ``tts.lang("en-US")`` : 设置语言。

.. note:: 

    用 ``lang("")`` 函数来切换各国语言，参数为下列的字符。

.. list-table:: 语言
    :widths: 15 50

    *   - zh-CN 
        - 普通话 (中文)
    *   - en-US 
        - 英语-美
    *   - en-GB     
        - 英语-英
    *   - de-DE     
        - 德语
    *   - es-ES     
        - 西班牙语
    *   - fr-FR  
        - 法语
    *   - it-IT  
        - 意大利语