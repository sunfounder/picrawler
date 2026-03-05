.. note:: 

    Bonjour, bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et obtenez des aperçus exclusifs.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions et concours festifs** : Participez à des concours et à des promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_pose:

Pose
=============

PiCrawler peut adopter une posture spécifique en définissant un tableau de coordonnées. Dans cet exemple, il adopte une posture avec la patte arrière droite levée.

.. image:: img/4cood.A.png

**Exécuter le code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 do_step.py

Après avoir lancé le programme, le robot se met d’abord debout lentement afin d’atteindre une posture stable.

Une fois debout, le robot exécute ensuite deux actions en boucle. Il commence par se placer dans une posture de pas en position debout et maintient cette position pendant quelques secondes, puis il passe à un pas personnalisé où les pattes se déplacent vers différentes coordonnées. Cela crée un mouvement répété de changement de posture.

Le robot continue d’alterner entre ces deux positions jusqu’à ce que le programme soit arrêté. Si **Ctrl+C** est pressé, le programme se termine en toute sécurité et le robot revient à une position assise.

**Code**

.. raw:: html

    <run></run>

.. code-block:: python

    #!/usr/bin/env python3
    from picrawler import Picrawler
    from time import sleep

    # Create Picrawler instance
    crawler = Picrawler()

    # Leg order:
    # [right front], [left front], [left rear], [right rear]
    new_step = [[45, 45, -75], [45, 0, -75], [45, 0, -30], [45, 45, -75]]

    # Get the default stand step from the move list
    stand_step = crawler.move_list['stand'][0]


    def main():
        action_speed = 80  # Speed for movement actions

        try:
            # Stand up slowly at 40% speed to reduce current spikes
            crawler.do_step('stand', 40)
            sleep(1.0)

            # Continuous action loop
            while True:
                crawler.do_step(stand_step, action_speed)
                sleep(3)

                crawler.do_step(new_step, action_speed)
                sleep(3)

        except KeyboardInterrupt:
            # Handle Ctrl+C for safe exit
            print("\nExiting safely...")

        finally:
            # Return to sitting position before shutting down
            try:
                crawler.do_step('sit', 40)
                sleep(1.0)
            except Exception:
                pass


    if __name__ == "__main__":
        main()

**Comment ça fonctionne ?**

Dans ce code, la ligne à surveiller est ``crawler.do_step()``.

Tout comme ``do_action()``, ``do_step()`` permet également de manipuler le comportement du PiCrawler. 
La différence est que ``do_action()`` permet d'effectuer des actions continues comme ``avancer``, tandis que ``do_step()`` permet de réaliser des gestes individuels comme ``se tenir debout`` ou ``s'asseoir``.


Il y a deux usages pour cette fonction :

Un : Elle peut utiliser des chaînes de caractères, en accédant directement au dictionnaire ``step_list`` de la bibliothèque ``picrawler``.

.. code-block:: python

    crawler.do_step('stand',speed) 
    # "speed" indique la vitesse de l'étape, la plage est de 0 à 100.

Deux : Elle peut également accepter un tableau de 4 valeurs de coordonnées.

.. code-block:: python

    new_step=[[45, 45, -75], [45, 0, -75], [45, 0, -30], [45, 45, -75]]
    # Ces quatre coordonnées servent à contrôler les quatre pattes : avant droit, avant gauche, arrière gauche et arrière droit.

Chaque patte possède un système de coordonnées indépendant. Comme montré ci-dessous :

.. image:: img/4cood.png

Il est nécessaire de mesurer les coordonnées de chaque orteil individuellement. Comme montré ci-dessous :

.. image:: img/1cood.png

À propos : le ``step_list`` utilisé dans la première méthode est également constitué d'un tableau contenant 4 valeurs de coordonnées.

.. code-block:: python

    step_list = {

        "stand":[
            [45, 45, -50], 
            [45, 45, -50], 
            [45, 45, -50], 
            [45, 45, -50]
        ],
        "sit":[
            [45, 45, -30], 
            [45, 45, -30], 
            [45, 45, -30], 
            [45, 45, -30]
        ],
              
    }





