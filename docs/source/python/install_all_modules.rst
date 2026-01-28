.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti Speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a promozioni e concorsi durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _install_all_modules:

Installare Tutti i Moduli (Importante)
=========================================

#. **Preparare il sistema**

   Assicurati che il tuo Raspberry Pi sia connesso a Internet, quindi aggiorna il sistema:

   .. raw:: html

      <run></run>

   .. code-block::

      sudo apt update
      sudo apt upgrade

   .. note::
      
      Se stai utilizzando Raspberry Pi OS Lite, installa prima i pacchetti Python 3 necessari:

   .. raw:: html

      <run></run>

   .. code-block::

         sudo apt install git python3-pip python3-setuptools python3-smbus

#. **Installare robot-hat**

   Scarica e installa il modulo ``robot-hat``:

   .. raw:: html

      <run></run>

   .. code-block::

      cd ~/
      git clone -b v2.0 https://github.com/sunfounder/robot-hat.git --depth 1
      cd robot-hat
      sudo python3 install.py

#. **Installare vilib**

   Scarica e installa il modulo ``vilib``:

   .. raw:: html

      <run></run>

   .. code-block::

      cd ~/
      git clone https://github.com/sunfounder/vilib.git --depth 1
      cd vilib
      sudo python3 install.py


#. **Installare picrawler**

   Quindi scarica il codice e installa il modulo ``picrawler``.
   
   .. raw:: html
   
       <run></run>
   
   .. code-block::
   
       cd ~/
       git clone https://github.com/sunfounder/picrawler.git --depth 1
       cd picrawler
       sudo python3 setup.py install
   
   Questo passaggio richiederà un po’ di tempo, quindi sii paziente.

#. **Abilitare l’audio (amplificatore I2S)**

   Per abilitare l’uscita audio, esegui lo script ``i2samp.sh`` per installare i componenti necessari dell’amplificatore I2S:

   .. raw:: html

      <run></run>

   .. code-block::

      cd ~/robot-hat
      sudo bash i2samp.sh

   Segui le istruzioni visualizzate sullo schermo digitando ``y`` e premendo Invio per continuare, esegui ``/dev/zero`` in background e riavvia il Picar-X.

   .. note::
      Se non c’è alcun suono dopo il riavvio, prova a eseguire lo script ``i2samp.sh`` più volte.
