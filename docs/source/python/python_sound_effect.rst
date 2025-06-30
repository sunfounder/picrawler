.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti Speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a promozioni e concorsi durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_sound:

Effetti Sonori
=====================

In questo esempio utilizziamo gli effetti sonori di PiCrawler (più precisamente del Robot HAT). È composto da tre parti: **Musica**, **Suono** e **Text-to-Speech**.

.. .. image:: img/tts.png

**Installa i2samp**

Prima di utilizzare queste funzioni, attiva il diffusore in modo che venga abilitato e possa emettere suoni.

Esegui ``i2samp.sh`` per installare tutto ciò che è necessario per utilizzare l'amplificatore i2s.

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/
    sudo bash i2samp.sh 

Durante l'esecuzione appariranno diversi prompt che richiedono conferma. Rispondi a tutti i prompt con **Y**. Dopo aver applicato le modifiche al sistema Raspberry Pi, sarà necessario riavviare il computer affinché queste modifiche abbiano effetto.

Dopo il riavvio, esegui di nuovo lo script ``i2samp.sh`` per testare l'amplificatore. Se il diffusore emette correttamente un suono, la configurazione è completa.

**Esegui il Codice**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 sound_effect.py

Dopo l'esecuzione del codice, segui le istruzioni stampate nel terminale.

Inserisci i tasti per chiamare la funzione!
* ``q``: Riproduci musica di sottofondo
* ``1``: Riproduci effetto sonoro
* ``2``: Riproduci effetto sonoro con thread
* ``t``: Testo da parlare
* Per uscire dal programma, premi ``Ctrl+C``.

**Codice**

.. code-block:: python

    '''
        Sorry, currently there is only sound when running with sudo
    '''

    from time import sleep
    from robot_hat import Music, TTS

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


**Come funziona?**

Le funzioni relative alla musica di sottofondo includono:

* ``music = Music()``: Dichiarare l'oggetto.
* ``music.music_set_volume(20)``: Imposta il volume, l'intervallo è 0~100.
* ``music.music_play(./musics/sports-Ahjay_Stelino.mp3)``: Riproduce il file musicale, in questo caso **sports-Ahjay_Stelino.mp3** nel percorso ``./musics``.
* ``music.music_stop()``: Interrompe la riproduzione della musica di sottofondo.

.. note::

    Puoi aggiungere diversi effetti sonori o musica alle cartelle ``musics`` o ``sounds`` tramite :ref:`filezilla`.

Le funzioni relative agli effetti sonori includono:

* ``music = Music()``
* ``music.sound_play('./sounds/talk1.wav')``: Riproduce il file dell'effetto sonoro, in questo caso **talk1.wav** nel percorso ``./sounds``.
* ``music.sound_play_threading('./sounds/talk1.wav')``: Riproduce il file dell'effetto sonoro in modalità thread senza sospendere il thread principale.

Le funzioni relative a Text-to-Speech includono:

* ``tts = TTS()``
* ``tts.say(words)``: Testo in audio.
* ``tts.lang("en-US")``: Imposta la lingua.

.. note:: 

    Imposta la lingua utilizzando i parametri di ``lang("")`` con i seguenti valori:

.. list-table:: Language
    :widths: 15 50

    *   - zh-CN 
        - Mandarino (Cinese)
    *   - en-US 
        - Inglese-Statunitense
    *   - en-GB     
        - Inglese-Britannico
    *   - de-DE     
        - Tedesco
    *   - es-ES     
        - Spagnolo
    *   - fr-FR  
        - Francese
    *   - it-IT  
        - Italiano
