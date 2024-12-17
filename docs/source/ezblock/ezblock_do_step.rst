.. note:: 

    Bonjour, bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez plus profondément dans Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et vos défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et bénéficiez de découvertes exclusives.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et promotions pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ezb_pose:

Posture
===============

PiCrawler peut adopter une posture spécifique en écrivant un tableau de coordonnées. Ici, il prend la posture avec le pied arrière droit levé.

.. image:: ../python/img/4cood.A.png

**Programme**

.. note:: 

    * Vous pouvez écrire le programme en suivant l'image ci-dessous, veuillez consulter le tutoriel : :ref:`ezblock:create_project_latest`.
    * Ou trouvez le code portant le même nom sur la page **Exemples** d'EzBlock Studio et cliquez directement sur **Exécuter** ou **Modifier**.

.. image:: img/dostep.png


**Comment ça fonctionne ?**

Dans ce code, l'élément à surveiller est **do step**.

Il a deux usages :

1. Il peut directement utiliser **stand** ou **sit**.

2. Il peut également écrire un tableau de 4 valeurs de coordonnées.

Chaque pied a un système de coordonnées indépendant. Comme montré ci-dessous :

.. image:: ../python/img/4cood.png

Il est nécessaire de mesurer les coordonnées de chaque orteil individuellement. Comme montré ci-dessous :

.. image:: ../python/img/1cood.png
