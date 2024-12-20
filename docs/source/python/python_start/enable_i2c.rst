.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti Speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a promozioni e concorsi durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _i2c_spi_config:

6. Verifica dell'interfaccia I2C
========================================

Utilizzeremo l'interfaccia I2C del Raspberry Pi. Questa interfaccia dovrebbe essere stata abilitata durante l'installazione del modulo ``robot-hat``. Per assicurarci che tutto sia configurato correttamente, verifichiamo che sia effettivamente abilitata.

#. Inserisci il seguente comando:

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. Seleziona **Interfacing Options** premendo il tasto freccia in giù sulla tastiera, quindi premi il tasto **Enter**.

    .. image:: img/image282.png
        :align: center

#. Successivamente, seleziona **I2C**.

    .. image:: img/image283.png
        :align: center

#. Usa i tasti freccia sulla tastiera per selezionare **<Yes>** -> **<OK>** per completare la configurazione dell'I2C.

    .. image:: img/image284.png
        :align: center