.. note:: 

    Bonjour et bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez au cœur de Raspberry Pi, Arduino et ESP32 avec des passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Aperçus exclusifs** : Profitez d'un accès anticipé aux annonces des nouveaux produits et avant-premières.
    - **Remises exclusives** : Bénéficiez de réductions spéciales sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des tirages au sort et à des promotions spéciales pour les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _remote_desktop:

Accès au Bureau à Distance pour Raspberry Pi
==================================================

Pour ceux qui préfèrent une interface utilisateur graphique (GUI) à un accès en ligne de commande, le Raspberry Pi prend en charge la fonctionnalité de bureau à distance. Ce guide vous explique comment configurer et utiliser VNC (Virtual Network Computing) pour un accès à distance.

Nous vous recommandons d'utiliser `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ à cette fin.

**Activer le service VNC sur le Raspberry Pi**

Le service VNC est préinstallé dans Raspberry Pi OS mais est désactivé par défaut. Suivez ces étapes pour l'activer :

#. Saisissez la commande suivante dans le terminal du Raspberry Pi :

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. Naviguez vers **Interfacing Options** en utilisant la flèche vers le bas, puis appuyez sur **Entrée**.

    .. image:: img/config_interface.png
        :align: center

#. Sélectionnez **VNC** parmi les options.

    .. image:: img/vnc.png
        :align: center

#. Utilisez les flèches pour choisir **<Oui>** -> **<OK>** -> **<Terminer** et finalisez l'activation du service VNC.

    .. image:: img/vnc_yes.png
        :align: center

**Se connecter via VNC Viewer**

#. Téléchargez et installez `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ sur votre ordinateur personnel.

#. Une fois installé, lancez VNC Viewer. Entrez le nom d'hôte ou l'adresse IP de votre Raspberry Pi et appuyez sur Entrée.

    .. image:: img/vnc_viewer1.png
        :align: center

#. Lorsque vous y êtes invité, entrez le nom d'utilisateur et le mot de passe de votre Raspberry Pi, puis cliquez sur **OK**.

    .. image:: img/vnc_viewer2.png
        :align: center

#. Après quelques secondes, le bureau de Raspberry Pi OS s'affichera. Vous pouvez maintenant ouvrir le Terminal pour commencer à entrer des commandes.

    .. image:: img/bookwarm.png
        :align: center
