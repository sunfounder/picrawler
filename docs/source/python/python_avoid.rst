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

Nach dem Start des Codes wird der PiCrawler vorwärts gehen. Wenn er feststellt, dass der Abstand zum Hindernis weniger als 10 cm beträgt, stoppt er, gibt einen Warnton aus, dreht sich nach links und hält an. Wenn in der neuen Richtung kein Hindernis ist oder der Abstand größer als 10 cm ist, bewegt er sich weiter vorwärts.  

**Code**  

.. note::
    Sie können den unten stehenden Code **bearbeiten/zurücksetzen/kopieren/ausführen/stoppen**. Gehen Sie dazu zunächst in das Verzeichnis des Quellcodes, z. B. ``picrawler\examples``. Nach der Bearbeitung können Sie den Code direkt ausführen, um den Effekt zu sehen.  

.. raw:: html  

    <run></run>  

.. code-block:: python  

    from picrawler import Picrawler  
    from robot_hat import TTS, Music  
    from robot_hat import Ultrasonic  
    from robot_hat import Pin  
    import time  

    tts = TTS()  
    music = Music()  

    crawler = Picrawler()  
    sonar = Ultrasonic(Pin("D2") ,Pin("D3"))
    music.music_set_volume(100)  

    alert_distance = 15  
    speed = 80  

    def main():  
        distance = sonar.read()  
        print(distance)  
        if distance < 0:  
            pass  
        elif distance <= alert_distance:  
            try:  
                music.sound_play_threading('./sounds/sign.wav', volume=100)  
            except Exception as e:  
                print(e)  
            crawler.do_action('turn left angle',3,speed)
            time.sleep(0.2)  
        else :
            crawler.do_action('forward', 1,speed)
            time.sleep(0.2)  

    if __name__ == "__main__":  
        while True:  
            main()  

**Funktionsweise**  

Sie können den Abstand ermitteln, indem Sie die Klasse ``Ultrasonic`` importieren.  

.. code-block:: python  

    from robot_hat import Ultrasonic  

Dann initialisieren Sie die Ultraschall-Pins.  

.. code-block:: python  

    sonar = Ultrasonic(Pin("D2") ,Pin("D3"))

Hier ist das Hauptprogramm.  

* Lesen Sie die vom Ultraschallmodul erkannten ``Abstände`` und filtern Sie Werte kleiner als 0 heraus (wenn das Ultraschallmodul zu weit vom Hindernis entfernt ist oder die Daten nicht korrekt gelesen werden können, erscheint ``distance < 0``).  
* Wenn der ``Abstand`` kleiner oder gleich dem ``alert_distance`` (dem zuvor festgelegten Schwellenwert, der 10 beträgt) ist, wird der Soundeffekt ``sign.wav`` abgespielt. Der PiCrawler führt ``turn left angle`` aus.  
* Wenn der ``Abstand`` größer als ``alert_distance`` ist, bewegt sich der PiCrawler ``vorwärts``.  

.. code-block:: python  

    distance = sonar.read()  
    print(distance)  
    if distance < 0:  
        pass  
    elif distance <= alert_distance:  
        try:  
            music.sound_play_threading('./sounds/sign.wav', volume=100)  
        except Exception as e:  
            print(e)  
        crawler.do_action('turn left angle',3,speed)
        time.sleep(0.2)  
    else :
        crawler.do_action('forward', 1,speed)
        time.sleep(0.2)  


.. note::

    Sie können verschiedene Soundeffekte oder Musikdateien im Ordner ``musics`` oder ``sounds`` über :ref:`filezilla` hinzufügen.  
