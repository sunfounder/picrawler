.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti Speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a promozioni e concorsi durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_pose:

Postura
===========

PiCrawler può assumere una postura specifica scrivendo un array di coordinate. Qui assume una postura con il piede posteriore destro sollevato.

.. image:: img/4cood.A.png

**Esegui il Codice**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 do_step.py

**Codice**

.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep

    crawler = Picrawler() 

    ## [anteriore destro], [anteriore sinistro], [posteriore sinistro], [posteriore destro]
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

**Come Funziona?**

In questo codice, la parte che devi considerare con attenzione è ``crawler.do_step()``.

Simile a ``do_action()``, ``do_step()`` può manipolare il comportamento del PiCrawler.
La differenza è che il primo può eseguire un comportamento continuo come ``move forward``, mentre il secondo può essere usato per gesti separati come ``stand`` e ``sit``.


Ha due utilizzi principali:

**Primo**: Può scrivere stringhe, utilizzando direttamente il dizionario ``step_list`` nella libreria ``picrawler``.

.. code-block:: python

    crawler.do_step('stand',speed) 
    # "speed" indica la velocità del passo, con un intervallo compreso tra 0~100.

**Secondo**: Può anche scrivere un array di 4 valori di coordinate.

.. code-block:: python

    new_step=[[45, 45, -75], [45, 0, -75], [45, 0, -30], [45, 45, -75]]
    # Queste quattro coordinate controllano rispettivamente le gambe: anteriore destra, anteriore sinistra, posteriore sinistra e posteriore destra.

Ogni piede ha un sistema di coordinate indipendente. Come mostrato nella figura sottostante:

.. image:: img/4cood.png

Devi misurare le coordinate di ciascun piede individualmente. Come mostrato qui sotto:

.. image:: img/1cood.png

**Nota**: Il ``step_list`` utilizzato nel primo metodo è composto da un array che contiene 4 valori di coordinate.

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





