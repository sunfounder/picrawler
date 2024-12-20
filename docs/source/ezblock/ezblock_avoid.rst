.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a omaggi e promozioni festive.

    👉 Sei pronto per esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _ezb_avoid:

Evitamento Ostacoli
=============================

In questo progetto, PiCrawler utilizzerà un modulo a ultrasuoni per rilevare ostacoli davanti a sé. 
Quando PiCrawler rileva un ostacolo, invierà un segnale e cercherà un'altra direzione per procedere.

.. image:: ../python/img/avoid1.png

**Programma**

.. note::

    * Puoi scrivere il programma seguendo l'immagine sottostante, facendo riferimento al tutorial: :ref:`ezblock:create_project_latest`.
    * Oppure trova il codice con lo stesso nome nella pagina **Esempi** di EzBlock Studio e clicca direttamente su **Esegui** o **Modifica**.

.. image:: img/avoid.png


**Come funziona?**

Puoi trovare i seguenti blocchi nella categoria **Modulo** per effettuare il rilevamento della distanza:

.. image:: img/sp210928_103046.png
    :width: 600

È importante notare che i due pin del blocco devono corrispondere al cablaggio effettivo, cioè trig-D2, echo-D3.

Ecco il programma principale.

* Leggi la ``distanza`` rilevata dal modulo a ultrasuoni e filtra i valori inferiori a 0 (quando il modulo a ultrasuoni è troppo lontano dall'ostacolo o non riesce a leggere correttamente i dati, apparirà ``distanza<0``).
* Quando la ``distanza`` è inferiore a ``alert_distance`` (la soglia impostata precedentemente, che è 10), riproduci l'effetto sonoro ``sign.wav``. PiCrawler eseguirà una ``svolta a sinistra``.
* Quando la ``distanza`` è maggiore di ``alert_distance``, PiCrawler procederà ``avanti``.
