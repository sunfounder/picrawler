.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein und verbinden Sie sich mit anderen Technikbegeisterten.

    **Warum mitmachen?**

    - **Expertenunterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Einblicken.
    - **Exklusive Rabatte**: Genießen Sie besondere Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und saisonalen Angeboten teil.

    👉 Bereit, mit uns zu entdecken und zu schaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _py_treasure:

Schatzsuche
============================

Richten Sie ein Labyrinth in Ihrem Raum ein und platzieren Sie sechs verschiedene Farbkarte in den sechs Ecken. Steuern Sie dann PiCrawler, um diese Farbkarte nacheinander zu suchen!

.. note:: Sie können die :download:`PDF Farbkarte <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>` für die Farberkennung herunterladen und ausdrucken.

**Code ausführen**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 treasure_hunt.py


**Bild anzeigen**

Nachdem der Code ausgeführt wurde, wird im Terminal die folgende Aufforderung angezeigt:

.. code-block::

    No desktop !
    * Serving Flask app "vilib.vilib" (lazy loading)
    * Environment: production
    WARNING: Do not use the development server in a production environment.
    Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)

Nun können Sie ``http://<Ihre IP>:9000/mjpg`` im Browser eingeben, um das Video anzuzeigen, z. B. ``http://192.168.18.113:9000/mjpg``

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

**Wie funktioniert es?**

#. Was dieses Programm macht

   Dieses Programm ist ein einfaches „Schatzsuche“-Spiel für den PiCrawler:

   • Die Kamera streamt zu einer Webseite (kein lokales GUI-Fenster).  
   • Vilib erkennt eine Zielfarbe (rot/orange/gelb/grün/blau/lila).  
   • Sie steuern den Roboter mit WASD.  
   • Wenn das erkannte Farbobjekt groß genug ist, meldet das Programm Erfolg
     und wechselt zu einer neuen Zielfarbe.  
   • Das Programm beendet sich sauber mit Ctrl+C, ohne Thread-Fehlermeldungen.

#. Tastatureingaben laufen in einem Hintergrund-Thread

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

   Das Einlesen der Tastatur erfolgt in einem eigenen Thread.  
   Dadurch wird verhindert, dass die Hauptschleife blockiert,
   während sie auf eine Tasteneingabe wartet.

   Ctrl+C kann innerhalb dieses Threads ein KeyboardInterrupt auslösen
   (typisches Verhalten von readchar).  
   Deshalb wird der Fehler abgefangen und stattdessen ein sauberes Beenden ausgelöst.

#. Tastaturereignisse werden sicher geteilt

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

   Das Programm verwendet ein Lock, um die gemeinsame Variable ``key_state`` zu schützen.  
   Der Tastatur-Thread schreibt Tasteneingaben mit ``set_key()``.  
   Die Hauptschleife liest und löscht Ereignisse mit ``pop_key()``.

   Dadurch reagiert der Roboter sicher auf Tasteneingaben,
   ohne Race Conditions zu verursachen.

#. Kamera und Web-Vorschau

   .. code-block:: python

      Vilib.camera_start(vflip=False, hflip=False)
      Vilib.display(local=False, web=True)

   Die Kamera wird gestartet und die Web-Vorschau aktiviert.  
   ``local=False`` verhindert GUI-Abstürze auf Systemen ohne Desktop-Umgebung.

#. Zuerst aufstehen, dann auf Bewegungstasten warten

   .. code-block:: python

      crawler.do_step('stand', 40)
      sleep(0.8)

   Nach dem Start steht der Roboter mit Geschwindigkeit 40 auf,
   um eine stabile Haltung zu erreichen.  
   Das Programm bewegt den Roboter nicht automatisch.  
   Bewegungen erfolgen nur, wenn eine WASD-Taste gedrückt wird.

#. Auswahl einer Zielfarbe

   .. code-block:: python

      color = random.choice(COLOR_LIST)
      Vilib.color_detect(color)
      tts.say("Look for " + color)

   Eine zufällige Farbe wird aus der Liste ausgewählt.  
   Die Farberkennung von Vilib wird für diese Farbe aktiviert.  
   Die Text-to-Speech-Funktion kündigt das aktuelle Ziel an,
   damit der Benutzer weiß, wonach er suchen soll.

#. Erfolgserkennung und Wechsel des Ziels

   .. code-block:: python

      n = Vilib.detect_obj_parameter.get('color_n', 0)
      w = Vilib.detect_obj_parameter.get('color_w', 0)

      if n != 0 and w > 100:
          tts.say("well done")
          renew_color_detect()

   Vilib aktualisiert ``detect_obj_parameter`` kontinuierlich.

   • ``color_n`` zeigt an, ob ein Ziel erkannt wurde  
   • ``color_w`` ist die Breite des erkannten Ziels (ein grobes Maß für Nähe oder Größe)

   Wenn ein Ziel vorhanden und groß genug ist,
   meldet das Programm Erfolg und wechselt sofort zu einer neuen zufälligen Zielfarbe.

#. Bewegungssteuerung mit WASD

   .. code-block:: python

      if k in key_dict:
          action = key_dict[k]

      if action is not None:
          crawler.do_action(action, 1, speed)
          action = None

   Die Hauptschleife prüft auf ein Tastaturereignis:

   • w → vorwärts  
   • s → rückwärts  
   • a → nach links drehen  
   • d → nach rechts drehen  

   Wenn eine Bewegungstaste gedrückt wird,
   führt der Roboter einen kurzen Bewegungsschritt aus.  
   Dieses Design sorgt für eine schnelle Reaktion
   und verhindert unkontrollierte Dauerbewegungen.

#. Leertaste: Zielansage wiederholen

   .. code-block:: python

      elif k == 'space':
          tts.say("Look for " + color)

   Durch Drücken der Leertaste wird die aktuelle Zielansage wiederholt.  
   Das ist hilfreich, wenn der Benutzer die Zielfarbe vergessen hat.

#. Beenden und Aufräumen

   .. code-block:: python

      finally:
          stop_event.set()
          Vilib.color_detect("close")
          Vilib.camera_close()
          crawler.do_step('sit', 40)

   Beim Beenden:

   • ``stop_event`` signalisiert dem Tastatur-Thread, zu stoppen.  
   • Die Farberkennung von Vilib wird deaktiviert.  
   • Die Kamera wird sicher geschlossen.  
   • Der Roboter setzt sich hin, um eine instabile Haltung nach dem Beenden zu vermeiden.

   Diese Reihenfolge hilft, Kamerafehler zu verhindern
   und stellt sicher, dass der Roboter in einer sicheren Position endet.
