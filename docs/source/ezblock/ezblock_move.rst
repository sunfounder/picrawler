.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a omaggi e promozioni festive.

    👉 Sei pronto per esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _ezb_move:

Movimento
=================

Questo è il primo progetto di PiCrawler. Svolge la sua funzione più basilare: il movimento.

.. .. image:: ../python/img/move.png

**Programma**

.. note::

    * Puoi scrivere il programma seguendo l'immagine sottostante, facendo riferimento al tutorial: :ref:`ezblock:create_project_latest`.
    * Oppure trova il codice con lo stesso nome nella pagina **Esempi** di EzBlock Studio e clicca direttamente su **Esegui** o **Modifica**.

.. image:: img/move.png

Clicca sul pulsante **Carica & Esegui** in basso a destra dello schermo, e PiCrawler eseguirà in sequenza le azioni di "avanzare" e "indietreggiare".

**Come funziona?**

Per prima cosa, devi comprendere la struttura del programma di Ezblock, come segue:

.. image:: img/sp210927_162828.png
    :width: 200

Tutti i progetti di Ezblock contengono questi due blocchi. Il blocco **Start** viene eseguito all'inizio del programma e viene eseguito una sola volta, spesso usato per impostare variabili; il blocco **Forever** viene eseguito dopo **Start** e viene ripetuto continuamente, spesso usato per implementare le funzioni principali.
Se elimini questi due blocchi, puoi trascinarli nuovamente dalla categoria **Base** sulla sinistra.

Successivamente, devi comprendere i seguenti blocchi.

.. image:: img/sp210927_165133.png

**do action** consente a PiCrawler di eseguire azioni di base. Puoi modificare le opzioni nel primo slot. Ad esempio, selezionare "Gira a sinistra", "Indietreggia" e così via.
Il secondo slot consente di impostare il numero di esecuzioni dell'azione; possono essere inseriti solo numeri interi maggiori di 0.
Il terzo slot consente di impostare la velocità dell'azione; possono essere inseriti solo numeri interi compresi tra 0 e 100.

.. image:: img/sp210927_170717.png
    :width: 500

**do step** è simile a **do action**, ma non si tratta di un'azione, bensì di una postura statica. Come "in piedi", "seduto".



Entrambi i blocchi possono essere trascinati dalla categoria **PiCrawler** sulla sinistra.
