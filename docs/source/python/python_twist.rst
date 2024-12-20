.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti Speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a promozioni e concorsi durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_twist:

Twist
==============

Sappiamo già come far assumere a PiCrawler una postura specifica. Il prossimo passo è combinare le posture per formare un'azione continua.

In questo esempio, le quattro zampe di PiCrawler si muovono su e giù a due a due, saltellando a ritmo di musica.

**Esegui il Codice**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 twist.py

**Codice**

.. note::
    Puoi **Modificare/Reimpostare/Copiare/Eseguire/Interrompere** il codice qui sotto. Prima di farlo, vai al percorso del codice sorgente come ``picrawler\examples``. Dopo averlo modificato, puoi eseguirlo direttamente per vedere l'effetto.

.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from robot_hat import Music

    music = Music()
    crawler = Picrawler()


    def twist(speed):
        new_step=[[50, 50, -80], [50, 50, -80],[50, 50, -80], [50, 50, -80]]
        for i in range(4):
            for inc in range(30, 60, 5): 
                rise = [50,50,(-80+inc*0.5)]
                drop = [50,50,(-80-inc)]

                new_step[i]=rise
                new_step[(i+2)%4] = drop
                new_step[(i+1)%4] = rise
                new_step[(i-1)%4] = drop
                # print(new_step)
                crawler.do_step(new_step,speed)


    def main():  

        music.music_play('./musics/sports-Ahjay_Stelino.mp3')
        music.music_set_volume(20)

        while True:
            twist(speed=100) 


    if __name__ == "__main__":
        main()

**Come funziona?**

In questo codice, presta attenzione a questa parte:

.. code-block:: python

    def twist(speed):
        ## [right front],[left front],[left rear],[right rear]
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

In parole semplici, utilizza due cicli for annidati per far sì che l'array ``new_step`` produca cambiamenti continui e regolari. Allo stesso tempo, ``crawler.do_step()`` esegue le posture per formare un'azione continua.

Puoi ottenere intuitivamente l'array di coordinate corrispondente a ciascuna postura da :ref:`py_posture`.

Inoltre, l'esempio riproduce anche della musica di sottofondo. Ecco come:

Riproduci la musica importando le seguenti librerie:

.. code-block:: python

    from robot_hat import Music

Dichiara un oggetto Music.

.. code-block:: python

    music = Music()

Riproduci la musica di sottofondo nella directory ``picrawler/examples/musics`` e imposta il volume a 20. Puoi anche aggiungere musica alla cartella ``musics`` tramite :ref:`filezilla`.

.. code-block:: python

    music.music_play('./musics/sports-Ahjay_Stelino.mp3')
    music.music_set_volume(20)


.. note::

    Puoi aggiungere effetti sonori o musica alla cartella ``musics`` o ``sounds`` tramite :ref:`filezilla`.
