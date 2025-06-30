.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti Speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a promozioni e concorsi durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_avoid:

Evitamento Ostacoli
=====================

In questo progetto, PiCrawler utilizzerà un modulo ultrasonico per rilevare gli ostacoli davanti a sé. 
Quando PiCrawler rileva un ostacolo, invierà un segnale e cercherà un'altra direzione per proseguire.

.. .. image:: img/avoid1.png

**Esegui il Codice**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 avoid.py

Dopo l'esecuzione del codice, PiCrawler inizierà a camminare in avanti. Se rileva che la distanza dell'ostacolo davanti è inferiore a 10 cm, si fermerà e emetterà un segnale acustico di avvertimento, quindi girerà a sinistra e si fermerà. Se non ci sono ostacoli nella direzione dopo aver girato a sinistra o la distanza dell'ostacolo è maggiore di 10 cm, continuerà a muoversi in avanti.

**Codice**

.. note::
    Puoi **Modificare/Reimpostare/Copiare/Eseguire/Fermare** il codice qui sotto. Prima di farlo, devi accedere al percorso del codice sorgente come ``picrawler\examples``. Dopo aver modificato il codice, puoi eseguirlo direttamente per vedere il risultato.

.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from robot_hat import TTS, Music
    from robot_hat import Ultrasonic
    from robot_hat import Pin
    import time

    tts = TTS()
    music = Music()

    crawler = Picrawler() 
    sonar = Ultrasonic(Pin("D2") ,Pin("D3"))
    music.music_set_volume(100)

    alert_distance = 15
    speed = 80

    def main():
        distance = sonar.read()
        print(distance)
        if distance < 0:
            pass
        elif distance <= alert_distance:
            try:
                music.sound_play_threading('./sounds/sign.wav', volume=100)
            except Exception as e:
                print(e)
            crawler.do_action('turn left angle',3,speed)
            time.sleep(0.2)
        else :
            crawler.do_action('forward', 1,speed)
            time.sleep(0.2)

    if __name__ == "__main__":
        while True:
            main()

**Come funziona?**

Puoi ottenere la distanza importando la classe ``Ultrasonic``.

.. code-block:: python

    from robot_hat import Ultrasonic

Successivamente, inizializza i pin ultrasonici.

.. code-block:: python

    sonar = Ultrasonic(Pin("D2") ,Pin("D3"))

Ecco il programma principale.

* Legge la ``distanza`` rilevata dal modulo ultrasonico e filtra i valori inferiori a 0 (Quando il modulo ultrasonico è troppo lontano dall'ostacolo o non può leggere i dati correttamente, comparirà ``distance<0``).
* Quando la ``distanza`` è minore o uguale a ``alert_distance`` (il valore di soglia impostato in precedenza, che è 10), riproduce l'effetto sonoro ``sign.wav``. PiCrawler esegue ``turn left angle``.
* Quando la ``distanza`` è maggiore di ``alert_distance``, PiCrawler si muove in ``forward``.

.. code-block:: python

    distance = sonar.read()
    print(distance)
    if distance < 0:
        pass
    elif distance <= alert_distance:
        try:
            music.sound_play_threading('./sounds/sign.wav', volume=100)
        except Exception as e:
            print(e)
        crawler.do_action('turn left angle',3,speed)
        time.sleep(0.2)
    else :
        crawler.do_action('forward', 1,speed)
        time.sleep(0.2)

.. note::

    Puoi aggiungere diversi effetti sonori o musiche alla cartella ``musics`` o ``sounds`` tramite :ref:`filezilla`.
