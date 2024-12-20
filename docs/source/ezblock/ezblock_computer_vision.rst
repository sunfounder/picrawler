.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a omaggi e promozioni festive.

    👉 Sei pronto per esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _ezb_vision:

Visione Artificiale
=============================

Questo progetto segna ufficialmente l'ingresso nel campo della visione artificiale!

.. note:: 

    Puoi leggere :ref:`ezblock:video_latest` per portare a termine questo progetto con successo.

**Programma**

.. note::

    * Puoi scrivere il programma seguendo l'immagine sottostante, facendo riferimento al tutorial: :ref:`ezblock:create_project_latest`.
    * Oppure trova il codice con lo stesso nome nella pagina **Esempi** di EzBlock Studio e clicca direttamente su **Esegui** o **Modifica**.

.. image:: img/sp210928_165255.png
    :width: 800

Passa all'interfaccia di controllo remoto e vedrai i seguenti widget.

.. image:: img/sp210928_165642.png

Dopo l'avvio del programma, puoi spostare il cursore per attivare/disattivare il rilevamento facciale; clicca sul D-Pad per selezionare il colore da rilevare; clicca sul pulsante per stampare il risultato del rilevamento.

**Come funziona?**

.. image:: img/sp210928_170920.png

Questo blocco viene utilizzato per abilitare il modulo della telecamera.

.. image:: img/sp210928_171021.png
    :width: 400

Questi due blocchi vengono utilizzati per abilitare la funzione di rilevamento facciale o rilevamento del colore.

.. image:: img/sp210928_171125.png
    :width: 400

Questi due blocchi vengono utilizzati per emettere informazioni. Il risultato del rilevamento ha cinque valori in uscita, ovvero il valore delle coordinate x, il valore delle coordinate y, la larghezza, l'altezza e il numero.
