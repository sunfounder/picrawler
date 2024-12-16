.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie gemeinsam mit anderen Enthusiasten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und bewältigen Sie technische Herausforderungen mit der Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Profitieren Sie von exklusiven Angeboten für unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Verlosungen und saisonalen Aktionen teil.

    👉 Bereit, mit uns zu entdecken und zu gestalten? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _ezb_vision:

Computer Vision  
=============================  

In diesem Projekt betreten wir offiziell das Feld der Computer Vision!  

.. note:: 

    Lesen Sie :ref:`ezblock:video_latest`, um dieses Projekt reibungslos umzusetzen.  

**Programm**  

.. note::

    * Sie können das Programm gemäß der folgenden Abbildung schreiben. Bitte folgen Sie dem Tutorial: :ref:`ezblock:create_project_latest`.  
    * Oder suchen Sie den gleichnamigen Code auf der **Beispiele**-Seite von EzBlock Studio und klicken Sie direkt auf **Ausführen** oder **Bearbeiten**.  

.. image:: img/sp210928_165255.png  
    :width: 800  

Wechseln Sie zur Schnittstelle für die Fernsteuerung, und Sie werden die folgenden Widgets sehen.  

.. image:: img/sp210928_165642.png  

Nach dem Start des Programms können Sie den Schieberegler verwenden, um die Gesichtserkennung ein- oder auszuschalten. Mit dem Steuerkreuz (D-Pad) können Sie die Farbe für die Erkennung auswählen, und mit einem Klick auf die Schaltfläche wird das Erkennungsergebnis angezeigt.  

**Wie funktioniert es?**  

.. image:: img/sp210928_170920.png  

Dieser Block wird verwendet, um das Kameramodul zu aktivieren.  

.. image:: img/sp210928_171021.png  
    :width: 400  

Diese beiden Blöcke werden verwendet, um die Gesichtserkennungs- bzw. Farberkennungsfunktion zu aktivieren.  

.. image:: img/sp210928_171125.png  
    :width: 400  

Diese beiden Blöcke werden verwendet, um Informationen auszugeben. Das Erkennungsergebnis liefert fünf Ausgabewerte: den x-Koordinatenwert, den y-Koordinatenwert, die Breite, die Höhe und die Anzahl.  
