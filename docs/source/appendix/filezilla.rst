.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie gemeinsam mit anderen Enthusiasten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und bewältigen Sie technische Herausforderungen mit der Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Profitieren Sie von exklusiven Angeboten für unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Verlosungen und saisonalen Aktionen teil.

    👉 Bereit, mit uns zu entdecken und zu gestalten? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _filezilla:

Filezilla-Software  
==========================

.. image:: img/filezilla_icon.png  

Das File Transfer Protocol (FTP) ist ein standardisiertes Kommunikationsprotokoll, das für den Austausch von Dateien zwischen einem Server und einem Client in einem Computernetzwerk verwendet wird.  

Filezilla ist eine Open-Source-Software, die nicht nur FTP unterstützt, sondern auch FTP über TLS (FTPS) und SFTP. Mit Filezilla können lokale Dateien (z. B. Bilder, Audiodateien usw.) auf den Raspberry Pi hochgeladen oder Dateien vom Raspberry Pi auf den lokalen Rechner heruntergeladen werden.  

**Schritt 1**: Filezilla herunterladen.  

Laden Sie den Client von der `offiziellen Website von Filezilla <https://filezilla-project.org/>`_ herunter. Filezilla bietet eine ausgezeichnete Dokumentation, siehe: `Dokumentation - Filezilla <https://wiki.filezilla-project.org/Documentation>`_.  

**Schritt 2**: Verbindung zum Raspberry Pi herstellen.  

Nach einer schnellen Installation öffnen Sie die Software und `verbinden sich mit einem FTP-Server <https://wiki.filezilla-project.org/Using#Connecting_to_an_FTP_server>`_. Es gibt drei Möglichkeiten, eine Verbindung herzustellen. Hier nutzen wir die **Schnellverbindungsleiste**. Geben Sie den **Hostnamen/die IP-Adresse**, den **Benutzernamen**, das **Passwort** und den **Port (22)** ein und klicken Sie anschließend auf **Quick Connect** oder drücken Sie **Enter**, um sich mit dem Server zu verbinden.  

.. image:: img/filezilla_connect.png  

.. note::

    Schnellverbindung ist eine gute Methode, um Ihre Anmeldedaten zu testen. Wenn Sie einen dauerhaften Eintrag erstellen möchten, können Sie nach einer erfolgreichen Schnellverbindung **Datei** -> **Aktuelle Verbindung in den Server-Manager kopieren** auswählen, einen Namen eingeben und auf **OK** klicken. Beim nächsten Mal können Sie sich verbinden, indem Sie die zuvor gespeicherte Seite unter **Datei** -> **Server-Manager** auswählen.  

    .. image:: img/ftp_site.png  

**Schritt 3**: Dateien hoch- und herunterladen.  

Sie können lokale Dateien auf den Raspberry Pi hochladen, indem Sie sie per Drag-and-Drop verschieben, oder Dateien vom Raspberry Pi auf Ihren lokalen Rechner herunterladen.  

.. image:: img/upload_ftp.png  
