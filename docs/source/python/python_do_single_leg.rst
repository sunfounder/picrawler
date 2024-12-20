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
            # readkey
            key = readchar.readkey()
            key = key.lower()
            # select the leg 
            if key in ('1234'):
                leg = int(key) - 1
                show_info()
            # move
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

* ``current_step_all_leg_value()``: Restituisce i valori delle coordinate di tutte le gambe.
* ``do_single_leg(leg,coordinate[leg],speed)``: Modifica individualmente il valore della coordinata di una determinata gamba.
