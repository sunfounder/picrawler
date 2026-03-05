.. note::

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein und verbinden Sie sich mit anderen Technikbegeisterten.

    **Warum mitmachen?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Einblicken.
    - **Exklusive Rabatte**: Profitieren Sie von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Verlosungen und festlichen Aktionen teil.

    👉 Bereit für spannende Projekte? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _py_emotional:

Emotionaler Roboter
=====================

Dieses Beispiel zeigt mehrere interessante benutzerdefinierte Aktionen des PiCrawler.

**Code ausführen**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 emotional_robot.py

Nachdem das Programm gestartet wurde, steht der Roboter zunächst langsam auf, um eine stabile Haltung zu erreichen.

Anschließend führt er eine Reihe von Bewegungen aus, darunter schwimmähnliche Bewegungen, Liegestütze, Winken mit den Vorderbeinen und eine Drehbewegung wie bei einem Tanz. Diese Aktionen werden nacheinander ausgeführt und erzeugen ein dynamisches und ausdrucksstarkes Verhalten.

Wenn **Ctrl+C** gedrückt wird, beendet sich das Programm sicher und der Roboter kehrt in eine Sitzposition zurück.

**Code**

.. note::
    Sie können den folgenden Code **Ändern/Zurücksetzen/Kopieren/Ausführen/Beenden**. Bevor Sie dies tun, wechseln Sie bitte zum Quellcode-Pfad wie ``picrawler\examples``. Nach Änderungen können Sie den Code direkt ausführen, um die Effekte zu sehen.


.. raw:: html

    <run></run>


.. code-block:: python

    from picrawler import Picrawler
    from time import sleep

    crawler = Picrawler()


    def get_sit_step():
        # Get a valid sit step used as the base pose for hand actions
        try:
            return crawler.move_list['sit'][0]
        except Exception:
            return None


    def handwork(speed):
        base = get_sit_step()

        # If a valid sit step cannot be retrieved, just perform a sit action
        if not base or len(base) < 4:
            crawler.do_step('sit', speed)
            sleep(0.6)
            return

        # Generate hand poses by modifying the sit step
        left_hand = crawler.mix_step(base, 0, [0, 50, 80])
        right_hand = crawler.mix_step(base, 1, [0, 50, 80])
        two_hand = crawler.mix_step(left_hand, 1, [0, 50, 80])

        crawler.do_step('sit', speed)
        sleep(0.6)

        crawler.do_step(left_hand, speed)
        sleep(0.6)

        crawler.do_step(two_hand, speed)
        sleep(0.6)

        crawler.do_step(right_hand, speed)
        sleep(0.6)

        crawler.do_step('sit', speed)
        sleep(0.6)

    def twist(speed):
        # Initialize the base position for all four legs
        new_step = [[50, 50, -80], [50, 50, -80], [50, 50, -80], [50, 50, -80]]

        # Create a twisting motion by alternating rise and drop movements
        for i in range(4):
            for inc in range(30, 60, 5):
                rise = [50, 50, (-80 + inc * 0.5)]
                drop = [50, 50, (-80 - inc)]

                new_step[i] = rise
                new_step[(i + 2) % 4] = drop
                new_step[(i + 1) % 4] = rise
                new_step[(i - 1) % 4] = drop

                crawler.do_step(new_step, speed)
                sleep(0.02)

    def pushup(speed):
        # Two poses used to simulate a push-up motion
        up = [[80, 0, -100], [80, 0, -100], [0, 120, -60], [0, 120, -60]]
        down = [[80, 0, -30], [80, 0, -30], [0, 120, -60], [0, 120, -60]]

        crawler.do_step(up, speed)
        sleep(0.6)

        crawler.do_step(down, speed)
        sleep(0.6)

    def swimming(speed, loops=100):
        # Simulate a swimming-like motion by gradually adjusting leg coordinates
        for i in range(loops):
            crawler.do_step(
                [
                    [100 - i, i, 0],
                    [100 - i, i, 0],
                    [0, 120, -60 + i / 5],
                    [0, 100, -40 - i / 5]
                ],
                speed
            )
            sleep(0.01)

    def main():
        speed = 100

        try:
            # Stand up slowly before performing actions
            crawler.do_step('stand', 40)
            sleep(1.0)

            swimming(speed)
            pushup(speed)
            handwork(speed)
            twist(speed)

        except KeyboardInterrupt:
            print("\nCtrl+C detected, exiting...")

        finally:
            # Return to a sitting posture before exiting
            try:
                crawler.do_step('sit', 40)
                sleep(1.0)
            except Exception:
                pass

    if __name__ == "__main__":
        main()

**Wie funktioniert es?**

#. Wenn das Programm startet, steht der Roboter zunächst langsam auf, um eine stabile Haltung zu erreichen.

   .. code-block:: python
   
      crawler.do_step('stand', 40)
      sleep(1.0)

   Nachdem der Roboter steht, führt das Programm mehrere vordefinierte Bewegungen nacheinander aus.

#. Schwimmbewegung

   Der Roboter führt eine schwimmähnliche Bewegung aus, indem die Bein-Koordinaten schrittweise angepasst werden.

   .. code-block:: python

      for i in range(loops):
          crawler.do_step([
              [100-i, i, 0],
              [100-i, i, 0],
              [0,120,-60+i/5],
              [0,100,-40-i/5]
          ], speed)

#. Liegestütz-Bewegung

   Zwei Positionen werden definiert, um eine Liegestützbewegung zu simulieren.

   .. code-block:: python

      up = [[80,0,-100],[80,0,-100],[0,120,-60],[0,120,-60]]
      down = [[80,0,-30],[80,0,-30],[0,120,-60],[0,120,-60]]

      crawler.do_step(up, speed)
      crawler.do_step(down, speed)

#. Handbewegung

   Das Programm verändert die Koordinaten der Vorderbeine mithilfe von ``mix_step()``, um eine Wellenbewegung zu erzeugen.

   .. code-block:: python

      left_hand = crawler.mix_step(base,0,[0,50,80])
      right_hand = crawler.mix_step(base,1,[0,50,80])

#. Twist-Bewegung

   Der Roboter dreht seinen Körper, indem diagonal gegenüberliegende Beine angehoben und abgesenkt werden.

   .. code-block:: python

      rise = [50,50,(-80+inc*0.5)]
      drop = [50,50,(-80-inc)]
      crawler.do_step(new_step, speed)

#. Wenn **Ctrl+C** gedrückt wird, beendet sich das Programm sicher und der Roboter kehrt in eine Sitzposition zurück.

   .. code-block:: python
   
      crawler.do_step('sit', 40)  
 
