.. note:: 

    Bonjour, bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 sur Facebook ! Explorez plus en profondeur Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et vos défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et bénéficiez de découvertes exclusives.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et promotions pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ezb_move:

Déplacement
=================

Voici le premier projet de PiCrawler. Il exécute sa fonction la plus basique : se déplacer.

.. image:: ../python/img/move.png

**Programme**

.. note:: 

    * Vous pouvez écrire le programme en suivant l'image ci-dessous, veuillez consulter le tutoriel : :ref:`ezblock:create_project_latest`.
    * Ou trouvez le code portant le même nom sur la page **Exemples** d'EzBlock Studio et cliquez directement sur **Exécuter** ou **Modifier**.

.. image:: img/move.png

Cliquez sur le bouton **Upload & Run** en bas à droite de l'écran, et PiCrawler exécutera les actions "avant" et "arrière" dans cet ordre.


**Comment ça fonctionne ?**

Tout d'abord, vous devez comprendre la structure du programme d'EzBlock, comme suit :

.. image:: img/sp210927_162828.png
    :width: 200

Tous les projets EzBlock contiennent ces deux blocs. Le bloc **Start** s'exécute au début du programme et n'est exécuté qu'une seule fois. Il est souvent utilisé pour définir des variables. Le bloc **Forever** s'exécute après **Start** et est répété indéfiniment, servant généralement à implémenter les fonctions principales.
Si vous supprimez ces deux blocs, vous pouvez les faire glisser à partir de la catégorie **Basique** à gauche.

Ensuite, vous devez comprendre les blocs suivants.

.. image:: img/sp210927_165133.png

**do action** permet à PiCrawler d'effectuer des actions de base. Vous pouvez modifier les options dans le premier emplacement. Par exemple, sélectionner "Tourner à gauche", "Reculer", etc.
Le deuxième emplacement permet de définir le nombre d'exécutions de l'action, et seuls des nombres entiers supérieurs à 0 peuvent être écrits.
Le troisième emplacement permet de définir la vitesse de l'action, et seuls des entiers compris entre 0 et 100 peuvent être écrits.

.. image:: img/sp210927_170717.png
    :width: 500

**do step** est similaire à **do action**, mais ce n'est pas une action, c'est une posture statique. Par exemple, "se lever", "s'asseoir".



Les deux blocs peuvent être glissés depuis la catégorie **PiCrawler** à gauche.
