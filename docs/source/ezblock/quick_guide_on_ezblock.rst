.. note::

    Bonjour, bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder sur Facebook ! Plongez plus profondément dans l'univers de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des tirages au sort et à des promotions saisonnières.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ezb_servo_adjust:

Guide rapide sur EzBlock
===========================

.. note::

    Si vous utilisez un Raspberry Pi 5, notre logiciel de programmation graphique, EzBlock, n'est pas supporté.

L'angle de fonctionnement du servo est compris entre -90° et 90°, mais l'angle préconfiguré en usine est aléatoire, pouvant être de 0°, 45° ou un autre angle. Si nous l'installons avec cet angle, cela peut entraîner un comportement erratique du robot après l'exécution du code, voire endommager le servo en provoquant un blocage ou une surchauffe.

Ainsi, nous devons d'abord régler tous les angles des servos à 0° avant de les installer, afin que l'angle soit centré, quel que soit le sens de rotation.

#. Tout d'abord, :ref:`ezblock:install_ezblock_os_latest` (les tutoriels EzBlock) sur une carte micro SD. Une fois l'installation terminée, insérez la carte dans le Raspberry Pi.

    .. note::
        Après l'installation, veuillez revenir à cette page.

    .. image:: img/insert_sd_card.png
        :width: 500
        :align: center

#. Pour vous assurer que le servo a bien été réglé à 0°, insérez d'abord le bras du servo dans l'axe du servo, puis faites tourner doucement le bras à un autre angle. Ce bras de servo vous permet de voir clairement que le servo effectue une rotation.

    .. image:: img/servo_arm.png

#. Suivez les instructions du guide de montage, insérez le câble de la batterie et mettez l'interrupteur d'alimentation sur ON. Branchez ensuite un câble USB-C alimenté pour activer la batterie. Attendez 1 à 2 minutes, un son indiquera que le Raspberry Pi a démarré avec succès.

    .. image:: img/Z_BTR.JPG
        :width: 800
        :align: center

#. Ensuite, branchez le câble du servo dans le port P11 comme suit.

    .. image:: img/Z_P11.JPG

#. Appuyez et maintenez la touche **USR**, puis appuyez sur la touche **RST** pour exécuter le script de mise à zéro du servo dans le système. Lorsque vous verrez le bras du servo se déplacer vers une position (c'est la position 0°, qui est un emplacement aléatoire et peut ne pas être verticale ou parallèle), cela indique que le programme a été exécuté.

    .. note::

        Cette étape n'a besoin d'être effectuée qu'une seule fois ; ensuite, il vous suffira d'insérer les câbles des autres servos, et ils se mettront automatiquement à zéro.

    .. image:: img/Z_P11_BT.png
        :width: 400
        :align: center

#. Maintenant, retirez le bras du servo, en veillant à ce que le câble du servo reste branché, et ne coupez pas l'alimentation. Continuez ensuite l'assemblage en suivant les instructions de montage sur papier.

.. note::

    * Ne débranchez pas ce câble de servo avant de fixer le servo avec la vis de servo, vous pouvez le débrancher une fois qu'il est bien fixé.
    * Ne tournez pas le servo lorsqu'il est sous tension afin d'éviter tout dommage ; si l'axe du servo est inséré sous un mauvais angle, retirez le servo et réinsérez-le correctement.
    * Avant de monter chaque servo, vous devez brancher le câble du servo dans le port P11 et allumer l'alimentation pour régler son angle à 0°.
    * Cette fonction de mise à zéro sera désactivée si vous téléchargez un programme sur le robot plus tard avec l'application EzBlock.
