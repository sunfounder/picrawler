.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie mit anderen Enthusiasten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.  

    **Warum beitreten?**  

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.  
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.  
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.  
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.  
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Gewinnspielen und saisonalen Aktionen teil.  

    👉 Bereit, mit uns zu entdecken und zu gestalten? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!  

.. _py_avoid:  

Hindernisvermeidung  
=====================

In diesem Projekt verwendet der PiCrawler ein Ultraschallmodul, um Hindernisse vor ihm zu erkennen.  
Wenn der PiCrawler ein Hindernis erkennt, sendet er ein Signal und sucht nach einer anderen Richtung, um weiterzugehen.  

.. .. image:: img/avoid1.png  

**Code ausführen**  

.. raw:: html  

    <run></run>  

.. code-block::  

    cd ~/picrawler/examples  
    sudo python3 avoid.py  

Wenn das Programm startet, steht der PiCrawler auf.

Er misst kontinuierlich die Entfernung mit dem Ultraschallsensor
und gibt den Wert im Terminal aus.

Wenn ein Hindernis innerhalb von 15 cm erkannt wird:
- Es wird ein Warnsignal abgespielt.
- Der Roboter führt eine kleine Linksdrehung aus.

Wenn der Weg frei ist:
- Der Roboter bewegt sich vorwärts.

Der Roboter vermeidet automatisch weiterhin Hindernisse,
bis Sie Ctrl+C drücken.

Vor dem Beenden setzt sich der Roboter sicher hin.

**Code**  

.. note::
    Sie können den unten stehenden Code **bearbeiten/zurücksetzen/kopieren/ausführen/stoppen**. Gehen Sie dazu zunächst in das Verzeichnis des Quellcodes, z. B. ``picrawler\examples``. Nach der Bearbeitung können Sie den Code direkt ausführen, um den Effekt zu sehen.  

.. raw:: html  

    <run></run>  

.. code-block:: python  

    from picrawler import Picrawler
    from robot_hat import Music, Ultrasonic, Pin
    import time
    import signal

    music = Music()
    crawler = Picrawler()
    sonar = Ultrasonic(Pin("D2"), Pin("D3"))  # Ultrasonic trigger/echo pins

    music.music_set_volume(100)  # Set speaker volume

    alert_distance = 15  # Obstacle warning distance (cm)
    speed = 80           # Movement speed

    # ----------------------------
    # Add hardware timeout to sonar.read()
    # Prevent program from freezing
    # ----------------------------
    class Timeout(Exception):
        pass

    def _alarm_handler(signum, frame):
        raise Timeout()

    signal.signal(signal.SIGALRM, _alarm_handler)

    # Read distance once with timeout protection
    def safe_read_once(timeout_s=1):
        try:
            signal.alarm(timeout_s)
            d = sonar.read()
            signal.alarm(0)
            return d
        except Timeout:
            signal.alarm(0)
            return None
        except Exception:
            signal.alarm(0)
            return None

    # Read multiple times and return median value (anti-noise)
    def read_distance_filtered(n=5, gap=0.03, timeout_s=1):
        vals = []
        for _ in range(n):
            d = safe_read_once(timeout_s=timeout_s)
            if d is not None and d > 0:
                vals.append(d)
            time.sleep(gap)

        if not vals:
            return None

        vals.sort()
        return vals[len(vals)//2]  # Median filter

    def main():
        distance = read_distance_filtered(n=5, gap=0.03, timeout_s=1)
        print("distance:", distance)

        if distance is None:
            time.sleep(0.15)  # Wait if read failed
            return

        if distance <= alert_distance:
            # Obstacle detected → play sound and turn
            try:
                music.sound_play_threading('./sounds/sign.wav', volume=100)
            except Exception as e:
                print("sound error:", e)

            crawler.do_action('turn left angle', 1, speed)
            time.sleep(0.5)  # Quiet window after movement
        else:
            # Path clear → move forward
            crawler.do_action('forward', 1, speed)
            time.sleep(0.4)

    if __name__ == "__main__":
        try:
            crawler.do_step('stand', 40)  # Stand before starting
            time.sleep(1.0)

            while True:
                main()

        except KeyboardInterrupt:
            print("\nStop.")
        finally:
            try:
                crawler.do_step('sit', 40)  # Sit before exit
                time.sleep(1.0)
            except Exception:
                pass 

**Funktionsweise**  

#. Initialisierungsblock

   .. code-block:: python

      music = Music()
      crawler = Picrawler()
      sonar = Ultrasonic(Pin("D2"), Pin("D3"))

      music.music_set_volume(100)
      alert_distance = 15
      speed = 80

   Dieser Block initialisiert die drei Hauptmodule:
   - ``music``: steuert die Audiowiedergabe.
   - ``crawler``: steuert die Bewegung des PiCrawler.
   - ``sonar``: misst die Entfernung mit dem Ultraschallsensor.

   Außerdem werden die Lautstärke des Lautsprechers, der Hindernis-Schwellenwert (cm)
   sowie die Bewegungsgeschwindigkeit festgelegt.

#. Timeout-Einstellungsblock (verhindert, dass sonar.read() einfriert)

   .. code-block:: python

      class Timeout(Exception):
          pass

      def _alarm_handler(signum, frame):
          raise Timeout()

      signal.signal(signal.SIGALRM, _alarm_handler)

   Der Ultraschalltreiber kann blockieren, während er auf das Echo-Signal wartet.
   Dieser Block installiert einen Signal-Handler, sodass das Programm einen
   festhängenden ``sonar.read()``-Aufruf unterbrechen und weiterlaufen kann.

#. Funktion: safe_read_once()

   .. code-block:: python

      def safe_read_once(timeout_s=1):
          try:
              signal.alarm(timeout_s)
              d = sonar.read()
              signal.alarm(0)
              return d
          except Timeout:
              signal.alarm(0)
              return None
          except Exception:
              signal.alarm(0)
              return None

   Diese Funktion liest die Ultraschallentfernung einmal mit Timeout-Schutz.
   - Wenn das Lesen erfolgreich ist, wird der Entfernungswert zurückgegeben.
   - Wenn ein Timeout oder ein Fehler auftritt, wird ``None`` zurückgegeben, anstatt dass das Programm hängen bleibt.

#. Funktion: read_distance_filtered()

   .. code-block:: python

      def read_distance_filtered(n=5, gap=0.03, timeout_s=1):
          vals = []
          for _ in range(n):
              d = safe_read_once(timeout_s=timeout_s)
              if d is not None and d > 0:
                  vals.append(d)
              time.sleep(gap)

          if not vals:
              return None

          vals.sort()
          return vals[len(vals)//2]

   Diese Funktion verbessert die Zuverlässigkeit, indem mehrere Messwerte gelesen werden:
   - Ungültige Werte (``None`` oder ``<= 0``) werden ignoriert.
   - Die verbleibenden Werte werden sortiert.
   - Der Medianwert wird zurückgegeben, um Messrauschen zu reduzieren.

#. Funktion: main() (Kernlogik für Entscheidung und Aktion)

   .. code-block:: python

      def main():
          distance = read_distance_filtered(...)
          if distance is None:
              return

          if distance <= alert_distance:
              music.sound_play_threading(...)
              crawler.do_action('turn left angle', 1, speed)
          else:
              crawler.do_action('forward', 1, speed)

   Dies ist die Hauptsteuerlogik:

   - Liest einen gefilterten Entfernungswert.
   - Wenn das Lesen fehlschlägt, wird dieser Zyklus übersprungen.
   - Wenn sich ein Hindernis näher als ``alert_distance`` befindet, wird ein Warnsound abgespielt und der Roboter dreht nach links.
   - Andernfalls fährt er vorwärts.

#. Programmeinstiegsblock (Endlosschleife + sicheres Beenden)

   .. code-block:: python

      if __name__ == "__main__":
          try:
              crawler.do_step('stand', 40)
              while True:
                  main()
          except KeyboardInterrupt:
              print("\nStop.")
          finally:
              crawler.do_step('sit', 40)

   Dieser Block steuert den gesamten Programmablauf:
   - Der Crawler steht zuerst auf, bevor das Programm startet.
   - Das Programm führt ``main()`` in einer Endlosschleife aus.
   - Durch Drücken von Ctrl+C wird die Schleife beendet.
   - Der Crawler setzt sich hin, bevor das Programm beendet wird.