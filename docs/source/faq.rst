.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie gemeinsam mit anderen Enthusiasten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und bewältigen Sie technische Herausforderungen mit der Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Profitieren Sie von exklusiven Angeboten für unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Verlosungen und saisonalen Aktionen teil.

    👉 Bereit, mit uns zu entdecken und zu gestalten? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

FAQ  
===========================  

F1: Nach der Installation von Ezblock OS kann sich der Servo nicht auf 0° einstellen?  
------------------------------------------------------------------------------------------

1) Überprüfen Sie, ob das Servokabel ordnungsgemäß angeschlossen ist und ob die Stromversorgung des Robot HAT eingeschaltet ist.  
2) Drücken Sie die Reset-Taste.  
3) Falls Sie bereits ein Programm in Ezblock Studio ausgeführt haben, ist das benutzerdefinierte Programm für P11 nicht mehr verfügbar. Sie können das untenstehende Bild verwenden, um in Ezblock Studio ein eigenes Programm zu schreiben, das den Servowinkel auf 0 einstellt.  

.. image:: img/faq_servo.png  

F2: Bei der Nutzung von VNC erhalte ich die Meldung, dass der Desktop momentan nicht angezeigt werden kann?  
-------------------------------------------------------------------------------------------------------------------

Geben Sie im Terminal ``sudo raspi-config`` ein, um die Bildschirmauflösung zu ändern.  

F3: Warum kehrt der Servo manchmal grundlos in die Mittelstellung zurück?  
------------------------------------------------------------------------------------

Wenn der Servo durch eine Struktur oder ein anderes Objekt blockiert ist und seine gewünschte Position nicht erreichen kann, wechselt er in den Stromausfallschutzmodus, um ein Durchbrennen durch zu hohen Strom zu verhindern.  

Nach einer Phase ohne Stromversorgung kehrt der Servo automatisch in seine ursprüngliche Position zurück, sofern kein PWM-Signal an den Servo gesendet wird.  

F4: Wo finde ich eine detaillierte Anleitung zum Robot HAT?  
-----------------------------------------------------------------

Eine umfassende Anleitung zum Robot HAT, einschließlich Informationen zu seiner Hardware und API, finden Sie hier:  

* |link_robot_hat|  

F5: Über das Batterieladegerät
-----------------------------------------------------------------

Um die Batterie aufzuladen, schließen Sie einfach ein 5V/2A Type-C-Netzteil an den Stromanschluss des Robot Hat an. Es ist nicht erforderlich, den Netzschalter des Robot Hat während des Ladevorgangs einzuschalten.
Das Gerät kann auch während des Ladevorgangs verwendet werden.

.. image:: img/robot_hat_pic.png
    :align: center
    :width: 500

Während des Ladevorgangs wird die Eingangsleistung durch den Ladechip verstärkt, um die Batterie zu laden und gleichzeitig den DC-DC-Wandler für die externe Nutzung zu versorgen. Die Ladeleistung beträgt dabei ungefähr 10W.
Wenn der externe Stromverbrauch über einen längeren Zeitraum hoch bleibt, kann die Batterie die Stromversorgung ergänzen, ähnlich wie bei der Nutzung eines Telefons während des Ladevorgangs. Beachten Sie jedoch die Kapazität der Batterie, um ein vollständiges Entladen während gleichzeitiger Nutzung und Aufladung zu vermeiden.