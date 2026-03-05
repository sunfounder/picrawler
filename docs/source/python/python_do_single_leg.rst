.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti Speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a promozioni e concorsi durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_posture:

Regolare la Postura
======================

In questo esempio utilizzeremo la tastiera per controllare il PiCrawler, piede per piede, e impostare la postura desiderata.

Puoi premere la barra spaziatrice per stampare i valori attuali delle coordinate. Questi valori delle coordinate saranno utili per creare azioni uniche per il PiCrawler.

.. image:: img/1cood.A.png

**Esegui il Codice**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 do_single_leg.py

Dopo l'esecuzione del codice, segui le istruzioni visualizzate nel terminale:

* Premi ``1234`` per selezionare i piedi separatamente: ``1``: piede anteriore destro, ``2``: piede anteriore sinistro, ``3``: piede posteriore sinistro, ``4``: piede posteriore destro.
* Premi ``w``, ``a``, ``s``, ``d``, ``r`` e ``f`` per controllare lentamente i valori delle coordinate del PiCrawler.
* Premi ``Ctrl+C`` per uscire.

**Codice**

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


* ``current_step_all_leg_value()``: Restituisce i valori delle coordinate di tutte le gambe.
* ``do_single_leg(leg,coordinate[leg],speed)``: Modifica individualmente il valore della coordinata di una determinata gamba.
