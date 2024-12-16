.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie gemeinsam mit anderen Enthusiasten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.  

    **Warum beitreten?**  

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und bewältigen Sie technische Herausforderungen mit der Hilfe unserer Community und unseres Teams.  
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu erweitern.  
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.  
    - **Spezielle Rabatte**: Profitieren Sie von exklusiven Angeboten für unsere neuesten Produkte.  
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Verlosungen und saisonalen Aktionen teil.  

    👉 Bereit, mit uns zu entdecken und zu gestalten? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!  

.. _install_all_modules:  

5. Installieren Sie alle Module (Wichtig)  
===============================================

Stellen Sie sicher, dass Sie mit dem Internet verbunden sind, und aktualisieren Sie Ihr System:  

.. raw:: html  

    <run></run>  

.. code-block::  

    sudo apt update  
    sudo apt upgrade  

.. note:: 

    Python3-bezogene Pakete müssen installiert sein, wenn Sie die Lite-Version des Betriebssystems verwenden.  

    .. raw:: html  

        <run></run>  

    .. code-block::  
    
        sudo apt install git python3-pip python3-setuptools python3-smbus  

Installieren Sie das ``robot-hat``-Modul.  

.. raw:: html  

    <run></run>  

.. code-block::  

    cd ~/  
    git clone -b v2.0 https://github.com/sunfounder/robot-hat.git  
    cd robot-hat  
    sudo python3 setup.py install  

Laden Sie anschließend den Code herunter und installieren Sie das ``vilib``-Modul.  

.. raw:: html  

    <run></run>  

.. code-block::  

    cd ~/  
    git clone -b picamera2 https://github.com/sunfounder/vilib.git  
    cd vilib  
    sudo python3 install.py  

Laden Sie anschließend den Code herunter und installieren Sie das ``picrawler``-Modul.  

.. raw:: html  

    <run></run>  

.. code-block::  

    cd ~/  
    git clone https://github.com/sunfounder/picrawler.git  
    cd picrawler  
    sudo python3 setup.py install  

Dieser Schritt wird etwas Zeit in Anspruch nehmen, bitte haben Sie Geduld.  

Abschließend müssen Sie das Skript ``i2samp.sh`` ausführen, um die für den i2s-Verstärker erforderlichen Komponenten zu installieren, andernfalls hat der PiCrawler keinen Ton.  

.. raw:: html  

    <run></run>  

.. code-block::  

    cd ~/picrawler  
    sudo bash i2samp.sh  
	
.. image:: img/i2s.png  

Geben Sie ``y`` ein und drücken Sie ``Enter``, um das Skript weiter auszuführen.  

.. image:: img/i2s2.png  

Geben Sie ``y`` ein und drücken Sie ``Enter``, um ``/dev/zero`` im Hintergrund auszuführen.  

.. image:: img/i2s3.png  

Geben Sie ``y`` ein und drücken Sie ``Enter``, um den Computer neu zu starten.  

.. note::  
    Falls nach dem Neustart kein Ton zu hören ist, müssen Sie das Skript ``i2samp.sh`` möglicherweise mehrfach ausführen.  
