.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein und verbinden Sie sich mit anderen Technikbegeisterten.

    **Warum mitmachen?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Unterstützung unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalten Sie frühen Zugang zu neuen Produktankündigungen und Einblicken.
    - **Exklusive Rabatte**: Genießen Sie besondere Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und saisonalen Angeboten teil.

    👉 Bereit, mit uns zu entdecken und zu schaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _py_record:

Neuen Schritt aufnehmen
==============================

In diesem Projekt verwenden wir die Tastatur, um PiCrawler verschiedene Posen ausführen zu lassen und diese Posen anschließend aufzuzeichnen. Diese können später abgespielt werden.

**Code ausführen**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 record_new_step_by_keyboard.py

Nachdem der Code ausgeführt wurde, folgen Sie den Anweisungen, die im Terminal angezeigt werden.

* Drücken Sie ``1234``, um die Beine einzeln auszuwählen: ``1``: rechtes Vorderbein, ``2``: linkes Vorderbein, ``3``: linkes Hinterbein, ``4``: rechtes Hinterbein
* Drücken Sie ``w``, ``a``, ``s``, ``d``, ``r`` und ``f``, um die Koordinatenwerte von PiCrawler langsam zu steuern.
* Drücken Sie ``Leertaste``, um alle Koordinatenwerte auszugeben.
* Drücken Sie ``p``, um die aufgezeichnete Aktion abzuspielen.
* Drücken Sie ``esc``, um das Programm zu beenden.

**Code**

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep
    import sys
    import tty
    import termios
    import copy

    crawler = Picrawler() 
    speed = 80

    def readchar():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


    manual = '''
    Drücken Sie Tasten auf der Tastatur zur Steuerung!
        w: Y++
        a: X--
        s: Y--
        d: X++
        r: Z++
        f: Z--
        1: Wählen Sie das rechte Vorderbein aus
        2: Wählen Sie das linke Vorderbein aus
        3: Wählen Sie das linke Hinterbein aus
        4: Wählen Sie das rechte Hinterbein aus
        Leertaste: Alle Bein-Koordinaten ausgeben & Schritt speichern
        p: Alle gespeicherten Schritte abspielen
        esc: Beenden
    '''

    new_step=[]

    def save_new_step():
        new_step.append(copy.deepcopy(crawler.current_step_all_leg_value()))
        print(new_step)

    def play_all_new_step():
        for step in new_step:
            crawler.do_step(step,speed)
            sleep(0.6)

    def main():  

        speed = 80
        print(manual)
        crawler.do_step('sit',speed)
        leg = 0 
        coodinate=crawler.current_step_leg_value(leg)   
        while True:
            key = readchar()
            key = key.lower()
            # print(key)
            if 'w' == key:
                coodinate[1]=coodinate[1]+2    
            elif 's' == key:
                coodinate[1]=coodinate[1]-2           
            elif 'a' == key:
                coodinate[0]=coodinate[0]-2         
            elif 'd' == key:
                coodinate[0]=coodinate[0]+2   
            elif 'r' == key:
                coodinate[2]=coodinate[2]+2         
            elif 'f' == key:
                coodinate[2]=coodinate[2]-2       
            elif '1' == key:
                leg=0
                coodinate=crawler.current_step_leg_value(leg)           
            elif '2' == key:
                leg=1   
                coodinate=crawler.current_step_leg_value(leg)              
            elif '3' == key:
                leg=2  
                coodinate=crawler.current_step_leg_value(leg)     
            elif '4' == key:
                leg=3     
                coodinate=crawler.current_step_leg_value(leg)  
            elif chr(32) == key:
                print("[[right front],[left front],[left rear],[right rear]]")
                print("saved new step")
                print(crawler.current_step_all_leg_value())
                save_new_step()
            elif 'p' == key:
                play_all_new_step()
            elif chr(27) == key:  # 27 für ESC
                break    

            sleep(0.05)
            crawler.do_single_leg(leg,coodinate,speed)          
        print("\n q Quit")  

    
    if __name__ == "__main__":
        main()

**Wie funktioniert es?**

Dieses Projekt basiert auf :ref:`py_posture` und fügt die Funktionen zur Aufnahme und Wiedergabe hinzu.

Die Aufnahmefunktion wird mit dem folgenden Code realisiert.

.. code-block:: python

    new_step=[]

    def save_new_step():
        new_step.append(copy.deepcopy(crawler.current_step_all_leg_value()))
        print(new_step)
.. note:: 
    Die Zuweisung hier benötigt die Verwendung der `Deep Copy <https://docs.python.org/3/library/copy.html>`_-Funktion, da sonst die ``new_step``-Liste nicht ein neues Array-Objekt beim Anhängen erhält.

Die Wiedergabefunktion wird mit folgendem Code umgesetzt.

.. code-block:: python

    def play_all_new_step():
        for step in new_step:
            crawler.do_step(step,speed)
            sleep(0.6)