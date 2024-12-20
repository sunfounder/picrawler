.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti Speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a promozioni e concorsi durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_bull:

Combattimento del Toro
==========================

Trasforma PiCrawler in un toro infuriato! Usalo per seguire e caricare un panno rosso utilizzando la sua fotocamera!

.. image:: img/bullfight.png

**Esegui il Codice**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 bull_fight.py


**Visualizza l'Immagine**

Dopo aver eseguito il codice, il terminale mostrerà il seguente messaggio:

.. code-block::

    No desktop !
    * Serving Flask app "vilib.vilib" (lazy loading)
    * Environment: production
    WARNING: Do not use the development server in a production environment.
    Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)

Puoi quindi inserire ``http://<il tuo IP>:9000/mjpg`` nel browser per visualizzare il feed video, ad esempio: ``https://192.168.18.113:9000/mjpg``

.. image:: img/display.png

**Codice**

.. note::
    Puoi **Modificare/Reimpostare/Copiare/Eseguire/Fermare** il codice qui sotto. Prima di farlo, devi accedere al percorso del codice sorgente, come ``picrawler\examples``. Dopo aver modificato il codice, puoi eseguirlo direttamente per vedere il risultato.

.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep
    from robot_hat import Music
    from vilib import Vilib
    
    
    crawler = Picrawler() 
    
    music = Music()
    
    def main():
        Vilib.camera_start()
        Vilib.display()
        Vilib.color_detect("red") 
        speed = 80
    
        while True:
            if Vilib.detect_obj_parameter['color_n']!=0:
                coordinate_x = Vilib.detect_obj_parameter['color_x']
                music.sound_play_threading('./sounds/talk1.wav')
    
                if coordinate_x < 100:
                    crawler.do_action('turn left',1,speed)
                    sleep(0.05) 
                elif coordinate_x > 220:
                    crawler.do_action('turn right',1,speed)
                    sleep(0.05) 
                else :
                    crawler.do_action('forward',2,speed)
                    sleep(0.05)    
            else :
                crawler.do_step('stand',speed)
                sleep(0.05)
    
    
    if __name__ == "__main__":
        main()


**Come Funziona?**

In generale, questo progetto combina i punti chiave di :ref:`py_move`, :ref:`py_vision` e :ref:`py_sound`.

Il suo flusso è mostrato nella figura seguente:

.. image:: img/bull_fight-f.png

