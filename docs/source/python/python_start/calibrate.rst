.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti Speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a promozioni e concorsi durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

Calibrazione del PiCrawler
=============================

A causa di possibili deviazioni durante l'installazione del PiCrawler o delle limitazioni intrinseche dei servomotori, alcuni angoli dei servo potrebbero risultare leggermente inclinati. È quindi possibile calibrarli.

Naturalmente, puoi saltare questo capitolo se ritieni che l'assemblaggio sia perfetto e non necessiti di calibrazione.

I passaggi specifici sono i seguenti:

1. Prendi il foglio di istruzioni per l'assemblaggio, giralo all'ultima pagina e posizionalo piatto sul tavolo. Quindi colloca il PiCrawler come mostrato di seguito, allineando la base con il contorno sulla scheda di calibrazione.

    .. image:: img/calibration2.png

#. Esegui il file ``calibration.py``.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/picrawler/examples/calibration
        sudo python3 calibration.py

    Dopo aver eseguito il codice sopra, vedrai la seguente interfaccia visualizzata nel terminale.

    .. image:: img/calibration1.png

#. Premi rispettivamente i tasti ``2`` e ``3`` per selezionare le due gambe sinistre, poi usa i tasti ``w``, ``a``, ``s``, ``d``, ``r``, e ``f`` per spostarle verso il punto di calibrazione.

    .. image:: img/calibration3.png

#. Ora, sposta la carta di calibrazione a destra e premi i tasti ``1`` e ``4`` per selezionare le due gambe destre, quindi usa i tasti ``w``, ``a``, ``s``, ``d``, ``r``, e ``f`` per spostarle verso il punto di calibrazione.

    .. image:: img/calibration4.png

#. Dopo aver completato la calibrazione, premi il tasto ``spazio`` per salvare; ti verrà chiesto di inserire ``Y`` per confermare, e successivamente di premere ``ctrl+c`` per uscire dal programma e completare la calibrazione.

    .. image:: img/calibration5.png



