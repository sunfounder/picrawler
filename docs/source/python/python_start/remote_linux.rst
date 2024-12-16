.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie mit anderen Enthusiasten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.  

    **Warum beitreten?**  

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.  
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.  
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.  
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.  
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Gewinnspielen und saisonalen Aktionen teil.  

    👉 Bereit, mit uns zu entdecken und zu gestalten? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!  

Für Linux/Unix-Nutzer  
==========================

#. Suchen und öffnen Sie das **Terminal** auf Ihrem Linux/Unix-System.  

#. Stellen Sie sicher, dass Ihr Raspberry Pi mit demselben Netzwerk verbunden ist. Überprüfen Sie dies, indem Sie den folgenden Befehl eingeben: ``ping <hostname>.local``. Zum Beispiel:  

    .. code-block::  

        ping raspberrypi.local  

    Sie sollten die IP-Adresse des Raspberry Pi sehen, wenn er mit dem Netzwerk verbunden ist.  

    * Wenn das Terminal eine Nachricht wie ``Ping request could not find host pi.local. Please check the name and try again.`` anzeigt, überprüfen Sie den eingegebenen Hostnamen.  
    * Falls Sie die IP-Adresse nicht abrufen können, überprüfen Sie die Netzwerkeinstellungen oder die WLAN-Verbindung auf dem Raspberry Pi.  

#. Starten Sie eine SSH-Verbindung, indem Sie ``ssh <username>@<hostname>.local`` oder ``ssh <username>@<IP-Adresse>`` eingeben. Zum Beispiel:  

    .. code-block::  

        ssh pi@raspberrypi.local  

#. Beim ersten Login erscheint eine Sicherheitsmeldung. Geben Sie ``yes`` ein, um fortzufahren.  

    .. code-block::  

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.  
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.  
        Are you sure you want to continue connecting (yes/no/[fingerprint])?  

#. Geben Sie das Passwort ein, das Sie zuvor festgelegt haben. Beachten Sie, dass das Passwort aus Sicherheitsgründen beim Tippen nicht sichtbar ist.  

    .. note:: 
        Es ist normal, dass die Passwortzeichen im Terminal nicht angezeigt werden. Stellen Sie einfach sicher, dass Sie das richtige Passwort eingeben.  

#. Nach erfolgreichem Login ist Ihr Raspberry Pi verbunden, und Sie können mit dem nächsten Schritt fortfahren.  
