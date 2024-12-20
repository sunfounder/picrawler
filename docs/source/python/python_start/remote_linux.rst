.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti Speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a promozioni e concorsi durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

Per Utenti Linux/Unix
==========================

#. Individua e apri il **Terminale** sul tuo sistema Linux/Unix.

#. Assicurati che il tuo Raspberry Pi sia connesso alla stessa rete. Verifica digitando ``ping <hostname>.local``. Per esempio:

    .. code-block::

        ping raspberrypi.local

    Dovresti vedere l'indirizzo IP del Raspberry Pi se è connesso alla rete.

    * Se il terminale mostra un messaggio come ``Ping request could not find host pi.local. Please check the name and try again.``, ricontrolla il nome host che hai inserito.
    * Se non riesci a recuperare l'indirizzo IP, controlla le impostazioni della rete o del WiFi sul Raspberry Pi.

#. Avvia una connessione SSH digitando ``ssh <username>@<hostname>.local`` o ``ssh <username>@<IP address>``. Per esempio:

    .. code-block::

        ssh pi@raspberrypi.local

#. Al primo accesso, incontrerai un messaggio di sicurezza. Digita ``yes`` per procedere.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Inserisci la password che hai impostato in precedenza. Nota che, per motivi di sicurezza, la password non sarà visibile mentre la digiti.

    .. note::
        È normale che i caratteri della password non vengano visualizzati nel terminale. Assicurati semplicemente di inserire la password corretta.

#. Una volta effettuato con successo l'accesso, il tuo Raspberry Pi è ora connesso e sei pronto per procedere al passaggio successivo.
