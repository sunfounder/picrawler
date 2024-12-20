.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti Speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a promozioni e concorsi durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

Per Utenti Windows
=======================

Per gli utenti di Windows 10 o versioni successive, il login remoto su un Raspberry Pi può essere effettuato seguendo i passaggi seguenti:

#. Cerca ``powershell`` nella barra di ricerca di Windows. Fai clic destro su ``Windows PowerShell`` e seleziona ``Esegui come amministratore``.

    .. image:: img/powershell_ssh.png
        :align: center

#. Determina l'indirizzo IP del tuo Raspberry Pi digitando ``ping -4 <hostname>.local`` in PowerShell.

    .. code-block::

        ping -4 raspberrypi.local

    .. image:: img/sp221221_145225.png
        :width: 550
        :align: center

    L'indirizzo IP del Raspberry Pi verrà mostrato una volta che è connesso alla rete.

    * Se il terminale visualizza ``Ping request could not find host pi.local. Please check the name and try again.``, verifica che il nome host inserito sia corretto.
    * Se non riesci ancora a recuperare l'indirizzo IP, controlla le impostazioni della rete o del WiFi sul Raspberry Pi.

#. Una volta confermato l'indirizzo IP, accedi al tuo Raspberry Pi utilizzando ``ssh <username>@<hostname>.local`` o ``ssh <username>@<IP address>``.

    .. code-block::

        ssh pi@raspberrypi.local

    .. warning::

        Se appare un errore che indica ``The term 'ssh' is not recognized as the name of a cmdlet...``, il tuo sistema potrebbe non avere gli strumenti SSH preinstallati. In tal caso, è necessario installare manualmente OpenSSH seguendo :ref:`openssh_powershell`, o utilizzare uno strumento di terze parti, come PuTTY.

#. Durante il primo accesso, apparirà un messaggio di sicurezza. Inserisci ``yes`` per procedere.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Inserisci la password che hai impostato in precedenza. Nota che i caratteri della password non verranno visualizzati sullo schermo, una caratteristica standard di sicurezza.

    .. note::
        L'assenza di caratteri visibili durante la digitazione della password è normale. Assicurati di inserire la password corretta.

#. Una volta connesso, il tuo Raspberry Pi è pronto per operazioni remote.

    .. image:: img/sp221221_140628.png
        :width: 550
        :align: center
