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

    #!/usr/bin/env python3
    from picrawler import Picrawler
    from time import sleep
    import readchar

    crawler = Picrawler()

    SPEED = 80
    STEP_SIZE = 2

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

    # Axis mapping for cleaner logic
    move_map = {
        'w': (1, +STEP_SIZE),  # Y++
        's': (1, -STEP_SIZE),  # Y--
        'a': (0, -STEP_SIZE),  # X--
        'd': (0, +STEP_SIZE),  # X++
        'r': (2, +STEP_SIZE),  # Z++
        'f': (2, -STEP_SIZE),  # Z--
    }


    def clear_screen():
        print("\033[H\033[J", end='')


    def show_info(selected_leg, coordinate):
        clear_screen()
        print(manual)
        print(f"Selected leg: {selected_leg + 1} - {legs_list[selected_leg]}")
        print(f"Coordinate: {coordinate}")


    def main():
        selected_leg = 0

        try:
            print(manual)

            # Stand up first
            crawler.do_step('stand', 40)
            sleep(0.5)

            # Get current coordinates
            coordinate = crawler.current_step_all_leg_value()
            show_info(selected_leg, coordinate)

            while True:
                key = readchar.readkey().lower()

                # Select leg
                if key in ('1', '2', '3', '4'):
                    selected_leg = int(key) - 1
                    show_info(selected_leg, coordinate)

                # Move selected leg
                elif key in move_map:
                    axis, delta = move_map[key]

                    # Update coordinate
                    coordinate[selected_leg][axis] += delta

                    # Send updated position
                    crawler.do_single_leg(selected_leg, coordinate[selected_leg], SPEED)
                    sleep(0.1)

                    show_info(selected_leg, coordinate)

                sleep(0.05)

        except KeyboardInterrupt:
            print("\nExiting safely...")

        finally:
            # Return to sitting position on exit
            try:
                crawler.do_step('sit', 40)
                sleep(1)
            except Exception:
                pass

            print("Robot is now sitting. Program ended.")


    if __name__ == "__main__":
        main()


* ``current_step_all_leg_value()`` : Retourne les valeurs des coordonnées de toutes les pattes.
* ``do_single_leg(leg, coordinate[leg], speed)`` : Modifie les coordonnées d'une patte spécifique.
