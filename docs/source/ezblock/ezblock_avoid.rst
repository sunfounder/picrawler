.. note:: 

    Bonjour, bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 sur Facebook ! Explorez plus en profondeur Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et vos défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et bénéficiez de découvertes exclusives.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et promotions pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ezb_avoid:

Évitement d'obstacles
=============================

Dans ce projet, le PiCrawler utilise un module ultrason pour détecter les obstacles 
devant lui. Lorsqu'il détecte un obstacle, le PiCrawler envoie un signal et cherche 
une autre direction pour avancer.

.. .. image:: ../python/img/avoid1.png

**Programme**

.. note:: 

    * Vous pouvez écrire le programme selon l'image ci-dessous, veuillez consulter le tutoriel : :ref:`ezblock:create_project_latest`.
    * Ou trouvez le code portant le même nom sur la page **Exemples** d'EzBlock Studio et cliquez directement sur **Exécuter** ou **Modifier**.

.. image:: img/avoid.png


**Comment ça fonctionne ?**

Vous pouvez trouver les blocs suivants dans la catégorie **Module** pour réaliser la détection de distance :

.. image:: img/sp210928_103046.png
    :width: 600

Il convient de noter que les deux broches du bloc doivent correspondre au câblage réel, à savoir trig-D2, echo-D3.

Voici le programme principal.

* Lire la ``distance`` détectée par le module ultrason et filtrer les valeurs inférieures à 0 (lorsque le module ultrason est trop éloigné de l'obstacle ou qu'il ne peut pas lire les données correctement, ``distance<0`` apparaîtra).
* Lorsque la ``distance`` est inférieure à ``alert_distance`` (la valeur seuil définie précédemment, qui est de 10), jouer l'effet sonore ``sign.wav``. Le PiCrawler effectue une ``rotation à gauche``.
* Lorsque la ``distance`` est supérieure à ``alert_distance``, le PiCrawler avance ``tout droit``.
