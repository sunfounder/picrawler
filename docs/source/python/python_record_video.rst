.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein und verbinden Sie sich mit anderen Technikbegeisterten.

    **Warum mitmachen?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Unterstützung unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalten Sie frühen Zugang zu neuen Produktankündigungen und Einblicken.
    - **Exklusive Rabatte**: Genießen Sie besondere Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und saisonalen Angeboten teil.

    👉 Bereit, mit uns zu entdecken und zu schaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _py_video:

Video aufnehmen
==================

Dieses Beispiel zeigt Ihnen, wie Sie die Aufnahmefunktion verwenden.

**Code ausführen**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 record_video.py

Nach dem Start des Codes können Sie ``http://<Ihre IP>:9000/mjpg`` im Browser eingeben, um das Video anzuzeigen, zum Beispiel: ``http://192.168.18.113:9000/mjpg``

.. image:: img/display.png

Die Aufnahme kann durch Drücken der Tasten auf der Tastatur gestartet, pausiert oder gestoppt werden.

* Drücken Sie ``q``, um die Aufnahme zu starten oder zu pausieren/fortzusetzen, ``e``, um die Aufnahme zu stoppen oder zu speichern.
* Wenn Sie das Programm beenden möchten, drücken Sie ``Ctrl+C``.

**Code**

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

**Wie funktioniert es?**

#. Was dieses Programm macht

   Dieses Programm ermöglicht es Ihnen, die Videoaufnahme mit der Tastatur zu steuern.

   • Q → Aufnahme starten / pausieren / fortsetzen  
   • E → Aufnahme stoppen  
   • Ctrl+C → Programm beenden  

   Das aufgenommene Video wird im Ordner **Videos** gespeichert.

#. Vorbereitung des Video-Ordners

   .. code-block:: python

      USERNAME = getlogin()
      VIDEO_PATH = f"/home/{USERNAME}/Videos/"
      os.makedirs(VIDEO_PATH, exist_ok=True)

   Das Programm ermittelt Ihren aktuellen Benutzernamen  
   und erstellt einen **Videos**-Ordner, falls dieser noch nicht existiert.

   Alle aufgenommenen Videos werden hier gespeichert.

#. Starten der Kamera

   .. code-block:: python

      Vilib.camera_start(vflip=False, hflip=False)
      Vilib.display(local=False, web=True)
      sleep(0.8)

   Die Kamera wird eingeschaltet.  
   Die Web-Vorschau wird aktiviert, sodass Sie den Live-Stream im Browser ansehen können.

   Die kurze Verzögerung sorgt dafür, dass die Kamera korrekt startet.

#. Einrichtung des Aufnahmezustands

   .. code-block:: python

      rec_flag = 'stop'
      vname = None

   Das Programm verwendet eine Variable namens ``rec_flag``,
   um den aktuellen Aufnahmezustand zu speichern:

   • stop  → keine Aufnahme  
   • start → Aufnahme läuft  
   • pause → Aufnahme pausiert 

#. Warten auf Tastatureingaben

   .. code-block:: python

      key = readchar.readkey().lower()

   Das Programm wartet auf eine Tasteneingabe.

#. Q drücken, um die Aufnahme zu starten

   .. code-block:: python

      if rec_flag == 'stop':
          vname = strftime("%Y-%m-%d-%H.%M.%S", localtime())
          Vilib.rec_video_set["name"] = vname
          Vilib.rec_video_run()
          Vilib.rec_video_start()

   Wenn Sie **Q** zum ersten Mal drücken:

   • Es wird ein Dateiname anhand des aktuellen Datums und der Uhrzeit erstellt  
   • Die Aufnahme startet sofort  

   Beispiel-Dateiname:  
   2026-03-03-15.30.21.avi

#. Q erneut drücken, um zu pausieren

   .. code-block:: python

      elif rec_flag == 'start':
          Vilib.rec_video_pause()

   Wenn die Aufnahme bereits läuft,  
   wird sie durch erneutes Drücken von **Q** pausiert.

#. Q erneut drücken, um fortzusetzen

   .. code-block:: python

      elif rec_flag == 'pause':
          Vilib.rec_video_start()

   Wenn die Aufnahme pausiert ist,  
   wird sie durch erneutes Drücken von **Q** fortgesetzt.

#. E drücken, um die Aufnahme zu stoppen

   .. code-block:: python

      elif key == 'e' and rec_flag != 'stop':
          Vilib.rec_video_stop()

   Durch Drücken von **E** wird die Aufnahme vollständig beendet.

   Die Videodatei wird gespeichert unter:  
   ``/home/your_username/Videos/``

#. Programm sicher beenden

   .. code-block:: python

      finally:
          if rec_flag != 'stop':
              Vilib.rec_video_stop()
          Vilib.camera_close()

   Wenn das Programm beendet wird:

   • Die Aufnahme wird gestoppt (falls sie noch läuft)  
   • Die Kamera wird sicher geschlossen  

   Dadurch werden beschädigte Videodateien oder Kamerafehler verhindert.