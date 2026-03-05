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

    #!/usr/bin/env python3
    from picrawler import Picrawler
    from time import sleep
    import readchar

    crawler = Picrawler()

    SPEED = 80
    STEP_SIZE = 2

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

    # Axis mapping for cleaner logic
    move_map = {
        'w': (1, +STEP_SIZE),  # Y++
        's': (1, -STEP_SIZE),  # Y--
        'a': (0, -STEP_SIZE),  # X--
        'd': (0, +STEP_SIZE),  # X++
        'r': (2, +STEP_SIZE),  # Z++
        'f': (2, -STEP_SIZE),  # Z--
    }


    def clear_screen():
        print("\033[H\033[J", end='')


    def show_info(selected_leg, coordinate):
        clear_screen()
        print(manual)
        print(f"Selected leg: {selected_leg + 1} - {legs_list[selected_leg]}")
        print(f"Coordinate: {coordinate}")


    def main():
        selected_leg = 0

        try:
            print(manual)

            # Stand up first
            crawler.do_step('stand', 40)
            sleep(0.5)

            # Get current coordinates
            coordinate = crawler.current_step_all_leg_value()
            show_info(selected_leg, coordinate)

            while True:
                key = readchar.readkey().lower()

                # Select leg
                if key in ('1', '2', '3', '4'):
                    selected_leg = int(key) - 1
                    show_info(selected_leg, coordinate)

                # Move selected leg
                elif key in move_map:
                    axis, delta = move_map[key]

                    # Update coordinate
                    coordinate[selected_leg][axis] += delta

                    # Send updated position
                    crawler.do_single_leg(selected_leg, coordinate[selected_leg], SPEED)
                    sleep(0.1)

                    show_info(selected_leg, coordinate)

                sleep(0.05)

        except KeyboardInterrupt:
            print("\nExiting safely...")

        finally:
            # Return to sitting position on exit
            try:
                crawler.do_step('sit', 40)
                sleep(1)
            except Exception:
                pass

            print("Robot is now sitting. Program ended.")


    if __name__ == "__main__":
        main()


* ``current_step_all_leg_value()``: Gibt die Koordinatenwerte aller Beine zurück.
* ``do_single_leg(leg, coordinate[leg], speed)``: Passt die Koordinatenwerte eines einzelnen Beins an.
