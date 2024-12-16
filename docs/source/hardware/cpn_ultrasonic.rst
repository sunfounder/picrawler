.. note::  

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie gemeinsam mit anderen Enthusiasten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.  

    **Warum beitreten?**  

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und bewältigen Sie technische Herausforderungen mit der Hilfe unserer Community und unseres Teams.  
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu erweitern.  
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.  
    - **Spezielle Rabatte**: Profitieren Sie von exklusiven Angeboten für unsere neuesten Produkte.  
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Verlosungen und saisonalen Aktionen teil.  

    👉 Bereit, mit uns zu entdecken und zu gestalten? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!  

Ultraschallmodul  
================================

.. image:: img/ultrasonic_pic.png  
    :width: 400  
    :align: center  

* **TRIG**: Trigger-Pulse-Eingang  
* **ECHO**: Echo-Pulse-Ausgang  
* **GND**: Masse  
* **VCC**: 5V Stromversorgung  

Dies ist der HC-SR04 Ultraschall-Entfernungssensor, der eine berührungslose Messung von 2 cm bis 400 cm mit einer Genauigkeit von bis zu 3 mm ermöglicht. Das Modul enthält einen Ultraschallsender, einen Empfänger und eine Steuerschaltung.  

Es sind lediglich 4 Pins anzuschließen: VCC (Stromversorgung), Trig (Trigger), Echo (Empfang) und GND (Masse). Dadurch ist der Sensor einfach für Ihre Messprojekte zu verwenden.  

**Eigenschaften**  

* Betriebsspannung: DC 5V  
* Betriebsstrom: 16mA  
* Arbeitsfrequenz: 40Hz  
* Maximale Reichweite: 500cm  
* Minimale Reichweite: 2cm  
* Trigger-Eingangssignal: 10µS TTL-Puls  
* Echo-Ausgangssignal: TTL-Pegelsignal proportional zur Entfernung  
* Anschluss: XH2.54-4P  
* Abmessungen: 46x20,5x15 mm  

**Funktionsprinzip**  

Die grundlegenden Prinzipien sind wie folgt:  

* Auslösen mit einem mindestens 10µS langen High-Level-Signal über IO.  
* Das Modul sendet einen 8-Zyklen-Ultraschallimpuls bei 40 kHz und erkennt, ob ein Rücksignal empfangen wird.  
* Echo gibt ein High-Level-Signal aus, wenn ein Rücksignal empfangen wird; die Dauer des High-Levels entspricht der Zeit vom Senden bis zum Empfang.  
* Entfernung = (High-Level-Zeit x Schallgeschwindigkeit (340 m/s)) / 2  

    .. image:: img/ultrasonic_prin.jpg  
        :width: 800  

Formeln:  

* µs / 58 = Entfernung in Zentimetern  
* µs / 148 = Entfernung in Zoll  
* Entfernung = High-Level-Zeit x Geschwindigkeit (340 m/s) / 2  

**Anwendungshinweise**  

* Dieses Modul sollte nicht unter Spannung angeschlossen werden. Falls erforderlich, verbinden Sie zuerst die Masse (GND) des Moduls. Andernfalls kann die Funktion des Moduls beeinträchtigt werden.  
* Die Fläche des zu messenden Objekts sollte mindestens 0,5 Quadratmeter betragen und möglichst flach sein, da sonst die Ergebnisse beeinträchtigt werden können.  
