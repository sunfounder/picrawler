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
    from time import sleep  
    from robot_hat import Music  
    from vilib import Vilib  
    
    
    crawler = Picrawler()  
    
    music = Music()  
    
    def main():  
        Vilib.camera_start()  
        Vilib.display()  
        Vilib.color_detect("red")  
        speed = 80  
    
        while True:  
            if Vilib.detect_obj_parameter['color_n']!=0:
                coordinate_x = Vilib.detect_obj_parameter['color_x']  
                music.sound_play_threading('./sounds/talk1.wav')  
    
                if coordinate_x < 100:  
                    crawler.do_action('turn left',1,speed)
                    sleep(0.05)  
                elif coordinate_x > 220:  
                    crawler.do_action('turn right',1,speed)
                    sleep(0.05)  
                else :
                    crawler.do_action('forward',2,speed)
                    sleep(0.05)  
            else :
                crawler.do_step('stand',speed)
                sleep(0.05)  
    
    
    if __name__ == "__main__":  
        main()  


**Funktionsweise**  

Im Allgemeinen kombiniert dieses Projekt die Wissenspunkte von :ref:`py_move`, :ref:`py_vision` und :ref:`py_sound`.  

Der Ablauf ist in der folgenden Abbildung dargestellt:  

.. image:: img/bull_fight-f.png  

