.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti Speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a promozioni e concorsi durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

Azzeramento del Servo per il Montaggio
=========================================

Prima di assemblare il servo, 
è necessario impostare l'angolo a zero. 
Questo perché il motore del servo ha un intervallo di movimento limitato; 
impostare l'angolo a zero gradi garantisce che il servo si trovi nella sua 
posizione iniziale e non superi il proprio intervallo di movimento quando è alimentato. 
Se il servo non viene impostato a zero gradi prima dell'assemblaggio, 
potrebbe tentare di superare il proprio intervallo di movimento una volta alimentato, 
potenzialmente danneggiando il servo o il sistema meccanico a cui è collegato. 
Pertanto, impostare l'angolo a zero è un passaggio fondamentale per garantire il 
funzionamento sicuro e regolare del motore del servo.


Per Utenti Python
------------------------

Fai riferimento a :ref:`quick_guide_python` per completare l'installazione 
del sistema operativo Raspberry Pi e regolare l'angolo dei servomotori.

Per Utenti Ezblock
-----------------------

.. note::

    Se stai utilizzando un Raspberry Pi 5, il nostro software di programmazione grafica, EzBlock, non è supportato.

Dopo aver installato il sistema EzBlock, 
il pin P11 può essere utilizzato per regolare il servo. 
Fai riferimento a :ref:`ezb_servo_adjust` per i dettagli.
