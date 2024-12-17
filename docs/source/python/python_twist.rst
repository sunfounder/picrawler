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


**Code**

.. note::
    Vous pouvez **modifier/réinitialiser/copier/exécuter/arrêter** le code ci-dessous. Mais avant cela, vous devez vous rendre dans le répertoire du code source, comme ``picrawler\examples``. Après avoir modifié le code, vous pouvez l'exécuter directement pour voir l'effet.

.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from robot_hat import Music

    music = Music()
    crawler = Picrawler()


    def twist(speed):
        new_step=[[50, 50, -80], [50, 50, -80],[50, 50, -80], [50, 50, -80]]
        for i in range(4):
            for inc in range(30, 60, 5): 
                rise = [50,50,(-80+inc*0.5)]
                drop = [50,50,(-80-inc)]

                new_step[i]=rise
                new_step[(i+2)%4] = drop
                new_step[(i+1)%4] = rise
                new_step[(i-1)%4] = drop
                # print(new_step)
                crawler.do_step(new_step,speed)


    def main():  

        music.music_play('./musics/sports-Ahjay_Stelino.mp3')
        music.music_set_volume(20)

        while True:
            twist(speed=100) 


    if __name__ == "__main__":
        main()

**Comment ça fonctionne ?**

Dans ce code, il faut prêter attention à cette partie :

.. code-block:: python

    def twist(speed):
        ## [avant droit], [avant gauche], [arrière gauche], [arrière droit]
        new_step=[[50, 50, -80], [50, 50, -80],[50, 50, -80], [50, 50, -80]]
        for i in range(4):
            for inc in range(30,60,5):  
                rise = [50,50,(-80+inc*0.5)]
                drop = [50,50,(-80-inc)]

                new_step[i]=rise
                new_step[(i+2)%4] = drop
                new_step[(i+1)%4] = rise
                new_step[(i-1)%4] = drop
                crawler.do_step(new_step,speed)

En résumé, cela utilise deux boucles `for` pour faire en sorte que le tableau ``new_step`` subisse des changements réguliers et continus, et simultanément, la fonction ``crawler.do_step()`` exécute la posture pour créer une action fluide.

Vous pouvez obtenir intuitivement le tableau des valeurs de coordonnées correspondant à chaque posture dans :ref:`py_posture`.


De plus, l'exemple joue également de la musique en arrière-plan. Voici comment cela est mis en œuvre.

Jouer de la musique en important les bibliothèques suivantes.

.. code-block:: python

    from robot_hat import Music

Déclarez un objet Music.

.. code-block:: python

    music = Music()

Jouez la musique située dans le répertoire ``picrawler/examples/musics`` et réglez le volume à 20. Vous pouvez également ajouter de la musique dans le dossier ``musics`` via :ref:`filezilla`.

.. code-block:: python

    music.music_play('./musics/sports-Ahjay_Stelino.mp3')
    music.music_set_volume(20)


.. note::

    Vous pouvez ajouter différents effets sonores ou musiques dans les dossiers ``musics`` ou ``sounds`` via :ref:`filezilla`.
