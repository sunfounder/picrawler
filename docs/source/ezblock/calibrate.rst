.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a omaggi e promozioni festive.

    👉 Sei pronto per esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

Calibrare il PiCrawler
================================

Dopo aver collegato il PiCrawler, sarà necessario effettuare una calibrazione. Questo passaggio è fondamentale a causa di possibili deviazioni durante il processo di installazione o di limitazioni intrinseche dei servomotori, che possono causare una leggera inclinazione degli angoli dei servi. Durante questa fase, potrai calibrare questi angoli.

Tuttavia, se ritieni che l'assemblaggio sia perfetto e non sia necessaria alcuna calibrazione, puoi saltare questo passaggio.

.. note::
    Se desideri ricalibrare il robot durante l'utilizzo, segui i passaggi indicati di seguito.

    Puoi aprire la pagina dei dettagli del prodotto cliccando sull'icona di connessione nell'angolo in alto a sinistra.

    .. image:: img/calibrate0.png

    Clicca sul pulsante **Impostazioni**.

    .. image:: img/calibrate1.png

    In questa pagina, puoi modificare il nome del prodotto, il tipo di prodotto, visualizzare la versione dell'app o calibrare il robot. Una volta cliccato su **Calibra**, verrai indirizzato alla pagina di calibrazione.

    .. image:: img/calibrate2.png


I passaggi per la calibrazione sono i seguenti:

#. Prendi il foglio di montaggio, giralo all'ultima pagina e posizionalo piatto sul tavolo. Poi posiziona il PiCrawler come mostrato nell'immagine, allineando la sua base con il contorno sul grafico di calibrazione.

    .. image:: img/calibration2.png
        :align: center

#. Torna a EzBlock Studio, seleziona un piede sul lato sinistro, quindi clicca sui 3 gruppi di pulsanti X, Y e Z, facendo in modo che le dita si allineino lentamente con il punto di calibrazione.

   * I pulsanti di calibrazione vengono utilizzati per le regolazioni fini; è necessario premere più volte questi pulsanti per vedere il cambiamento nella posizione del perno.
   * Si consiglia di cliccare prima sul pulsante "su" dell'asse Z per sollevare il piede, quindi regolare gli assi X e Y.

    .. image:: img/calibration4.jpg
        :align: center

#. Allinea nello stesso modo l'altro piede sul lato sinistro.

    .. image:: img/calibration3.png
        :align: center

#. Dopo aver calibrato i due piedi sinistri, sposta il foglio di calibrazione sul lato destro e calibra i due piedi destri seguendo lo stesso metodo descritto.

    .. image:: img/calibration4.png
        :align: center