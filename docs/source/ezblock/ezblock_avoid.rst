.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie gemeinsam mit anderen Enthusiasten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und bewältigen Sie technische Herausforderungen mit der Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Profitieren Sie von exklusiven Angeboten für unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Verlosungen und saisonalen Aktionen teil.

    👉 Bereit, mit uns zu entdecken und zu gestalten? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _ezb_avoid:

Hindernisvermeidung  
=============================

In diesem Projekt wird PiCrawler ein Ultraschallmodul verwenden, um Hindernisse vor ihm zu erkennen.  
Sobald PiCrawler ein Hindernis erkennt, sendet er ein Signal und sucht eine andere Richtung, um weiterzugehen.  

.. .. image:: ../python/img/avoid1.png  

**Programm**  

.. note::

    * Sie können das Programm gemäß der folgenden Abbildung schreiben. Bitte folgen Sie dem Tutorial: :ref:`ezblock:create_project_latest`.  
    * Oder suchen Sie den gleichnamigen Code auf der **Beispiele**-Seite von EzBlock Studio und klicken Sie direkt auf **Ausführen** oder **Bearbeiten**.  

.. image:: img/avoid.png  

**Wie funktioniert es?**  

Im Abschnitt **Module** finden Sie die folgenden Blöcke, um die Entfernungsmessung zu realisieren:  

.. image:: img/sp210928_103046.png  
    :width: 600  

Beachten Sie, dass die beiden Pins des Blocks mit der tatsächlichen Verkabelung übereinstimmen müssen, also trig-D2 und echo-D3.  

Hier ist das Hauptprogramm:  

* Lesen Sie die ``distance`` (Entfernung), die vom Ultraschallmodul erfasst wird, und filtern Sie Werte unter 0 heraus. (Wenn das Ultraschallmodul zu weit vom Hindernis entfernt ist oder die Daten nicht korrekt lesen kann, erscheint ``distance<0``.)  
* Wenn die ``distance`` kleiner als ``alert_distance`` ist (der zuvor festgelegte Schwellenwert, hier 10), wird der Soundeffekt ``sign.wav`` abgespielt, und PiCrawler führt eine Aktion ``links drehen`` aus.  
* Wenn die ``distance`` größer als ``alert_distance`` ist, bewegt sich PiCrawler ``vorwärts``.  
