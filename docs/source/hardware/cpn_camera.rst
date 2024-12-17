.. note:: 

    Bonjour, bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez plus profondément dans l'univers de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et bénéficiez d'aperçus exclusifs.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et à des promotions pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Camera Module
================

**Description**

.. image:: img/camera_module_pic.png
   :width: 200
   :align: center

Il s'agit d'un module caméra 5MP pour Raspberry Pi avec un capteur OV5647. Il est prêt à l'emploi : il vous suffit de connecter le câble ruban inclus au port CSI (Camera Serial Interface) de votre Raspberry Pi et vous êtes prêt à l'utiliser.

La carte est de petite taille, environ 25 mm x 23 mm x 9 mm, et pèse 3 g, ce qui la rend idéale pour les applications mobiles ou autres applications où la taille et le poids sont critiques. Le module caméra a une résolution native de 5 mégapixels et un objectif à mise au point fixe qui capture des images fixes à 2592 x 1944 pixels. Il prend également en charge la vidéo en 1080p à 30 ips, 720p à 60 ips et 640x480p à 90 ips.

.. note:: 

   Le module est uniquement capable de capturer des images et des vidéos, mais pas de son.

**Spécifications**

* **Résolution des images fixes** : 2592×1944 
* **Résolution vidéo prise en charge** : 1080p/30 ips, 720p/60 ips et 640x480p à 60/90 ips
* **Ouverture (F)** : 1.8 
* **Angle de vue** : 65 degrés
* **Dimensions** : 24 mm x 23,5 mm x 8 mm
* **Poids** : 3 g
* **Interface** : Connecteur CSI
* **Systèmes d'exploitation pris en charge** : Raspberry Pi OS (version la plus récente recommandée)


**Assemblez le module caméra**



Sur le module caméra ou le Raspberry Pi, vous trouverez un connecteur plastique plat. Tirez soigneusement sur le commutateur de fixation noir jusqu'à ce qu'il soit partiellement sorti. Insérez le câble FFC dans le connecteur plastique dans la direction indiquée et poussez le commutateur de fixation en place.

Si le câble FFC est correctement installé, il sera droit et ne se détachera pas si vous tirez légèrement dessus. Sinon, réinstallez-le correctement.

.. image:: img/connect_ffc.png
.. image:: img/1.10_camera.png
   :width: 700

.. warning:: 

   Ne pas installer la caméra lorsque l'alimentation est activée, cela pourrait endommager votre caméra.
