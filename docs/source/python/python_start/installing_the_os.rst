.. note:: 

    Bonjour et bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez au cœur de Raspberry Pi, Arduino et ESP32 avec des passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Aperçus exclusifs** : Profitez d'un accès anticipé aux annonces des nouveaux produits et avant-premières.
    - **Remises exclusives** : Bénéficiez de réductions spéciales sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des tirages au sort et à des promotions spéciales pour les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _install_os_sd:

2. Installation du système d'exploitation
=============================================

**Composants requis**

* Un ordinateur personnel
* Une carte Micro SD et un lecteur de cartes


1. Installation de Raspberry Pi Imager
--------------------------------------

#. Rendez-vous sur la page de téléchargement de logiciels Raspberry Pi à l'adresse suivante : `Raspberry Pi Imager <https://www.raspberrypi.org/software/>`_. Choisissez la version de l'Imager compatible avec votre système d'exploitation. Téléchargez et ouvrez le fichier pour lancer l'installation.

    .. image:: img/os_install_imager.png
        :align: center

#. Une alerte de sécurité peut s'afficher lors de l'installation, selon votre système d'exploitation. Par exemple, Windows peut afficher un message d'avertissement. Dans ce cas, sélectionnez **Plus d'informations** puis **Exécuter quand même**. Suivez les instructions à l'écran pour finaliser l'installation de Raspberry Pi Imager.

    .. image:: img/os_info.png
        :align: center

#. Lancez l'application Raspberry Pi Imager en cliquant sur son icône ou en tapant ``rpi-imager`` dans votre terminal.

    .. image:: img/os_open_imager.png
        :align: center

2. Installation du système d'exploitation sur une carte Micro SD
----------------------------------------------------------------------

#. Insérez votre carte SD dans votre ordinateur ou votre ordinateur portable à l'aide d'un lecteur de cartes.

#. Dans l'Imager, cliquez sur **Raspberry Pi Device** et sélectionnez le modèle Raspberry Pi dans la liste déroulante.

    .. image:: img/os_choose_device.png
        :align: center

#. Sélectionnez **Système d'exploitation** et optez pour la version recommandée.

    .. image:: img/os_choose_os.png
        :align: center

#. Cliquez sur **Choisir le stockage** et sélectionnez l'appareil de stockage approprié pour l'installation.

    .. note::

        Assurez-vous de sélectionner le bon appareil de stockage. Pour éviter toute confusion, déconnectez tout appareil de stockage supplémentaire si plusieurs sont connectés.

    .. image:: img/os_choose_sd.png
        :align: center

#. Cliquez sur **NEXT**, puis sur **EDIT SETTINGS** pour personnaliser vos paramètres du système d'exploitation.

    .. note::

        Si vous disposez d'un moniteur pour votre Raspberry Pi, vous pouvez ignorer les étapes suivantes et cliquer sur "Yes" pour démarrer l'installation. Ajustez les autres paramètres ultérieurement sur le moniteur.

    .. image:: img/os_enter_setting.png
        :align: center

#. Définissez un **nom d'hôte** pour votre Raspberry Pi.

    .. note::

        Le nom d'hôte est l'identifiant réseau de votre Raspberry Pi. Vous pouvez y accéder en utilisant ``<hostname>.local`` ou ``<hostname>.lan``.

    .. image:: img/os_set_hostname.png
        :align: center

#. Créez un **nom d'utilisateur** et un **mot de passe** pour le compte administrateur de votre Raspberry Pi.

    .. note::

        La création d'un nom d'utilisateur et d'un mot de passe uniques est essentielle pour sécuriser votre Raspberry Pi, qui ne possède pas de mot de passe par défaut.

    .. image:: img/os_set_username.png
        :align: center

#. Configurez le réseau sans fil en fournissant le **SSID** et le **mot de passe** de votre réseau.

    .. note::

        Réglez le ``Pays LAN sans fil`` sur le code à deux lettres correspondant à votre localisation selon `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_.

    .. image:: img/os_set_wifi.png
        :align: center

#. Pour vous connecter à distance à votre Raspberry Pi, activez SSH dans l'onglet Services.

    * Pour l'authentification par mot de passe, utilisez le nom d'utilisateur et le mot de passe définis dans l'onglet Général.
    * Pour l'authentification par clé publique, choisissez "Allow public-key authentication only". Si vous avez une clé RSA, elle sera utilisée. Sinon, cliquez sur "Run SSH-keygen" pour générer une nouvelle paire de clés.

    .. image:: img/os_enable_ssh.png
        :align: center

#. Le menu **Options** vous permet de configurer le comportement de l'Imager lors de l'écriture, notamment pour jouer un son à la fin, éjecter le média terminé et activer la télémétrie.

    .. image:: img/os_options.png
        :align: center

#. Une fois vos paramètres de personnalisation du système d'exploitation terminés, cliquez sur **Enregistrer** pour les sauvegarder. Ensuite, cliquez sur **Yes** pour les appliquer lors de l'écriture de l'image.

    .. image:: img/os_click_yes.png
        :align: center

#. Si la carte SD contient des données existantes, assurez-vous de sauvegarder celles-ci pour éviter toute perte de données. Cliquez sur **Yes** si aucune sauvegarde n'est nécessaire.

    .. image:: img/os_continue.png
        :align: center

#. Lorsque la fenêtre contextuelle "Write Successful" apparaît, cela signifie que votre image a été écrite et vérifiée avec succès. Vous êtes maintenant prêt à démarrer un Raspberry Pi depuis la carte Micro SD !

    .. image:: img/os_finish.png
        :align: center

#. Insérez la carte SD configurée avec Raspberry Pi OS dans le logement microSD situé sur la face inférieure du Raspberry Pi.

    .. image:: img/insert_sd_card.png
        :width: 500
        :align: center