.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti Speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a promozioni e concorsi durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_emotional:

Robot Emotivo
================

Questo esempio mostra diverse azioni personalizzate e divertenti di PiCrawler.

**Esegui il Codice**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 emotional_robot.py

**Codice**

.. note::
    Puoi **Modificare/Reimpostare/Copiare/Eseguire/Interrompere** il codice qui sotto. Prima di farlo, devi accedere al percorso del codice sorgente come ``picrawler\examples``. Dopo aver modificato il codice, puoi eseguirlo direttamente per vedere il risultato.

.. raw:: html

    <run></run>


.. code-block:: python

    from picrawler import Picrawler
    from time import sleep

    crawler = Picrawler() 

    def handwork(speed):

        basic_step = []
        basic_step = crawler.step_list.get("sit")
        left_hand  = crawler.mix_step(basic_step,0,[0,50,80])
        right_hand  = crawler.mix_step(basic_step,1,[0,50,80])
        two_hand = crawler.mix_step(left_hand,1,[0,50,80])

        crawler.do_step('sit',speed)
        sleep(0.6)    
        crawler.do_step(left_hand,speed)
        sleep(0.6)
        crawler.do_step(two_hand,speed)
        sleep(0.6)
        crawler.do_step(right_hand,speed)
        sleep(0.6)
        crawler.do_step('sit',speed)
        sleep(0.6)

    def twist(speed):
        new_step=[[50, 50, -80], [50, 50, -80],[50, 50, -80], [50, 50, -80]]
        for i in range(4):
            for inc in range(30,60,5): 
                rise = [50,50,(-80+inc*0.5)]
                drop = [50,50,(-80-inc)]

                new_step[i]=rise
                new_step[(i+2)%4] = drop
                new_step[(i+1)%4] = rise
                new_step[(i-1)%4] = drop
                crawler.do_step(new_step,speed)

    ##"[[anteriore destro], [anteriore sinistro], [posteriore sinistro], [posteriore destro]]")

    def pushup(speed):
        up=[[80, 0, -100], [80, 0, -100],[0, 120, -60], [0, 120, -60]]
        down=[[80, 0, -30], [80, 0, -30],[0, 120, -60], [0, 120, -60]]
        crawler.do_step(up,speed)
        sleep(0.6)
        crawler.do_step(down,speed)
        sleep(0.6)

    def swimming(speed):
        for i in range(100):
            crawler.do_step([[100-i,i,0],[100-i,i,0],[0,120,-60+i/5],[0,100,-40-i/5]],speed)

    # main
    def main():
        speed = 100

        swimming(speed)
        pushup(speed)
        handwork(speed)
        twist(speed)

        sleep(0.05)

    if __name__ == "__main__":
        main()

    
 
