.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie gemeinsam mit anderen Enthusiasten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und bewältigen Sie technische Herausforderungen mit der Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Profitieren Sie von exklusiven Angeboten für unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Verlosungen und saisonalen Aktionen teil.

    👉 Bereit, mit uns zu entdecken und zu gestalten? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Servo-Nullstellung für die Montage  
=====================================

Vor der Montage des Servos muss der Winkel auf Null eingestellt werden.  
Dies liegt daran, dass der Servomotor einen begrenzten Bewegungsbereich hat.  
Durch das Einstellen des Winkels auf null Grad wird sichergestellt, dass sich 
der Servo in seiner Ausgangsposition befindet und den Bewegungsbereich nicht 
überschreitet, wenn er eingeschaltet wird.  
Falls der Servo vor der Montage nicht auf null Grad eingestellt wird, könnte er 
beim Einschalten versuchen, seinen Bewegungsbereich zu überschreiten, was 
möglicherweise den Servo oder das angeschlossene mechanische System beschädigen könnte.  
Daher ist die Einstellung des Winkels auf Null ein wichtiger Schritt, um den sicheren 
und normalen Betrieb des Servomotors zu gewährleisten.  


Für Python-Nutzer  
------------------------

Bitte folgen Sie :ref:`quick_guide_python`, um die Installation des Raspberry Pi OS 
abzuschließen und die Winkel der Servos anzupassen.  

Für Ezblock-Nutzer  
-----------------------

.. note:: 

    Falls Sie einen Raspberry Pi 5 verwenden, wird unsere grafische Programmiersoftware EzBlock nicht unterstützt.  


Nach der Installation des Ezblock-Systems kann der P11-Pin zur 
Anpassung des Servos verwendet werden.  
Bitte folgen Sie :ref:`ezb_servo_adjust` für weitere Details.  
