.. note:: 

    Bonjour, bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 sur Facebook ! Explorez plus en profondeur l'univers de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes post-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et d'aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_record:

Enregistrer un Nouveau Pas
================================

Nous utilisons le clavier pour contrôler le PiCrawler afin de réaliser plusieurs poses successivement et d'enregistrer ces poses pour les rejouer ensuite.

**Exécuter le Code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 record_new_step_by_keyboard.py

Une fois le code exécuté, veuillez suivre les instructions affichées dans le terminal.

* Appuyez sur ``1234`` pour sélectionner les pieds séparément : ``1`` : pied avant droit, ``2`` : pied avant gauche, ``3`` : pied arrière gauche, ``4`` : pied arrière droit.
* Appuyez sur ``w``, ``a``, ``s``, ``d``, ``r`` et ``f`` pour contrôler lentement les valeurs de coordonnées du PiCrawler.
* Appuyez sur ``espace`` pour afficher toutes les valeurs des coordonnées.
* Appuyez sur ``p`` pour faire rejouer l'action enregistrée.
* Appuyez sur ``esc`` pour quitter.

**Code**

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep
    import sys
    import tty
    import termios
    import copy

    crawler = Picrawler() 
    speed = 80

    def readchar():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


    manual = '''
    Press keys on keyboard to control!
        w: Y++
        a: X--
        s: Y--
        d: X++
        r: Z++
        f: Z--
        1: Select right front leg
        2: Select left front leg
        3: Select left rear leg
        4: Select right rear leg
        Space: Print all leg coodinate & Save this step
        p: Play all saved step
        esc: Quit
    '''


    new_step=[]

    def save_new_step():
        new_step.append(copy.deepcopy(crawler.current_step_all_leg_value()))
        print(new_step)

    def play_all_new_step():
        for step in new_step:
            crawler.do_step(step,speed)
            sleep(0.6)

    def main():  

        speed = 80
        print(manual)
        crawler.do_step('sit',speed)
        leg = 0 
        coodinate=crawler.current_step_leg_value(leg)   
        while True:
            key = readchar()
            key = key.lower()
            # print(key)
            if 'w' == key:
                coodinate[1]=coodinate[1]+2    
            elif 's' == key:
                coodinate[1]=coodinate[1]-2           
            elif 'a' == key:
                coodinate[0]=coodinate[0]-2         
            elif 'd' == key:
                coodinate[0]=coodinate[0]+2   
            elif 'r' == key:
                coodinate[2]=coodinate[2]+2         
            elif 'f' == key:
                coodinate[2]=coodinate[2]-2       
            elif '1' == key:
                leg=0
                coodinate=crawler.current_step_leg_value(leg)           
            elif '2' == key:
                leg=1   
                coodinate=crawler.current_step_leg_value(leg)              
            elif '3' == key:
                leg=2  
                coodinate=crawler.current_step_leg_value(leg)     
            elif '4' == key:
                leg=3     
                coodinate=crawler.current_step_leg_value(leg)  
            elif chr(32) == key:
                print("[[right front],[left front],[left rear],[right rear]]")
                print("saved new step")
                print(crawler.current_step_all_leg_value())
                save_new_step()
            elif 'p' == key:
                play_all_new_step()
            elif chr(27) == key:  # 27 pour ESC
                break    

            sleep(0.05)
            crawler.do_single_leg(leg,coodinate,speed)          
        print("\n q Quit")  

    
    if __name__ == "__main__":
        main()

**Comment ça fonctionne ?**

Ce projet est né du :ref:`py_posture`. Il a ajouté des fonctions d'enregistrement et de lecture.

La fonction d'enregistrement est implémentée par le code suivant.

.. code-block:: python

    new_step=[]

    def save_new_step():
        new_step.append(copy.deepcopy(crawler.current_step_all_leg_value()))
        print(new_step)

.. note:: 
    L'assignation ici doit utiliser la fonction `Deep Copy <https://docs.python.org/3/library/copy.html>`_ , sinon ``new_step`` ne recevra pas un nouvel objet de type tableau lors de l'ajout.

La fonction de lecture est implémentée par le code suivant.

.. code-block:: python

    def play_all_new_step():
        for step in new_step:
            crawler.do_step(step,speed)
            sleep(0.6)