.. note:: 

    Bonjour, bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et obtenez des aperçus exclusifs.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions et concours festifs** : Participez à des concours et à des promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_emotional:

Robot Émotionnel
===================

Cet exemple montre plusieurs actions personnalisées intéressantes du PiCrawler.

**Exécuter le code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 emotional_robot.py


**Code**

.. note::
    Vous pouvez **modifier/réinitialiser/copier/exécuter/arrêter** le code ci-dessous. Mais avant cela, vous devez vous rendre dans le répertoire contenant le code source, tel que ``picrawler\examples``. Après avoir modifié le code, vous pouvez l'exécuter directement pour voir l'effet.

.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep

    crawler = Picrawler() 

    def handwork(speed):

        basic_step = []
        basic_step = crawler.step_list.get("sit")
        left_hand  = crawler.mix_step(basic_step,0,[0,50,80])
        right_hand  = crawler.mix_step(basic_step,1,[0,50,80])
        two_hand = crawler.mix_step(left_hand,1,[0,50,80])

        crawler.do_step('sit',speed)
        sleep(0.6)    
        crawler.do_step(left_hand,speed)
        sleep(0.6)
        crawler.do_step(two_hand,speed)
        sleep(0.6)
        crawler.do_step(right_hand,speed)
        sleep(0.6)
        crawler.do_step('sit',speed)
        sleep(0.6)

    def twist(speed):
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

    ##"[[droit avant], [gauche avant], [gauche arrière], [droit arrière]]")

    def pushup(speed):
        up=[[80, 0, -100], [80, 0, -100],[0, 120, -60], [0, 120, -60]]
        down=[[80, 0, -30], [80, 0, -30],[0, 120, -60], [0, 120, -60]]
        crawler.do_step(up,speed)
        sleep(0.6)
        crawler.do_step(down,speed)
        sleep(0.6)

    def swimming(speed):
        for i in range(100):
            crawler.do_step([[100-i,i,0],[100-i,i,0],[0,120,-60+i/5],[0,100,-40-i/5]],speed)

    # principal
    def main():
        speed = 100

        swimming(speed)
        pushup(speed)
        handwork(speed)
        twist(speed)

        sleep(0.05)

    if __name__ == "__main__":
        main()

    
 
