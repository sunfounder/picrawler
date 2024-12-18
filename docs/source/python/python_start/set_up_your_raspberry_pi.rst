.. note:: 

    Bonjour et bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez au cœur de Raspberry Pi, Arduino et ESP32 avec des passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Aperçus exclusifs** : Profitez d'un accès anticipé aux annonces des nouveaux produits et avant-premières.
    - **Remises exclusives** : Bénéficiez de réductions spéciales sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des tirages au sort et à des promotions spéciales pour les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

4. Configurer votre Raspberry Pi
==================================

Si vous avez un écran
-----------------------

Si vous disposez d’un écran, il sera facile d’opérer directement sur le Raspberry Pi.

**Composants nécessaires**

* Tout modèle de Raspberry Pi
* 1 * Adaptateur secteur
* 1 * Carte Micro SD
* 1 * Adaptateur secteur pour écran
* 1 * Câble HDMI
* 1 * Écran
* 1 * Souris
* 1 * Clavier

1. Insérez la carte SD configurée avec Raspberry Pi OS dans le lecteur de carte micro SD situé sous votre Raspberry Pi.

#. Branchez la souris et le clavier.

#. Connectez l'écran au port HDMI du Raspberry Pi et assurez-vous que votre écran est branché à une prise murale et allumé.

    .. note::

        Si vous utilisez un Raspberry Pi 4, connectez l'écran au port HDMI0 (le plus proche du port d'alimentation).

#. Utilisez l'adaptateur secteur pour alimenter le Raspberry Pi.

#. Après quelques secondes, le bureau de Raspberry Pi OS s'affichera. Vous pouvez désormais ouvrir le Terminal pour commencer à entrer des commandes.

    .. image:: img/bookwarm.png
        :align: center

Si vous n'avez pas d'écran
-----------------------------

Si vous ne disposez pas d’un écran, vous pouvez accéder à votre Raspberry Pi à distance.

Vous pouvez utiliser la commande SSH pour ouvrir le shell Bash du Raspberry Pi. Bash est le shell par défaut standard pour Linux. Le shell est une interface permettant à l'utilisateur d'envoyer des instructions à Unix/Linux. La plupart des tâches que vous devez réaliser peuvent être effectuées via le shell.

Si vous trouvez que l'utilisation de la fenêtre de commande pour accéder à votre Raspberry Pi est limitée, vous pouvez également utiliser la fonctionnalité de bureau à distance pour gérer facilement les fichiers sur votre Raspberry Pi via une interface graphique.

Voir ci-dessous les tutoriels détaillés pour chaque système.

.. toctree::

    remote_macosx
    remote_windows
    remote_linux
    remote_desktop

