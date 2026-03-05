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
    from time import sleep, time
    from robot_hat import Music
    from vilib import Vilib

    # Create robot and audio controller objects
    crawler = Picrawler()
    music = Music()

    def main():
        # Start camera and enable preview window
        Vilib.camera_start(vflip=False, hflip=False)
        Vilib.display(local=False, web=True)

        # Enable red color detection
        Vilib.color_detect("red")

        speed = 80                  # Movement speed
        last_seen = False           # Indicates whether the red target was detected in previous loop
        last_beep = 0               # Timestamp of last sound playback
        BEEP_COOLDOWN = 1.0         # Minimum interval between sound effects (seconds)

        # Stand once before starting tracking
        crawler.do_step('stand', 40)
        sleep(1.0)

        try:
            while True:
                # Read detection result
                if Vilib.detect_obj_parameter.get('color_n', 0) != 0:

                    # Get horizontal coordinate of detected red object
                    coordinate_x = Vilib.detect_obj_parameter.get('color_x', 0)

                    # Play sound effect with cooldown to avoid spamming
                    now = time()
                    if now - last_beep >= BEEP_COOLDOWN:
                        try:
                            music.sound_play_threading('./sounds/talk1.wav')
                        except Exception:
                            pass
                        last_beep = now

                    # Steering logic based on horizontal position
                    # Left side of image
                    if coordinate_x < 100:
                        crawler.do_action('turn left', 1, speed)

                    # Right side of image
                    elif coordinate_x > 220:
                        crawler.do_action('turn right', 1, speed)

                    # Center area → move forward
                    else:
                        crawler.do_action('forward', 2, speed)

                    last_seen = True
                    sleep(0.05)

                else:
                    # No red target detected

                    # Stop movement only once when target is lost
                    # This prevents repeated stand() calls that cause "push-up" effect
                    if last_seen:
                        crawler.do_step('stand', 40)
                        last_seen = False

                    sleep(0.15)

        except KeyboardInterrupt:
            # Stop program safely when Ctrl+C is pressed
            print("\nStop.")

        finally:
            # Cleanup section to avoid exit errors

            # Disable color detection
            try:
                Vilib.color_detect("close")
            except Exception:
                pass

            # Close camera safely
            try:
                Vilib.camera_close()
            except Exception:
                pass

            # Make the robot sit before exit
            try:
                crawler.do_step('sit', 40)
                sleep(1.0)
            except Exception:
                pass

    if __name__ == "__main__":
        main()



**Comment ça fonctionne ?**

#. Initialisation de la caméra

   .. code-block:: python

      Vilib.camera_start(vflip=False, hflip=False)
      Vilib.display(local=False, web=True)
      Vilib.color_detect("red")

   La caméra est démarrée et l’aperçu web est activé.
   La détection de la couleur rouge est activée.
   Vilib traite continuellement les images en arrière-plan
   et stocke les résultats de détection dans ``detect_obj_parameter``.

#. Préparation du robot

   .. code-block:: python

      crawler.do_step('stand', 40)
      sleep(1.0)

   Le robot exécute une action de mise en position debout avant de commencer le suivi.
   Un court délai garantit que la posture est stable.

#. Détection de la cible

   .. code-block:: python

      if Vilib.detect_obj_parameter.get('color_n', 0) != 0:
          coordinate_x = Vilib.detect_obj_parameter.get('color_x', 0)

   Le programme vérifie si un objet rouge est détecté.
   Si c’est le cas, il lit la coordonnée horizontale centrale (position x)
   de l’objet rouge dans l’image.

#. Logique de décision de direction

   .. code-block:: python

      if coordinate_x < 100:
          crawler.do_action('turn left', 1, speed)
      elif coordinate_x > 220:
          crawler.do_action('turn right', 1, speed)
      else:
          crawler.do_action('forward', 2, speed)

   L’image est divisée en trois zones horizontales :
   gauche, centre et droite.

   • Zone gauche → tourner à gauche  
   • Zone droite → tourner à droite  
   • Zone centrale → avancer  

   Cela permet au robot de suivre l’objet rouge.

#. Mécanisme de temporisation du son

   .. code-block:: python

      now = time()
      if now - last_beep >= BEEP_COOLDOWN:
          music.sound_play_threading('./sounds/talk1.wav')
          last_beep = now

   Un minuteur empêche la lecture répétée du son.
   L’effet sonore est joué au maximum une fois par seconde,
   même si l’objet reste détecté.

#. Gestion de la perte de la cible

   .. code-block:: python

      if last_seen:
          crawler.do_step('stand', 40)
          last_seen = False

   Lorsque l’objet rouge disparaît,
   le robot s’arrête et revient à une position debout stable.

   Le drapeau ``last_seen`` garantit que ``stand()`` est appelé une seule fois.
   Cela évite une réinitialisation répétée de la posture qui pourrait provoquer des tremblements.

#. Sortie sécurisée et nettoyage

   .. code-block:: python

      finally:
          Vilib.color_detect("close")
          Vilib.camera_close()
          crawler.do_step('sit', 40)

   Lorsque le programme se termine (par exemple avec Ctrl+C),
   la détection de couleur est désactivée,
   la caméra est fermée correctement,
   et le robot exécute une action de position assise.

   Cela évite les erreurs de caméra et les arrêts instables du programme.

