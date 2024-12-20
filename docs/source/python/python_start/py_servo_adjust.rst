.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti Speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a promozioni e concorsi durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

7. Regolazione del Servo (Importante)
=========================================

.. note::

    Se il tuo Robot HAT è versione V44 o superiore (con l'altoparlante situato nella parte superiore della scheda) e include un pulsante **Zero** integrato, puoi saltare questo passaggio e semplicemente premere il pulsante **Zero** per attivare il programma di azzeramento del servo.

    .. image:: img/robot_hat_v44.png
        :width: 500
        :align: center


L'intervallo di angolazione del servo è compreso tra -90° e 90°, ma l'angolazione impostata in fabbrica è casuale, potrebbe essere 0° o 45°. Se assembliamo il servo con un angolo casuale, il robot potrebbe comportarsi in modo caotico durante l'esecuzione del codice, o peggio, il servo potrebbe bloccarsi e danneggiarsi.

Pertanto, dobbiamo impostare tutti gli angoli del servo a 0° prima dell'assemblaggio, garantendo che l'angolo del servo sia in posizione centrale, indipendentemente dalla direzione in cui ruota.

#. Per garantire che il servo sia stato correttamente impostato su 0°, inserisci prima il braccio del servo sull'albero del servo, quindi ruota delicatamente il braccio per osservare il movimento. Questo serve solo per verificare che il servo ruoti correttamente.

    .. image:: img/servo_arm.png
        :align: center

#. Ora, esegui ``servo_zeroing.py`` nella cartella ``examples/``.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/picrawler/examples
        sudo python3 servo_zeroing.py

#. Successivamente, collega il cavo del servo alla porta P11 come mostrato. Contemporaneamente, vedrai il braccio del servo ruotare in una posizione (questa è la posizione di 0°, che potrebbe non essere necessariamente verticale o parallela).

    .. image:: img/servo_pin11.jpg

#. Rimuovi il braccio del servo, assicurandoti che il cavo rimanga collegato, e non spegnere l'alimentazione. Continua quindi l'assemblaggio seguendo le istruzioni cartacee.

.. note::

    * Non scollegare il cavo del servo prima di fissarlo con la vite del servo; puoi scollegarlo dopo averlo fissato.
    * Non ruotare il servo mentre è alimentato per evitare danni; se l'albero del servo non è inserito nell'angolazione corretta, estrai il servo e reinseriscilo.
    * Prima di assemblare ciascun servo, è necessario collegare il cavo del servo al pin PWM e accendere l'alimentazione per impostare l'angolo a 0°.
