Sound Effect
=====================

In this example, we use PiCrawler's (to be precise, Robot HAT's) sound effects. It consists of three parts, namely **Muisc**, **Sound**, **Text to Speech**.

.. image:: image/tts.png

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

After the code runs, please operate according to the prompt that printed on the terminal.

**Code** 

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
            if key == "q"  or 'Q' == key:
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

            elif key == "t" or 'T' == key:
                words = "Hello"
                tts.say(words)
            
    if __name__ == "__main__":
        main()

**How it works?**

Functions related to background music include these:

* ``music = Music()`` : Declare the object.
* ``music.music_set_volume(20)`` : Set the volume, the range is 0~100.
* ``music.background_music(./musics/sports-Ahjay_Stelino.mp3)`` : Play music files, here is the **sports-Ahjay_Stelino.mp3** file under the ``./musics`` path.
* ``music.music_stop()`` : Stop playing background music.

.. note::

    You can add different sound effects or music to ``musics`` or ``sounds`` folder via :ref:`Filezilla Software`.


Functions related to sound effects include these:

* ``music = Music()``
* ``music.sound_effect_play('./sounds/talk1.wav')`` : Play the sound effect file, here is the **talk1.wav** file under the ``./musics`` path.
* ``muisc.sound_effect_threading('./sounds/talk1.wav')`` : Play the sound effect file in a new thread mode without suspending the main thread.

Functions related to Text to Speech include these:

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