.. note:: 

    Bonjour, bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 sur Facebook ! Explorez plus en profondeur Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et vos défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et bénéficiez de découvertes exclusives.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et promotions pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ezb_posture:

Ajuster la posture
==========================

Dans cet exemple, nous utilisons la fonction de télécommande pour contrôler chaque pied du PiCrawler et obtenir la posture souhaitée.

Vous pouvez appuyer sur le bouton pour afficher les valeurs de coordonnées actuelles. Ces valeurs de coordonnées seront utiles lorsque vous créerez des actions uniques pour PiCrawler.

.. image:: ../python/img/1cood.A.png

**Programme**

.. note:: 

    * Vous pouvez écrire le programme en suivant l'image ci-dessous, veuillez consulter le tutoriel : :ref:`ezblock:create_project_latest`.
    * Ou trouvez le code portant le même nom sur la page **Exemples** d'EzBlock Studio et cliquez directement sur **Exécuter** ou **Modifier**.

.. image:: img/do_single_leg.png
    :width: 800

Passez à l'interface de télécommande, vous verrez les widgets suivants.

.. image:: img/do_single_leg_B-1.png
    :width: 600

**Comment ça fonctionne ?**

Les trois blocs suivants sont à prendre en compte dans ce projet :

.. image:: img/sp210928_115847.png

Modifiez la valeur des coordonnées d'un pied spécifique.

.. image:: img/sp210928_115908.png

Retourne la valeur des coordonnées du pied correspondant.

.. image:: img/sp210928_115958.png

Vous souhaiterez peut-être simplifier le programme avec des Fonctions, notamment lorsque vous effectuez la même opération plusieurs fois. Regrouper ces opérations dans une fonction nouvellement déclarée peut grandement faciliter votre utilisation.

.. image:: img/sp210928_135733.png
    :width: 500