.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a omaggi e promozioni festive.

    👉 Sei pronto per esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _filezilla:

Software Filezilla
==========================

.. image:: img/filezilla_icon.png

Il File Transfer Protocol (FTP) è un protocollo di comunicazione standard utilizzato per il trasferimento di file da un server a un client in una rete informatica.

Filezilla è un software open source che supporta non solo l'FTP, ma anche FTP su TLS (FTPS) e SFTP. Possiamo utilizzare Filezilla per caricare file locali (come immagini e audio, ecc.) sul Raspberry Pi o scaricare file dal Raspberry Pi sul computer locale.

**Passo 1**: Scarica Filezilla.

Scarica il client dal `sito ufficiale di Filezilla <https://filezilla-project.org/>`_. Filezilla dispone di un eccellente tutorial; consulta: `Documentazione - Filezilla <https://wiki.filezilla-project.org/Documentation>`_.

**Passo 2**: Connettiti al Raspberry Pi

Dopo una rapida installazione, aprilo e `connettiti a un server FTP <https://wiki.filezilla-project.org/Using#Connecting_to_an_FTP_server>`_. Esistono 3 modi per connettersi, qui utilizziamo la barra **Quick Connect**. Inserisci il **hostname/IP**, **username**, **password** e **porta (22)**, quindi clicca su **Quick Connect** o premi **Invio** per connetterti al server.

.. image:: img/filezilla_connect.png

.. note::

    Quick Connect è un ottimo modo per testare le informazioni di accesso. Se desideri creare un collegamento permanente, puoi selezionare **File** -> **Copia connessione corrente al gestore siti** dopo una connessione riuscita, inserire un nome e cliccare su **OK**. La prossima volta potrai connetterti selezionando il sito salvato precedentemente in **File** -> **Gestore siti**.
    
    .. image:: img/ftp_site.png

**Passo 3**: Carica/scarica file.

Puoi caricare file locali sul Raspberry Pi trascinandoli e rilasciandoli oppure scaricare file dal Raspberry Pi sul computer locale.

.. image:: img/upload_ftp.png
