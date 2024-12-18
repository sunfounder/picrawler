.. note:: 

    Bonjour et bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez au cœur de Raspberry Pi, Arduino et ESP32 avec des passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Aperçus exclusifs** : Profitez d'un accès anticipé aux annonces des nouveaux produits et avant-premières.
    - **Remises exclusives** : Bénéficiez de réductions spéciales sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des tirages au sort et à des promotions spéciales pour les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _i2c_spi_config:

6. Vérifiez l'interface I2C
========================================

Nous utiliserons l'interface I2C du Raspberry Pi. Cette interface doit avoir été activée lors de l'installation du module ``robot-hat``. Pour vous assurer que tout est en ordre, vérifions si elle est bien activée.

#. Saisissez la commande suivante :

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. Sélectionnez **Interfacing Options** en appuyant sur la flèche bas de votre clavier, puis appuyez sur la touche **Entrée**.

    .. image:: img/image282.png
        :align: center

#. Ensuite, sélectionnez **I2C**.

    .. image:: img/image283.png
        :align: center

#. Utilisez les flèches directionnelles du clavier pour sélectionner **<Yes>** -> **<OK>** afin de terminer la configuration de l'interface I2C.

    .. image:: img/image284.png
        :align: center