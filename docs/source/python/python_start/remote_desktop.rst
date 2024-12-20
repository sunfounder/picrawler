.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti Speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a promozioni e concorsi durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _remote_desktop:

Accesso al Desktop Remoto per Raspberry Pi
==================================================

Per coloro che preferiscono un'interfaccia grafica utente (GUI) rispetto all'accesso tramite riga di comando, il Raspberry Pi supporta la funzionalità di desktop remoto. Questa guida ti accompagnerà nella configurazione e nell'utilizzo di VNC (Virtual Network Computing) per l'accesso remoto.

Raccomandiamo l'uso di `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ per questo scopo.

**Abilitare il Servizio VNC su Raspberry Pi**

Il servizio VNC è preinstallato nel Raspberry Pi OS ma è disabilitato per impostazione predefinita. Segui questi passaggi per abilitarlo:

#. Inserisci il seguente comando nel terminale del Raspberry Pi:

    .. raw:: html

        <run></run>

    .. code-block::

        sudo raspi-config

#. Naviga fino a **Opzioni di Interfacciamento** utilizzando il tasto freccia in basso, quindi premi **Invio**.

    .. image:: img/config_interface.png
        :align: center

#. Seleziona **VNC** dalle opzioni.

    .. image:: img/vnc.png
        :align: center

#. Usa i tasti freccia per scegliere **<Sì>** -> **<OK>** -> **<Fine** per completare l'attivazione del servizio VNC.

    .. image:: img/vnc_yes.png
        :align: center

**Accesso tramite VNC Viewer**

#. Scarica e installa `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ sul tuo computer personale.

#. Una volta installato, avvia VNC Viewer. Inserisci il nome host o l'indirizzo IP del tuo Raspberry Pi e premi Invio.

    .. image:: img/vnc_viewer1.png
        :align: center

#. Quando richiesto, inserisci il nome utente e la password del tuo Raspberry Pi, quindi clicca su **OK**.

    .. image:: img/vnc_viewer2.png
        :align: center

#. Dopo alcuni secondi, verrà visualizzato il desktop del sistema operativo Raspberry Pi. Ora puoi aprire il Terminale per iniziare a inserire comandi.

    .. image:: img/bookwarm.png
        :align: center
