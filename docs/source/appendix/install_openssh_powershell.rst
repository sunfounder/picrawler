.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie gemeinsam mit anderen Enthusiasten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und bewältigen Sie technische Herausforderungen mit der Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Profitieren Sie von exklusiven Angeboten für unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Verlosungen und saisonalen Aktionen teil.

    👉 Bereit, mit uns zu entdecken und zu gestalten? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _openssh_powershell:

Installation von OpenSSH über PowerShell  
===========================================

Wenn Sie versuchen, eine Verbindung zu Ihrem Raspberry Pi mit dem Befehl ``ssh <Benutzername>@<Hostname>.local`` (oder ``ssh <Benutzername>@<IP-Adresse>``) herzustellen, aber die folgende Fehlermeldung erscheint:  

    .. code-block::  

        ssh: Der Begriff 'ssh' ist nicht als Name eines Cmdlets, einer Funktion, einer Skriptdatei oder eines ausführbaren Programms erkannt. Überprüfen Sie  
        die Schreibweise des Namens, oder wenn ein Pfad enthalten ist, stellen Sie sicher, dass der Pfad korrekt ist, und versuchen Sie es erneut.  


Dies bedeutet, dass Ihr Betriebssystem zu alt ist und `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ nicht vorinstalliert ist. Sie müssen es manuell installieren, indem Sie der folgenden Anleitung folgen.  

#. Geben Sie ``powershell`` in das Suchfeld auf Ihrem Windows-Desktop ein, klicken Sie mit der rechten Maustaste auf ``Windows PowerShell`` und wählen Sie im angezeigten Menü ``Als Administrator ausführen`` aus.  

    .. image:: img/powershell_ssh.png  
        :align: center  

#. Verwenden Sie den folgenden Befehl, um ``OpenSSH.Client`` zu installieren.  

    .. code-block::  

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0  

#. Nach der Installation wird die folgende Ausgabe angezeigt.  

    .. code-block::  

        Path          :  
        Online        : True  
        RestartNeeded : False  

#. Überprüfen Sie die Installation mit dem folgenden Befehl.  

    .. code-block::  

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'  

#. Es wird nun angezeigt, dass ``OpenSSH.Client`` erfolgreich installiert wurde.  

    .. code-block::  

        Name  : OpenSSH.Client~~~~0.0.1.0  
        State : Installed  

        Name  : OpenSSH.Server~~~~0.0.1.0  
        State : NotPresent  

    .. warning:: 
        Wenn die obige Anzeige nicht erscheint, bedeutet dies, dass Ihr Windows-System weiterhin zu alt ist. In diesem Fall wird empfohlen, ein Drittanbieter-SSH-Tool wie PuTTY zu installieren.  

#. Starten Sie PowerShell neu und führen Sie es erneut als Administrator aus. Ab diesem Punkt können Sie sich mit dem Befehl ``ssh`` bei Ihrem Raspberry Pi anmelden. Sie werden aufgefordert, das zuvor eingerichtete Passwort einzugeben.  

    .. image:: img/powershell_login.png  