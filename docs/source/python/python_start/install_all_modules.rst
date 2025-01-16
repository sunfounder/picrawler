.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti Speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a promozioni e concorsi durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _install_all_modules:

5. Installa Tutti i Moduli (Importante)
===============================================

Assicurati di essere connesso a Internet e aggiorna il tuo sistema:

.. raw:: html

    <run></run>

.. code-block::

    sudo apt update
    sudo apt upgrade

.. note::

    I pacchetti relativi a Python3 devono essere installati se stai utilizzando il sistema operativo in versione Lite.

    .. raw:: html

        <run></run>

    .. code-block::
    
        sudo apt install git python3-pip python3-setuptools python3-smbus

Installa il modulo ``robot-hat``.

.. raw:: html

    <run></run>

.. code-block::

    cd ~/
    git clone -b v2.0 https://github.com/sunfounder/robot-hat.git
    cd robot-hat
    sudo python3 setup.py install

Successivamente, scarica il codice e installa il modulo ``vilib``.

.. raw:: html

    <run></run>

.. code-block::

    cd ~/
    git clone -b picamera2 https://github.com/sunfounder/vilib.git
    cd vilib
    sudo python3 install.py

Poi scarica il codice e installa il modulo ``picrawler``.

.. raw:: html

    <run></run>

.. code-block::

    cd ~/
    git clone https://github.com/sunfounder/picrawler.git --depth 1
    cd picrawler
    sudo python3 setup.py install

Questo passaggio richiederà un po' di tempo, quindi sii paziente.

Infine, è necessario eseguire lo script ``i2samp.sh`` per installare i componenti richiesti dall'amplificatore i2s, altrimenti il pislot non avrà suono.

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler
    sudo bash i2samp.sh
	
.. image:: img/i2s.png

Digita ``y`` e premi ``Enter`` per continuare l'esecuzione dello script.

.. image:: img/i2s2.png

Digita ``y`` e premi ``Enter`` per eseguire ``/dev/zero`` in background.

.. image:: img/i2s3.png

Digita ``y`` e premi ``Enter`` per riavviare il sistema.

.. note::
    Se non senti alcun suono dopo il riavvio, potrebbe essere necessario eseguire lo script ``i2samp.sh`` più volte.
