.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie gemeinsam mit anderen Enthusiasten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.  

    **Warum beitreten?**  

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und bewältigen Sie technische Herausforderungen mit der Hilfe unserer Community und unseres Teams.  
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu erweitern.  
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.  
    - **Spezielle Rabatte**: Profitieren Sie von exklusiven Angeboten für unsere neuesten Produkte.  
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Verlosungen und saisonalen Aktionen teil.  

    👉 Bereit, mit uns zu entdecken und zu gestalten? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!  

.. _ezb_twist:  

Twist  
==================  

Wir wissen bereits, wie PiCrawler eine bestimmte Pose einnehmen kann. Der nächste Schritt ist, diese Posen zu kombinieren, um eine kontinuierliche Bewegung zu erzeugen.  

Hier bewegen sich PiCrawlers vier Beine paarweise auf und ab und hüpfen im Takt der Musik.  

**Programm**  

.. note::

    * Sie können das Programm gemäß der folgenden Abbildung schreiben. Bitte folgen Sie dem Tutorial: :ref:`ezblock:create_project_latest`.  
    * Oder suchen Sie den gleichnamigen Code auf der **Beispiele**-Seite von EzBlock Studio und klicken Sie direkt auf **Ausführen** oder **Bearbeiten**.  

.. image:: img/twist.png  
    :width: 800  

**Wie funktioniert es?**  

Es verwendet zwei geschachtelte **for**-Schleifen, um das ``new_step``-Array kontinuierlich und regelmäßig zu verändern, während gleichzeitig der Block **do step** die Haltung ausführt, um eine fließende Bewegung zu erzeugen.  

Sie können die Koordinatenwert-Arrays, die den einzelnen Posen entsprechen, direkt aus :ref:`ezb_posture` erhalten.  

Ein Punkt, auf den Sie achten sollten, ist der Koordinatenmatrix-Block:  

.. image:: img/sp210928_154257.png  

Er ist im Wesentlichen ein zweidimensionales Array, das mit Blöcken aus der Kategorie **Liste** verarbeitet werden kann. Seine Struktur lautet ``[[vorn rechts],[vorn links],[hinten links],[hinten rechts]]``.  
Das bedeutet, dass in diesem Beispiel ``new_step#1`` dem rechten Vorderbein entspricht, ``new_step#2`` dem linken Vorderbein, ``new_step#3`` dem linken Hinterbein und ``new_step#4`` dem rechten Hinterbein.  
