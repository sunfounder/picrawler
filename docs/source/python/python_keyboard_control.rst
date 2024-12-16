.. note::

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein und verbinden Sie sich mit anderen Technikbegeisterten.

    **Warum mitmachen?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitig Zugriff auf neue Produktankündigungen und Einblicke.
    - **Exklusive Rabatte**: Genießen Sie besondere Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und saisonalen Aktionen teil.

    👉 Bereit für spannende Projekte? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _py_keyboard:

Tastatursteuerung
====================

In diesem Projekt lernen wir, wie man den PiCrawler mit der Tastatur fernsteuert. Sie können den PiCrawler vorwärts, rückwärts, nach links und nach rechts bewegen.

**Code ausführen**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 keyboard_control.py

Press keys on keyboard to control PiCrawler!

* ``w``: Vorwärts
* ``a``: Nach links drehen
* ``s``: Rückwärts
* ``d``: Nach rechts drehen
* ``Ctrl+C``: Beenden

**Code**

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep
    import readchar

    crawler = Picrawler() 
    speed = 90

    manual = '''
    Press keys on keyboard to control PiCrawler!
        W: Forward
        A: Turn left
        S: Backward
        D: Turn right

        Ctrl^C: Quit
    '''

    def show_info():
        print("\033[H\033[J",end='')  # Terminalfenster leeren 
        print(manual)


    def main(): 
        show_info()   
        while True:
            key = readchar.readkey()
            key = key.lower()
            if key in('wsad'):
                if 'w' == key:
                    crawler.do_action('forward',1,speed)     
                elif 's' == key:
                    crawler.do_action('backward',1,speed)          
                elif 'a' == key:
                    crawler.do_action('turn left',1,speed)           
                elif 'd' == key:
                    crawler.do_action('turn right',1,speed)
                sleep(0.05)
                show_info()  
            elif key == readchar.key.CTRL_C:
                print("\n Quit") 
                break    

            sleep(0.02)          

    
    if __name__ == "__main__":
        main()

**Wie funktioniert das?**

Der PiCrawler sollte basierend auf den eingelesenen Tastaturzeichen die entsprechenden Aktionen ausführen. Die Funktion ``lower()`` wandelt Großbuchstaben in Kleinbuchstaben um, sodass die Eingabe unabhängig von der Groß-/Kleinschreibung funktioniert.

.. code-block:: python

    def main(): 
        show_info()   
        while True:
            key = readchar.readkey()
            key = key.lower()
            if key in('wsad'):
                if 'w' == key:
                    crawler.do_action('forward',1,speed)     
                elif 's' == key:
                    crawler.do_action('backward',1,speed)          
                elif 'a' == key:
                    crawler.do_action('turn left',1,speed)           
                elif 'd' == key:
                    crawler.do_action('turn right',1,speed)
                sleep(0.05)
                show_info()  
            elif key == readchar.key.CTRL_C:
                print("\n Quit") 
                break    
            
            sleep(0.02)  
