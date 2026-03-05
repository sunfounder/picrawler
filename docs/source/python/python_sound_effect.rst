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

Quando il programma si avvia, nel terminale viene visualizzato un menu di controllo.

Premendo un tasto viene immediatamente attivata la funzione corrispondente.

* ``q``: Attiva o disattiva la musica di sottofondo.
* ``1``: Riproduce diversi effetti sonori uno dopo l'altro (modalità bloccante).
* ``2``: Riproduce gli stessi effetti sonori utilizzando il threading (modalità non bloccante).
* ``t``: Il sistema pronuncia la parola "Hello" utilizzando il text-to-speech.

Il programma continua a funzionare e resta in attesa dell'input da tastiera.

Premi Ctrl+C per interrompere il programma.
Prima di uscire, qualsiasi musica di sottofondo viene interrotta automaticamente.

**Codice**

.. code-block:: python

    from time import sleep
    import readchar
    from robot_hat import Music, TTS

    music = Music()
    tts = TTS()

    manual = '''
    Press a key to trigger actions (no Enter needed):
        q: Play/Stop background music
        1: Play sound effect (blocking)
        2: Play sound effect (threading)
        t: Text to speak

        Ctrl^C: quit
    '''

    def main():
        print(manual)

        flag_bgm = False
        music.music_set_volume(20)
        tts.lang("en-US")

        try:
            while True:
                # Real-time key input (no Enter required)
                key = readchar.readkey().lower()

                if key == "q":
                    flag_bgm = not flag_bgm
                    if flag_bgm:
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

                elif key == "2":
                    music.sound_play_threading('./sounds/talk1.wav')
                    sleep(0.05)
                    music.sound_play_threading('./sounds/talk3.wav')
                    sleep(0.05)
                    music.sound_play_threading('./sounds/sign.wav')
                    sleep(0.5)

                elif key == "t":
                    tts.say("Hello")

        except KeyboardInterrupt:
            print("\nquit")

        finally:
            # Stop music before exit to reduce error messages
            try:
                music.music_stop()
            except Exception:
                pass

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
