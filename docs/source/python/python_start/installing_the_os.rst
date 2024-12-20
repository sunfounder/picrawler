.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti Speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a promozioni e concorsi durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _install_os_sd:

2. Installazione del Sistema Operativo
============================================================


**Componenti Necessari**

* Un computer personale
* Una scheda Micro SD e un lettore di schede

1. Installa Raspberry Pi Imager
----------------------------------

#. Visita la pagina di download del software Raspberry Pi su `Raspberry Pi Imager <https://www.raspberrypi.org/software/>`_. Scegli la versione di Imager compatibile con il tuo sistema operativo. Scarica e apri il file per avviare l'installazione.

    .. image:: img/os_install_imager.png
        :align: center

#. Durante l'installazione, potrebbe apparire un avviso di sicurezza a seconda del tuo sistema operativo. Ad esempio, Windows potrebbe mostrare un messaggio di avvertimento. In tal caso, seleziona **Ulteriori informazioni** e quindi **Esegui comunque**. Segui le istruzioni sullo schermo per completare l'installazione di Raspberry Pi Imager.

    .. image:: img/os_info.png
        :align: center

#. Avvia l'applicazione Raspberry Pi Imager cliccando sulla sua icona o digitando ``rpi-imager`` nel terminale.

    .. image:: img/os_open_imager.png
        :align: center

2. Installa il Sistema Operativo sulla Micro SD Card
--------------------------------------------------------

#. Inserisci la tua scheda SD nel computer o laptop utilizzando un lettore di schede.

#. All'interno di Imager, clicca su **Dispositivo Raspberry Pi** e seleziona il modello di Raspberry Pi dall'elenco a discesa.

    .. image:: img/os_choose_device.png
        :align: center

#. Seleziona **Sistema Operativo** e scegli la versione consigliata del sistema operativo.

    .. image:: img/os_choose_os.png
        :align: center

#. Clicca su **Scegli Archiviazione** e seleziona il dispositivo di archiviazione appropriato per l'installazione.

    .. note::

        Assicurati di selezionare il dispositivo di archiviazione corretto. Per evitare confusione, scollega eventuali dispositivi di archiviazione aggiuntivi se ne sono collegati più di uno.

    .. image:: img/os_choose_sd.png
        :align: center

#. Clicca su **Avanti** e poi su **Modifica Impostazioni** per personalizzare le impostazioni del sistema operativo.

    .. note::

        Se hai un monitor per il tuo Raspberry Pi, puoi saltare i passaggi successivi e cliccare su 'Sì' per iniziare l'installazione. Potrai regolare altre impostazioni successivamente sul monitor.

    .. image:: img/os_enter_setting.png
        :align: center

#. Definisci un **hostname** per il tuo Raspberry Pi.

    .. note::

        L'hostname è l'identificativo di rete del tuo Raspberry Pi. Puoi accedere al tuo Pi utilizzando ``<hostname>.local`` o ``<hostname>.lan``.

    .. image:: img/os_set_hostname.png
        :align: center

#. Crea un **Nome Utente** e una **Password** per l'account amministratore del Raspberry Pi.

    .. note::

        Creare un nome utente e una password univoci è essenziale per la sicurezza del tuo Raspberry Pi, poiché non ha una password predefinita.

    .. image:: img/os_set_username.png
        :align: center

#. Configura la LAN wireless fornendo l'**SSID** e la **Password** della tua rete.

    .. note::

        Imposta il ``Paese LAN wireless`` sul codice a due lettere `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ corrispondente alla tua posizione.

    .. image:: img/os_set_wifi.png
        :align: center

#. Per connetterti al tuo Raspberry Pi da remoto, abilita SSH nella scheda Servizi.

    * Per l'autenticazione con password, utilizza il nome utente e la password dalla scheda Generale.
    * Per l'autenticazione con chiave pubblica, scegli "Consenti solo autenticazione con chiave pubblica". Se hai una chiave RSA, verrà utilizzata. In caso contrario, clicca su "Esegui SSH-keygen" per generare una nuova coppia di chiavi.

    .. image:: img/os_enable_ssh.png
        :align: center

#. Il menu **Opzioni** ti consente di configurare il comportamento di Imager durante la scrittura, inclusa la riproduzione di un suono al termine, l'espulsione del supporto al termine e l'abilitazione della telemetria.

    .. image:: img/os_options.png
        :align: center

#. Una volta terminata la personalizzazione delle impostazioni del sistema operativo, clicca su **Salva** per salvare la personalizzazione. Poi, clicca su **Sì** per applicarle durante la scrittura dell'immagine.

    .. image:: img/os_click_yes.png
        :align: center

#. Se la scheda SD contiene dati esistenti, assicurati di eseguire un backup per evitare la perdita di dati. Procedi cliccando su **Sì** se non è necessario eseguire il backup.

    .. image:: img/os_continue.png
        :align: center

#. Quando vedi il popup "Scrittura riuscita", l'immagine è stata completamente scritta e verificata. Ora sei pronto per avviare un Raspberry Pi dalla Micro SD Card!

    .. image:: img/os_finish.png
        :align: center

#. Ora puoi inserire la scheda SD configurata con Raspberry Pi OS nello slot microSD situato sotto il Raspberry Pi.

    .. image:: img/insert_sd_card.png
        :width: 500
        :align: center