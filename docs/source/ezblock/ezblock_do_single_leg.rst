.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie gemeinsam mit anderen Enthusiasten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und bewältigen Sie technische Herausforderungen mit der Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Profitieren Sie von exklusiven Angeboten für unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Verlosungen und saisonalen Aktionen teil.

    👉 Bereit, mit uns zu entdecken und zu gestalten? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _ezb_posture:

Haltung anpassen  
==========================

In diesem Beispiel verwenden wir die Fernsteuerungsfunktion, um PiCrawler Fuß für Fuß zu steuern und die gewünschte Haltung einzunehmen.  

Sie können die Schaltfläche antippen, um die aktuellen Koordinatenwerte auszugeben. Diese Koordinatenwerte sind nützlich, wenn Sie einzigartige Bewegungen für PiCrawler erstellen möchten.  

.. image:: ../python/img/1cood.A.png  

**Programm**  

.. note::

    * Sie können das Programm gemäß der folgenden Abbildung schreiben. Bitte folgen Sie dem Tutorial: :ref:`ezblock:create_project_latest`.  
    * Oder suchen Sie den gleichnamigen Code auf der **Beispiele**-Seite von EzBlock Studio und klicken Sie direkt auf **Ausführen** oder **Bearbeiten**.  

.. image:: img/do_single_leg.png  
    :width: 800  

Wechseln Sie zur Schnittstelle für die Fernsteuerung, und Sie werden die folgenden Widgets sehen.  

.. image:: img/do_single_leg_B-1.png  
    :width: 600  

**Wie funktioniert es?**  

In diesem Projekt sollten Sie besonders auf die folgenden drei Blöcke achten:  

.. image:: img/sp210928_115847.png  

Ändern Sie den Koordinatenwert eines bestimmten Beins individuell.  

.. image:: img/sp210928_115908.png  

Gibt den Koordinatenwert des entsprechenden Beins zurück.  

.. image:: img/sp210928_115958.png  

Sie können das Programm mit Funktionen vereinfachen, insbesondere wenn Sie dieselbe Operation mehrfach ausführen. Indem Sie diese Operationen in eine neu deklarierte Funktion einfügen, wird die Nutzung erheblich erleichtert.  

.. image:: img/sp210928_135733.png  
    :width: 500  