.. note:: 

    Bonjour, bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et obtenez des aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et à des promotions pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_move:

Déplacer
==============

Voici le premier projet de PiCrawler. Il exécute sa fonction de base : se déplacer.

.. .. image:: img/move.png

**Exécuter le code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 move.py

Lorsque le programme démarre, le PiCrawler se met debout et attend brièvement.

Il exécute ensuite en continu un cycle de mouvements :
avancer, reculer, tourner à gauche, tourner à droite,
petit virage à gauche et petit virage à droite.

Chaque action est séparée par de courts délais afin de rendre les mouvements plus fluides.

Appuyez sur Ctrl+C pour arrêter le programme.
Avant de quitter, le PiCrawler se met en position assise en toute sécurité.

**Code**

.. note::
    Vous pouvez **modifier/réinitialiser/copier/exécuter/arrêter** le code ci-dessous. Mais avant cela, vous devez accéder au répertoire source du code, comme ``picrawler\examples``. Après avoir modifié le code, vous pouvez l'exécuter directement pour voir l'effet.

.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep

    crawler = Picrawler()  # Create PiCrawler object

    def main():
        speed = 80  # Movement speed

        try:
            crawler.do_step('stand', 40)  # Stand up
            sleep(1.0)

            while True:
                crawler.do_action('forward', 1, speed)   # Move forward
                sleep(0.25)

                crawler.do_action('backward', 1, speed)  # Move backward
                sleep(0.25)

                crawler.do_action('turn left', 1, speed)  # Turn left
                sleep(0.25)

                crawler.do_action('turn right', 1, speed)  # Turn right
                sleep(0.25)

                crawler.do_action('turn left angle', 1, speed)  # Small left turn
                sleep(0.3)

                crawler.do_action('turn right angle', 1, speed)  # Small right turn
                sleep(0.3)

                sleep(0.5)

        except KeyboardInterrupt:
            print("\nCtrl+C pressed...")

        finally:
            crawler.do_step('sit', 40)  # Sit down before exit
            sleep(1.0)

    if __name__ == "__main__":
        main()


**Comment cela fonctionne ?**

#. Importation et initialisation

   .. code-block:: python

      from picrawler import Picrawler
      from time import sleep

      crawler = Picrawler()

   Le script importe les modules nécessaires et crée un objet
   ``Picrawler``, utilisé pour contrôler tous les mouvements du robot.

#. Fonction principale et préparation

   .. code-block:: python

      def main():
          speed = 80
          crawler.do_step('stand', 40)
          sleep(1.0)

   La fonction ``main()`` définit la vitesse de déplacement.
   Avant de démarrer la boucle, le robot se met debout et se stabilise.

#. Boucle de mouvement continue

   .. code-block:: python

      while True:
          crawler.do_action('forward', 1, speed)
          crawler.do_action('backward', 1, speed)
          crawler.do_action('turn left', 1, speed)
          crawler.do_action('turn right', 1, speed)
          crawler.do_action('turn left angle', 1, speed)
          crawler.do_action('turn right angle', 1, speed)

   Le robot exécute en continu une séquence prédéfinie
   d’actions de mouvement dans une boucle infinie.
   De courts délais entre les actions permettent d’obtenir
   des mouvements plus fluides.

#. Gestion de la sortie sécurisée

   .. code-block:: python

      except KeyboardInterrupt:
          print("\nCtrl+C pressed...")
      finally:
          crawler.do_step('sit', 40)

   La structure ``try / except / finally`` garantit que :

   - **Ctrl+C** arrête la boucle en toute sécurité.
   - Le robot se remet en position assise avant la fin du programme.

#. Point d’entrée du programme

   .. code-block:: python

      if __name__ == "__main__":
          main()

   Cela garantit que ``main()`` s’exécute uniquement lorsque
   le script est lancé directement.