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

.. image:: img/move.png

**Code ausführen**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 move.py

Nach dem Ausführen des Codes wird PiCrawler die folgenden Aktionen in dieser Reihenfolge ausführen: vorwärts bewegen, rückwärts bewegen, nach links drehen, nach rechts drehen, stehen bleiben.

**Code**

.. note::
    Sie können den folgenden Code **ändern/zurücksetzen/kopieren/ausführen/anhalten**. Stellen Sie jedoch sicher, dass Sie vorher zum Quellcode-Verzeichnis wie ``pisloth\examples`` navigieren. Nachdem Sie den Code geändert haben, können Sie ihn direkt ausführen, um die Auswirkungen zu sehen.

.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep
    
    crawler = Picrawler() 
    
    def main():  
        
        speed = 80
              
        while True:
           
            crawler.do_action('forward',2,speed)
            sleep(0.05)     
            crawler.do_action('backward',2,speed)
            sleep(0.05)          
            crawler.do_action('turn left',2,speed)
            sleep(0.05)           
            crawler.do_action('turn right',2,speed)
            sleep(0.05)  
            crawler.do_action('turn left angle',2,speed)
            sleep(0.05)  
            crawler.do_action('turn right angle',2,speed)
            sleep(0.05) 
            crawler.do_step('stand',speed)
            sleep(1)
    
    if __name__ == "__main__":
        main()


**Wie funktioniert es?**

Zuerst importieren Sie die ``Picrawler``-Klasse aus der ``picrawler``-Bibliothek, die alle Aktionen von PiCrawler und die zugehörigen Funktionen enthält.

.. code-block:: python

    from picrawler import Picrawler

Dann instanziieren Sie die ``crawler``-Klasse.

.. code-block:: python

    crawler = Picrawler() 

Schließlich verwenden Sie die Funktion ``crawler.do_action()`` , um PiCrawler in Bewegung zu setzen.

.. code-block:: python
    
    crawler.do_action('forward',2,speed)    
    crawler.do_action('backward',2,speed)         
    crawler.do_action('turn left',2,speed)          
    crawler.do_action('turn right',2,speed) 
    crawler.do_action('turn left angle',2,speed) 
    crawler.do_action('turn right angle',2,speed)

Im Allgemeinen kann jede Bewegung von PiCrawler mit der Funktion ``do_action()`` durchgeführt werden. Sie hat drei Parameter:

* ``motion_name`` ist der Name der spezifischen Aktion, z. B.: ``forward``, ``turn right``, ``turn left``, ``backward``, ``turn left angle``, ``turn right angle``.
* ``step`` gibt die Anzahl der Wiederholungen der jeweiligen Aktion an, der Standardwert ist 1.
* ``speed`` gibt die Geschwindigkeit der Aktion an, der Standardwert ist 50 und der Bereich reicht von 0 bis 100.

Zusätzlich wird hier auch ``crawler.do_step('stand',speed)`` verwendet, um PiCrawler zum Stehen zu bringen. Die Verwendung dieser Funktion wird im nächsten Beispiel erklärt.
