.. note:: 

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook. ¡Explora más a fondo Raspberry Pi, Arduino y ESP32 con otros entusiastas!

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y vistas previas.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _py_bull:

Lucha de Toros
=================

¡Convierte a PiCrawler en un toro enojado! Usa su cámara para seguir y embestir la tela roja.

.. .. image:: img/bullfight.png

**Ejecutar el Código**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 bull_fight.py


**Ver la Imagen**

Después de ejecutar el código, el terminal mostrará el siguiente mensaje:

.. code-block::

    No desktop !
    * Serving Flask app "vilib.vilib" (lazy loading)
    * Environment: production
    WARNING: Do not use the development server in a production environment.
    Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)

Luego puedes ingresar ``http://<tu IP>:9000/mjpg`` en el navegador para ver la pantalla de video. Por ejemplo: ``https://192.168.18.113:9000/mjpg``

.. image:: img/display.png

**Código**

.. note::
    Puedes **Modificar/Restablecer/Copiar/Ejecutar/Detener** el código a continuación. Pero antes de eso, necesitas ir a la ruta del código fuente como ``picrawler\examples``. Después de modificar el código, puedes ejecutarlo directamente para ver el efecto.

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


**¿Cómo funciona?**

#. Inicialización de la Cámara

   .. code-block:: python

      Vilib.camera_start(vflip=False, hflip=False)
      Vilib.display(local=False, web=True)
      Vilib.color_detect("red")

   La cámara se inicia y se habilita la vista previa en la web.
   Se activa la detección del color rojo.
   Vilib procesa continuamente los fotogramas en segundo plano
   y almacena los resultados de detección en ``detect_obj_parameter``.

#. Preparación del Robot

   .. code-block:: python

      crawler.do_step('stand', 40)
      sleep(1.0)

   El robot realiza una acción de ponerse de pie antes de comenzar el seguimiento.
   Un breve retraso garantiza que la postura sea estable.

#. Detección del Objetivo

   .. code-block:: python

      if Vilib.detect_obj_parameter.get('color_n', 0) != 0:
          coordinate_x = Vilib.detect_obj_parameter.get('color_x', 0)

   El programa comprueba si se detecta un objeto rojo.
   Si se detecta, lee la coordenada horizontal central (posición x)
   del objeto rojo en la imagen.

#. Lógica de Decisión de Dirección

   .. code-block:: python

      if coordinate_x < 100:
          crawler.do_action('turn left', 1, speed)
      elif coordinate_x > 220:
          crawler.do_action('turn right', 1, speed)
      else:
          crawler.do_action('forward', 2, speed)

   La imagen se divide en tres zonas horizontales:
   izquierda, centro y derecha.

   • Zona izquierda → girar a la izquierda  
   • Zona derecha → girar a la derecha  
   • Zona central → avanzar  

   Esto permite que el robot siga y persiga el objeto rojo.

#. Mecanismo de Enfriamiento del Sonido

   .. code-block:: python

      now = time()
      if now - last_beep >= BEEP_COOLDOWN:
          music.sound_play_threading('./sounds/talk1.wav')
          last_beep = now

   Un temporizador de enfriamiento evita la reproducción repetida del sonido.
   El efecto de sonido se reproduce como máximo una vez por segundo,
   incluso si el objeto sigue siendo detectado.

#. Manejo de Pérdida del Objetivo

   .. code-block:: python

      if last_seen:
          crawler.do_step('stand', 40)
          last_seen = False

   Cuando el objeto rojo desaparece,
   el robot se detiene y vuelve a una posición estable de pie.

   La bandera ``last_seen`` garantiza que ``stand()`` se llame solo una vez.
   Esto evita reinicios repetidos de postura que pueden causar vibraciones.

#. Salida Segura y Limpieza

   .. code-block:: python

      finally:
          Vilib.color_detect("close")
          Vilib.camera_close()
          crawler.do_step('sit', 40)

   Cuando el programa termina (por ejemplo, al presionar Ctrl+C),
   se desactiva la detección de color,
   la cámara se cierra de forma segura,
   y el robot ejecuta la acción de sentarse.

   Esto evita errores de cámara y comportamientos inestables durante el apagado.
