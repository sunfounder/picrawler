.. note:: 

    Bonjour, bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et obtenez des aperçus exclusifs.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions et concours festifs** : Participez à des concours et à des promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_bull:

Le Combat de Taureaux
==========================

Transformez PiCrawler en un taureau enragé ! Utilisez sa caméra pour suivre et foncer sur le drap rouge !

.. .. image:: img/bullfight.png

**Exécuter le Code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 bull_fight.py


**Voir l'Image**

Après l'exécution du code, le terminal affichera le message suivant :

.. code-block::

    No desktop !
    * Serving Flask app "vilib.vilib" (lazy loading)
    * Environment: production
    WARNING: Do not use the development server in a production environment.
    Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)

Vous pouvez ensuite entrer ``http://<votre IP>:9000/mjpg`` dans votre navigateur pour afficher l'écran vidéo. Par exemple : ``https://192.168.18.113:9000/mjpg``

.. image:: img/display.png

**Code**

.. note::
    Vous pouvez **Modifier/Réinitialiser/Copier/Exécuter/Arrêter** le code ci-dessous. Mais avant cela, vous devez vous rendre dans le répertoire du code source, comme ``picrawler\examples``. Après avoir modifié le code, vous pouvez l'exécuter directement pour voir l'effet.

.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep
    from robot_hat import Music
    from vilib import Vilib
    
    
    crawler = Picrawler() 
    
    music = Music()
    
    def main():
        Vilib.camera_start()
        Vilib.display()
        Vilib.color_detect("red") 
        speed = 80
    
        while True:
            if Vilib.detect_obj_parameter['color_n']!=0:
                coordinate_x = Vilib.detect_obj_parameter['color_x']
                music.sound_play_threading('./sounds/talk1.wav')
    
                if coordinate_x < 100:
                    crawler.do_action('turn left',1,speed)
                    sleep(0.05) 
                elif coordinate_x > 220:
                    crawler.do_action('turn right',1,speed)
                    sleep(0.05) 
                else :
                    crawler.do_action('forward',2,speed)
                    sleep(0.05)    
            else :
                crawler.do_step('stand',speed)
                sleep(0.05)
    
    
    if __name__ == "__main__":
        main()


**Comment ça fonctionne ?**

En général, ce projet combine les points de connaissances de :ref:`py_move`, :ref:`py_vision` et :ref:`py_sound`.

Son déroulement est illustré dans la figure ci-dessous :

.. image:: img/bull_fight-f.png

