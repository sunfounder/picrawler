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

5. Installer tous les modules (Important)
===============================================

Assurez-vous d'être connecté à Internet et mettez à jour votre système :

.. raw:: html

    <run></run>

.. code-block::

    sudo apt update
    sudo apt upgrade

.. note::

    Les packages liés à Python3 doivent être installés si vous utilisez la version Lite du système d'exploitation.

    .. raw:: html

        <run></run>

    .. code-block::

        sudo apt install git python3-pip python3-setuptools python3-smbus

Installez le module ``robot-hat``.

.. raw:: html

    <run></run>

.. code-block::

    cd ~/
    git clone -b v2.0 https://github.com/sunfounder/robot-hat.git
    cd robot-hat
    sudo python3 setup.py install

Téléchargez ensuite le code et installez le module ``vilib``.

.. raw:: html

    <run></run>

.. code-block::

    cd ~/
    git clone -b picamera2 https://github.com/sunfounder/vilib.git
    cd vilib
    sudo python3 install.py

Ensuite, téléchargez le code et installez le module ``picrawler``.

.. raw:: html

    <run></run>

.. code-block::

    cd ~/
    git clone https://github.com/sunfounder/picrawler.git --depth 1
    cd picrawler
    sudo python3 setup.py install

Cette étape prendra un peu de temps, soyez patient.

Enfin, vous devez exécuter le script ``i2samp.sh`` pour installer les composants requis par l'amplificateur i2s, sinon le pislot n'aura pas de son.

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler
    sudo bash i2samp.sh
	
.. image:: img/i2s.png

Tapez ``y`` et appuyez sur ``Entrée`` pour continuer à exécuter le script.

.. image:: img/i2s2.png

Tapez ``y`` et appuyez sur ``Entrée`` pour exécuter ``/dev/zero`` en arrière-plan.

.. image:: img/i2s3.png

Tapez ``y`` et appuyez sur ``Entrée`` pour redémarrer la machine.

.. note::
    Si aucun son n'est émis après le redémarrage, vous devrez peut-être exécuter le script ``i2samp.sh`` plusieurs fois.
