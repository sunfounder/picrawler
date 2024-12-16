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
        rec_flag = 'stop' # start, pause, stop
        vname = None
        Vilib.rec_video_set["path"] = VIDEO_PATH
    
        Vilib.camera_start(vflip=False, hflip=False) 
        Vilib.display(local=True, web=True)
        sleep(0.8)  # Warte auf den Start
    
        print(MANUAL)
        while True:
            # Tastatureingabe lesen
            key = readchar.readkey()
            key = key.lower()
            # Start, Pause
            if key == 'q':
                key = None
                if rec_flag == 'stop':            
                    rec_flag = 'start'
                    # Name festlegen
                    vname = strftime("%Y-%m-%d-%H.%M.%S", localtime())
                    Vilib.rec_video_set["name"] = vname
                    # Aufnahme starten
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

**Wie funktioniert es?**


Die mit der Aufnahme verbundenen Funktionen sind wie folgt:


* ``Vilib.rec_video_run(video_name)``: Startet den Thread für die Videoaufnahme. ``video_name`` ist der Name der Videodatei und sollte ein String sein.
* ``Vilib.rec_video_start()``: Startet oder setzt die Videoaufnahme fort.
* ``Vilib.rec_video_pause()``: Pausiert die Aufnahme.
* ``Vilib.rec_video_stop()``: Stoppt die Aufnahme.

``Vilib.rec_video_set["path"] = "~/video/test/"`` legt den Speicherort der Videodateien fest.
