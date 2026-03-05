.. note:: 

    Bonjour, bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 sur Facebook ! Explorez plus en profondeur l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes post-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et d'aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_treasure:

Chasse au Trésor
============================

Aménagez un labyrinthe dans votre pièce et placez six cartes de couleur différentes dans six coins. Ensuite, contrôlez PiCrawler pour rechercher ces cartes de couleur une par une !

.. note:: Vous pouvez télécharger et imprimer les :download:`cartes de couleur PDF <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>` pour la détection des couleurs.

**Exécuter le Code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 treasure_hunt.py


**Affichage de l'Image**

Après l'exécution du code, le terminal affichera l'invite suivante :

.. code-block::

    No desktop !
    * Serving Flask app "vilib.vilib" (lazy loading)
    * Environment: production
    WARNING: Do not use the development server in a production environment.
    Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)

Vous pouvez alors entrer ``http://<votre IP>:9000/mjpg`` dans le navigateur pour afficher l'écran vidéo. Par exemple : ``http://192.168.18.113:9000/mjpg``

.. image:: img/display.png

**Code**

.. code-block:: python

	#!/usr/bin/env python3
	from picrawler import Picrawler
	from time import sleep, time
	from robot_hat import Music, TTS
	from vilib import Vilib
	import readchar
	import random
	import threading

	crawler = Picrawler()
	music = Music()   # kept for compatibility (not used here)
	tts = TTS()

	MANUAL = '''
	Press keys on keyboard to control Picrawler!
		w: Forward
		a: Turn left
		s: Backward
		d: Turn right
		space: Say the target again
		Ctrl+C: Quit
	'''

	color = "red"
	color_list = ["red", "orange", "yellow", "green", "blue", "purple"]

	key_dict = {
		'w': 'forward',
		's': 'backward',
		'a': 'turn_left',
		'd': 'turn_right',
	}

	# ----------------------------
	# Thread-safe key handling
	# ----------------------------
	lock = threading.Lock()
	key_state = None               # last key event
	stop_event = threading.Event() # signal to exit cleanly

	def set_key(k):
		global key_state
		with lock:
			key_state = k

	def pop_key():
		"""Read and clear the last key event."""
		global key_state
		with lock:
			k = key_state
			key_state = None
		return k

	def key_scan_thread():
		"""Keyboard input thread (quiet exit on Ctrl+C)."""
		while not stop_event.is_set():
			try:
				k = readchar.readkey()
			except KeyboardInterrupt:
				# Ctrl+C may raise KeyboardInterrupt inside this thread
				stop_event.set()
				break
			except Exception:
				sleep(0.02)
				continue

			if k == readchar.key.SPACE:
				set_key('space')
			elif k == readchar.key.CTRL_C:
				set_key('quit')
				stop_event.set()
				break
			else:
				try:
					set_key(str(k).lower())
				except Exception:
					pass

			sleep(0.01)

	# ----------------------------
	# Game logic
	# ----------------------------
	def renew_color_detect():
		global color
		color = random.choice(color_list)
		try:
			Vilib.color_detect(color)
		except Exception:
			pass
		try:
			tts.say("Look for " + color)
		except Exception:
			pass

	def safe_camera_close():
		try:
			Vilib.color_detect("close")
		except Exception:
			pass
		try:
			Vilib.camera_close()
		except Exception:
			pass

	def safe_sit():
		try:
			crawler.do_step('sit', 40)
			sleep(0.5)
		except Exception:
			pass

	def stand_ready():
		"""
		Stand up after startup.
		Requirement: stand at 40, then only move after WASD is pressed.
		"""
		try:
			crawler.do_step('stand', 40)
			sleep(0.8)
		except Exception:
			pass

	def main():
		speed = 80
		action = None

		# Start camera + web preview
		Vilib.camera_start(vflip=False, hflip=False)
		Vilib.display(local=False, web=True)
		sleep(0.8)

		print(MANUAL)

		# Start keyboard thread (daemon, so it won't block process exit)
		t = threading.Thread(target=key_scan_thread, daemon=True)
		t.start()

		# Announce and stand up to 40
		try:
			tts.say("game start")
		except Exception:
			pass
		sleep(0.05)

		stand_ready()
		renew_color_detect()

		try:
			while not stop_event.is_set():
				# If target detected and large enough -> renew target
				try:
					n = Vilib.detect_obj_parameter.get('color_n', 0)
					w = Vilib.detect_obj_parameter.get('color_w', 0)
				except Exception:
					n, w = 0, 0

				if n != 0 and w > 100:
					try:
						tts.say("well done")
					except Exception:
						pass
					sleep(0.05)
					renew_color_detect()

				# Handle key event
				k = pop_key()

				if k in key_dict:
					action = key_dict[k]

				elif k == 'space':
					try:
						tts.say("Look for " + color)
					except Exception:
						pass

				elif k == 'quit':
					stop_event.set()

				# Move only after receiving a WASD action
				if action is not None:
					try:
						crawler.do_action(action, 1, speed)
					except Exception:
						pass
					action = None

				sleep(0.05)

		except KeyboardInterrupt:
			stop_event.set()

		finally:
			# Clean exit
			stop_event.set()
			safe_camera_close()
			safe_sit()
			print("\nQuit")

	if __name__ == "__main__":
		main()

**Comment ça fonctionne ?**

#. Ce que fait ce programme

   Ce programme est un petit jeu de « chasse au trésor » pour PiCrawler :

   • La caméra diffuse le flux vidéo vers une page web (sans fenêtre GUI locale).  
   • Vilib détecte une couleur cible (red/orange/yellow/green/blue/purple).  
   • Vous contrôlez le robot avec les touches WASD.  
   • Lorsque l’objet de la couleur détectée est suffisamment grand, le programme annonce la réussite
     et passe à une nouvelle couleur cible.  
   • Le programme se termine proprement avec Ctrl+C sans afficher d’erreur de thread.

#. L’entrée clavier s’exécute dans un thread en arrière-plan

   .. code-block:: python

      stop_event = threading.Event()
      key_state = None

      def key_scan_thread():
          while not stop_event.is_set():
              try:
                  k = readchar.readkey()
              except KeyboardInterrupt:
                  stop_event.set()
                  break

   La lecture du clavier est séparée dans son propre thread.
   Cela évite que la boucle principale se bloque en attendant une touche.

   Ctrl+C peut déclencher KeyboardInterrupt dans ce thread (comportement de readchar),
   donc l’exception est interceptée pour déclencher une sortie propre
   au lieu d’afficher une erreur.

#. Les événements clavier sont partagés en toute sécurité

   .. code-block:: python

      lock = threading.Lock()

      def set_key(k):
          global key_state
          with lock:
              key_state = k

      def pop_key():
          global key_state
          with lock:
              k = key_state
              key_state = None
          return k

   Le programme utilise un verrou (lock) pour protéger la variable partagée ``key_state``.
   Le thread clavier écrit les événements avec ``set_key()``.
   La boucle principale lit et efface les événements avec ``pop_key()``.

   Cela garantit que le robot réagit correctement aux touches
   sans provoquer de conflits entre threads.

#. Caméra et aperçu web

   .. code-block:: python

      Vilib.camera_start(vflip=False, hflip=False)
      Vilib.display(local=False, web=True)

   La caméra est démarrée et l’aperçu web est activé.
   ``local=False`` évite les plantages GUI sur les systèmes
   qui n’ont pas d’environnement graphique.

#. Se mettre debout d’abord, puis attendre les touches de déplacement

   .. code-block:: python

      crawler.do_step('stand', 40)
      sleep(0.8)

   Au démarrage, le robot se met debout à la vitesse 40
   afin de stabiliser sa posture.

   Le programme ne déplace pas le robot automatiquement.
   Il ne bouge que lorsqu’une touche WASD est pressée.

#. Sélection d’une couleur cible

   .. code-block:: python

      color = random.choice(COLOR_LIST)
      Vilib.color_detect(color)
      tts.say("Look for " + color)

   Une couleur aléatoire est choisie dans la liste.
   La détection de couleur de Vilib est activée pour cette couleur.

   La synthèse vocale (TTS) annonce la cible actuelle
   afin que l’utilisateur sache quelle couleur chercher.

#. Détection du « succès » et changement de cible

   .. code-block:: python

      n = Vilib.detect_obj_parameter.get('color_n', 0)
      w = Vilib.detect_obj_parameter.get('color_w', 0)

      if n != 0 and w > 100:
          tts.say("well done")
          renew_color_detect()

   Vilib met à jour ``detect_obj_parameter`` en continu.

   • ``color_n`` indique si une cible est détectée  
   • ``color_w`` représente la largeur de la cible détectée
     (une estimation de sa taille ou de sa proximité)

   Lorsque la cible est détectée et suffisamment grande,
   le programme annonce la réussite
   puis sélectionne immédiatement une nouvelle couleur cible.

#. Contrôle du mouvement avec WASD

   .. code-block:: python

      if k in key_dict:
          action = key_dict[k]

      if action is not None:
          crawler.do_action(action, 1, speed)
          action = None

   La boucle principale vérifie les événements clavier :

   • w → avancer  
   • s → reculer  
   • a → tourner à gauche  
   • d → tourner à droite  

   Lorsqu’une touche de déplacement est reçue,
   le robot exécute une courte action.

   Cette conception garde le contrôle réactif
   et évite un mouvement continu incontrôlé.

#. Touche espace : répéter la consigne

   .. code-block:: python

      elif k == 'space':
          tts.say("Look for " + color)

   Appuyer sur la touche espace répète le message
   indiquant la couleur cible actuelle.

   Cela est utile si l’utilisateur a oublié la couleur à rechercher.

#. Quitter et nettoyage

   .. code-block:: python

      finally:
          stop_event.set()
          Vilib.color_detect("close")
          Vilib.camera_close()
          crawler.do_step('sit', 40)

   Lors de la fermeture du programme :

   • ``stop_event`` indique au thread clavier de s’arrêter.  
   • La détection de couleur de Vilib est désactivée.  
   • La caméra est fermée proprement.  
   • Le robot se met en position assise pour éviter une posture instable.

   Cet ordre de nettoyage aide à éviter les erreurs liées à la caméra
   et garantit que le robot termine dans une position sûre.
