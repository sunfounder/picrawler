.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie gemeinsam mit anderen Enthusiasten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und bewältigen Sie technische Herausforderungen mit der Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Profitieren Sie von exklusiven Angeboten für unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Verlosungen und saisonalen Aktionen teil.

    👉 Bereit, mit uns zu entdecken und zu gestalten? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _ezb_pose:

Pose  
===============  

PiCrawler kann eine bestimmte Haltung einnehmen, indem ein Koordinatenarray geschrieben wird. Hier wird eine Haltung mit angehobenem rechten Hinterfuß eingenommen.  

.. image:: ../python/img/4cood.A.png  

**Programm**  

.. note::  

    * Sie können das Programm gemäß der folgenden Abbildung schreiben. Bitte folgen Sie dem Tutorial: :ref:`ezblock:create_project_latest`.  
    * Oder suchen Sie den gleichnamigen Code auf der **Beispiele**-Seite von EzBlock Studio und klicken Sie direkt auf **Ausführen** oder **Bearbeiten**.  

.. image:: img/dostep.png  

**Wie funktioniert es?**  

In diesem Code ist der Abschnitt **do step** besonders wichtig.  

Er hat zwei Hauptfunktionen:  

1. Er kann direkt mit den Befehlen **stand** (stehen) oder **sit** (sitzen) verwendet werden.  
2. Er ermöglicht das Schreiben eines Arrays mit 4 Koordinatenwerten.  

Jeder Fuß hat ein eigenes Koordinatensystem. Dies wird in der folgenden Abbildung dargestellt:  

.. image:: ../python/img/4cood.png  

Sie müssen die Koordinaten jedes einzelnen Zehs individuell messen. Wie unten gezeigt:  

.. image:: ../python/img/1cood.png  
