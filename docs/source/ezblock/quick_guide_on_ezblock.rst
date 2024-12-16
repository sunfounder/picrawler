.. note::
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie gemeinsam mit anderen Enthusiasten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.  

    **Warum beitreten?**  

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und bewältigen Sie technische Herausforderungen mit der Hilfe unserer Community und unseres Teams.  
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu erweitern.  
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.  
    - **Spezielle Rabatte**: Profitieren Sie von exklusiven Angeboten für unsere neuesten Produkte.  
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Verlosungen und saisonalen Aktionen teil.  

    👉 Bereit, mit uns zu entdecken und zu gestalten? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!  

.. _ezb_servo_adjust:  

Schnellanleitung für EzBlock  
==============================

.. note::

    Wenn Sie einen Raspberry Pi 5 verwenden, wird unsere grafische Programmiersoftware EzBlock nicht unterstützt.  

Der Drehwinkel des Servos reicht von -90° bis 90°, aber der Winkel, der ab Werk eingestellt ist, ist zufällig, möglicherweise 0°, möglicherweise 45°. Wenn wir es direkt in diesem Winkel montieren, führt dies zu einem chaotischen Zustand, wenn der Roboter den Code ausführt. Schlimmer noch, das Servo kann blockieren und durchbrennen.  

Deshalb müssen wir hier alle Servowinkel auf 0° einstellen und erst dann montieren, damit sich der Servowinkel in der Mitte befindet, unabhängig davon, in welche Richtung er gedreht wird.  

#. Installieren Sie zuerst :ref:`ezblock:install_ezblock_os_latest` (EzBlocks eigene Anleitungen) auf einer Micro-SD-Karte. Sobald die Installation abgeschlossen ist, setzen Sie die Karte in den Raspberry Pi ein.  

    .. note:: 
        Nach Abschluss der Installation kehren Sie bitte zu dieser Seite zurück.  

    .. image:: img/insert_sd_card.png  
        :width: 500  
        :align: center  

#. Um sicherzustellen, dass das Servo korrekt auf 0° eingestellt ist, setzen Sie zuerst den Servoarm auf die Servowelle und drehen Sie den Hebelarm vorsichtig in verschiedene Winkel. Der Servoarm dient lediglich dazu, sichtbar zu machen, dass das Servo sich dreht.  

    .. image:: img/servo_arm.png  

#. Folgen Sie den Anweisungen im Montagefaltblatt, stecken Sie das Batteriekabel ein und schalten Sie den Netzschalter auf ON. Schließen Sie anschließend ein USB-C-Kabel an, um den Akku zu aktivieren. Warten Sie 1-2 Minuten, bis ein Signalton ertönt, der anzeigt, dass der Raspberry Pi erfolgreich gestartet ist.  

    .. image:: img/Z_BTR.JPG  
        :width: 800  
        :align: center  

#. Stecken Sie anschließend das Servokabel in den P11-Port wie folgt.  

    .. image:: img/Z_P11.JPG  

#. Halten Sie die **USR**-Taste gedrückt und drücken Sie dann die **RST**-Taste, um das Servozentrierskript im System auszuführen. Wenn Sie sehen, dass sich der Servoarm in eine Position dreht (dies ist die 0°-Position, die zufällig ist und möglicherweise nicht vertikal oder parallel ausgerichtet ist), bedeutet dies, dass das Programm ausgeführt wurde.  

    .. note::  

        Dieser Schritt muss nur einmal durchgeführt werden. Danach können Sie einfach die anderen Servokabel anschließen, und diese werden automatisch zentriert.  

    .. image:: img/Z_P11_BT.png  
        :width: 400  
        :align: center  

#. Entfernen Sie jetzt den Servoarm, stellen Sie sicher, dass das Servokabel angeschlossen bleibt, und schalten Sie die Stromversorgung nicht aus. Fahren Sie dann mit der Montage gemäß den gedruckten Montageanweisungen fort.  

.. note::

    * Ziehen Sie das Servokabel erst ab, nachdem das Servo mit der Servoschraube befestigt wurde. Danach können Sie es abziehen.  
    * Drehen Sie das Servo nicht, während es eingeschaltet ist, um Schäden zu vermeiden. Wenn die Servowelle in einem falschen Winkel eingesetzt wurde, ziehen Sie das Servo heraus und setzen Sie es erneut ein.  
    * Bevor Sie jedes Servo montieren, müssen Sie das Servokabel in P11 stecken und die Stromversorgung einschalten, um den Winkel auf 0° einzustellen.  
    * Diese Zentrierfunktion wird deaktiviert, sobald Sie später mit der EzBlock-App ein Programm auf den Roboter herunterladen.  
