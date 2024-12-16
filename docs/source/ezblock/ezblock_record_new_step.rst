.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie gemeinsam mit anderen Enthusiasten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.  

    **Warum beitreten?**  

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und bewältigen Sie technische Herausforderungen mit der Hilfe unserer Community und unseres Teams.  
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu erweitern.  
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.  
    - **Spezielle Rabatte**: Profitieren Sie von exklusiven Angeboten für unsere neuesten Produkte.  
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Verlosungen und saisonalen Aktionen teil.  

    👉 Bereit, mit uns zu entdecken und zu gestalten? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!  

.. _ezb_record:  

Neue Schritte aufzeichnen  
==============================

Mit der Fernsteuerungsfunktion können wir PiCrawler nacheinander verschiedene Posen einnehmen lassen und diese Posen aufzeichnen. Später können diese wieder abgespielt werden.  

**Programm**  

.. note::

    * Sie können das Programm gemäß der folgenden Abbildung schreiben. Bitte folgen Sie dem Tutorial: :ref:`ezblock:create_project_latest`.  
    * Oder suchen Sie den gleichnamigen Code auf der **Beispiele**-Seite von EzBlock Studio und klicken Sie direkt auf **Ausführen** oder **Bearbeiten**.  

.. image:: img/record.png  
    :width: 800  

Wechseln Sie zur Schnittstelle für die Fernsteuerung, und Sie werden die folgenden Widgets sehen.  

.. image:: img/sp210928_164343-1.png  
    :width: 600  

**Wie funktioniert es?**  


Dieses Projekt basiert auf :ref:`ezb_posture`. Es wurde um Aufnahme- und Wiedergabefunktionen erweitert.  

Die Aufzeichnungsfunktion wird durch den folgenden Code realisiert.  

.. image:: img/sp210928_164449.png  

Die Wiedergabefunktion wird durch den folgenden Code realisiert.  

.. image:: img/sp210928_164500.png  