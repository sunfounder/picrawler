.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti Speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a promozioni e concorsi durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_move:

Movimento
=========

Questo è il primo progetto di PiCrawler. Realizza la sua funzione più basilare: il movimento.

.. image:: img/move.png

**Esegui il Codice**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 move.py

Dopo l'esecuzione del codice, PiCrawler eseguirà le seguenti azioni in sequenza: avanzare, indietreggiare, girare a sinistra, girare a destra, stare in piedi.

**Codice**

.. note::
    Puoi **Modificare/Reimpostare/Copiare/Eseguire/Interrompere** il codice seguente. Tuttavia, prima di farlo, devi accedere al percorso del codice sorgente come ``pisloth\examples``. Dopo aver modificato il codice, puoi eseguirlo direttamente per vedere l'effetto.

.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep
    
    crawler = Picrawler() 
    
    def main():  
        
        speed = 80
              
        while True:
           
            crawler.do_action('forward',2,speed)
            sleep(0.05)     
            crawler.do_action('backward',2,speed)
            sleep(0.05)          
            crawler.do_action('turn left',2,speed)
            sleep(0.05)           
            crawler.do_action('turn right',2,speed)
            sleep(0.05)  
            crawler.do_action('turn left angle',2,speed)
            sleep(0.05)  
            crawler.do_action('turn right angle',2,speed)
            sleep(0.05) 
            crawler.do_step('stand',speed)
            sleep(1)
    
    if __name__ == "__main__":
        main()


**Come funziona?**

Per prima cosa, importa la classe ``Picrawler`` dalla libreria ``picrawler`` che hai installato. Questa classe contiene tutte le azioni di PiCrawler e le funzioni che le implementano.

.. code-block:: python

    from picrawler import Picrawler

Successivamente, istanzia la classe ``crawler``.

.. code-block:: python

    crawler = Picrawler() 

Infine, utilizza la funzione ``crawler.do_action()`` per far muovere PiCrawler.

.. code-block:: python
    
    crawler.do_action('forward',2,speed)    
    crawler.do_action('backward',2,speed)         
    crawler.do_action('turn left',2,speed)          
    crawler.do_action('turn right',2,speed) 
    crawler.do_action('turn left angle',2,speed) 
    crawler.do_action('turn right angle',2,speed)

In generale, tutti i movimenti di PiCrawler possono essere implementati con la funzione ``do_action()``. Questa funzione accetta 3 parametri:

* ``motion_name`` è il nome di azioni specifiche, inclusi: ``forward``, ``turn right``, ``turn left``, ``backward``, ``turn left angle``, ``turn right angle``.
* ``step`` rappresenta il numero di volte in cui ogni azione viene eseguita, il valore predefinito è 1.
* ``speed`` indica la velocità dell'azione, il valore predefinito è 50 e l'intervallo è 0~100.

Inoltre, qui viene utilizzato anche ``crawler.do_step('stand',speed)`` per far stare in piedi PiCrawler. L'utilizzo di questa funzione sarà spiegato nel prossimo esempio.
