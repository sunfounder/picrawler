.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a omaggi e promozioni festive.

    👉 Sei pronto per esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _ezb_pose:

Postura
===============

PiCrawler può assumere una postura specifica scrivendo un array di coordinate. Qui assume una postura con la zampa posteriore destra sollevata.

.. image:: ../python/img/4cood.A.png

**Programma**

.. note::

    * Puoi scrivere il programma seguendo l'immagine sottostante, facendo riferimento al tutorial: :ref:`ezblock:create_project_latest`.
    * Oppure trova il codice con lo stesso nome nella pagina **Esempi** di EzBlock Studio e clicca direttamente su **Esegui** o **Modifica**.

.. image:: img/dostep.png


**Come funziona?**

Nel codice, la parte che devi osservare con attenzione è il comando **do step**.

Ha due usi principali:

Primo: Può utilizzare direttamente **stand** o **sit**.

Secondo: Può anche scrivere un array di 4 valori di coordinate.

Ogni zampa ha un sistema di coordinate indipendente, come mostrato di seguito:

.. image:: ../python/img/4cood.png

Devi misurare le coordinate di ciascun dito del piede individualmente. Come mostrato di seguito:

.. image:: ../python/img/1cood.png
