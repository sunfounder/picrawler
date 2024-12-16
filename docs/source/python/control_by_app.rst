.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie mit anderen Enthusiasten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.  

    **Warum beitreten?**  

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.  
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.  
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.  
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.  
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Gewinnspielen und saisonalen Aktionen teil.  

    👉 Bereit, mit uns zu entdecken und zu gestalten? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!  

.. _control_by_app:  

Steuerung per APP  
=======================

Der SunFounder-Controller wird verwendet, um Roboter auf Basis von Raspberry Pi/Pico zu steuern.  

Die APP integriert Buttons, Schalter, Joystick, D-Pad, Schieberegler und Gas-Schieberegler-Widgets sowie Eingabewidgets wie Digitalanzeige, Ultraschallradar, Graustufenerkennung und Tachometer.  

Es gibt 17 Bereiche (A–Q), in denen Sie verschiedene Widgets platzieren können, um Ihren eigenen Controller zu erstellen.  

Zusätzlich bietet diese Anwendung einen Live-Video-Streaming-Service.  

Erstellen wir einen PiCrawler-Controller mit dieser App.  

**Wie geht das?**  

#. Installieren Sie das Modul ``sunfounder-controller``.  

    Die Module ``robot-hat``, ``vilib`` und ``picrawler`` müssen zuerst installiert werden. Details dazu finden Sie unter: :ref:`install_all_modules`.  

    .. raw:: html  

        <run></run>  

    .. code-block::  

        cd ~  
        git clone https://github.com/sunfounder/sunfounder-controller.git  
        cd ~/sunfounder-controller  
        sudo python3 setup.py install  

#. Führen Sie den Code aus.  

    .. raw:: html  

        <run></run>  

    .. code-block::  

        cd ~/sunfounder-controller/examples  
        sudo python3 picrawler_control.py  

#. Installieren Sie die `SunFounder Controller <https://docs.sunfounder.com/projects/sf-controller/en/latest/>`_ App aus dem **APP Store (iOS)** oder **Google Play (Android)**.  


#. Öffnen Sie die App und erstellen Sie einen neuen Controller.  

    Erstellen Sie einen neuen Controller, indem Sie in der SunFounder Controller App auf das + Zeichen klicken.  

    .. image:: img/app1.PNG  

    Es gibt vorkonfigurierte Controller für einige Produkte im Abschnitt „Preset“. Wählen Sie hier PiCrawler aus.  

    .. image:: img/app_control1.jpg  

    Geben Sie dem Controller einen Namen und wählen Sie den Controller-Typ aus.  

    .. image:: img/app_control2.jpg  

    Nachdem Sie den vorkonfigurierten Controller betreten haben, sehen Sie bereits einige Widgets. Wenn Sie keine weiteren Änderungen vornehmen möchten, klicken Sie auf die |app_save| Taste.  

    .. image:: img/app_control3.jpg  

#. Stellen Sie eine Verbindung zum PiCrawler her.  

    Wenn Sie auf die **Verbinden**-Schaltfläche klicken, sucht die App automatisch nach Robotern in der Nähe. Der Name wird in ``picrawler_control.py`` definiert und muss ständig ausgeführt werden.  

    .. image:: img/app_control6.jpg  

    Sobald Sie auf den Produktnamen klicken, erscheint die Nachricht „Erfolgreich verbunden“, und der Produktname wird oben rechts angezeigt.  

    .. image:: img/app_control7.jpg  

    .. note::

        * Stellen Sie sicher, dass Ihr mobiles Gerät mit demselben LAN wie PiCrawler verbunden ist.  
        * Falls keine automatische Suche erfolgt, können Sie auch die IP-Adresse manuell eingeben, um die Verbindung herzustellen.  

        .. image:: img/app11.PNG  

#. Starten Sie den Controller.  

    Klicken Sie auf die **Starten**-Schaltfläche, um den Controller zu aktivieren. Sie sehen die Aufnahmen des Autos, und jetzt können Sie den PiCrawler mit den Widgets steuern.  

    .. image:: img/app_control8.jpg  

    Hier sind die Funktionen der Widgets:  

    * **A**: Stellt die Leistung des PiCrawler ein.  
    * **B**: Zeigt die Bewegungsgeschwindigkeit des Roboters an.  
    * **C**: Hat dieselbe Funktion wie Widget B.  
    * **D**: Zeigt erkannte Hindernisse als rote Punkte an.  
    * **G**: Sprachsteuerung, drücken und halten Sie dieses Widget, um zu sprechen. Beim Loslassen wird die erkannte Stimme angezeigt. Es gibt vier vordefinierte Befehle: ``vorwärts``, ``rückwärts``, ``links`` und ``rechts`` zur Steuerung des Autos.  
    * **K**: Steuert die Vorwärts-, Rückwärts-, Links- und Rechtsbewegungen des Autos.  
    * **Q**: Bewegt den Kopf (Kamera) nach oben, unten, links und rechts.  
    * **N**: Aktiviert die Farberkennungsfunktion.  
    * **O**: Aktiviert die Gesichtserkennungsfunktion.  
    * **P**: Aktiviert die Objekterkennung, die fast 90 Objekte erkennen kann. Eine Liste der Modelle finden Sie hier: https://github.com/sunfounder/vilib/blob/master/workspace/coco_labels.txt.  
