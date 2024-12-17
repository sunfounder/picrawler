.. note:: 

    Bonjour, bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et obtenez des aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et à des promotions pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_keyboard:

Contrôle au clavier
=======================

Dans ce projet, nous allons apprendre à utiliser le clavier pour contrôler à distance le PiCrawler. Vous pourrez commander le PiCrawler pour avancer, reculer, tourner à gauche et à droite.

**Exécuter le code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 keyboard_control.py

Appuyez sur les touches du clavier pour contrôler PiCrawler !

* ``w`` : Avancer
* ``a`` : Tourner à gauche
* ``s`` : Reculer
* ``d`` : Tourner à droite
* ``Ctrl+C`` : Quitter

**Code**

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep
    import readchar

    crawler = Picrawler() 
    speed = 90

    manual = '''
    Press keys on keyboard to control PiCrawler!
        W: Forward
        A: Turn left
        S: Backward
        D: Turn right

        Ctrl^C: Quit
    '''

    def show_info():
        print("\033[H\033[J",end='')  # effacer l'écran du terminal 
        print(manual)


    def main(): 
        show_info()   
        while True:
            key = readchar.readkey()
            key = key.lower()
            if key in('wsad'):
                if 'w' == key:
                    crawler.do_action('forward',1,speed)     
                elif 's' == key:
                    crawler.do_action('backward',1,speed)          
                elif 'a' == key:
                    crawler.do_action('turn left',1,speed)           
                elif 'd' == key:
                    crawler.do_action('turn right',1,speed)
                sleep(0.05)
                show_info()  
            elif key == readchar.key.CTRL_C:
                print("\n Quit") 
                break    

            sleep(0.02)          

    
    if __name__ == "__main__":
        main()

**Comment ça fonctionne ?**

PiCrawler doit effectuer l'action appropriée en fonction des caractères du clavier lus. La fonction ``lower()`` convertit les caractères majuscules en minuscules, de sorte que la touche reste valide indépendamment de la casse.

.. code-block:: python

    def main(): 
        show_info()   
        while True:
            key = readchar.readkey()
            key = key.lower()
            if key in('wsad'):
                if 'w' == key:
                    crawler.do_action('forward',1,speed)     
                elif 's' == key:
                    crawler.do_action('backward',1,speed)          
                elif 'a' == key:
                    crawler.do_action('turn left',1,speed)           
                elif 'd' == key:
                    crawler.do_action('turn right',1,speed)
                sleep(0.05)
                show_info()  
            elif key == readchar.key.CTRL_C:
                print("\n Quit") 
                break    
            
            sleep(0.02)  
