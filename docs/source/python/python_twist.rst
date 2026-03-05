.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein und verbinden Sie sich mit anderen Technikbegeisterten.

    **Warum mitmachen?**

    - **Expertenunterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Einblicken.
    - **Exklusive Rabatte**: Genießen Sie besondere Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und saisonalen Angeboten teil.

    👉 Bereit, mit uns zu entdecken und zu schaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _py_twist:

Twist
==============

Wir wissen bereits, wie PiCrawler eine bestimmte Pose einnimmt. Der nächste Schritt besteht darin, diese Posen zu kombinieren, um eine kontinuierliche Bewegung zu erzeugen.

Hierbei hebt und senkt PiCrawler seine vier Beine paarweise, um im Takt der Musik zu springen.

**Code ausführen**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 twist.py

Nachdem das Programm gestartet wurde, steht der Roboter zunächst langsam auf, um eine stabile Haltung zu erreichen.

Sobald er steht, beginnt die Hintergrundmusik zu spielen. Gleichzeitig führt der Roboter eine kontinuierliche Dreh-Tanzbewegung aus. Während dieser Bewegung heben und senken sich die vier Beine abwechselnd, wodurch ein rhythmischer Dreh-Effekt entsteht. Die Beine bewegen sich paarweise koordiniert, sodass der Körper scheinbar von Seite zu Seite schwingt.

Eine kurze Verzögerung zwischen jedem Schritt sorgt dafür, dass die Bewegung flüssiger und stabiler wirkt, anstatt abrupt oder zu schnell zu sein.

Der Roboter tanzt weiter, während die Musik abgespielt wird. Wenn **Ctrl+C** gedrückt wird, stoppt das Programm und der Roboter kehrt vor dem Beenden sicher in eine Sitzposition zurück.

**Code**

.. note::
    Sie können den folgenden Code **ändern/zurücksetzen/kopieren/ausführen/stoppen**. Dazu müssen Sie jedoch zunächst in den Quellcode-Pfad wie ``picrawler/examples`` wechseln. Nach der Änderung des Codes können Sie ihn direkt ausführen, um die Wirkung zu sehen.

.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from robot_hat import Music
    from time import sleep

    music = Music()
    crawler = Picrawler()

    def twist(speed):
        new_step = [[50, 50, -80], [50, 50, -80], [50, 50, -80], [50, 50, -80]]

        for i in range(4):
            for inc in range(30, 60, 5):
                rise = [50, 50, (-80 + inc * 0.5)]
                drop = [50, 50, (-80 - inc)]

                new_step[i] = rise
                new_step[(i + 2) % 4] = drop
                new_step[(i + 1) % 4] = rise
                new_step[(i - 1) % 4] = drop

                crawler.do_step(new_step, speed)
                sleep(0.03)  # small delay to make motion smoother and less "crazy"

    def main():
        try:
            # Stand up slowly first
            crawler.do_step('stand', 40)
            sleep(1.0)

            # Start music
            music.music_play('./musics/sports-Ahjay_Stelino.mp3')
            music.music_set_volume(20)

            while True:
                twist(speed=100)

        except KeyboardInterrupt:
            print("\nCtrl+C detected, exiting...")

        finally:
            # Sit down safely before exit
            try:
                crawler.do_step('sit', 40)
                sleep(1.0)
            except Exception:
                pass

    if __name__ == "__main__":
        main()

**Wie funktioniert es?**

In diesem Code sollten Sie besonders auf folgenden Abschnitt achten:

.. code-block:: python

    def twist(speed):
        new_step = [[50, 50, -80], [50, 50, -80], [50, 50, -80], [50, 50, -80]]

        for i in range(4):
            for inc in range(30, 60, 5):
                rise = [50, 50, (-80 + inc * 0.5)]
                drop = [50, 50, (-80 - inc)]

                new_step[i] = rise
                new_step[(i + 2) % 4] = drop
                new_step[(i + 1) % 4] = rise
                new_step[(i - 1) % 4] = drop

                crawler.do_step(new_step, speed)
                sleep(0.03)  # kleine Verzögerung, damit die Bewegung flüssiger und weniger „hektisch“ wirkt

Vereinfacht gesagt verwendet dieser Abschnitt zwei verschachtelte ``for``-Schleifen, um das ``new_step``-Array kontinuierlich und regelmäßig zu verändern.  
Gleichzeitig führt ``crawler.do_step()`` jede neue Haltung aus, wodurch eine durchgehende Bewegungssequenz entsteht.

Die Koordinatenwert-Arrays, die zu jeder Pose gehören, können Sie in :ref:`py_posture` nachschlagen.


Zusätzlich spielt das Beispiel auch Hintergrundmusik ab. Die Umsetzung erfolgt folgendermaßen.

Zuerst wird die folgende Bibliothek importiert, um Musik abzuspielen.

.. code-block:: python

    from robot_hat import Music

Danach wird ein ``Music``-Objekt erstellt.

.. code-block:: python

    music = Music()

Die Hintergrundmusik aus dem Verzeichnis ``picrawler/examples/musics`` wird abgespielt und die Lautstärke auf 20 gesetzt.  
Sie können auch eigene Musikdateien über :ref:`filezilla` in den Ordner ``musics`` hochladen.

.. code-block:: python

    music.music_play('./musics/sports-Ahjay_Stelino.mp3')
    music.music_set_volume(20)