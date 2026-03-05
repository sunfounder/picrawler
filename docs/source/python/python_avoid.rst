.. note:: 

    Bonjour, bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 sur Facebook ! Explorez plus en profondeur l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et obtenez des aperçus exclusifs.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions et concours festifs** : Participez à des concours et des promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_avoid:

Évitement d'Obstacle
=========================

Dans ce projet, PiCrawler utilise un module ultrasonique pour détecter les obstacles 
devant lui. Lorsque PiCrawler détecte un obstacle, il envoie un signal et cherche une 
autre direction pour continuer à avancer.

.. .. image:: img/avoid1.png

**Exécuter le Code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 avoid.py

Au démarrage du programme, le PiCrawler se met debout.

Il mesure en continu la distance à l’aide du capteur ultrasonique
et affiche la valeur dans le terminal.

Si un obstacle est détecté à moins de 15 cm :
- Un son d’avertissement est joué.
- Le robot effectue un petit virage à gauche.

Si le chemin est dégagé :
- Le robot avance.

Le robot continue d’éviter les obstacles automatiquement jusqu’à ce que vous appuyiez sur Ctrl+C.

Avant de quitter, il se rassoit en toute sécurité.

**Code**

.. note::
    Vous pouvez **Modifier/Réinitialiser/Copier/Exécuter/Arrêter** le code ci-dessous. Mais avant cela, vous devez vous rendre dans le répertoire du code source, tel que ``picrawler\examples``. Après avoir modifié le code, vous pouvez l'exécuter directement pour voir l'effet.

.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from robot_hat import Music, Ultrasonic, Pin
    import time
    import signal

    music = Music()
    crawler = Picrawler()
    sonar = Ultrasonic(Pin("D2"), Pin("D3"))  # Ultrasonic trigger/echo pins

    music.music_set_volume(100)  # Set speaker volume

    alert_distance = 15  # Obstacle warning distance (cm)
    speed = 80           # Movement speed

    # ----------------------------
    # Add hardware timeout to sonar.read()
    # Prevent program from freezing
    # ----------------------------
    class Timeout(Exception):
        pass

    def _alarm_handler(signum, frame):
        raise Timeout()

    signal.signal(signal.SIGALRM, _alarm_handler)

    # Read distance once with timeout protection
    def safe_read_once(timeout_s=1):
        try:
            signal.alarm(timeout_s)
            d = sonar.read()
            signal.alarm(0)
            return d
        except Timeout:
            signal.alarm(0)
            return None
        except Exception:
            signal.alarm(0)
            return None

    # Read multiple times and return median value (anti-noise)
    def read_distance_filtered(n=5, gap=0.03, timeout_s=1):
        vals = []
        for _ in range(n):
            d = safe_read_once(timeout_s=timeout_s)
            if d is not None and d > 0:
                vals.append(d)
            time.sleep(gap)

        if not vals:
            return None

        vals.sort()
        return vals[len(vals)//2]  # Median filter

    def main():
        distance = read_distance_filtered(n=5, gap=0.03, timeout_s=1)
        print("distance:", distance)

        if distance is None:
            time.sleep(0.15)  # Wait if read failed
            return

        if distance <= alert_distance:
            # Obstacle detected → play sound and turn
            try:
                music.sound_play_threading('./sounds/sign.wav', volume=100)
            except Exception as e:
                print("sound error:", e)

            crawler.do_action('turn left angle', 1, speed)
            time.sleep(0.5)  # Quiet window after movement
        else:
            # Path clear → move forward
            crawler.do_action('forward', 1, speed)
            time.sleep(0.4)

    if __name__ == "__main__":
        try:
            crawler.do_step('stand', 40)  # Stand before starting
            time.sleep(1.0)

            while True:
                main()

        except KeyboardInterrupt:
            print("\nStop.")
        finally:
            try:
                crawler.do_step('sit', 40)  # Sit before exit
                time.sleep(1.0)
            except Exception:
                pass

**Comment ça fonctionne ?**

#. Bloc d'initialisation

   .. code-block:: python

      music = Music()
      crawler = Picrawler()
      sonar = Ultrasonic(Pin("D2"), Pin("D3"))

      music.music_set_volume(100)
      alert_distance = 15
      speed = 80

   Ce bloc initialise les trois modules principaux :
   - ``music`` : contrôle la lecture du son.
   - ``crawler`` : contrôle les mouvements du PiCrawler.
   - ``sonar`` : lit la distance à l’aide du capteur ultrasonique.

   Il définit également le volume du haut-parleur, le seuil de détection d’obstacle (en cm)
   et la vitesse de déplacement.

#. Bloc de configuration du timeout (empêche ``sonar.read()`` de se bloquer)

   .. code-block:: python

      class Timeout(Exception):
          pass

      def _alarm_handler(signum, frame):
          raise Timeout()

      signal.signal(signal.SIGALRM, _alarm_handler)

   Le pilote du capteur ultrasonique peut se bloquer en attendant le signal d’écho.
   Ce bloc installe un gestionnaire de signal afin que le programme puisse interrompre
   un appel ``sonar.read()`` bloqué et continuer à fonctionner.

#. Fonction : safe_read_once()

   .. code-block:: python

      def safe_read_once(timeout_s=1):
          try:
              signal.alarm(timeout_s)
              d = sonar.read()
              signal.alarm(0)
              return d
          except Timeout:
              signal.alarm(0)
              return None
          except Exception:
              signal.alarm(0)
              return None

   Cette fonction lit une fois la distance ultrasonique avec une protection de timeout.
   - Si la lecture réussit, elle renvoie la valeur de distance.
   - Si un timeout se produit ou si une erreur survient, elle renvoie ``None`` au lieu de bloquer le programme.

#. Fonction : read_distance_filtered()

   .. code-block:: python

      def read_distance_filtered(n=5, gap=0.03, timeout_s=1):
          vals = []
          for _ in range(n):
              d = safe_read_once(timeout_s=timeout_s)
              if d is not None and d > 0:
                  vals.append(d)
              time.sleep(gap)

          if not vals:
              return None

          vals.sort()
          return vals[len(vals)//2]

   Cette fonction améliore la fiabilité en lisant plusieurs échantillons :
   - Les valeurs invalides (``None`` ou ``<= 0``) sont ignorées.
   - Les valeurs restantes sont triées.
   - La valeur médiane est renvoyée afin de réduire le bruit des mesures.

#. Fonction : main() (décision principale et action)

   .. code-block:: python

      def main():
          distance = read_distance_filtered(...)
          if distance is None:
              return

          if distance <= alert_distance:
              music.sound_play_threading(...)
              crawler.do_action('turn left angle', 1, speed)
          else:
              crawler.do_action('forward', 1, speed)

   Voici la logique principale de contrôle :

   - Lit une valeur de distance filtrée.
   - Si la lecture échoue, ce cycle est ignoré.
   - Si un obstacle est plus proche que ``alert_distance``, le robot joue un son d’avertissement et tourne à gauche.
   - Sinon, il avance.

#. Bloc d’entrée du programme (boucle continue + arrêt sécurisé)

   .. code-block:: python

      if __name__ == "__main__":
          try:
              crawler.do_step('stand', 40)
              while True:
                  main()
          except KeyboardInterrupt:
              print("\nStop.")
          finally:
              crawler.do_step('sit', 40)

   Ce bloc contrôle le flux global du programme :
   - Le robot se met debout avant de commencer.
   - Le programme exécute ``main()`` en boucle infinie.
   - Appuyer sur Ctrl+C arrête la boucle.
   - Le robot se remet en position assise avant la fin du programme.