.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti Speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a promozioni e concorsi durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

Per Utenti Mac OS X
==========================

Per gli utenti di Mac OS X, SSH (Secure Shell) offre un metodo sicuro e pratico per accedere e controllare un Raspberry Pi in remoto. Questo è particolarmente utile per lavorare con il Raspberry Pi quando non è collegato a un monitor. Utilizzando l'applicazione Terminal su un Mac, puoi stabilire questa connessione sicura. Il processo prevede un comando SSH che include il nome utente e il nome host del Raspberry Pi. Durante la connessione iniziale, un prompt di sicurezza chiederà conferma dell'autenticità del Raspberry Pi.

#. Per connetterti al Raspberry Pi, digita il seguente comando SSH:

    .. code-block::

        ssh pi@raspberrypi.local

    .. image:: img/mac-ping.png

#. Durante il primo accesso, comparirà un messaggio di sicurezza. Rispondi con **yes** per procedere.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Inserisci la password del Raspberry Pi. Tieni presente che la password non verrà visualizzata sullo schermo mentre la digiti, una misura di sicurezza standard.

    .. code-block::

        pi@raspberrypi.local's password: 
        Linux raspberrypi 5.15.61-v8+ #1579 SMP PREEMPT Fri Aug 26 11:16:44 BST 2022 aarch64

        The programs included with the Debian GNU/Linux system are free software;
        the exact distribution terms for each program are described in the
        individual files in /usr/share/doc/*/copyright.

        Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
        permitted by applicable law.
        Last login: Thu Sep 22 12:18:22 2022
        pi@raspberrypi:~ $ 

