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

Au démarrage du programme, le PiCrawler s’initialise et une interface de contrôle au clavier
s’affiche dans le terminal.

Appuyez sur les touches du clavier pour contrôler le PiCrawler !

* ``w`` : Avancer
* ``a`` : Tourner à gauche
* ``s`` : Reculer
* ``d`` : Tourner à droite
* ``Ctrl+C`` : Quitter

La vitesse actuelle est affichée et peut être ajustée avec :

- + / ] pour augmenter la vitesse
- - / [ pour diminuer la vitesse

Après chaque action, un court délai est appliqué pour améliorer la stabilité.

Appuyez sur Ctrl+C pour quitter.
Avant de s’arrêter, le PiCrawler exécute une action « sit » (assise) en toute sécurité.

**Code**

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep
    import readchar

    crawler = Picrawler()

    SPEED_MIN = 20
    SPEED_MAX = 70
    speed = 60

    STEP = 1            # Number of action steps per key press
    ACTION_GAP = 0.25   # Delay after each action to reduce current spikes

    manual = """
    Keyboard Control - PiCrawler

    Movement:
    W: Forward
    A: Turn left
    S: Backward
    D: Turn right

    Speed Control:
    + / ] : Increase speed
    - / [ : Decrease speed

    Other:
    Space  : Stop (no action)
    Ctrl+C : Quit (auto sit)
    """

    def clamp(value, min_value, max_value):
        """Limit value within a specified range."""
        return max(min_value, min(max_value, value))

    def show_info():
        """Clear terminal and display control instructions."""
        print("\033[H\033[J", end="")  # Clear terminal screen
        print(manual)
        print(f"Current speed: {speed}  (range {SPEED_MIN}-{SPEED_MAX})")
        print(f"Action gap: {ACTION_GAP:.2f}s")

    def do_move(action_name):
        """Execute movement action with safety delay."""
        crawler.do_action(action_name, STEP, speed)
        sleep(ACTION_GAP)

    def safe_sit():
        """Safely sit down before program exit."""
        try:
            crawler.do_step("sit", clamp(speed, 20, 40))
            sleep(1.0)
        except Exception:
            pass

    def main():
        show_info()

        try:
            while True:
                key = readchar.readkey()
                k = key.lower()

                if k == "w":
                    do_move("forward")
                elif k == "s":
                    do_move("backward")
                elif k == "a":
                    do_move("turn left")
                elif k == "d":
                    do_move("turn right")

                # Speed increase
                elif k in ("+", "]"):
                    global speed
                    speed = clamp(speed + 5, SPEED_MIN, SPEED_MAX)

                # Speed decrease
                elif k in ("-", "["):
                    speed = clamp(speed - 5, SPEED_MIN, SPEED_MAX)

                # Stop (no movement)
                elif k == " ":
                    pass

                # Quit using readchar special key
                elif key == readchar.key.CTRL_C:
                    print("\nQuit.")
                    break

                show_info()
                sleep(0.02)

        except KeyboardInterrupt:
            print("\nQuit (KeyboardInterrupt).")

        finally:
            safe_sit()

    if __name__ == "__main__":
        main()

**Comment cela fonctionne ?**

#. Création de l’objet robot

   .. code-block:: python

      crawler = Picrawler()

   Cette ligne crée un objet ``Picrawler``.
   Il permet au programme de contrôler les mouvements du robot.

#. Définition d’une plage de vitesse sûre

   .. code-block:: python

      SPEED_MIN = 20
      SPEED_MAX = 70
      speed = 60

   Ces variables définissent la plage de vitesse autorisée.
   ``speed`` stocke la vitesse de déplacement actuelle.
   Le robot ne se déplacera pas plus vite que la valeur maximale.

#. Limitation de la vitesse avec clamp()

   .. code-block:: python

      def clamp(value, min_value, max_value):
          return max(min_value, min(max_value, value))

   Cette fonction garantit que la vitesse reste dans une plage sûre.
   Elle empêche les mouvements instables causés par des valeurs extrêmes.

#. Exécution d’un mouvement

   .. code-block:: python

      def do_move(action_name):
          crawler.do_action(action_name, STEP, speed)
          sleep(ACTION_GAP)

   Cette fonction envoie une commande de mouvement au robot.
   ``ACTION_GAP`` ajoute un court délai afin d’améliorer la stabilité.

#. Lecture de l’entrée clavier

   .. code-block:: python

      key = readchar.readkey()
      k = key.lower()

   Le programme attend qu’une touche soit pressée.
   La touche est convertie en minuscule pour assurer la cohérence.

#. Logique de contrôle du mouvement

   .. code-block:: python

      if k == "w":
          do_move("forward")
      elif k == "s":
          do_move("backward")

   Lorsqu’une touche est pressée, le mouvement correspondant est exécuté immédiatement.
   Il n’est pas nécessaire d’appuyer sur Entrée.

#. Sortie sécurisée

   .. code-block:: python

      finally:
          safe_sit()

   Avant la fin du programme, le robot exécute une action « sit » sécurisée.
   Cela évite une posture instable ou un arrêt brutal.