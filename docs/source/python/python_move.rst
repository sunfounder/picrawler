.. note:: 

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook. ¡Explora más a fondo Raspberry Pi, Arduino y ESP32 con otros entusiastas!

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y vistas previas.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _py_move:

Moverse
==============

Este es el primer proyecto de PiCrawler. Realiza su función más básica: moverse.

.. .. image:: img/move.png

**Ejecutar el Código**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 move.py

Cuando el programa comienza, PiCrawler se pone de pie y espera brevemente.

Luego realiza continuamente un ciclo de movimientos:
avanzar, retroceder, girar a la izquierda, girar a la derecha,
pequeño giro a la izquierda y pequeño giro a la derecha.

Cada acción está separada por breves pausas para lograr un movimiento más suave.

Presione Ctrl+C para detener el programa.
Antes de salir, el crawler se sienta de forma segura.

**Código**

.. note::
    Puedes **Modificar/Restablecer/Copiar/Ejecutar/Detener** el código a continuación. Pero antes de eso, debes dirigirte a la ruta del código fuente, como ``picrawler\examples``. Después de modificar el código, puedes ejecutarlo directamente para ver el efecto.

.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep

    crawler = Picrawler()  # Create PiCrawler object

    def main():
        speed = 80  # Movement speed

        try:
            crawler.do_step('stand', 40)  # Stand up
            sleep(1.0)

            while True:
                crawler.do_action('forward', 1, speed)   # Move forward
                sleep(0.25)

                crawler.do_action('backward', 1, speed)  # Move backward
                sleep(0.25)

                crawler.do_action('turn left', 1, speed)  # Turn left
                sleep(0.25)

                crawler.do_action('turn right', 1, speed)  # Turn right
                sleep(0.25)

                crawler.do_action('turn left angle', 1, speed)  # Small left turn
                sleep(0.3)

                crawler.do_action('turn right angle', 1, speed)  # Small right turn
                sleep(0.3)

                sleep(0.5)

        except KeyboardInterrupt:
            print("\nCtrl+C pressed...")

        finally:
            crawler.do_step('sit', 40)  # Sit down before exit
            sleep(1.0)

    if __name__ == "__main__":
        main()


**¿Cómo funciona?**

#. Importación e Inicialización

   .. code-block:: python

      from picrawler import Picrawler
      from time import sleep

      crawler = Picrawler()

   El script importa los módulos necesarios y crea un
   objeto ``Picrawler``, que se utiliza para controlar todos los movimientos del robot.

#. Función Principal y Configuración

   .. code-block:: python

      def main():
          speed = 80
          crawler.do_step('stand', 40)
          sleep(1.0)

   La función ``main()`` define la velocidad de movimiento.
   Antes de iniciar el bucle, el robot se pone de pie y se estabiliza.

#. Bucle de Movimiento Continuo

   .. code-block:: python

      while True:
          crawler.do_action('forward', 1, speed)
          crawler.do_action('backward', 1, speed)
          crawler.do_action('turn left', 1, speed)
          crawler.do_action('turn right', 1, speed)
          crawler.do_action('turn left angle', 1, speed)
          crawler.do_action('turn right angle', 1, speed)

   El robot ejecuta continuamente una secuencia predefinida
   de acciones de movimiento dentro de un bucle infinito.
   Pequeñas pausas entre las acciones ayudan a suavizar el movimiento.

#. Manejo de Salida Segura

   .. code-block:: python

      except KeyboardInterrupt:
          print("\nCtrl+C pressed...")
      finally:
          crawler.do_step('sit', 40)

   La estructura ``try / except / finally`` garantiza que:
   - Ctrl+C detiene el bucle de forma segura.
   - El robot se sienta antes de que el programa termine.

#. Entrada del Programa

   .. code-block:: python

      if __name__ == "__main__":
          main()

   Esto asegura que ``main()`` se ejecute solo cuando el script
   se ejecuta directamente.