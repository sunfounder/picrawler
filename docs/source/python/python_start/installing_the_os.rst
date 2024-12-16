.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie mit anderen Enthusiasten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.  

    **Warum beitreten?**  

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.  
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.  
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.  
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.  
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Gewinnspielen und saisonalen Aktionen teil.  

    👉 Bereit, mit uns zu entdecken und zu gestalten? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!  

.. _install_os_sd:  

2. Betriebssystem installieren  
============================================================

**Erforderliche Komponenten**  

* Ein PC  
* Eine Micro-SD-Karte und ein Kartenlesegerät  


1. Raspberry Pi Imager installieren  
--------------------------------------

#. Besuchen Sie die Software-Download-Seite von Raspberry Pi unter `Raspberry Pi Imager <https://www.raspberrypi.org/software/>`_. Wählen Sie die Version des Imagers aus, die mit Ihrem Betriebssystem kompatibel ist. Laden Sie die Datei herunter und öffnen Sie sie, um die Installation zu starten.  

    .. image:: img/os_install_imager.png  
        :align: center  

#. Während der Installation kann je nach Betriebssystem eine Sicherheitsaufforderung erscheinen. Beispielsweise zeigt Windows möglicherweise eine Warnmeldung an. In diesem Fall wählen Sie **Weitere Informationen** und dann **Trotzdem ausführen**. Folgen Sie den Anweisungen auf dem Bildschirm, um die Installation des Raspberry Pi Imagers abzuschließen.  

    .. image:: img/os_info.png  
        :align: center  

#. Starten Sie die Raspberry Pi Imager-Anwendung, indem Sie auf das Icon klicken oder ``rpi-imager`` in Ihrem Terminal eingeben.  

    .. image:: img/os_open_imager.png  
        :align: center  

2. Betriebssystem auf die Micro-SD-Karte installieren  
-----------------------------------------------------------

#. Legen Sie Ihre SD-Karte mit einem Kartenlesegerät in Ihren Computer oder Laptop ein.  

#. Wählen Sie im Imager **Raspberry Pi Gerät** und wählen Sie das Raspberry Pi-Modell aus der Dropdown-Liste aus.  

    .. image:: img/os_choose_device.png  
        :align: center  

#. Wählen Sie **Betriebssystem** und entscheiden Sie sich für die empfohlene Betriebssystemversion.  

    .. image:: img/os_choose_os.png  
        :align: center  

#. Klicken Sie auf **Speicher wählen** und wählen Sie das passende Speichermedium für die Installation aus.  

    .. note::

        Stellen Sie sicher, dass Sie das richtige Speichermedium auswählen. Um Verwechslungen zu vermeiden, trennen Sie andere Speichermedien, falls mehrere angeschlossen sind.  

    .. image:: img/os_choose_sd.png  
        :align: center  

#. Klicken Sie auf **Weiter** und dann auf **Einstellungen bearbeiten**, um Ihre Betriebssystemeinstellungen anzupassen.  
    .. note::  

        Wenn Sie ein Monitor für Ihr Raspberry Pi verwenden, können Sie die nächsten Schritte überspringen und direkt mit 'Ja' die Installation starten. Andere Einstellungen können später am Monitor vorgenommen werden.  

    .. image:: img/os_enter_setting.png  
        :align: center  

#. Definieren Sie einen **Hostname** für Ihr Raspberry Pi.  

    .. note::

        Der Hostname ist die Netzwerkkennung Ihres Raspberry Pi. Sie können auf Ihr Pi mit ``<hostname>.local`` oder ``<hostname>.lan`` zugreifen.  

    .. image:: img/os_set_hostname.png  
        :align: center  

#. Erstellen Sie einen **Benutzernamen** und ein **Passwort** für das Administrator-Konto des Raspberry Pi.  

    .. note:: 

        Die Einrichtung eines eindeutigen Benutzernamens und Passworts ist wichtig, um Ihr Raspberry Pi abzusichern, da es kein Standardpasswort gibt.  

    .. image:: img/os_set_username.png  
        :align: center  

#. Konfigurieren Sie das drahtlose LAN, indem Sie die **SSID** und das **Passwort** Ihres Netzwerks eingeben.  

    .. note:: 

        Stellen Sie das ``Wireless LAN country`` auf den entsprechenden zwei-Buchstaben-`ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ für Ihren Standort ein.  

    .. image:: img/os_set_wifi.png  
        :align: center  

#. Um eine Remote-Verbindung zu Ihrem Raspberry Pi herzustellen, aktivieren Sie SSH im Reiter "Dienste".  

    * Für **Passwortauthentifizierung** verwenden Sie den Benutzernamen und das Passwort aus dem Reiter Allgemein.  
    * Für Public-Key-Authentifizierung wählen Sie "Nur Public-Key-Authentifizierung erlauben". Wenn Sie einen RSA-Schlüssel haben, wird dieser verwendet. Falls nicht, klicken Sie auf "SSH-keygen ausführen", um ein neues Schlüsselpaar zu generieren.  

    .. image:: img/os_enable_ssh.png  
        :align: center  

#. Im **Optionen**-Menü können Sie das Verhalten des Imagers während des Schreibvorgangs konfigurieren, einschließlich Benachrichtigung bei Abschluss, automatischem Auswerfen des Mediums und Aktivieren der Telemetrie.  

    .. image:: img/os_options.png  
        :align: center  

#. Wenn Sie die Einstellungen für die Betriebssystemanpassung eingegeben haben, klicken Sie auf **Speichern**, um die Anpassung zu speichern. Klicken Sie dann auf **Ja**, um sie beim Schreiben des Images anzuwenden.  

    .. image:: img/os_click_yes.png  
        :align: center  

#. Falls sich bereits Daten auf der SD-Karte befinden, sichern Sie diese, um Datenverlust zu vermeiden. Klicken Sie auf **Ja**, wenn keine Sicherung erforderlich ist.  

    .. image:: img/os_continue.png  
        :align: center  

#. Sobald das Popup "Schreiben erfolgreich" erscheint, wurde Ihr Image vollständig geschrieben und überprüft. Ihr Raspberry Pi ist nun bereit zum Booten von der Micro-SD-Karte!  

    .. image:: img/os_finish.png  
        :align: center  

#. Jetzt können Sie die SD-Karte mit dem Raspberry Pi OS in den Micro-SD-Kartensteckplatz auf der Unterseite des Raspberry Pi einlegen.  

    .. image:: img/insert_sd_card.png  
        :width: 500  
        :align: center  