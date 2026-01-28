.. note:: 

    Bonjour et bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez au cœur de Raspberry Pi, Arduino et ESP32 avec des passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Aperçus exclusifs** : Profitez d'un accès anticipé aux annonces des nouveaux produits et avant-premières.
    - **Remises exclusives** : Bénéficiez de réductions spéciales sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des tirages au sort et à des promotions spéciales pour les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Réglage des Servos (Important)
===================================

.. note:: 

    Si votre Robot HAT est en version V44 ou supérieure (avec le haut-parleur situé en haut de la carte) et comprend un bouton intégré **Zero**, vous pouvez ignorer cette étape et simplement appuyer sur le bouton **Zero** pour activer le programme de mise à zéro des servos.

    .. image:: img/robot_hat_v44.png
        :width: 500
        :align: center


L'angle de fonctionnement des servos varie de -90° à 90°, mais l'angle configuré en usine est aléatoire, pouvant être 0°, 45°, ou autre. Si nous assemblons directement le robot avec ces angles aléatoires, cela entraînera un fonctionnement désordonné du robot ou, pire, le blocage et la surchauffe des servos.

Nous devons donc régler tous les servos à un angle de 0° avant de les installer, ce qui place l'angle du servo au centre, quelle que soit la direction de rotation.

#. Pour vérifier que le servo est bien réglé sur 0°, insérez d'abord le bras du servo dans l'axe du servo, puis faites doucement pivoter le bras pour observer son fonctionnement.

    .. image:: img/servo_arm.png
        :align: center

#. Ensuite, exécutez le script ``servo_zeroing.py`` situé dans le dossier ``examples/``.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/picrawler/examples
        sudo python3 servo_zeroing.py

#. Branchez ensuite le câble du servo sur le port P11 comme indiqué ci-dessous. Vous verrez alors le bras du servo pivoter pour atteindre une position. (Ceci est la position 0°, qui peut être une position aléatoire et non nécessairement verticale ou parallèle.)

    .. image:: img/servo_pin11.jpg

#. Retirez maintenant le bras du servo tout en maintenant le câble du servo branché et sans éteindre l'alimentation. Continuez l'assemblage en suivant les instructions du manuel papier.

.. note::

    * Ne débranchez pas ce câble servo avant de le fixer avec la vis du servo. Vous pouvez le débrancher après l'avoir fixé.
    * Ne faites pas tourner le servo lorsqu'il est alimenté pour éviter de l'endommager. Si l'axe du servo n'est pas inséré dans la bonne position, retirez le servo et réinsérez-le correctement.
    * Avant d'assembler chaque servo, branchez le câble du servo sur une broche PWM et allumez l'alimentation pour régler son angle à 0°.
