.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein und verbinden Sie sich mit anderen Technikbegeisterten.

    **Warum mitmachen?**

    - **Expertenunterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Einblicken.
    - **Exklusive Rabatte**: Genießen Sie besondere Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und saisonalen Angeboten teil.

    👉 Bereit, mit uns zu entdecken und zu schaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _py_sound:

Soundeffekte
=====================

In diesem Beispiel verwenden wir die Soundeffekte von PiCrawler (genauer gesagt, von Robot HAT). Es besteht aus drei Teilen: **Musik**, **Soundeffekte** und **Text-zu-Sprache**.

.. image:: img/tts.png

**Installieren von i2samp**

Bevor Sie diese Funktionen nutzen können, müssen Sie zuerst den Lautsprecher aktivieren, damit dieser eingeschaltet wird und Töne erzeugen kann.

Führen Sie ``i2samp.sh`` aus, und dieses Skript installiert alles, was für die Nutzung des i2s-Verstärkers erforderlich ist.

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/
    sudo bash i2samp.sh

Es werden mehrere Aufforderungen angezeigt, um die Anfrage zu bestätigen. Bestätigen Sie alle Aufforderungen mit **Y**. Nach den Änderungen am Raspberry Pi-System ist ein Neustart erforderlich, damit diese wirksam werden.

Nach dem Neustart führen Sie das Skript ``i2samp.sh`` erneut aus, um den Verstärker zu testen. Wenn der Lautsprecher erfolgreich einen Ton abspielt, ist die Konfiguration abgeschlossen.

**Code ausführen**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 sound_effect.py

Nach dem Ausführen des Codes folgen Sie den Anweisungen, die im Terminal angezeigt werden.

Geben Sie eine Taste ein, um die Funktion aufzurufen!
* ``q``: Hintergrundmusik abspielen
* ``1``: Soundeffekt abspielen
* ``2``: Soundeffekt mit Threads abspielen
* ``t``: Text vorlesen lassen
* Wenn Sie das Programm beenden möchten, drücken Sie ``Ctrl+C``.

**Code**

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


**Wie funktioniert es?**

Die mit Hintergrundmusik verbundenen Funktionen sind:

* ``music = Music()`` : Deklariert das Objekt.
* ``music.music_set_volume(20)`` : Stellt die Lautstärke ein, der Bereich reicht von 0 bis 100.
* ``music.music_play(./musics/sports-Ahjay_Stelino.mp3)`` : Spielt Musikdateien ab, hier die Datei **sports-Ahjay_Stelino.mp3** im Verzeichnis ``./musics``.
* ``music.music_stop()`` : Stoppt die Hintergrundmusik.

.. note::

    Sie können verschiedene Soundeffekte oder Musik in den Ordner ``musics`` oder ``sounds`` über :ref:`filezilla` hinzufügen.

Die mit den Soundeffekten verbundenen Funktionen sind:

* ``music = Music()``
* ``music.sound_play('./sounds/talk1.wav')``: Spielt die Soundeffektdatei ab, hier die Datei **talk1.wav** im Verzeichnis ``./sounds``.
* ``music.sound_play_threading('./sounds/talk1.wav')``: Spielt die Soundeffektdatei im Modus eines neuen Threads ab, ohne den Haupt-Thread zu unterbrechen.

Die mit Text-zu-Sprache verbundenen Funktionen sind:

* ``tts = TTS()``
* ``tts.say(words)`` : Text-to-Speech-Ausgabe.
* ``tts.lang("en-US")`` : Setzt die Sprache.

.. note:: 

    Setzen Sie die Sprache, indem Sie den Parameter von ``lang("")`` mit den folgenden Zeichen einstellen.

.. list-table:: Language
    :widths: 15 50

    *   - zh-CN 
        - Mandarin (Chinesisch)
    *   - en-US 
        - Englisch (Vereinigte Staaten)
    *   - en-GB     
        - Englisch (Vereinigtes Königreich)
    *   - de-DE     
        - Deutsch (Deutschland)
    *   - es-ES     
        - Spanisch (Spanien)
    *   - fr-FR  
        - Französisch (Frankreich)
    *   - it-IT  
        - Italienisch (Italien)
