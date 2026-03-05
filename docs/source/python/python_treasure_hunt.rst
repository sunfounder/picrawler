.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti Speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a promozioni e concorsi durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_treasure:

Caccia al Tesoro
============================

Organizza un labirinto nella tua stanza e posiziona sei cartellini di colori diversi in sei angoli. Poi controlla PiCrawler per cercare questi cartellini uno alla volta!

.. note:: Puoi scaricare e stampare i :download:`PDF Color Cards <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>` per il rilevamento dei colori.

**Esegui il Codice**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 treasure_hunt.py


**Visualizza le Immagini**

Dopo aver eseguito il codice, il terminale mostrerà il seguente messaggio:

.. code-block::

    No desktop !
    * Serving Flask app "vilib.vilib" (lazy loading)
    * Environment: production
    WARNING: Do not use the development server in a production environment.
    Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)

Inserisci quindi ``http://<il tuo IP>:9000/mjpg`` nel browser per visualizzare il feed video. Ad esempio: ``http://192.168.18.113:9000/mjpg``.

.. image:: img/display.png

**Codice**

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


**Come funziona?**

#. Cosa fa questo programma

   Questo programma è un semplice gioco di “caccia al tesoro” per PiCrawler:

   • La fotocamera trasmette lo streaming su una pagina web (senza finestra GUI locale).  
   • Vilib rileva un colore bersaglio (rosso/arancione/giallo/verde/blu/viola).  
   • Controlli il robot con WASD.  
   • Quando l'oggetto del colore rilevato è abbastanza grande, il programma annuncia il successo
     e passa a un nuovo colore bersaglio.  
   • Il programma termina correttamente con Ctrl+C senza traceback dei thread.

#. L'input da tastiera viene eseguito in un thread in background

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

   La lettura della tastiera è separata in un thread dedicato.
   Questo impedisce al ciclo principale di bloccarsi mentre attende la pressione di un tasto.

   Ctrl+C può generare KeyboardInterrupt all'interno di questo thread (comportamento di readchar),
   quindi viene intercettato e usato per avviare un'uscita pulita invece di stampare un errore.

#. Gli eventi dei tasti sono condivisi in modo sicuro

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

   Il programma utilizza un lock per proteggere la variabile condivisa key_state.
   Il thread della tastiera scrive gli eventi dei tasti usando set_key().
   Il ciclo principale legge e cancella gli eventi usando pop_key().

   Questo garantisce che il robot reagisca ai tasti in modo sicuro senza condizioni di gara.

#. Fotocamera e anteprima web

   .. code-block:: python

      Vilib.camera_start(vflip=False, hflip=False)
      Vilib.display(local=False, web=True)

   La fotocamera viene avviata e l'anteprima web viene abilitata.
   local=False evita crash della GUI sui sistemi senza ambiente desktop.

#. Prima si alza, poi attende i tasti di movimento

   .. code-block:: python

      crawler.do_step('stand', 40)
      sleep(0.8)

   Dopo l'avvio, il robot si alza con velocità 40 per stabilizzare la postura.
   Il programma non muove il robot automaticamente.
   Si muove solo quando riceve un tasto WASD.

#. Selezione di un colore bersaglio

   .. code-block:: python

      color = random.choice(COLOR_LIST)
      Vilib.color_detect(color)
      tts.say("Look for " + color)

   Un colore casuale viene selezionato dalla lista.
   Il rilevamento del colore in Vilib viene attivato per quel colore.
   Il TTS annuncia il bersaglio corrente così l'utente sa cosa cercare.

#. Rilevare il “successo” e cambiare bersaglio

   .. code-block:: python

      n = Vilib.detect_obj_parameter.get('color_n', 0)
      w = Vilib.detect_obj_parameter.get('color_w', 0)

      if n != 0 and w > 100:
          tts.say("well done")
          renew_color_detect()

   Vilib aggiorna continuamente detect_obj_parameter.

   • color_n indica se un bersaglio è stato rilevato  
   • color_w è la larghezza dell'oggetto rilevato (una misura approssimativa di quanto sia vicino/grande)

   Quando il bersaglio esiste ed è abbastanza grande, il programma annuncia il successo
   e passa immediatamente a un nuovo colore bersaglio casuale.

#. Controllo del movimento con WASD

   .. code-block:: python

      if k in key_dict:
          action = key_dict[k]

      if action is not None:
          crawler.do_action(action, 1, speed)
          action = None

   Il ciclo principale controlla se è stato ricevuto un evento da tastiera:

   • w → forward  
   • s → backward  
   • a → turn_left  
   • d → turn_right  

   Quando viene ricevuto un tasto di movimento, il robot esegue un breve passo di azione.
   Questo design mantiene il controllo reattivo ed evita movimenti continui incontrollati.

#. Tasto Space: ripetere il messaggio del bersaglio

   .. code-block:: python

      elif k == 'space':
          tts.say("Look for " + color)

   Premendo Space viene ripetuto il messaggio del bersaglio corrente.
   Questo è utile se l'utente ha dimenticato il colore bersaglio.

#. Uscita e pulizia

   .. code-block:: python

      finally:
          stop_event.set()
          Vilib.color_detect("close")
          Vilib.camera_close()
          crawler.do_step('sit', 40)

   Quando si esce:

   • stop_event indica al thread della tastiera di fermarsi.  
   • Il rilevamento del colore di Vilib viene disabilitato.  
   • La fotocamera viene chiusa in modo sicuro.  
   • Il robot si siede per evitare una postura instabile dopo l'uscita.

   Questo ordine di pulizia aiuta a prevenire errori delle risorse della fotocamera
   e garantisce che il robot termini in una posizione sicura.

