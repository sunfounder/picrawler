.. note:: 

    Bonjour, bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 sur Facebook ! Explorez plus en profondeur Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et vos défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et bénéficiez de découvertes exclusives.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et promotions pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ezb_remote:

Contrôle à distance
=========================

Dans ce projet, nous allons apprendre à contrôler à distance le PiCrawler.  
Vous pouvez contrôler le PiCrawler pour le faire avancer, reculer, tourner à gauche et à droite.

.. .. image:: img/remote_control.png

.. note:: 

    Vous pouvez consulter :ref:`ezblock:remote_control_latest`. Venez et réalisez ce projet sans problème.

**Programme**

.. note:: 

    * Vous pouvez écrire le programme en suivant l'image ci-dessous, veuillez consulter le tutoriel : :ref:`ezblock:create_project_latest`.
    * Ou trouvez le code portant le même nom sur la page **Exemples** d'EzBlock Studio et cliquez directement sur **Exécuter** ou **Modifier**.

.. image:: img/remote.png

Passez à l'interface de contrôle à distance, et vous verrez les widgets suivants.

.. image:: img/remote_B.png

Une fois le programme exécuté, vous pouvez activer le PiCrawler via le D-Pad.

**Comment ça fonctionne ?**

Après avoir déplacé le widget dans l'interface de contrôle à distance, une catégorie nommée **Remote** apparaîtra dans la colonne des catégories de blocs de l'interface de programmation.

Ici, nous ajoutons le widget D-Pad, ce qui fait apparaître le bloc **D-Pad get value**.

.. image:: img/sp210927_180739.png

Le D-Pad peut être considéré comme un bouton quatre-en-un. Vous pouvez choisir quel bouton lire dans le second espace du bloc.

Lorsque le bouton est pressé, la valeur est "1" ; lorsque le bouton n'est pas pressé, la valeur est "0".

.. image:: img/sp210927_182447.png
    :width: 200

Nous avons utilisé un bloc **if** (que vous pouvez trouver dans la catégorie **Logique** à gauche) pour faire avancer le PiCrawler lorsque le bouton **UP** du D-Pad est pressé.

.. image:: img/sp210927_182828.png
    :width: 600

Vous pouvez cliquer sur l'icône en forme d'engrenage en haut à gauche du bloc pour modifier la forme du bloc **if** et ainsi réaliser plusieurs branches de jugement.

.. image:: img/sp210927_183237.png
    :width: 300

Le bloc **if** est généralement utilisé avec le bloc **=**. Le bloc **=** peut être modifié en **>**, **<** et d'autres conditions via le menu déroulant, n'hésitez pas à l'utiliser de manière flexible.
