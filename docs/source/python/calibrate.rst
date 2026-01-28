.. note:: 

    Bonjour et bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez au cœur de Raspberry Pi, Arduino et ESP32 avec des passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Aperçus exclusifs** : Profitez d'un accès anticipé aux annonces des nouveaux produits et avant-premières.
    - **Remises exclusives** : Bénéficiez de réductions spéciales sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des tirages au sort et à des promotions spéciales pour les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Calibrer le PiCrawler
=============================


En raison des possibles déviations lors de l'installation du PiCrawler ou des limitations des servomoteurs eux-mêmes, certains angles des servos peuvent être légèrement inclinés. Vous pouvez donc les calibrer.

Bien sûr, vous pouvez sauter ce chapitre si vous pensez que l'assemblage est parfait et qu'aucune calibration n'est nécessaire.

Étapes spécifiques :

1. Prenez le feuillet d'assemblage, tournez-le à la dernière page et posez-le à plat sur la table. Ensuite, placez le PiCrawler comme indiqué ci-dessous, en alignant sa base avec le contour du graphique de calibration.

    .. image:: img/calibration2.png

2. Exécutez le fichier ``calibration.py``.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/picrawler/examples/calibration
        sudo python3 calibration.py
        
    Après avoir exécuté le code ci-dessus, l'interface suivante s'affichera dans le terminal.

    .. image:: img/calibration1.png

3. Appuyez respectivement sur les touches ``2`` et ``3`` pour choisir les deux jambes de gauche, puis utilisez les touches ``w``, ``a``, ``s``, ``d``, ``r`` et ``f`` pour les déplacer jusqu'au point de calibration.

    .. image:: img/calibration3.png

4. Changez maintenant le papier de calibration pour le côté droit et appuyez sur les touches ``1`` et ``4`` pour sélectionner les deux jambes de droite, puis utilisez les mêmes touches pour les aligner avec le point de calibration.

    .. image:: img/calibration4.png

5. Une fois la calibration terminée, appuyez sur la touche ``espace`` pour sauvegarder. Vous serez invité à entrer ``Y`` pour confirmer, puis appuyez sur ``ctrl+c`` pour quitter le programme et finaliser la calibration.

    .. image:: img/calibration5.png
