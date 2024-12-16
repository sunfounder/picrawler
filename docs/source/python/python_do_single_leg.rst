.. note::

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 ein und tauschen Sie sich mit anderen Technikbegeisterten aus.

    **Warum mitmachen?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Einblicken.
    - **Exklusive Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit für spannende Projekte? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _py_posture:

Anpassung der Haltung
========================

In diesem Beispiel verwenden wir die Tastatur, um die Beine des PiCrawler einzeln zu steuern und die gewünschte Haltung einzunehmen.

Sie können die Leertaste drücken, um die aktuellen Koordinatenwerte auszudrucken. Diese Werte sind nützlich, wenn Sie eigene Aktionen für den PiCrawler erstellen möchten.

.. image:: img/1cood.A.png

**Code ausführen**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 do_single_leg.py

Nach dem Ausführen des Codes folgen Sie bitte den Anweisungen im Terminal.

* Drücken Sie ``1234``, um die Beine einzeln auszuwählen. ``1``: rechtes Vorderbein, ``2``: linkes Vorderbein, ``3``: linkes Hinterbein, ``4``: rechtes Hinterbein.
* Drücken Sie ``w``, ``a``, ``s``, ``d``, ``r`` und ``f``, um die Koordinaten des PiCrawler schrittweise anzupassen.
* Drücken Sie ``Ctrl+C``, um das Programm zu beenden.

**Code**

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep
    import readchar

    crawler = Picrawler()
    speed = 80


    manual = '''
    -------- PiCrawler Controller --------- 
           .......          .......
        <=|   2   |┌-┌┐┌┐-┐|   1   |=>
           ``````` ├      ┤ ```````
           ....... ├      ┤ .......
        <=|   3   |└------┘|   4   |=>
           ```````          ```````
        1: Select right front leg
        2: Select left front leg
        3: Select left rear leg
        4: Select right rear leg

        W: Y++          R: Z++             
        A: X--          F: Z--
        S: Y--
        D: X++          Ctrl+C: Quit
    '''
    legs_list = ['right front', 'left front', 'left rear', 'right rear']

    def main():  
        leg = 0
        speed = 80
        step = 2
        print(manual)
        crawler.do_step('stand', speed)
        sleep(0.2)
        coordinate=crawler.current_step_all_leg_value()  

        def show_info():
            print("\033[H\033[J", end='')  # clear terminal windows
            print(manual)   
            print('%s : %s'%(leg+1, legs_list[leg])) 
            print('coordinate: %s'%(coordinate))  

        show_info()

        while True:
            # Eingabe lesen
            key = readchar.readkey()
            key = key.lower()
            # Bein auswählen
            if key in ('1234'):
                leg = int(key) - 1
                show_info()
            # Bewegung
            elif key in ('wsadrf'):         
                if 'w' == key:
                    coordinate[leg][1]=coordinate[leg][1] + step    
                elif 's' == key:
                    coordinate[leg][1]=coordinate[leg][1] - step           
                elif 'a' == key:
                    coordinate[leg][0]=coordinate[leg][0] - step         
                elif 'd' == key:
                    coordinate[leg][0]=coordinate[leg][0] + step   
                elif 'r' == key:
                    coordinate[leg][2]=coordinate[leg][2] + step         
                elif 'f' == key:
                    coordinate[leg][2]=coordinate[leg][2] - step 

                crawler.do_single_leg(leg,coordinate[leg],speed) 
                sleep(0.1)  
                # coordinate=crawler.current_step_all_leg_value()
                show_info()

            sleep(0.05)


    if __name__ == "__main__":
        main()

* ``current_step_all_leg_value()``: Gibt die Koordinatenwerte aller Beine zurück.
* ``do_single_leg(leg, coordinate[leg], speed)``: Passt die Koordinatenwerte eines einzelnen Beins an.
