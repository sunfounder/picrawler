.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie mit anderen Enthusiasten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.  

    **Warum beitreten?**  

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.  
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.  
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.  
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.  
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Gewinnspielen und saisonalen Aktionen teil.  

    👉 Bereit, mit uns zu entdecken und zu gestalten? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!  

4. Einrichten Ihres Raspberry Pi  
==================================

Wenn Sie einen Bildschirm haben  
-------------------------------------

Wenn Sie einen Bildschirm haben, können Sie den Raspberry Pi ganz einfach bedienen.  

**Erforderliche Komponenten**  

* Ein beliebiger Raspberry Pi  
* 1 * Netzteil  
* 1 * Micro-SD-Karte  
* 1 * Bildschirm-Netzteil  
* 1 * HDMI-Kabel  
* 1 * Bildschirm  
* 1 * Maus  
* 1 * Tastatur  

#. Stecken Sie die mit dem Raspberry Pi OS vorbereitete SD-Karte in den Micro-SD-Kartensteckplatz auf der Unterseite Ihres Raspberry Pi.  

#. Schließen Sie die Maus und die Tastatur an.  

#. Verbinden Sie den Bildschirm mit dem HDMI-Anschluss des Raspberry Pi und stellen Sie sicher, dass der Bildschirm an eine Steckdose angeschlossen und eingeschaltet ist.  

    .. note::

        Wenn Sie einen Raspberry Pi 4 verwenden, schließen Sie den Bildschirm an HDMI0 (nächster Anschluss zur Stromversorgung) an.  

#. Nutzen Sie das Netzteil, um den Raspberry Pi mit Strom zu versorgen.  

#. Nach einigen Sekunden wird der Desktop des Raspberry Pi OS angezeigt. Sie können nun das Terminal öffnen, um Befehle einzugeben.  

    .. image:: img/bookwarm.png  
        :align: center  

Wenn Sie keinen Bildschirm haben  
----------------------------------------

Wenn Sie keinen Monitor haben, können Sie sich remote in Ihren Raspberry Pi einloggen.  

Sie können den SSH-Befehl verwenden, um die Bash-Shell des Raspberry Pi zu öffnen. Bash ist die standardmäßige Shell für Linux. Die Shell selbst ist eine Befehlseingabe, die von Benutzern unter Unix/Linux verwendet wird. Die meisten Ihrer Aufgaben können über die Shell erledigt werden.  

Wenn Sie mit der Nutzung des Befehlsfensters zum Zugriff auf Ihren Raspberry Pi nicht zufrieden sind, können Sie auch die Remote-Desktop-Funktion nutzen, um Dateien auf Ihrem Raspberry Pi über eine grafische Benutzeroberfläche (GUI) zu verwalten.  

Im Folgenden finden Sie detaillierte Anleitungen für jedes System.  

.. toctree::  

    remote_macosx  
    remote_windows  
    remote_linux  
    remote_desktop  

