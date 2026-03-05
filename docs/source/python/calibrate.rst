.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie gemeinsam mit anderen Enthusiasten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.  

    **Warum beitreten?**  

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und bewältigen Sie technische Herausforderungen mit der Hilfe unserer Community und unseres Teams.  
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu erweitern.  
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.  
    - **Spezielle Rabatte**: Profitieren Sie von exklusiven Angeboten für unsere neuesten Produkte.  
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Verlosungen und saisonalen Aktionen teil.  

    👉 Bereit, mit uns zu entdecken und zu gestalten? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!  

Kalibrierung des PiCrawler  
=============================

Aufgrund möglicher Abweichungen während der Installation des PiCrawler oder Einschränkungen der Servos können einige Servowinkel leicht geneigt sein. Daher können Sie diese kalibrieren.  

Selbstverständlich können Sie dieses Kapitel überspringen, wenn Sie der Meinung sind, dass die Montage perfekt ist und keine Kalibrierung erfordert.  

.. raw:: html

    <iframe width="600" height="400" src="https://www.youtube.com/embed/48FLHB_cw3k?si=Zla7BApIt0o6tq73" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Die spezifischen Schritte sind wie folgt:  

1. Nehmen Sie die Montageanleitung, schlagen Sie die letzte Seite auf und legen Sie sie flach auf den Tisch. Platzieren Sie dann den PiCrawler wie unten gezeigt, wobei sein Boden mit der Umrisslinie auf der Kalibrierungskarte ausgerichtet ist.  

    .. image:: img/calibration2.png  

#. Führen Sie die Datei ``calibration.py`` aus.  

    .. raw:: html  

        <run></run>  

    .. code-block::  

        cd ~/picrawler/examples/calibration  
        sudo python3 calibration.py  

    Nach der Ausführung des obigen Codes wird im Terminal die folgende Oberfläche angezeigt.  

    .. image:: img/calibration1.png  

#. Drücken Sie die Tasten ``2`` und ``3``, um die linken zwei Beine auszuwählen. Drücken Sie anschließend die Tasten ``w``, ``a``, ``s``, ``d``, ``r`` und ``f``, um sie zum Kalibrierungspunkt zu bewegen.  

    .. image:: img/calibration3.png  

#. Wechseln Sie nun das Kalibrierungspapier nach rechts und drücken Sie die Tasten ``1`` und ``4``, um die rechten zwei Beine auszuwählen. Drücken Sie anschließend die Tasten ``w``, ``a``, ``s``, ``d``, ``r`` und ``f``, um sie zum Kalibrierungspunkt zu bewegen.  

    .. image:: img/calibration4.png  

#. Nach Abschluss der Kalibrierung drücken Sie die Taste ``space``, um die Einstellungen zu speichern. Sie werden aufgefordert, ``Y`` einzugeben, um zu bestätigen, und dann ``ctrl+c``, um das Programm zu beenden und die Kalibrierung abzuschließen.  

    .. image:: img/calibration5.png  
