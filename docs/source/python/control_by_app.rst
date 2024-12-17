.. note:: 

    Bonjour, bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et obtenez des aperçus exclusifs.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions et concours festifs** : Participez à des concours et des promotions pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _control_by_app:

Contrôlé par l'application
==============================

Le contrôleur SunFounder est utilisé pour contrôler les robots basés sur Raspberry Pi/Pico.

L'application intègre des widgets pour des boutons, des interrupteurs, des joysticks, des croix directionnelles, des curseurs et des curseurs de gaz ; des widgets pour l'affichage numérique, le radar ultrasonique, la détection en niveaux de gris et la vitesse.

Il y a 17 zones (A-Q), où vous pouvez placer différents widgets pour personnaliser votre propre contrôleur.

De plus, cette application propose un service de diffusion vidéo en direct.

Personnalisons un contrôleur PiCrawler avec cette application.

**Comment faire ?**

#. Installez le module ``sunfounder-controller``.

    Les modules ``robot-hat``, ``vilib`` et ``picrawler`` doivent d'abord être installés. Pour plus de détails, consultez :ref:`install_all_modules`.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~
        git clone https://github.com/sunfounder/sunfounder-controller.git
        cd ~/sunfounder-controller
        sudo python3 setup.py install

#. Exécutez le code.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/sunfounder-controller/examples
        sudo python3 picrawler_control.py

#. Installez `SunFounder Controller <https://docs.sunfounder.com/projects/sf-controller/en/latest/>`_ depuis l'**App Store (iOS)** ou **Google Play (Android)**.


#. Ouvrez l'application et créez un nouveau contrôleur.

    Créez un nouveau contrôleur en cliquant sur le signe + dans l'application SunFounder Controller.

    .. image:: img/app1.PNG

    Il existe des contrôleurs prédéfinis pour certains produits dans la section Prédéfinis. Ici, nous choisissons PiCrawler.

    .. image:: img/app_control1.jpg

    Donnez-lui un nom et sélectionnez le type de contrôleur.

    .. image:: img/app_control2.jpg

    Une fois dans ce contrôleur prédéfini, vous remarquerez déjà quelques widgets. Si vous n'avez rien d'autre à modifier, cliquez sur le bouton |app_save|.

    .. image:: img/app_control3.jpg

#. Connectez-vous à PiCrawler.

    Lorsque vous cliquez sur le bouton **Connecter**, l'application recherche automatiquement les robots à proximité. Leur nom est défini dans ``picrawler_control.py`` et doit être en cours d'exécution en tout temps.

    .. image:: img/app_control6.jpg

    Une fois que vous avez cliqué sur le nom du produit, le message "Connecté avec succès" apparaît et le nom du produit s'affiche dans le coin supérieur droit.

    .. image:: img/app_control7.jpg

    .. note::

        * Vous devez vous assurer que votre appareil mobile est connecté au même réseau local que PiCrawler.
        * Si la recherche automatique échoue, vous pouvez aussi entrer manuellement l'IP pour vous connecter.

        .. image:: img/app11.PNG

#. Exécutez ce contrôleur.

    Cliquez sur le bouton **Exécuter** pour démarrer le contrôleur. Vous verrez l'image capturée par la caméra, et vous pourrez désormais contrôler votre PiCrawler avec ces widgets.

    .. image:: img/app_control8.jpg

    Voici les fonctions des widgets.

    * **A** : Réglez l'alimentation de PiCrawler.
    * **B** : Affichez la vitesse de déplacement du robot.
    * **C** : Fonction identique à celle du widget B.
    * **D** : Affichez les obstacles détectés sous forme de points rouges.
    * **G** : Reconnaissance vocale, appuyez et maintenez ce widget pour commencer à parler. Il affichera la voix reconnue lorsque vous le relâcherez. Nous avons défini les commandes ``avant``, ``arrière``, ``gauche`` et ``droite`` dans le code pour contrôler le robot.
    * **K** : Contrôlez les mouvements avant, arrière, gauche et droite du robot.
    * **Q** : Tournez la tête (caméra) vers le haut, vers le bas, à gauche ou à droite.
    * **N** : Activez la fonction de reconnaissance des couleurs.
    * **O** : Activez la fonction de reconnaissance faciale.
    * **P** : Activez la fonction de reconnaissance d'objets, elle peut reconnaître près de 90 types d'objets. Pour la liste des modèles, veuillez consulter : https://github.com/sunfounder/vilib/blob/master/workspace/coco_labels.txt.
