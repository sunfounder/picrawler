.. note::

    Bonjour, bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder sur Facebook ! Plongez plus profondément dans l'univers de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et vos défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aperçus exclusifs.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des tirages au sort et à des promotions pendant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _filezilla:

Logiciel Filezilla
==========================

.. image:: img/filezilla_icon.png

Le protocole de transfert de fichiers (FTP) est un protocole de communication standard utilisé pour le transfert de fichiers d'un serveur vers un client sur un réseau informatique.

Filezilla est un logiciel open source qui prend en charge non seulement FTP, mais aussi FTP sécurisé (FTPS) et SFTP. Nous pouvons utiliser Filezilla pour télécharger des fichiers locaux (comme des images et des fichiers audio, etc.) vers le Raspberry Pi, ou pour récupérer des fichiers depuis le Raspberry Pi vers notre ordinateur.

**Étape 1** : Télécharger Filezilla.

Téléchargez le client depuis le `site officiel de Filezilla <https://filezilla-project.org/>`_. Filezilla propose un excellent tutoriel, veuillez consulter : `Documentation - Filezilla <https://wiki.filezilla-project.org/Documentation>`_.

**Étape 2** : Se connecter au Raspberry Pi

Après une installation rapide, ouvrez Filezilla et `connectez-vous à un serveur FTP <https://wiki.filezilla-project.org/Using#Connecting_to_an_FTP_server>`_. Il existe trois méthodes de connexion, ici nous utilisons la barre **Connexion rapide**. Entrez le **nom d'hôte/IP**, **nom d'utilisateur**, **mot de passe** et **port (22)**, puis cliquez sur **Connexion rapide** ou appuyez sur **Entrée** pour vous connecter au serveur.

.. image:: img/filezilla_connect.png

.. note::

    La connexion rapide est une bonne méthode pour tester vos informations de connexion. Si vous souhaitez créer une entrée permanente, vous pouvez sélectionner **Fichier** -> **Copier la connexion actuelle dans le gestionnaire de sites** après une connexion rapide réussie, entrez un nom et cliquez sur **OK**. La prochaine fois, vous pourrez vous connecter en sélectionnant le site enregistré dans **Fichier** -> **Gestionnaire de sites**.
    
    .. image:: img/ftp_site.png

**Étape 3** : Télécharger/téléverser des fichiers.

Vous pouvez téléverser des fichiers locaux vers le Raspberry Pi en les faisant 
glisser-déposer, ou bien télécharger les fichiers présents sur le Raspberry Pi 
vers votre ordinateur local.

.. image:: img/upload_ftp.png
