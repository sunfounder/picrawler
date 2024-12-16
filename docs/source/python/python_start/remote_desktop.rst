.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie mit anderen Enthusiasten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.  

    **Warum beitreten?**  

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.  
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.  
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.  
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.  
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Gewinnspielen und saisonalen Aktionen teil.  

    👉 Bereit, mit uns zu entdecken und zu gestalten? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!  

.. _remote_desktop:  

Remote-Desktop-Zugriff für Raspberry Pi  
==================================================

Für alle, die eine grafische Benutzeroberfläche (GUI) der Arbeit mit der Befehlszeile vorziehen, unterstützt der Raspberry Pi die Remote-Desktop-Funktionalität. Diese Anleitung zeigt Ihnen, wie Sie VNC (Virtual Network Computing) einrichten und verwenden können.  

Wir empfehlen die Verwendung von `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ zu diesem Zweck.  

**VNC-Dienst auf dem Raspberry Pi aktivieren**  

Der VNC-Dienst ist im Raspberry Pi OS vorinstalliert, jedoch standardmäßig deaktiviert. Befolgen Sie diese Schritte, um ihn zu aktivieren:  

#. Geben Sie den folgenden Befehl in das Terminal des Raspberry Pi ein:  

    .. raw:: html  

        <run></run>  

    .. code-block::  

        sudo raspi-config  

#. Navigieren Sie mit der Pfeiltaste nach unten zu **Interfacing Options** und drücken Sie **Enter**.  

    .. image:: img/config_interface.png  
        :align: center  

#. Wählen Sie **VNC** aus den Optionen.  

    .. image:: img/vnc.png  
        :align: center  

#. Wählen Sie mit den Pfeiltasten **<Yes>** -> **<OK>** -> **<Finish>**, um die Aktivierung des VNC-Dienstes abzuschließen.  

    .. image:: img/vnc_yes.png  
        :align: center  

**Anmelden über den VNC Viewer**  

#. Laden Sie `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ herunter und installieren Sie ihn auf Ihrem Computer.  

#. Starten Sie nach der Installation den VNC Viewer. Geben Sie den Hostnamen oder die IP-Adresse Ihres Raspberry Pi ein und drücken Sie Enter.  

    .. image:: img/vnc_viewer1.png  
        :align: center  

#. Geben Sie bei Aufforderung den Benutzernamen und das Passwort Ihres Raspberry Pi ein und klicken Sie auf **OK**.  

    .. image:: img/vnc_viewer2.png  
        :align: center  

#. Nach einigen Sekunden wird der Desktop des Raspberry Pi OS angezeigt. Nun können Sie das Terminal öffnen und mit der Eingabe von Befehlen beginnen.  

    .. image:: img/bookwarm.png  
        :align: center  
