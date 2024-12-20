.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a omaggi e promozioni festive.

    👉 Sei pronto per esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _ezb_record:

Registra un Nuovo Passo
==============================

Usiamo la funzione di controllo remoto per fare in modo che PiCrawler assuma diverse pose a turno e registriamo queste pose. In seguito, è possibile riprodurle.

**Programma**

.. note::

    * Puoi scrivere il programma seguendo l'immagine sottostante, facendo riferimento al tutorial: :ref:`ezblock:create_project_latest`.
    * Oppure trova il codice con lo stesso nome nella pagina **Esempi** di EzBlock Studio e clicca direttamente su **Esegui** o **Modifica**.

.. image:: img/record.png
    :width: 800

Passa all'interfaccia di Controllo Remoto e vedrai i seguenti widget.

.. image:: img/sp210928_164343-1.png
    :width: 600

**Come funziona?**


Questo progetto deriva da :ref:`ezb_posture`. Sono state aggiunte le funzioni di registrazione e riproduzione.

La funzione di registrazione è implementata tramite il seguente codice.

.. image:: img/sp210928_164449.png

La funzione di riproduzione è implementata tramite il seguente codice.

.. image:: img/sp210928_164500.png
