.. note:: 

    Bonjour, bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 sur Facebook ! Explorez plus en profondeur l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes post-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et d'aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_twist:

Twist
==============

Nous savons déjà comment faire en sorte que PiCrawler adopte une posture spécifique. L'étape suivante consiste à combiner plusieurs postures pour créer une action continue.

Ici, les quatre pieds de PiCrawler se soulèvent et s'abaissent par paires, en sautant au rythme de la musique.

**Exécuter le code**

.. raw:: html

    <run></run>

.. code-block:: 

    cd ~/picrawler/examples
    sudo python3 twist.py

Après le démarrage du programme, le robot se met d’abord debout lentement afin d’atteindre une posture stable.

Une fois debout, la musique de fond commence à jouer. En même temps, le robot effectue un mouvement de danse en torsion continu. Pendant ce mouvement, les quatre pattes se lèvent et s’abaissent alternativement, créant un effet de torsion rythmique. Les pattes se déplacent par paires coordonnées, ce qui donne l’impression que le corps se balance de gauche à droite.

Un court délai entre chaque étape rend le mouvement plus fluide et plus stable, au lieu d’être brusque ou trop rapide.

Le robot continue de danser pendant que la musique joue. Lorsque **Ctrl+C** est pressé, le programme s’arrête et le robot revient en toute sécurité à une position assise avant de quitter.


**Code**

.. note::
    Vous pouvez **modifier/réinitialiser/copier/exécuter/arrêter** le code ci-dessous. Mais avant cela, vous devez vous rendre dans le répertoire du code source, comme ``picrawler\examples``. Après avoir modifié le code, vous pouvez l'exécuter directement pour voir l'effet.

.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from robot_hat import Music
    from time import sleep

    music = Music()
    crawler = Picrawler()

    def twist(speed):
        new_step = [[50, 50, -80], [50, 50, -80], [50, 50, -80], [50, 50, -80]]

        for i in range(4):
            for inc in range(30, 60, 5):
                rise = [50, 50, (-80 + inc * 0.5)]
                drop = [50, 50, (-80 - inc)]

                new_step[i] = rise
                new_step[(i + 2) % 4] = drop
                new_step[(i + 1) % 4] = rise
                new_step[(i - 1) % 4] = drop

                crawler.do_step(new_step, speed)
                sleep(0.03)  # small delay to make motion smoother and less "crazy"

    def main():
        try:
            # Stand up slowly first
            crawler.do_step('stand', 40)
            sleep(1.0)

            # Start music
            music.music_play('./musics/sports-Ahjay_Stelino.mp3')
            music.music_set_volume(20)

            while True:
                twist(speed=100)

        except KeyboardInterrupt:
            print("\nCtrl+C detected, exiting...")

        finally:
            # Sit down safely before exit
            try:
                crawler.do_step('sit', 40)
                sleep(1.0)
            except Exception:
                pass

    if __name__ == "__main__":
        main()

**Comment cela fonctionne ?**

Dans ce code, vous devez porter attention à la partie suivante :

.. code-block:: python

    def twist(speed):
        new_step = [[50, 50, -80], [50, 50, -80], [50, 50, -80], [50, 50, -80]]

        for i in range(4):
            for inc in range(30, 60, 5):
                rise = [50, 50, (-80 + inc * 0.5)]
                drop = [50, 50, (-80 - inc)]

                new_step[i] = rise
                new_step[(i + 2) % 4] = drop
                new_step[(i + 1) % 4] = rise
                new_step[(i - 1) % 4] = drop

                crawler.do_step(new_step, speed)
                sleep(0.03)  # petit délai pour rendre le mouvement plus fluide et moins brusque

En termes simples, ce code utilise deux boucles ``for`` imbriquées pour faire varier
de manière continue et régulière les valeurs du tableau ``new_step``.  
En même temps, ``crawler.do_step()`` exécute chaque posture, ce qui crée
un mouvement continu.

Vous pouvez obtenir intuitivement le tableau de coordonnées correspondant
à chaque posture dans :ref:`py_posture`.

De plus, cet exemple joue également une musique de fond.  
La méthode d’implémentation est la suivante.

Jouer de la musique en important la bibliothèque suivante :

.. code-block:: python

    from robot_hat import Music

Déclarer un objet ``Music`` :

.. code-block:: python

    music = Music()

Lire la musique de fond située dans le dossier ``picrawler/examples/musics``
et régler le volume à 20. Vous pouvez également ajouter de la musique
dans le dossier ``musics`` via :ref:`filezilla`.

.. code-block:: python

    music.music_play('./musics/sports-Ahjay_Stelino.mp3')
    music.music_set_volume(20)