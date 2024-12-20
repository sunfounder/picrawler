.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti Speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a promozioni e concorsi durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_record:

Registra Nuovo Passo
=======================

Utilizziamo la tastiera per controllare PiCrawler affinché assuma diverse pose, registriamo queste pose e le riproduciamo successivamente.

**Esegui il Codice**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 record_new_step_by_keyboard.py

Dopo l'esecuzione del codice, segui le istruzioni che appaiono nel terminale.

* Premi ``1234`` per selezionare le zampe singolarmente, ``1``: zampa anteriore destra, ``2``: zampa anteriore sinistra, ``3``: zampa posteriore sinistra, ``4``: zampa posteriore destra
* Premi ``w``, ``a``, ``s``, ``d``, ``r`` e ``f`` per controllare lentamente i valori delle coordinate del PiCrawler.
* Premi ``space`` per stampare tutti i valori delle coordinate.
* Premi ``p`` per far riprodurre a PiCrawler l'azione registrata.
* Premi ``esc`` per uscire.

**Codice**

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
    Press keys on keyboard to control!
        w: Y++
        a: X--
        s: Y--
        d: X++
        r: Z++
        f: Z--
        1: Select right front leg
        2: Select left front leg
        3: Select left rear leg
        4: Select right rear leg
        Space: Print all leg coodinate & Save this step
        p: Play all saved step
        esc: Quit
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
            elif chr(27) == key:  # 27 per ESC
                break    

            sleep(0.05)
            crawler.do_single_leg(leg,coodinate,speed)          
        print("\n q Quit")  

    
    if __name__ == "__main__":
        main()

**Come funziona?**

Questo progetto nasce da :ref:`py_posture` e aggiunge funzioni di registrazione e riproduzione.

La funzione di registrazione è implementata con il seguente codice.

.. code-block:: python

    new_step=[]

    def save_new_step():
        new_step.append(copy.deepcopy(crawler.current_step_all_leg_value()))
        print(new_step)

.. note:: 
    L'assegnazione qui richiede l'uso della funzione `Deep Copy <https://docs.python.org/3/library/copy.html>`_, altrimenti ``new_step`` non otterrà un nuovo oggetto array quando viene aggiunto.

La funzione di riproduzione è implementata con il seguente codice.

.. code-block:: python

    def play_all_new_step():
        for step in new_step:
            crawler.do_step(step,speed)
            sleep(0.6)