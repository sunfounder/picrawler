.. note:: 

    Bonjour, bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 sur Facebook ! Explorez plus en profondeur Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et vos défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et bénéficiez de découvertes exclusives.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et promotions pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Calibrer le PiCrawler
=======================

Après avoir connecté le PiCrawler, il sera nécessaire de procéder à une étape de calibration. Cela est dû à des écarts éventuels lors du processus d'assemblage ou aux limitations des servomoteurs eux-mêmes, ce qui peut entraîner une légère inclinaison de certains angles des servomoteurs. Vous pouvez donc les calibrer lors de cette étape.

Cependant, si vous estimez que l'assemblage est parfait et qu'aucune calibration n'est nécessaire, vous pouvez également passer cette étape.

.. note:: 
    Si vous souhaitez recalibrer le robot pendant son utilisation, veuillez suivre les étapes ci-dessous.

    Vous pouvez ouvrir la page de détail du produit en cliquant sur l'icône de connexion dans le coin supérieur gauche.

    .. image:: img/calibrate0.png

    Cliquez sur le bouton **Paramètres**.

    .. image:: img/calibrate1.png

    Sur cette page, vous pouvez modifier le nom du produit, le type de produit, consulter la version de l'application ou calibrer le robot. Une fois que vous avez cliqué sur **Calibrer**, vous serez dirigé vers la page de calibration.

    .. image:: img/calibrate2.png


Les étapes de calibration sont les suivantes :

#. Prenez la feuille d'assemblage, retournez-la à la dernière page et placez-la à plat sur la table. Ensuite, placez le PiCrawler comme montré ci-dessous, en alignant sa base avec le contour du schéma de calibration.

    .. image:: img/calibration2.png
        :align: center

#. Retournez dans EzBlock Studio, sélectionnez un pied à gauche, puis cliquez sur les 3 ensembles de boutons X, Y et Z, et laissez les orteils s'aligner lentement avec le point de calibration.

   * Les boutons de calibration servent à affiner l'ajustement, et vous devrez appuyer sur ces boutons plusieurs fois pour voir la position des pinces changer.
   * Il est recommandé de commencer par cliquer sur le bouton haut de l'axe Z pour soulever le pied, puis d'ajuster les axes X et Y.

    .. image:: img/calibration4.jpg
        :align: center

#. Alignez de la même manière l'autre pied à gauche.

    .. image:: img/calibration3.png
        :align: center

#. Après avoir calibré les deux pieds de gauche, déplacez le papier de calibration à droite et calibrez les deux pieds droits en suivant la méthode ci-dessus.

    .. image:: img/calibration4.png
        :align: center