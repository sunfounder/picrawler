Sound Effect
=====================

在这个示例中，我们使用PiCrawler的(准确的说，robot hat的)音效功能。它由三个部分组成，分别是 **Muisc**, **Sound**, **Text to Speech**.

**Install i2samp**

Before using that functions, first activate the speaker so that it will be enabled and can make sounds.

Run ``i2samp.sh`` in, and this script will install everything needed to use i2s amplifier.

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picrawler/
    sudo bash i2samp.sh 

There will be several prompts asking to confirm the request. Respond to all prompts with a **Y**. After the changes have been made to the Raspberry Pi system, the computer will need to reboot for these changes to take effect.

After rebooting, run the ``i2samp.sh`` script again to test the amplifier. If a sound successfully plays from the speaker, the configuration is complete.


**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picrawler/examples
    sudo python3 sound_effect.py

代码运行后，请根据terminal中弹出的提示进行操作。

**Code** 

.. code-block::python

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
            if key == "q":
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

            elif key == "t":
                words = "Hello"
                tts.say(words)
            
    if __name__ == "__main__":
        main()

**How it works?**

与背景音乐相关的函数包括这些：

* ``music = Music()`` : 声明对象
* ``music.music_set_volume(20)`` : 设置音量，范围是0~100。
* ``music.background_music(./musics/sports-Ahjay_Stelino.mp3)`` : 播放音乐文件，在这里是 ``./musics`` 路径下的 **sports-Ahjay_Stelino.mp3** 文件.
* ``music.music_stop()`` : 停止播放背景音乐

.. note::

    You can add different sound effects or music to ``musics`` or ``sounds`` folder via :ref:`Filezilla Software`.


与音效相关的函数包括这些：

* ``music = Music()``
* ``music.sound_effect_play('./sounds/talk1.wav')`` : 播放音效文件，在这里是 ``./musics`` 路径下的 **talk1.wav** 文件.
* ``muisc.sound_effect_threading('./sounds/talk1.wav')`` ： 以新线程的方式播放音效文件，不会暂停主线程的运行。

与 Text to Speech 相关的函数包括这些：

* ``tts = TTS()``
* ``tts.say(words)`` : Text audio.
* ``tts.lang("en-US")`` :  Set the language.

.. note:: 

    Set the language by setting the parameters of ``lang("")`` with the following characters.

.. list-table:: Language
    :widths: 15 50

    *   - zh-CN 
        - Mandarin (Chinese)
    *   - en-US 
        - English-United States
    *   - en-GB     
        - English-United Kingdom
    *   - de-DE     
        - Germany-Deutsch
    *   - es-ES     
        - España-Español
    *   - fr-FR  
        - France-Le français
    *   - it-IT  
        - Italia-lingua italiana