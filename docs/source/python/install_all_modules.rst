.. note:: 

    Bonjour et bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez au cœur de Raspberry Pi, Arduino et ESP32 avec des passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Aperçus exclusifs** : Profitez d'un accès anticipé aux annonces des nouveaux produits et avant-premières.
    - **Remises exclusives** : Bénéficiez de réductions spéciales sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des tirages au sort et à des promotions spéciales pour les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _install_all_modules:

Installer tous les modules (Important)
=========================================

#. **Préparer le système**

   Assurez-vous que votre Raspberry Pi est connecté à Internet, puis mettez le système à jour :

   .. raw:: html

      <run></run>

   .. code-block::

      sudo apt update
      sudo apt upgrade

   .. note::
      
      Si vous utilisez Raspberry Pi OS Lite, installez d’abord les paquets Python 3 requis :

   .. raw:: html

      <run></run>

   .. code-block::

         sudo apt install git python3-pip python3-setuptools python3-smbus

#. **Installer robot-hat**

   Téléchargez et installez le module ``robot-hat`` :

   .. raw:: html

      <run></run>

   .. code-block::

      cd ~/
      git clone -b v2.0 https://github.com/sunfounder/robot-hat.git --depth 1
      cd robot-hat
      sudo python3 install.py

#. **Installer vilib**

   Téléchargez et installez le module ``vilib`` :

   .. raw:: html

      <run></run>

   .. code-block::

      cd ~/
      git clone https://github.com/sunfounder/vilib.git --depth 1
      cd vilib
      sudo python3 install.py


#. **Installer picrawler**

   Téléchargez ensuite le code et installez le module ``picrawler``.
   
   .. raw:: html
   
       <run></run>
   
   .. code-block::
   
       cd ~/
       git clone https://github.com/sunfounder/picrawler.git --depth 1
       cd picrawler
       sudo python3 setup.py install
   
   Cette étape prendra un certain temps, veuillez donc patienter.

#. **Activer le son (amplificateur I2S)**

   Pour activer la sortie audio, exécutez le script ``i2samp.sh`` afin d’installer les composants nécessaires de l’amplificateur I2S :

   .. raw:: html

      <run></run>

   .. code-block::

      cd ~/robot-hat
      sudo bash i2samp.sh

   Suivez les instructions à l’écran en tapant ``y`` puis en appuyant sur Entrée pour continuer, exécuter ``/dev/zero`` en arrière-plan et redémarrer le Picar-X.

   .. note::
      S’il n’y a pas de son après le redémarrage, essayez d’exécuter le script ``i2samp.sh`` plusieurs fois.
