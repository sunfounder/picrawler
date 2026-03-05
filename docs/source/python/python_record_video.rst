.. note:: 

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook. ¡Explora más a fondo Raspberry Pi, Arduino y ESP32 con otros entusiastas!

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y vistas previas.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _py_video:

Grabar Video
==================

Este ejemplo te guiará sobre cómo utilizar la función de grabación.

**Ejecutar el Código**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 record_video.py

Después de ejecutar el código, puedes ingresar ``http://<tu IP>:9000/mjpg`` en el navegador para ver la pantalla de video, por ejemplo: ``http://192.168.18.113:9000/mjpg``.

.. image:: img/display.png

La grabación se puede detener o iniciar presionando teclas en el teclado.

* Pulsa ``q`` para comenzar la grabación, pausar/continuar, y ``e`` para detener la grabación o guardar.
* Si deseas salir del programa, presiona ``Ctrl+C``.

**Código**

.. code-block:: python

    from time import sleep, strftime, localtime
    from vilib import Vilib
    import readchar
    from os import getlogin
    import os

    USERNAME = getlogin()
    VIDEO_PATH = f"/home/{USERNAME}/Videos/"

    MANUAL = '''
    Press keys on keyboard to control recording:
        Q: record/pause/continue
        E: stop
        Ctrl+C: Quit
    '''

    def print_overwrite(msg, end='', flush=True):
        """Overwrite the current terminal line."""
        print('\r\033[2K', end='', flush=True)
        print(msg, end=end, flush=True)

    def safe_stop_recording():
        """Stop recording safely (avoid exceptions during exit)."""
        try:
            Vilib.rec_video_stop()
        except Exception:
            pass

    def safe_close_camera():
        """Close camera safely (avoid exceptions during exit)."""
        try:
            Vilib.camera_close()
        except Exception:
            pass

    def main():
        rec_flag = 'stop'  # Possible states: start, pause, stop
        vname = None

        # Ensure the video directory exists
        os.makedirs(VIDEO_PATH, exist_ok=True)

        # Set save path for recorded videos
        Vilib.rec_video_set["path"] = VIDEO_PATH

        # Start camera and preview
        Vilib.camera_start(vflip=False, hflip=False)
        Vilib.display(local=False, web=True)
        sleep(0.8)  # Wait for camera startup

        print(MANUAL)

        try:
            while True:
                # Read keyboard input (no Enter needed)
                key = readchar.readkey().lower()

                # Q: start / pause / continue
                if key == 'q':
                    if rec_flag == 'stop':
                        rec_flag = 'start'

                        # Generate filename based on timestamp
                        vname = strftime("%Y-%m-%d-%H.%M.%S", localtime())
                        Vilib.rec_video_set["name"] = vname

                        # Start recording
                        Vilib.rec_video_run()
                        Vilib.rec_video_start()
                        print_overwrite('rec start ...')

                    elif rec_flag == 'start':
                        rec_flag = 'pause'
                        Vilib.rec_video_pause()
                        print_overwrite('pause')

                    elif rec_flag == 'pause':
                        rec_flag = 'start'
                        Vilib.rec_video_start()
                        print_overwrite('continue')

                # E: stop recording
                elif key == 'e' and rec_flag != 'stop':
                    rec_flag = 'stop'
                    safe_stop_recording()
                    print_overwrite(
                        "The video saved as %s%s.avi" % (Vilib.rec_video_set["path"], vname),
                        end='\n'
                    )

                # Ctrl+C (readchar special key): quit
                elif key == readchar.key.CTRL_C:
                    print('\nquit')
                    break

                sleep(0.1)

        except KeyboardInterrupt:
            # Handle Ctrl+C from terminal as well
            print('\nquit')

        finally:
            # If recording is still active, stop it before closing camera
            if rec_flag != 'stop':
                safe_stop_recording()
            safe_close_camera()
            sleep(0.1)

    if __name__ == "__main__":
        main()

**¿Cómo funciona?**

#. Qué Hace Este Programa

   Este programa permite controlar la grabación de video usando el teclado.

   • Q → Iniciar / Pausar / Continuar la grabación  
   • E → Detener la grabación  
   • Ctrl+C → Salir del programa  

   El video grabado se guardará en la carpeta Videos.

#. Preparar la Carpeta de Video

   .. code-block:: python

      USERNAME = getlogin()
      VIDEO_PATH = f"/home/{USERNAME}/Videos/"
      os.makedirs(VIDEO_PATH, exist_ok=True)

   El programa obtiene el nombre de usuario actual  
   y crea una carpeta Videos si aún no existe.

   Todos los videos grabados se guardarán aquí.

#. Iniciar la Cámara

   .. code-block:: python

      Vilib.camera_start(vflip=False, hflip=False)
      Vilib.display(local=False, web=True)
      sleep(0.8)

   La cámara se enciende.
   Se habilita la vista previa web para que pueda ver la transmisión en vivo en el navegador.

   El pequeño retraso permite que la cámara se inicie correctamente.

#. Configuración del Estado de Grabación

   .. code-block:: python

      rec_flag = 'stop'
      vname = None

   El programa utiliza una variable llamada ``rec_flag``
   para recordar el estado actual de la grabación:

   • stop  → no está grabando  
   • start → grabando  
   • pause → en pausa 

#. Esperar Entrada del Teclado

   .. code-block:: python

      key = readchar.readkey().lower()

   El programa espera a que se presione una tecla.

#. Presione Q para Iniciar la Grabación

   .. code-block:: python

      if rec_flag == 'stop':
          vname = strftime("%Y-%m-%d-%H.%M.%S", localtime())
          Vilib.rec_video_set["name"] = vname
          Vilib.rec_video_run()
          Vilib.rec_video_start()

   Cuando presiona Q por primera vez:

   • Se genera un nombre de archivo usando la fecha y hora actuales  
   • La grabación comienza inmediatamente  

   Ejemplo de nombre de archivo:
   2026-03-03-15.30.21.avi

#. Presione Q Otra Vez para Pausar

   .. code-block:: python

      elif rec_flag == 'start':
          Vilib.rec_video_pause()

   Si la grabación ya está en curso,
   presionar Q pausará la grabación.

#. Presione Q Otra Vez para Continuar

   .. code-block:: python

      elif rec_flag == 'pause':
          Vilib.rec_video_start()

   Si la grabación está en pausa,
   presionar Q nuevamente continuará la grabación.

#. Presione E para Detener la Grabación

   .. code-block:: python

      elif key == 'e' and rec_flag != 'stop':
          Vilib.rec_video_stop()

   Presionar E detendrá completamente la grabación.

   El archivo de video se guardará en: ``/home/your_username/Videos/``

#. Salir del Programa de Forma Segura

   .. code-block:: python

      finally:
          if rec_flag != 'stop':
              Vilib.rec_video_stop()
          Vilib.camera_close()

   Cuando el programa finaliza:

   • La grabación se detiene (si aún está en ejecución)  
   • La cámara se cierra de forma segura  

   Esto evita archivos de video dañados o errores de cámara.