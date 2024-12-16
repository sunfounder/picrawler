.. note::

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 ein und tauschen Sie sich mit anderen Technikbegeisterten aus.

    **Warum mitmachen?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Einblicken.
    - **Exklusive Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit für spannende Projekte? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _py_pose:

Pose
=============

Der PiCrawler kann durch die Angabe eines Koordinatenarrays eine bestimmte Haltung einnehmen. Hier nimmt er eine Haltung mit erhobenem rechten Hinterbein ein.

.. image:: img/4cood.A.png

**Code ausführen**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 do_step.py


**Code**

.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep

    crawler = Picrawler() 

    ## [rechts vorne], [links vorne], [links hinten], [rechts hinten]
    new_step=[[45, 45, -75], [45, 0, -75], [45, 0, -30], [45, 45, -75]]
    stand_step = crawler.move_list['stand'][0]

    def main():  
        while True:
            speed = 80

            print(f"stand step: {stand_step}")
            crawler.do_step(stand_step, speed)
            sleep(3)
            print(f"new step: {new_step}")
            crawler.do_step(new_step,speed)
            sleep(3)

    
    if __name__ == "__main__":
        main()

**Funktionsweise**

In diesem Code ist die Funktion ``crawler.do_step()`` besonders wichtig.

Ähnlich wie bei ``do_action()`` kann auch ``do_step()`` das Verhalten des PiCrawler 
steuern. Der Unterschied besteht darin, dass die erste Methode kontinuierliche Bewegungen wie ``vorwärts gehen`` ausführt, während die zweite Methode separate Haltungen wie ``stehen`` oder ``sitzen`` ermöglicht.

**Zwei Verwendungsmöglichkeiten:**


1. **Verwendung mit String:**  
   Sie können direkt auf die ``step_list``-Daten im ``picrawler``-Modul zugreifen.

   .. code-block:: python

       crawler.do_step('stand',speed) 
       # "speed" gibt die Geschwindigkeit des Schritts an, der Bereich liegt zwischen 0~100.

2. **Verwendung mit Koordinatenarray:**  
   Sie können ein Array mit vier Koordinatenwerten angeben.

   .. code-block:: python

       new_step=[[45, 45, -75], [45, 0, -75], [45, 0, -30], [45, 45, -75]]
       # Diese vier Koordinaten steuern die Beine in der Reihenfolge rechts vorne, links vorne, links hinten, rechts hinten.

Jedes Bein hat ein eigenes Koordinatensystem, wie unten dargestellt:

.. image:: img/4cood.png

Die Koordinaten jedes Zehs müssen individuell gemessen werden. Beispiel:

.. image:: img/1cood.png

**Hinweis:**  
Die ``step_list``-Werte der ersten Methode bestehen ebenfalls aus Arrays mit vier Koordinatenwerten.

.. code-block:: python

    step_list = {

        "stand":[
            [45, 45, -50], 
            [45, 45, -50], 
            [45, 45, -50], 
            [45, 45, -50]
        ],
        "sit":[
            [45, 45, -30], 
            [45, 45, -30], 
            [45, 45, -30], 
            [45, 45, -30]
        ],
              
    }





