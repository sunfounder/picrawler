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

Installieren aller Module (Wichtig)
=========================================

#. **System vorbereiten**

   Stellen Sie sicher, dass Ihr Raspberry Pi mit dem Internet verbunden ist, und aktualisieren Sie dann das System:

   .. raw:: html

      <run></run>

   .. code-block::

      sudo apt update
      sudo apt upgrade

   .. note::
      
      Wenn Sie Raspberry Pi OS Lite verwenden, installieren Sie zuerst die erforderlichen Python-3-Pakete:

   .. raw:: html

      <run></run>

   .. code-block::

         sudo apt install git python3-pip python3-setuptools python3-smbus

#. **robot-hat installieren**

   Laden Sie das Modul ``robot-hat`` herunter und installieren Sie es:

   .. raw:: html

      <run></run>

   .. code-block::

      cd ~/
      git clone -b v2.0 https://github.com/sunfounder/robot-hat.git --depth 1
      cd robot-hat
      sudo python3 install.py

#. **vilib installieren**

   Laden Sie das Modul ``vilib`` herunter und installieren Sie es:

   .. raw:: html

      <run></run>

   .. code-block::

      cd ~/
      git clone https://github.com/sunfounder/vilib.git --depth 1
      cd vilib
      sudo python3 install.py


#. **picrawler installieren**

   Laden Sie anschließend den Code herunter und installieren Sie das Modul ``picrawler``.
   
   .. raw:: html
   
       <run></run>
   
   .. code-block::
   
       cd ~/
       git clone https://github.com/sunfounder/picrawler.git --depth 1
       cd picrawler
       sudo python3 setup.py install
   
   Dieser Schritt dauert etwas, bitte haben Sie Geduld.

#. **Sound aktivieren (I2S-Verstärker)**

   Um die Audioausgabe zu aktivieren, führen Sie das Skript ``i2samp.sh`` aus, um die erforderlichen I2S-Verstärkerkomponenten zu installieren:

   .. raw:: html

      <run></run>

   .. code-block::

      cd ~/robot-hat
      sudo bash i2samp.sh

   Folgen Sie den Anweisungen auf dem Bildschirm, indem Sie ``y`` eingeben und Enter drücken, um fortzufahren, ``/dev/zero`` im Hintergrund auszuführen und den Picar-X neu zu starten.

   .. note::
      Wenn nach dem Neustart kein Ton zu hören ist, versuchen Sie, das Skript ``i2samp.sh`` mehrmals auszuführen.
