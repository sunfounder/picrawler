.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a omaggi e promozioni festive.

    👉 Sei pronto per esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _openssh_powershell:

Installa OpenSSH tramite Powershell
=======================================

Quando utilizzi il comando ``ssh <username>@<hostname>.local`` (o ``ssh <username>@<IP address>``) per connetterti al tuo Raspberry Pi, ma compare il seguente messaggio di errore:

    .. code-block::

        ssh: Il termine 'ssh' non è riconosciuto come nome di un cmdlet, funzione, file di script o programma eseguibile. Controlla
        l'ortografia del nome, oppure se è stato incluso un percorso, verifica che il percorso sia corretto e riprova.


Ciò significa che il tuo sistema operativo è troppo vecchio e non ha `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ preinstallato. Segui il tutorial qui sotto per installarlo manualmente.

#. Digita ``powershell`` nella barra di ricerca del desktop di Windows, fai clic con il tasto destro su ``Windows PowerShell`` e seleziona ``Esegui come amministratore`` dal menu che appare.

    .. image:: img/powershell_ssh.png
        :align: center

#. Utilizza il seguente comando per installare ``OpenSSH.Client``.

    .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. Dopo l'installazione, verrà restituito il seguente output.

    .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. Verifica l'installazione utilizzando il seguente comando.

    .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. Ora viene indicato che ``OpenSSH.Client`` è stato installato con successo.

    .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

    .. warning:: 
        Se il messaggio sopra riportato non compare, significa che il tuo sistema Windows è ancora troppo vecchio. Ti consigliamo di installare un tool SSH di terze parti, come PuTTY.

#. Riavvia PowerShell e continua a eseguirlo come amministratore. A questo punto potrai accedere al tuo Raspberry Pi utilizzando il comando ``ssh``, dove ti verrà richiesto di inserire la password configurata in precedenza.

    .. image:: img/powershell_login.png