.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie mit anderen Enthusiasten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.  

    **Warum beitreten?**  

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.  
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.  
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.  
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.  
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Gewinnspielen und saisonalen Aktionen teil.  

    👉 Bereit, mit uns zu entdecken und zu gestalten? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!  

Servoanpassung (Wichtig)  
===================================

.. note::

    Wenn Ihre Robot HAT-Version V44 oder höher ist (mit einem Lautsprecher oben auf der Platine) und einen eingebauten **Zero**-Knopf enthält, können Sie diesen Schritt überspringen und einfach den **Zero**-Knopf drücken, um das Servo-Nullstellungsprogramm zu aktivieren.  

    .. image:: img/robot_hat_v44.png  
        :width: 500  
        :align: center  


Der Winkelbereich des Servos liegt zwischen -90° und 90°, jedoch ist der ab Werk eingestellte Winkel zufällig, möglicherweise 0° oder 45°. Wenn wir das Servo mit einem solchen Winkel direkt montieren, führt dies zu einem chaotischen Verhalten des Roboters beim Ausführen des Codes oder im schlimmsten Fall zum Blockieren und Durchbrennen des Servos.  

Daher müssen wir alle Servowinkel auf 0° einstellen, bevor sie installiert werden, sodass der Servowinkel mittig ist, unabhängig davon, in welche Richtung er sich dreht.  

#. Um sicherzustellen, dass das Servo korrekt auf 0° eingestellt ist, stecken Sie zunächst den Servoarm auf die Servowelle und drehen Sie den Hebelarm vorsichtig in eine andere Position. Dieser Servoarm dient lediglich dazu, klar zu sehen, dass sich das Servo dreht.  

    .. image:: img/servo_arm.png  
        :align: center  

#. Führen Sie nun ``servo_zeroing.py`` im Ordner ``examples/`` aus.  

    .. raw:: html  

        <run></run>  

    .. code-block::  

        cd ~/picrawler/examples  
        sudo python3 servo_zeroing.py  

#. Schließen Sie anschließend das Servokabel an den P11-Port an, wie unten gezeigt. Gleichzeitig sehen Sie, wie sich der Servoarm in eine Position dreht (dies ist die 0°-Position, die zufällig sein kann und möglicherweise nicht vertikal oder parallel ist).  

    .. image:: img/servo_pin11.jpg  

#. Entfernen Sie nun den Servoarm, während das Servokabel verbunden bleibt, und schalten Sie die Stromversorgung nicht aus. Fahren Sie dann mit der Montage gemäß der gedruckten Anleitung fort.  

.. note:: 

    * Ziehen Sie das Servokabel nicht ab, bevor das Servo mit der Schraube befestigt ist. Sie können es erst danach abziehen.  
    * Drehen Sie das Servo nicht, während es eingeschaltet ist, um Schäden zu vermeiden. Wenn die Servowelle nicht im richtigen Winkel eingeführt wurde, ziehen Sie das Servo heraus und setzen Sie es erneut ein.  
    * Vor der Montage jedes Servos müssen Sie das Servokabel in den PWM-Pin einstecken und die Stromversorgung einschalten, um den Winkel auf 0° einzustellen.  
