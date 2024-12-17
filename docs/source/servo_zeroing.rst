.. note::

    Bonjour et bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans le Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Réglage du zéro du servo pour l'assemblage
=================================================

Avant d'assembler le servo, il est nécessaire de régler l'angle à zéro. 
Cela est dû au fait que le moteur servo a une plage de mouvement limitée. 
En réglant l'angle à zéro degrés, on s'assure que le servo est dans sa position initiale et qu'il ne dépasse pas sa plage de mouvement lorsqu'il est sous tension. 
Si le servo n'est pas réglé à zéro avant l'assemblage, 
il pourrait tenter de dépasser sa plage de mouvement lorsqu'il est alimenté, 
ce qui pourrait endommager le servo ou le système mécanique auquel il est connecté. 
Ainsi, le réglage de l'angle à zéro est une étape importante pour garantir le bon fonctionnement et la sécurité du moteur servo.





Pour les utilisateurs Python
----------------------------------

Veuillez consulter :ref:`quick_guide_python` pour compléter l'installation 
du système d'exploitation Raspberry Pi et ajuster l'angle des servos.

Pour les utilisateurs Ezblock
---------------------------------

.. note::

    Si vous utilisez un Raspberry Pi 5, notre logiciel de programmation graphique, EzBlock, n'est pas pris en charge.

Après avoir installé le système Ezblock, 
le pin P11 peut être utilisé pour ajuster le servo. 
Pour plus de détails, veuillez consulter :ref:`ezb_servo_adjust`.
