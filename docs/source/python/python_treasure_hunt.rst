.. note:: 

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook. ¡Explora más a fondo Raspberry Pi, Arduino y ESP32 con otros entusiastas!

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y vistas previas.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _py_treasure:

Búsqueda del Tesoro
============================

Organiza un laberinto en tu habitación y coloca seis tarjetas de colores diferentes en seis esquinas. Luego, controla a PiCrawler para buscar estas tarjetas de colores una por una.

.. note:: Puedes descargar e imprimir las :download:`Tarjetas de Color en PDF <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>` para la detección de colores.

**Ejecutar el Código**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 treasure_hunt.py


**Ver la Imagen**

Después de ejecutar el código, la terminal mostrará el siguiente mensaje:

.. code-block::

    No desktop !
    * Serving Flask app "vilib.vilib" (lazy loading)
    * Environment: production
    WARNING: Do not use the development server in a production environment.
    Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)

Luego, puedes ingresar ``http://<tu IP>:9000/mjpg`` en el navegador para ver la pantalla de video. Por ejemplo: ``http://192.168.18.113:9000/mjpg``.

.. image:: img/display.png

**Código**

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


**¿Cómo funciona?**

#. Qué Hace Este Programa

   Este programa es un sencillo juego de “búsqueda del tesoro” para PiCrawler:

   • La cámara transmite a una página web (sin ventana GUI local).  
   • Vilib detecta un color objetivo (red/orange/yellow/green/blue/purple).  
   • Controlas el robot usando WASD.  
   • Cuando el objeto del color detectado es lo suficientemente grande, el programa anuncia el éxito
     y cambia a un nuevo color objetivo.  
   • El programa termina limpiamente con Ctrl+C sin mostrar errores de hilos.

#. La Entrada del Teclado se Ejecuta en un Hilo en Segundo Plano

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

   La lectura del teclado se ejecuta en su propio hilo.
   Esto evita que el bucle principal se bloquee mientras espera una tecla.

   Ctrl+C puede generar KeyboardInterrupt dentro de este hilo (comportamiento de readchar),
   por lo que se captura y se utiliza para iniciar una salida limpia en lugar de mostrar un error.

#. Los Eventos de Tecla se Comparten de Forma Segura

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

   El programa usa un lock para proteger la variable compartida key_state.
   El hilo del teclado escribe eventos de tecla usando set_key().
   El bucle principal lee y limpia los eventos usando pop_key().

   Esto garantiza que el robot reaccione a las teclas de forma segura sin condiciones de carrera.

#. Cámara y Vista Previa Web

   .. code-block:: python

      Vilib.camera_start(vflip=False, hflip=False)
      Vilib.display(local=False, web=True)

   La cámara se inicia y se habilita la vista previa web.
   local=False evita fallos de GUI en sistemas sin entorno de escritorio.

#. Primero Ponerse de Pie, Luego Esperar las Teclas de Movimiento

   .. code-block:: python

      crawler.do_step('stand', 40)
      sleep(0.8)

   Después de iniciar, el robot se pone de pie a velocidad 40 para estabilizar la postura.
   El programa no mueve el robot automáticamente.
   Solo se mueve cuando recibe una tecla WASD.

#. Selección de un Color Objetivo

   .. code-block:: python

      color = random.choice(COLOR_LIST)
      Vilib.color_detect(color)
      tts.say("Look for " + color)

   Se selecciona un color aleatorio de la lista.
   La detección de color de Vilib se activa para ese color.
   TTS anuncia el objetivo actual para que el usuario sepa qué buscar.

#. Detección de “Éxito” y Cambio de Objetivo

   .. code-block:: python

      n = Vilib.detect_obj_parameter.get('color_n', 0)
      w = Vilib.detect_obj_parameter.get('color_w', 0)

      if n != 0 and w > 100:
          tts.say("well done")
          renew_color_detect()

   Vilib actualiza ``detect_obj_parameter`` continuamente.

   • ``color_n`` indica si se detecta un objetivo  
   • ``color_w`` es el ancho del objetivo detectado (una medida aproximada de “qué tan cerca o grande es”)

   Cuando el objetivo existe y es lo suficientemente grande, el programa anuncia el éxito
   y cambia inmediatamente a un nuevo color objetivo aleatorio.

#. Control de Movimiento con WASD

   .. code-block:: python

      if k in key_dict:
          action = key_dict[k]

      if action is not None:
          crawler.do_action(action, 1, speed)
          action = None

   El bucle principal comprueba si hay un evento de tecla:

   • w → forward  
   • s → backward  
   • a → turn_left  
   • d → turn_right  

   Cuando se recibe una tecla de movimiento, el robot ejecuta un paso corto de acción.
   Este diseño mantiene el control sensible y evita movimientos continuos descontrolados.

#. Tecla Espacio: Repetir el Mensaje del Objetivo

   .. code-block:: python

      elif k == 'space':
          tts.say("Look for " + color)

   Al presionar la barra espaciadora se repite el mensaje del objetivo actual.
   Esto es útil si el usuario olvidó el color objetivo.

#. Salir y Limpieza

   .. code-block:: python

      finally:
          stop_event.set()
          Vilib.color_detect("close")
          Vilib.camera_close()
          crawler.do_step('sit', 40)

   Al salir:

   • ``stop_event`` indica al hilo del teclado que debe detenerse.  
   • La detección de color de Vilib se desactiva.  
   • La cámara se cierra de forma segura.  
   • El robot se sienta para evitar una postura inestable después de salir.

   Este orden de limpieza ayuda a prevenir errores de recursos de cámara
   y garantiza que el robot termine en una posición segura.