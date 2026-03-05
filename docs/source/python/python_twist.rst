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

Dopo l’avvio del programma, il robot si alza lentamente per raggiungere una postura stabile.

Una volta in piedi, la musica di sottofondo inizia a suonare. Allo stesso tempo, il robot esegue un movimento di danza con torsioni in modo continuo. Durante questo movimento, le quattro zampe si alzano e si abbassano alternativamente, creando un effetto di torsione ritmico. Le zampe si muovono in coppie coordinate, facendo apparire il corpo oscillare da un lato all’altro.

Un breve ritardo tra ogni passo rende il movimento più fluido e stabile, evitando movimenti bruschi o troppo rapidi.

Il robot continua a danzare mentre la musica è in riproduzione. Quando si preme **Ctrl+C**, il programma si interrompe e il robot torna in modo sicuro alla posizione seduta prima di uscire.

**Codice**

.. note::
    Puoi **Modificare/Reimpostare/Copiare/Eseguire/Interrompere** il codice qui sotto. Prima di farlo, vai al percorso del codice sorgente come ``picrawler\examples``. Dopo averlo modificato, puoi eseguirlo direttamente per vedere l'effetto.

.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from robot_hat import Music
    from time import sleep

    music = Music()
    crawler = Picrawler()

    def twist(speed):
        new_step = [[50, 50, -80], [50, 50, -80], [50, 50, -80], [50, 50, -80]]

        for i in range(4):
            for inc in range(30, 60, 5):
                rise = [50, 50, (-80 + inc * 0.5)]
                drop = [50, 50, (-80 - inc)]

                new_step[i] = rise
                new_step[(i + 2) % 4] = drop
                new_step[(i + 1) % 4] = rise
                new_step[(i - 1) % 4] = drop

                crawler.do_step(new_step, speed)
                sleep(0.03)  # small delay to make motion smoother and less "crazy"

    def main():
        try:
            # Stand up slowly first
            crawler.do_step('stand', 40)
            sleep(1.0)

            # Start music
            music.music_play('./musics/sports-Ahjay_Stelino.mp3')
            music.music_set_volume(20)

            while True:
                twist(speed=100)

        except KeyboardInterrupt:
            print("\nCtrl+C detected, exiting...")

        finally:
            # Sit down safely before exit
            try:
                crawler.do_step('sit', 40)
                sleep(1.0)
            except Exception:
                pass

    if __name__ == "__main__":
        main()

**Come funziona?**

In questo codice, presta attenzione a questa parte:

.. code-block:: python

    def twist(speed):
        new_step = [[50, 50, -80], [50, 50, -80], [50, 50, -80], [50, 50, -80]]

        for i in range(4):
            for inc in range(30, 60, 5):
                rise = [50, 50, (-80 + inc * 0.5)]
                drop = [50, 50, (-80 - inc)]

                new_step[i] = rise
                new_step[(i + 2) % 4] = drop
                new_step[(i + 1) % 4] = rise
                new_step[(i - 1) % 4] = drop

                crawler.do_step(new_step, speed)
                sleep(0.03)  # small delay to make motion smoother and less "crazy"

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
