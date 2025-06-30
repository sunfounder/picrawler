.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie gemeinsam mit anderen Enthusiasten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.  

    **Warum beitreten?**  

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und bewältigen Sie technische Herausforderungen mit der Hilfe unserer Community und unseres Teams.  
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu erweitern.  
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.  
    - **Spezielle Rabatte**: Profitieren Sie von exklusiven Angeboten für unsere neuesten Produkte.  
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Verlosungen und saisonalen Aktionen teil.  

    👉 Bereit, mit uns zu entdecken und zu gestalten? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!  

.. _ezb_move:  

Bewegung  
=================

Dies ist das erste Projekt von PiCrawler. Es führt die grundlegendste Funktion aus – Bewegung.  

.. .. image:: ../python/img/move.png  

**Programm**  

.. note::

    * Sie können das Programm gemäß der folgenden Abbildung schreiben. Bitte folgen Sie dem Tutorial: :ref:`ezblock:create_project_latest`.  
    * Oder suchen Sie den gleichnamigen Code auf der **Beispiele**-Seite von EzBlock Studio und klicken Sie direkt auf **Ausführen** oder **Bearbeiten**.  

.. image:: img/move.png  

Klicken Sie auf die Schaltfläche **Hochladen & Ausführen** unten rechts auf dem Bildschirm, und PiCrawler wird die Aktionen „Vorwärts“ und „Rückwärts“ nacheinander ausführen.  


**Wie funktioniert es?**  

Zuerst müssen Sie den Programmrahmen von Ezblock verstehen. Wie folgt:  

.. image:: img/sp210927_162828.png  
    :width: 200  

Alle Ezblock-Projekte enthalten diese zwei Blöcke. Der **Start**-Block wird zu Beginn des Programms ausgeführt und nur einmal ausgeführt. Er wird häufig zum Setzen von Variablen verwendet. Der **Forever**-Block läuft nach dem **Start**-Block und wird wiederholt ausgeführt. Er dient oft zur Implementierung der Hauptfunktionen.  
Falls Sie diese beiden Blöcke löschen, können Sie sie aus der Kategorie **Basic** links wiederherstellen.  

Als Nächstes müssen Sie die folgenden Blöcke verstehen.  

.. image:: img/sp210927_165133.png  

Mit **do action** kann PiCrawler grundlegende Aktionen ausführen. Sie können die Optionen in der ersten Aussparung ändern, z. B. „Links drehen“, „Zurück“ usw.  
Die zweite Aussparung kann die Anzahl der Aktionsausführungen einstellen. Es dürfen nur ganze Zahlen größer als 0 eingegeben werden.  
Die dritte Aussparung kann die Geschwindigkeit der Aktion festlegen. Es dürfen nur ganze Zahlen im Bereich von 0 bis 100 eingegeben werden.  

.. image:: img/sp210927_170717.png  
    :width: 500  

**do step** ähnelt **do action**, ist jedoch keine Aktion, sondern eine statische Haltung wie „stehen“ oder „sitzen“.  


Beide Blöcke können aus der Kategorie **PiCrawler** auf der linken Seite gezogen werden.  
