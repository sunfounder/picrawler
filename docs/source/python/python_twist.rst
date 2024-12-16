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

**Code**

.. note::
    Sie können den folgenden Code **ändern/zurücksetzen/kopieren/ausführen/stoppen**. Dazu müssen Sie jedoch zunächst in den Quellcode-Pfad wie ``picrawler/examples`` wechseln. Nach der Änderung des Codes können Sie ihn direkt ausführen, um die Wirkung zu sehen.

.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from robot_hat import Music

    music = Music()
    crawler = Picrawler()


    def twist(speed):
        new_step=[[50, 50, -80], [50, 50, -80],[50, 50, -80], [50, 50, -80]]
        for i in range(4):
            for inc in range(30, 60, 5): 
                rise = [50,50,(-80+inc*0.5)]
                drop = [50,50,(-80-inc)]

                new_step[i]=rise
                new_step[(i+2)%4] = drop
                new_step[(i+1)%4] = rise
                new_step[(i-1)%4] = drop
                # print(new_step)
                crawler.do_step(new_step,speed)


    def main():  

        music.music_play('./musics/sports-Ahjay_Stelino.mp3')
        music.music_set_volume(20)

        while True:
            twist(speed=100) 

    
    if __name__ == "__main__":
        main()

**Wie funktioniert es?**

In diesem Code sollten Sie auf folgenden Abschnitt achten:

.. code-block:: python

    def twist(speed):
        ## [Rechtes Vorderbein],[Linkes Vorderbein],[Linkes Hinterbein],[Rechtes Hinterbein]
        new_step=[[50, 50, -80], [50, 50, -80],[50, 50, -80], [50, 50, -80]]
        for i in range(4):
            for inc in range(30,60,5):  
                rise = [50,50,(-80+inc*0.5)]
                drop = [50,50,(-80-inc)]

                new_step[i]=rise
                new_step[(i+2)%4] = drop
                new_step[(i+1)%4] = rise
                new_step[(i-1)%4] = drop
                crawler.do_step(new_step,speed)

Einfach ausgedrückt, wird durch zwei Schleifen das Array ``new_step`` so verändert, dass es kontinuierliche und regelmäßige Änderungen aufweist, während gleichzeitig ``crawler.do_step()`` die Pose ausführt und eine fließende Bewegung erzeugt.

Sie können die zugehörigen Koordinatenwerte für jede Pose intuitiv aus :ref:`py_posture` entnehmen.


Zusätzlich wurde in diesem Beispiel auch Hintergrundmusik abgespielt. Die Implementierung erfolgt wie folgt:

Hintergrundmusik abspielen, indem die folgenden Bibliotheken importiert werden.

.. code-block:: python

    from robot_hat import Music

Erstellen Sie ein Music-Objekt.

.. code-block:: python

    music = Music()

Spielen Sie die Hintergrundmusik aus dem Verzeichnis ``picrawler/examples/musics`` ab und stellen Sie die Lautstärke auf 20. Sie können auch Musik in den Ordner ``musics`` über :ref:`filezilla` hinzufügen.

.. code-block:: python

    music.music_play('./musics/sports-Ahjay_Stelino.mp3')
    music.music_set_volume(20)


.. note::

    Sie können verschiedene Soundeffekte oder Musik in den Ordner ``musics`` oder ``sounds`` über :ref:`filezilla` hinzufügen.
