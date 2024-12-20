.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a omaggi e promozioni festive.

    👉 Sei pronto per esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _ezb_twist:

Twist
==================

Abbiamo già imparato come far assumere a PiCrawler una postura specifica; il passo successivo è combinare le posture per creare un'azione continua.

In questo esempio, le quattro zampe di PiCrawler si muovono su e giù a coppie, saltando a ritmo di musica.

**Programma**

.. note::

    * Puoi scrivere il programma seguendo l'immagine sottostante, facendo riferimento al tutorial: :ref:`ezblock:create_project_latest`.
    * Oppure trova il codice con lo stesso nome nella pagina **Esempi** di EzBlock Studio e clicca direttamente su **Esegui** o **Modifica**.

.. image:: img/twist.png
    :width: 800

**Come funziona?**

Utilizza due cicli **for** annidati per fare in modo che l'array ``new_step`` produca cambiamenti continui e regolari. Allo stesso tempo, il blocco **do step** esegue le posture per formare un'azione continua.

Puoi ottenere intuitivamente l'array di coordinate corrispondente a ciascuna postura da :ref:`ezb_posture`.

Un elemento importante da tenere in considerazione è questo blocco della matrice delle coordinate:

.. image:: img/sp210928_154257.png

È essenzialmente un array bidimensionale che può essere elaborato tramite i blocchi della categoria **Lista**. La sua struttura è ``[[anteriore destro],[anteriore sinistro],[posteriore sinistro],[posteriore destro]]``.
In altre parole, in questo esempio, ``new_step#1`` corrisponde all'anteriore destro; ``new_step#2`` corrisponde all'anteriore sinistro; ``new_step#3`` corrisponde al posteriore sinistro; e ``new_step#4`` corrisponde al posteriore destro.
