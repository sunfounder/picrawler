.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a omaggi e promozioni festive.

    👉 Sei pronto per esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _ezb_remote:

Controllo Remoto
=========================

In questo progetto, impareremo come controllare a distanza il PiCrawler. 
Puoi comandare il PiCrawler a muoversi in avanti, indietro, a sinistra e a destra.

.. .. image:: img/remote_control.png

.. note:: 

    Puoi fare riferimento a :ref:`ezblock:remote_control_latest`. Realizza questo progetto con facilità.

**Programma**

.. note::

    * Puoi scrivere il programma seguendo l'immagine sottostante, facendo riferimento al tutorial: :ref:`ezblock:create_project_latest`.
    * Oppure trova il codice con lo stesso nome nella pagina **Esempi** di EzBlock Studio e clicca direttamente su **Esegui** o **Modifica**.

.. image:: img/remote.png

Passa all'interfaccia di Controllo Remoto e vedrai i seguenti widget.

.. image:: img/remote_B.png

Dopo l'avvio del programma, puoi attivare il PiCrawler tramite il D-Pad.

**Come funziona?**

Dopo aver aggiunto il widget sull'interfaccia di Controllo Remoto, apparirà una categoria denominata **Remote** nella colonna delle categorie dei blocchi dell'interfaccia di programmazione.

Qui abbiamo aggiunto il widget D-Pad, quindi il blocco **D-Pad get value** è presente in questa sezione.

.. image:: img/sp210927_180739.png

Il D-Pad può essere considerato come un pulsante "quattro in uno". Puoi scegliere quale pulsante leggere nel secondo spazio del blocco.

Quando il pulsante è premuto, il valore è "1"; quando il pulsante non è premuto, il valore è "0".

.. image:: img/sp210927_182447.png
    :width: 200

Abbiamo utilizzato un blocco **if** (puoi trovarlo nella categoria **Logic** a sinistra) per fare in modo che il PiCrawler si muova in avanti una volta quando il pulsante **UP** del D-pad è premuto.

.. image:: img/sp210927_182828.png
    :width: 600

Puoi cliccare l'icona a forma di ingranaggio in alto a sinistra del blocco per modificare la struttura del blocco **if** e realizzare ramificazioni multiple di giudizio.

.. image:: img/sp210927_183237.png
    :width: 300

Il blocco **if** è solitamente utilizzato insieme al blocco **=**. Quest'ultimo può essere modificato in **>**, **<** e altre condizioni tramite il menu a discesa. Usalo in modo flessibile.
