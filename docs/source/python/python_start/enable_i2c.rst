.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie gemeinsam mit anderen Enthusiasten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.  

    **Warum beitreten?**  

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und bewältigen Sie technische Herausforderungen mit der Hilfe unserer Community und unseres Teams.  
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu erweitern.  
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.  
    - **Spezielle Rabatte**: Profitieren Sie von exklusiven Angeboten für unsere neuesten Produkte.  
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Verlosungen und saisonalen Aktionen teil.  

    👉 Bereit, mit uns zu entdecken und zu gestalten? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!  

.. _i2c_spi_config:  

6. Überprüfung der I2C-Schnittstelle  
========================================

Wir werden die I2C-Schnittstelle des Raspberry Pi verwenden. Diese Schnittstelle sollte bereits beim Installieren des ``robot-hat``-Moduls aktiviert worden sein. Um sicherzustellen, dass alles korrekt eingerichtet ist, überprüfen wir, ob sie tatsächlich aktiviert ist.  

#. Geben Sie den folgenden Befehl ein:  

    .. raw:: html  

        <run></run>  

    .. code-block::  

        sudo raspi-config  

#. Wählen Sie **Interfacing Options**, indem Sie die Pfeiltaste nach unten auf Ihrer Tastatur drücken und anschließend die **Enter**-Taste betätigen.  

    .. image:: img/image282.png  
        :align: center  

#. Wählen Sie dann **I2C** aus.  

    .. image:: img/image283.png  
        :align: center  

#. Verwenden Sie die Pfeiltasten auf der Tastatur, um **<Ja>** -> **<OK>** auszuwählen und die Einrichtung der I2C-Schnittstelle abzuschließen.  

    .. image:: img/image284.png  
        :align: center  