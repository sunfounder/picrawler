.. note:: 

    Bonjour, bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 sur Facebook ! Explorez plus en profondeur Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et vos défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et bénéficiez de découvertes exclusives.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et promotions pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ezb_twist:

Twist
==================

Nous savons déjà comment faire en sorte que PiCrawler adopte une posture spécifique, l'étape suivante consiste à combiner ces postures pour former une action continue.

Ici, les quatre pattes de PiCrawler se lèvent et s'abaissent par paires, en sautant au rythme de la musique.

**Programme**

.. note:: 

    * Vous pouvez écrire le programme en suivant l'image ci-dessous, veuillez consulter le tutoriel : :ref:`ezblock:create_project_latest`.
    * Ou trouvez le code portant le même nom sur la page **Exemples** d'EzBlock Studio et cliquez directement sur **Exécuter** ou **Modifier**.

.. image:: img/twist.png
    :width: 800

**Comment ça fonctionne ?**

Le programme utilise deux boucles for imbriquées pour faire en sorte que le tableau ``new_step`` produise des changements continus et réguliers. En même temps, **do step** exécute la posture pour former une action continue.

Vous pouvez obtenir intuitivement le tableau des valeurs de coordonnées correspondant à chaque posture à partir de :ref:`ezb_posture`.

Un point auquel il faut prêter attention est ce bloc de matrice de coordonnées :

.. image:: img/sp210928_154257.png

Il s'agit essentiellement d'un tableau bidimensionnel, qui peut être traité à l'aide des blocs de la catégorie **Liste**. Sa structure est ``[[avant droit], [avant gauche], [arrière gauche], [arrière droit]]``.
Autrement dit, dans cet exemple, ``new_step#1`` correspond à l'avant droit ; ``new_step#2`` correspond à l'avant gauche ; ``new_step#3`` correspond à l'arrière gauche ; et ``new_step#4`` correspond à l'arrière droit.
