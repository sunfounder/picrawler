.. note:: 

    Bonjour, bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et obtenez des aperçus exclusifs.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions et concours festifs** : Participez à des concours et à des promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_posture:

Ajuster la posture
=====================

Dans cet exemple, nous utilisons le clavier pour contrôler le PiCrawler, pied par pied, et adopter la posture souhaitée.

Vous pouvez appuyer sur la barre d'espace pour afficher les valeurs de coordonnées actuelles. Ces valeurs sont utiles lorsque vous créez des actions uniques pour le PiCrawler.

.. image:: img/1cood.A.png

**Exécuter le code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 do_single_leg.py

Après avoir exécuté le code, veuillez suivre les instructions qui apparaîtront dans le terminal.

* Appuyez sur ``1234`` pour sélectionner chaque patte séparément, ``1`` : patte avant droite, ``2`` : patte avant gauche, ``3`` : patte arrière gauche, ``4`` : patte arrière droite
* Appuyez sur ``w``, ``a``, ``s``, ``d``, ``r`` et ``f`` pour contrôler lentement les valeurs de coordonnées du PiCrawler.
* Appuyez sur ``Ctrl+C`` pour quitter.


**Code**

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep
    import readchar

    crawler = Picrawler()
    speed = 80


    manual = '''
    -------- PiCrawler Controller --------- 
           .......          .......
        <=|   2   |┌-┌┐┌┐-┐|   1   |=>
           ``````` ├      ┤ ```````
           ....... ├      ┤ .......
        <=|   3   |└------┘|   4   |=>
           ```````          ```````
        1: Select right front leg
        2: Select left front leg
        3: Select left rear leg
        4: Select right rear leg

        W: Y++          R: Z++             
        A: X--          F: Z-- 
        S: Y--  
        D: X++          Ctrl+C: Quit
    '''
    legs_list = ['right front', 'left front', 'left rear', 'right rear']

    def main():  
        leg = 0
        speed = 80
        step = 2
        print(manual)
        crawler.do_step('stand', speed)
        sleep(0.2)
        coordinate=crawler.current_step_all_leg_value()  

        def show_info():
            print("\033[H\033[J", end='')  # Effacer la fenêtre du terminal
            print(manual)   
            print('%s : %s'%(leg+1, legs_list[leg])) 
            print('coordinate: %s'%(coordinate))  

        show_info()

        while True:
            # lire la touche
            key = readchar.readkey()
            key = key.lower()
            # sélectionner la patte 
            if key in ('1234'):
                leg = int(key) - 1
                show_info()
            # mouvement
            elif key in ('wsadrf'):         
                if 'w' == key:
                    coordinate[leg][1]=coordinate[leg][1] + step    
                elif 's' == key:
                    coordinate[leg][1]=coordinate[leg][1] - step           
                elif 'a' == key:
                    coordinate[leg][0]=coordinate[leg][0] - step         
                elif 'd' == key:
                    coordinate[leg][0]=coordinate[leg][0] + step   
                elif 'r' == key:
                    coordinate[leg][2]=coordinate[leg][2] + step         
                elif 'f' == key:
                    coordinate[leg][2]=coordinate[leg][2] - step 

                crawler.do_single_leg(leg,coordinate[leg],speed) 
                sleep(0.1)  
                # coordinate = crawler.current_step_all_leg_value()
                show_info()

            sleep(0.05)

    
    if __name__ == "__main__": 
        main()

* ``current_step_all_leg_value()`` : Retourne les valeurs des coordonnées de toutes les pattes.
* ``do_single_leg(leg, coordinate[leg], speed)`` : Modifie les coordonnées d'une patte spécifique.
