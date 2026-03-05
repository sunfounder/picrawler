.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie mit anderen Enthusiasten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.  

    **Warum beitreten?**  

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.  
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.  
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.  
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.  
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Gewinnspielen und saisonalen Aktionen teil.  

    👉 Bereit, mit uns zu entdecken und zu gestalten? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!  

.. _py_bull:  

Bullenkampf  
===============

Verwandeln Sie den PiCrawler in einen wütenden Stier! Nutzen Sie seine Kamera, um das rote Tuch zu verfolgen und darauf loszustürmen!  

.. .. image:: img/bullfight.png  

**Code ausführen**

.. raw:: html  

    <run></run>  

.. code-block::  

    cd ~/picrawler/examples  
    sudo python3 bull_fight.py  


**Bild anzeigen**  

Nach dem Start des Codes wird im Terminal folgende Eingabeaufforderung angezeigt:  

.. code-block::  

    No desktop !  
    * Serving Flask app "vilib.vilib" (lazy loading)  
    * Environment: production  
    WARNING: Do not use the development server in a production environment.  
    Use a production WSGI server instead.  
    * Debug mode: off  
    * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)  

Dann können Sie im Browser ``http://<Ihre IP>:9000/mjpg`` eingeben, um den Videostream anzuzeigen. Beispiel: ``https://192.168.18.113:9000/mjpg``  

.. image:: img/display.png  

**Code**  

.. note:: 
    Sie können den unten stehenden Code **bearbeiten/zurücksetzen/kopieren/ausführen/stoppen**. Gehen Sie dazu zunächst in das Quellcode-Verzeichnis, z. B. ``picrawler\examples``. Nach der Bearbeitung können Sie den Code direkt ausführen, um den Effekt zu sehen.  

.. raw:: html  

    <run></run>  

.. code-block:: python  

    from picrawler import Picrawler
    from time import sleep, time
    from robot_hat import Music
    from vilib import Vilib

    # Create robot and audio controller objects
    crawler = Picrawler()
    music = Music()

    def main():
        # Start camera and enable preview window
        Vilib.camera_start(vflip=False, hflip=False)
        Vilib.display(local=False, web=True)

        # Enable red color detection
        Vilib.color_detect("red")

        speed = 80                  # Movement speed
        last_seen = False           # Indicates whether the red target was detected in previous loop
        last_beep = 0               # Timestamp of last sound playback
        BEEP_COOLDOWN = 1.0         # Minimum interval between sound effects (seconds)

        # Stand once before starting tracking
        crawler.do_step('stand', 40)
        sleep(1.0)

        try:
            while True:
                # Read detection result
                if Vilib.detect_obj_parameter.get('color_n', 0) != 0:

                    # Get horizontal coordinate of detected red object
                    coordinate_x = Vilib.detect_obj_parameter.get('color_x', 0)

                    # Play sound effect with cooldown to avoid spamming
                    now = time()
                    if now - last_beep >= BEEP_COOLDOWN:
                        try:
                            music.sound_play_threading('./sounds/talk1.wav')
                        except Exception:
                            pass
                        last_beep = now

                    # Steering logic based on horizontal position
                    # Left side of image
                    if coordinate_x < 100:
                        crawler.do_action('turn left', 1, speed)

                    # Right side of image
                    elif coordinate_x > 220:
                        crawler.do_action('turn right', 1, speed)

                    # Center area → move forward
                    else:
                        crawler.do_action('forward', 2, speed)

                    last_seen = True
                    sleep(0.05)

                else:
                    # No red target detected

                    # Stop movement only once when target is lost
                    # This prevents repeated stand() calls that cause "push-up" effect
                    if last_seen:
                        crawler.do_step('stand', 40)
                        last_seen = False

                    sleep(0.15)

        except KeyboardInterrupt:
            # Stop program safely when Ctrl+C is pressed
            print("\nStop.")

        finally:
            # Cleanup section to avoid exit errors

            # Disable color detection
            try:
                Vilib.color_detect("close")
            except Exception:
                pass

            # Close camera safely
            try:
                Vilib.camera_close()
            except Exception:
                pass

            # Make the robot sit before exit
            try:
                crawler.do_step('sit', 40)
                sleep(1.0)
            except Exception:
                pass

    if __name__ == "__main__":
        main()



**Funktionsweise**  

#. Kamera-Initialisierung

   .. code-block:: python

      Vilib.camera_start(vflip=False, hflip=False)
      Vilib.display(local=False, web=True)
      Vilib.color_detect("red")

   Die Kamera wird gestartet und die Web-Vorschau wird aktiviert.  
   Die Erkennung der roten Farbe wird eingeschaltet.  
   Vilib verarbeitet kontinuierlich die Kamerabilder im Hintergrund
   und speichert die Erkennungsergebnisse in ``detect_obj_parameter``.

#. Vorbereitung des Roboters

   .. code-block:: python

      crawler.do_step('stand', 40)
      sleep(1.0)

   Der Roboter führt zunächst eine Standbewegung aus, bevor das Tracking beginnt.  
   Eine kurze Verzögerung stellt sicher, dass die Haltung stabil ist.

#. Erkennung des Ziels

   .. code-block:: python

      if Vilib.detect_obj_parameter.get('color_n', 0) != 0:
          coordinate_x = Vilib.detect_obj_parameter.get('color_x', 0)

   Das Programm prüft, ob ein rotes Objekt erkannt wurde.  
   Wenn ein Objekt erkannt wird, liest das Programm die horizontale
   Mittelpunktkoordinate (x-Position) des roten Objekts im Bild aus.

#. Entscheidungslogik für die Steuerung

   .. code-block:: python

      if coordinate_x < 100:
          crawler.do_action('turn left', 1, speed)
      elif coordinate_x > 220:
          crawler.do_action('turn right', 1, speed)
      else:
          crawler.do_action('forward', 2, speed)

   Das Bild wird in drei horizontale Zonen unterteilt:
   links, Mitte und rechts.

   • Linke Zone → nach links drehen  
   • Rechte Zone → nach rechts drehen  
   • Mittlere Zone → vorwärts bewegen  

   Dadurch kann der Roboter dem roten Objekt folgen.

#. Sound-Cooldown-Mechanismus

   .. code-block:: python

      now = time()
      if now - last_beep >= BEEP_COOLDOWN:
          music.sound_play_threading('./sounds/talk1.wav')
          last_beep = now

   Ein Cooldown-Timer verhindert eine wiederholte Audiowiedergabe.  
   Der Soundeffekt wird höchstens einmal pro Sekunde abgespielt,
   selbst wenn das Objekt weiterhin erkannt wird.

#. Behandlung bei verlorenem Ziel

   .. code-block:: python

      if last_seen:
          crawler.do_step('stand', 40)
          last_seen = False

   Wenn das rote Objekt verschwindet,
   stoppt der Roboter und kehrt in eine stabile Standposition zurück.

   Das Flag ``last_seen`` stellt sicher, dass ``stand()`` nur einmal aufgerufen wird.  
   Dadurch wird verhindert, dass die Haltung wiederholt zurückgesetzt wird,
   was zu Zittern führen könnte.

#. Sicheres Beenden und Aufräumen

   .. code-block:: python

      finally:
          Vilib.color_detect("close")
          Vilib.camera_close()
          crawler.do_step('sit', 40)

   Wenn das Programm beendet wird (zum Beispiel mit Ctrl+C),
   wird die Farberkennung deaktiviert,
   die Kamera sicher geschlossen
   und der Roboter führt eine Sitzbewegung aus.

   Dadurch werden Kamerafehler und ein instabiles Herunterfahren vermieden.