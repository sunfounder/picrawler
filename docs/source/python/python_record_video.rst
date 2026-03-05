.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti Speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a promozioni e concorsi durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_video:

Registra Video
=================

Questo esempio ti guiderà su come utilizzare la funzione di registrazione.

**Esegui il Codice**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 record_video.py

Dopo l'esecuzione del codice, puoi inserire ``http://<il tuo IP>:9000/mjpg`` nel browser per visualizzare lo schermo video. Ad esempio: ``http://192.168.18.113:9000/mjpg``

.. image:: img/display.png

La registrazione può essere avviata o interrotta premendo i tasti sulla tastiera.

* Premi ``q`` per avviare la registrazione o mettere in pausa/continuare, ``e`` per fermare la registrazione o salvare.
* Per uscire dal programma, premi ``Ctrl+C``.

**Codice**

.. code-block:: python

    from time import sleep, strftime, localtime
    from vilib import Vilib
    import readchar
    from os import getlogin
    import os

    USERNAME = getlogin()
    VIDEO_PATH = f"/home/{USERNAME}/Videos/"

    MANUAL = '''
    Press keys on keyboard to control recording:
        Q: record/pause/continue
        E: stop
        Ctrl+C: Quit
    '''

    def print_overwrite(msg, end='', flush=True):
        """Overwrite the current terminal line."""
        print('\r\033[2K', end='', flush=True)
        print(msg, end=end, flush=True)

    def safe_stop_recording():
        """Stop recording safely (avoid exceptions during exit)."""
        try:
            Vilib.rec_video_stop()
        except Exception:
            pass

    def safe_close_camera():
        """Close camera safely (avoid exceptions during exit)."""
        try:
            Vilib.camera_close()
        except Exception:
            pass

    def main():
        rec_flag = 'stop'  # Possible states: start, pause, stop
        vname = None

        # Ensure the video directory exists
        os.makedirs(VIDEO_PATH, exist_ok=True)

        # Set save path for recorded videos
        Vilib.rec_video_set["path"] = VIDEO_PATH

        # Start camera and preview
        Vilib.camera_start(vflip=False, hflip=False)
        Vilib.display(local=False, web=True)
        sleep(0.8)  # Wait for camera startup

        print(MANUAL)

        try:
            while True:
                # Read keyboard input (no Enter needed)
                key = readchar.readkey().lower()

                # Q: start / pause / continue
                if key == 'q':
                    if rec_flag == 'stop':
                        rec_flag = 'start'

                        # Generate filename based on timestamp
                        vname = strftime("%Y-%m-%d-%H.%M.%S", localtime())
                        Vilib.rec_video_set["name"] = vname

                        # Start recording
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

                # E: stop recording
                elif key == 'e' and rec_flag != 'stop':
                    rec_flag = 'stop'
                    safe_stop_recording()
                    print_overwrite(
                        "The video saved as %s%s.avi" % (Vilib.rec_video_set["path"], vname),
                        end='\n'
                    )

                # Ctrl+C (readchar special key): quit
                elif key == readchar.key.CTRL_C:
                    print('\nquit')
                    break

                sleep(0.1)

        except KeyboardInterrupt:
            # Handle Ctrl+C from terminal as well
            print('\nquit')

        finally:
            # If recording is still active, stop it before closing camera
            if rec_flag != 'stop':
                safe_stop_recording()
            safe_close_camera()
            sleep(0.1)

    if __name__ == "__main__":
        main()

**Come funziona?**

#. Cosa fa questo programma

   Questo programma consente di controllare la registrazione video utilizzando la tastiera.

   • Q → Avvia / Pausa / Continua la registrazione  
   • E → Interrompe la registrazione  
   • Ctrl+C → Esce dal programma  

   Il video registrato verrà salvato nella cartella Videos.

#. Preparare la cartella Video

   .. code-block:: python

      USERNAME = getlogin()
      VIDEO_PATH = f"/home/{USERNAME}/Videos/"
      os.makedirs(VIDEO_PATH, exist_ok=True)

   Il programma individua il tuo nome utente corrente  
   e crea una cartella Videos se non esiste già.

   Tutti i video registrati verranno salvati qui.

#. Avviare la fotocamera

   .. code-block:: python

      Vilib.camera_start(vflip=False, hflip=False)
      Vilib.display(local=False, web=True)
      sleep(0.8)

   La fotocamera viene attivata.
   L'anteprima web viene abilitata così puoi guardare lo streaming live nel browser.

   Il breve ritardo consente alla fotocamera di avviarsi correttamente.

#. Impostazione dello stato di registrazione

   .. code-block:: python

      rec_flag = 'stop'
      vname = None

   Il programma utilizza una variabile chiamata rec_flag
   per ricordare lo stato corrente della registrazione:

   • stop  → non sta registrando  
   • start → sta registrando  
   • pause → in pausa 

#. Attendere l'input da tastiera

   .. code-block:: python

      key = readchar.readkey().lower()

   Il programma attende la pressione di un tasto.

#. Premere Q per avviare la registrazione

   .. code-block:: python

      if rec_flag == 'stop':
          vname = strftime("%Y-%m-%d-%H.%M.%S", localtime())
          Vilib.rec_video_set["name"] = vname
          Vilib.rec_video_run()
          Vilib.rec_video_start()

   Quando premi Q per la prima volta:

   • Viene generato un nome file utilizzando la data e l'ora correnti  
   • La registrazione inizia immediatamente  

   Esempio di nome file:
   2026-03-03-15.30.21.avi

#. Premere di nuovo Q per mettere in pausa

   .. code-block:: python

      elif rec_flag == 'start':
          Vilib.rec_video_pause()

   Se la registrazione è già in corso,
   premendo Q la registrazione verrà messa in pausa.

#. Premere di nuovo Q per continuare

   .. code-block:: python

      elif rec_flag == 'pause':
          Vilib.rec_video_start()

   Se la registrazione è in pausa,
   premendo di nuovo Q la registrazione continuerà.

#. Premere E per interrompere la registrazione

   .. code-block:: python

      elif key == 'e' and rec_flag != 'stop':
          Vilib.rec_video_stop()

   Premendo E la registrazione verrà interrotta completamente.

   Il file video verrà salvato in: ``/home/your_username/Videos/``

#. Uscire dal programma in modo sicuro

   .. code-block:: python

      finally:
          if rec_flag != 'stop':
              Vilib.rec_video_stop()
          Vilib.camera_close()

   Quando il programma termina:

   • La registrazione viene interrotta (se è ancora in esecuzione)  
   • La fotocamera viene chiusa in modo sicuro  

   Questo evita file video danneggiati o errori della fotocamera.