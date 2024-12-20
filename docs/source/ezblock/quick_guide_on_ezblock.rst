.. note:: 

    Ciao, benvenuto nella Community SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Esplora a fondo Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Accedi in anteprima agli annunci di nuovi prodotti.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a concorsi e promozioni speciali.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti subito!

.. _ezb_servo_adjust:

Guida Rapida su EzBlock
===========================

.. note::

    Se stai utilizzando un Raspberry Pi 5, il nostro software di programmazione grafica, EzBlock, non è supportato.

L'intervallo di angolazione del servo è -90~90°, ma l'angolo impostato in fabbrica è casuale, potrebbe essere 0°, 45° o altro. Se lo assembliamo con tale angolazione, ciò potrebbe causare uno stato caotico durante l'esecuzione del codice, o peggio, bloccare e bruciare il servo.

Per questo motivo, è necessario impostare tutti gli angoli dei servocomandi a 0° prima dell'installazione, in modo che l'angolo sia al centro, consentendo al servo di ruotare in entrambe le direzioni senza problemi.

#. Per prima cosa, :ref:`ezblock:install_ezblock_os_latest` (i tutorial dedicati a EzBlock) su una scheda Micro SD. Una volta completata l'installazione, inseriscila nel Raspberry Pi.

    .. note::
        Dopo aver completato l'installazione, torna a questa pagina.

    .. image:: img/insert_sd_card.png
        :width: 500
        :align: center

#. Per assicurarti che il servo sia stato correttamente impostato su 0°, inserisci prima il braccio del servo sull'asse e ruota delicatamente il braccio per vedere l'angolazione raggiunta. Questo serve per verificare chiaramente la rotazione del servo.

    .. image:: img/servo_arm.png

#. Segui le istruzioni sul foglio di montaggio, collega il cavo della batteria e sposta l'interruttore di alimentazione su ON. Successivamente, collega un cavo USB-C alimentato per attivare la batteria. Attendi 1-2 minuti: un segnale acustico indicherà che il Raspberry Pi si è avviato con successo.

    .. image:: img/Z_BTR.JPG
        :width: 800
        :align: center

#. Collega il cavo del servo alla porta P11 come mostrato.

    .. image:: img/Z_P11.JPG

#. Tieni premuto il tasto **USR**, quindi premi il tasto **RST** per eseguire lo script di azzeramento del servo integrato nel sistema. Quando vedi il braccio del servo ruotare in una posizione (che corrisponde a 0°, un punto casuale che potrebbe non essere verticale o parallelo), significa che il programma è stato eseguito.

    .. note::

        Questo passaggio deve essere eseguito solo una volta; successivamente, basta inserire gli altri cavi dei servocomandi e saranno automaticamente azzerati.

    .. image:: img/Z_P11_BT.png
        :width: 400
        :align: center
    
#. Ora rimuovi il braccio del servo, assicurandoti che il cavo del servo rimanga collegato, e non spegnere l'alimentazione. Procedi quindi al montaggio seguendo le istruzioni cartacee di assemblaggio.

.. note::

    * Non scollegare il cavo del servo prima di fissare il servo con la vite; puoi scollegarlo solo dopo averlo fissato.
    * Non ruotare il servo mentre è alimentato per evitare danni; se l'asse del servo è inserito con un'angolazione errata, estrai il servo e reinseriscilo.
    * Prima di assemblare ciascun servo, collega il cavo del servo a P11 e accendi l'alimentazione per impostare l'angolo a 0°.
    * Questa funzione di azzeramento verrà disattivata se successivamente scarichi un programma sul robot tramite l'app EzBlock.
