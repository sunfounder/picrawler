.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie mit anderen Enthusiasten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.  

    **Warum beitreten?**  

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.  
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.  
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.  
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.  
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Gewinnspielen und saisonalen Aktionen teil.  

    👉 Bereit, mit uns zu entdecken und zu gestalten? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!  

Für Windows-Nutzer  
=======================

Für Nutzer von Windows 10 oder höher kann die Remote-Anmeldung an einem Raspberry Pi durch folgende Schritte erfolgen:  

#. Suchen Sie im Suchfeld von Windows nach ``powershell``. Klicken Sie mit der rechten Maustaste auf ``Windows PowerShell`` und wählen Sie ``Als Administrator ausführen``.  

    .. image:: img/powershell_ssh.png  
        :align: center  

#. Ermitteln Sie die IP-Adresse Ihres Raspberry Pi, indem Sie in PowerShell den Befehl ``ping -4 <hostname>.local`` eingeben.  

    .. code-block::  

        ping -4 raspberrypi.local  

    .. image:: img/sp221221_145225.png  
        :width: 550  
        :align: center  

    Die IP-Adresse des Raspberry Pi wird angezeigt, sobald es mit dem Netzwerk verbunden ist.  

    * Falls die Meldung ``Ping request could not find host pi.local. Please check the name and try again.`` erscheint, überprüfen Sie den eingegebenen Hostnamen.  
    * Sollte die IP-Adresse weiterhin nicht abrufbar sein, überprüfen Sie die Netzwerk- oder WiFi-Einstellungen auf dem Raspberry Pi.  

#. Sobald die IP-Adresse bestätigt ist, melden Sie sich mit dem Befehl ``ssh <username>@<hostname>.local`` oder ``ssh <username>@<IP-Adresse>`` bei Ihrem Raspberry Pi an.  

    .. code-block::  

        ssh pi@raspberrypi.local  

    .. warning::

        Falls ein Fehler wie ``The term 'ssh' is not recognized as the name of a cmdlet...`` erscheint, sind die SSH-Tools möglicherweise nicht vorinstalliert. In diesem Fall müssen Sie OpenSSH manuell gemäß :ref:`openssh_powershell` installieren oder ein Drittanbieter-Tool wie PuTTY verwenden.  

#. Bei der ersten Anmeldung erscheint eine Sicherheitsmeldung. Geben Sie ``yes`` ein, um fortzufahren.  

    .. code-block::  

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.  
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.  
        Are you sure you want to continue connecting (yes/no/[fingerprint])?  

#. Geben Sie das zuvor festgelegte Passwort ein. Beachten Sie, dass die Zeichen des Passworts aus Sicherheitsgründen nicht auf dem Bildschirm angezeigt werden.  

    .. note::
        Die fehlende Anzeige von Zeichen beim Eingeben des Passworts ist normal. Stellen Sie sicher, dass Sie das korrekte Passwort eingeben.  

#. Sobald die Verbindung hergestellt ist, ist Ihr Raspberry Pi für Remote-Operationen bereit.  

    .. image:: img/sp221221_140628.png  
        :width: 550  
        :align: center  
