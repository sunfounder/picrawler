.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a omaggi e promozioni festive.

    👉 Sei pronto per esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _ezb_posture:

Regolazione della Postura
===========================

In questo esempio, utilizziamo la funzione remota per controllare il PiCrawler piede per piede e assumere la postura desiderata.

Puoi premere il pulsante per stampare i valori delle coordinate attuali. Questi valori di coordinate sono utili quando crei azioni uniche per PiCrawler.

.. image:: ../python/img/1cood.A.png

**Programma**

.. note::

    * Puoi scrivere il programma seguendo l'immagine sottostante, facendo riferimento al tutorial: :ref:`ezblock:create_project_latest`.
    * Oppure trova il codice con lo stesso nome nella pagina **Esempi** di EzBlock Studio e clicca direttamente su **Esegui** o **Modifica**.

.. image:: img/do_single_leg.png
    :width: 800

Passa all'interfaccia di controllo remoto e vedrai i seguenti widget.

.. image:: img/do_single_leg_B-1.png
    :width: 600

**Come funziona?**

In questo progetto, devi prestare attenzione ai seguenti tre blocchi:

.. image:: img/sp210928_115847.png

Modifica individualmente il valore delle coordinate di una gamba specifica.

.. image:: img/sp210928_115908.png

Restituisce il valore delle coordinate della gamba corrispondente.

.. image:: img/sp210928_115958.png

Potresti voler semplificare il programma con le Funzioni, specialmente quando esegui la stessa operazione più volte. Inserire queste operazioni in una funzione appena dichiarata può facilitare notevolmente il tuo utilizzo.

.. image:: img/sp210928_135733.png
    :width: 500