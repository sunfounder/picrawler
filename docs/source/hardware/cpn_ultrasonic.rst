.. note:: 

    Bonjour, bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 sur Facebook ! Explorez plus en profondeur Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et vos défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et bénéficiez de découvertes exclusives.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et promotions pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Module Ultrason
===================

.. image:: img/ultrasonic_pic.png
    :width: 400
    :align: center

* **TRIG** : Entrée de signal de déclenchement
* **ECHO** : Sortie du signal d'écho
* **GND** : Masse
* **VCC** : Alimentation 5V

Il s'agit du capteur de distance ultrasonique HC-SR04, permettant une mesure sans contact allant de 2 cm à 400 cm avec une précision de mesure pouvant atteindre 3 mm. Le module comprend un émetteur ultrasonique, un récepteur et un circuit de commande.

Vous n'avez besoin de connecter que 4 broches : VCC (alimentation), TRIG (déclenchement), ECHO (réception) et GND (masse), ce qui le rend facile à utiliser pour vos projets de mesure.

**Caractéristiques**

* Tension de fonctionnement : 5V DC
* Courant de fonctionnement : 16mA
* Fréquence de fonctionnement : 40Hz
* Plage maximale : 500 cm
* Plage minimale : 2 cm
* Signal d'entrée du déclencheur : impulsion TTL de 10 µS
* Signal de sortie de l'écho : signal de niveau TTL en fonction de la distance
* Connecteur : XH2.54-4P
* Dimensions : 46x20.5x15 mm

**Principe**

Les principes de fonctionnement sont les suivants :

* Utilisation d'un déclencheur IO pour envoyer un signal haut d'au moins 10 µS.
* Le module émet une impulsion ultrasonique de 8 cycles à 40 kHz et détecte si un signal d'écho est reçu.
* L'écho renverra un signal haut si un signal est retourné ; la durée du niveau haut correspond au temps écoulé entre l'émission et la réception du signal.
* Distance = (durée du signal haut x vitesse du son (340 m/s)) / 2

    .. image:: img/ultrasonic_prin.jpg
        :width: 800

Formule : 

* us / 58 = distance en centimètres
* us / 148 = distance en pouces
* distance = durée du signal haut x vitesse (340 m/s) / 2

**Remarques d'application**

* Ce module ne doit pas être connecté sous tension. Si nécessaire, connectez d'abord le GND du module. Sinon, cela pourrait affecter le fonctionnement du module.
* L'objet à mesurer doit avoir une surface d'au moins 0,5 m² et être aussi plat que possible. Dans le cas contraire, les résultats pourraient être affectés.
