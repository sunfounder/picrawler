.. note::

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein und verbinden Sie sich mit anderen Technikbegeisterten.

    **Warum mitmachen?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitig Zugriff auf neue Produktankündigungen und Einblicke.
    - **Exklusive Rabatte**: Genießen Sie besondere Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und saisonalen Aktionen teil.

    👉 Bereit für spannende Projekte? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _py_move:

Bewegung
==============

Dies ist das erste Projekt von PiCrawler. Es führt seine grundlegende Funktion aus – die Bewegung.

.. .. image:: img/move.png

**Code ausführen**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 move.py

Wenn das Programm startet, steht der PiCrawler auf und wartet kurz.

Anschließend führt er kontinuierlich einen Bewegungszyklus aus:
vorwärts, rückwärts, nach links drehen, nach rechts drehen,
eine kleine Linksdrehung und eine kleine Rechtsdrehung.

Zwischen jeder Aktion gibt es kurze Pausen, um die Bewegung flüssiger zu machen.

Drücken Sie Ctrl+C, um das Programm zu stoppen.
Vor dem Beenden setzt sich der Crawler sicher hin.

**Code**

.. note::
    Sie können den folgenden Code **ändern/zurücksetzen/kopieren/ausführen/anhalten**. Stellen Sie jedoch sicher, dass Sie vorher zum Quellcode-Verzeichnis wie ``picrawler\examples`` navigieren. Nachdem Sie den Code geändert haben, können Sie ihn direkt ausführen, um die Auswirkungen zu sehen.

.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep

    crawler = Picrawler()  # Create PiCrawler object

    def main():
        speed = 80  # Movement speed

        try:
            crawler.do_step('stand', 40)  # Stand up
            sleep(1.0)

            while True:
                crawler.do_action('forward', 1, speed)   # Move forward
                sleep(0.25)

                crawler.do_action('backward', 1, speed)  # Move backward
                sleep(0.25)

                crawler.do_action('turn left', 1, speed)  # Turn left
                sleep(0.25)

                crawler.do_action('turn right', 1, speed)  # Turn right
                sleep(0.25)

                crawler.do_action('turn left angle', 1, speed)  # Small left turn
                sleep(0.3)

                crawler.do_action('turn right angle', 1, speed)  # Small right turn
                sleep(0.3)

                sleep(0.5)

        except KeyboardInterrupt:
            print("\nCtrl+C pressed...")

        finally:
            crawler.do_step('sit', 40)  # Sit down before exit
            sleep(1.0)

    if __name__ == "__main__":
        main()


**Wie funktioniert es?**

#. Import und Initialisierung

   .. code-block:: python

      from picrawler import Picrawler
      from time import sleep

      crawler = Picrawler()

   Das Skript importiert die benötigten Module und erstellt ein
   ``Picrawler``-Objekt, das zur Steuerung aller Roboterbewegungen verwendet wird.

#. Hauptfunktion und Vorbereitung

   .. code-block:: python

      def main():
          speed = 80
          crawler.do_step('stand', 40)
          sleep(1.0)

   Die Funktion ``main()`` definiert die Bewegungsgeschwindigkeit.  
   Bevor die Schleife startet, steht der Roboter auf und stabilisiert seine Haltung.

#. Kontinuierliche Bewegungsschleife

   .. code-block:: python

      while True:
          crawler.do_action('forward', 1, speed)
          crawler.do_action('backward', 1, speed)
          crawler.do_action('turn left', 1, speed)
          crawler.do_action('turn right', 1, speed)
          crawler.do_action('turn left angle', 1, speed)
          crawler.do_action('turn right angle', 1, speed)

   Der Roboter führt kontinuierlich eine vordefinierte Sequenz von
   Bewegungsaktionen innerhalb einer Endlosschleife aus.  
   Kurze Pausen zwischen den Aktionen sorgen für eine flüssigere Bewegung.

#. Sicheres Beenden

   .. code-block:: python

      except KeyboardInterrupt:
          print("\nCtrl+C pressed...")
      finally:
          crawler.do_step('sit', 40)

   Die Struktur ``try / except / finally`` stellt sicher:
   - ``Ctrl+C`` stoppt die Schleife sicher.
   - Der Roboter setzt sich hin, bevor das Programm beendet wird.

#. Programmeinstieg

   .. code-block:: python

      if __name__ == "__main__":
          main()

   Dadurch wird sichergestellt, dass ``main()`` nur ausgeführt wird,
   wenn das Skript direkt gestartet wird.