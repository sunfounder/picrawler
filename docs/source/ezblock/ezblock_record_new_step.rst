.. note:: 

    Bonjour, bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 sur Facebook ! Explorez plus en profondeur Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et vos défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et bénéficiez de découvertes exclusives.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et promotions pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ezb_record:

Enregistrer un Nouveau Pas
==============================

Nous utilisons la fonction de télécommande pour contrôler PiCrawler afin qu'il effectue plusieurs postures successivement, puis enregistrer ces postures. Vous pourrez ensuite les rejouer.

**Programme**

.. note:: 

    * Vous pouvez écrire le programme en suivant l'image ci-dessous, veuillez consulter le tutoriel : :ref:`ezblock:create_project_latest`.
    * Ou trouvez le code portant le même nom sur la page **Exemples** d'EzBlock Studio et cliquez directement sur **Exécuter** ou **Modifier**.

.. image:: img/record.png
    :width: 800

Passez à l'interface de contrôle à distance et vous verrez les widgets suivants.

.. image:: img/sp210928_164343-1.png
    :width: 600

**Comment ça fonctionne ?**


Ce projet est basé sur :ref:`ezb_posture`. Des fonctions d'enregistrement et de lecture ont été ajoutées.

La fonction d'enregistrement est mise en œuvre par le code suivant.

.. image:: img/sp210928_164449.png

La fonction de lecture est mise en œuvre par le code suivant.

.. image:: img/sp210928_164500.png