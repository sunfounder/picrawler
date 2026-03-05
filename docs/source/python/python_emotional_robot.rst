.. note:: 

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook. ¡Explora más a fondo Raspberry Pi, Arduino y ESP32 con otros entusiastas!

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y vistas previas.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _py_emotional:

Robot Emocional
===================

Este ejemplo muestra varias acciones personalizadas interesantes de PiCrawler.

**Ejecutar el Código**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 emotional_robot.py

Después de ejecutar el programa, el robot primero se pone de pie lentamente para alcanzar una postura estable.

Luego realiza una serie de movimientos, incluidos movimientos similares a nadar, flexiones, gestos de saludo con las patas delanteras y un baile de torsión. Estas acciones se ejecutan de forma secuencial, creando un comportamiento dinámico y expresivo.

Si se presiona **Ctrl+C**, el programa se cierra de forma segura y el robot vuelve a una posición sentada.

**Código**

.. note::
    Puedes **Modificar/Restablecer/Copiar/Ejecutar/Detener** el código a continuación. Pero antes de eso, necesitas ir a la ruta del código fuente como ``picrawler\examples``. Después de modificar el código, puedes ejecutarlo directamente para ver el efecto.


.. raw:: html

    <run></run>


.. code-block:: python

    from picrawler import Picrawler
    from time import sleep

    crawler = Picrawler()


    def get_sit_step():
        # Get a valid sit step used as the base pose for hand actions
        try:
            return crawler.move_list['sit'][0]
        except Exception:
            return None


    def handwork(speed):
        base = get_sit_step()

        # If a valid sit step cannot be retrieved, just perform a sit action
        if not base or len(base) < 4:
            crawler.do_step('sit', speed)
            sleep(0.6)
            return

        # Generate hand poses by modifying the sit step
        left_hand = crawler.mix_step(base, 0, [0, 50, 80])
        right_hand = crawler.mix_step(base, 1, [0, 50, 80])
        two_hand = crawler.mix_step(left_hand, 1, [0, 50, 80])

        crawler.do_step('sit', speed)
        sleep(0.6)

        crawler.do_step(left_hand, speed)
        sleep(0.6)

        crawler.do_step(two_hand, speed)
        sleep(0.6)

        crawler.do_step(right_hand, speed)
        sleep(0.6)

        crawler.do_step('sit', speed)
        sleep(0.6)

    def twist(speed):
        # Initialize the base position for all four legs
        new_step = [[50, 50, -80], [50, 50, -80], [50, 50, -80], [50, 50, -80]]

        # Create a twisting motion by alternating rise and drop movements
        for i in range(4):
            for inc in range(30, 60, 5):
                rise = [50, 50, (-80 + inc * 0.5)]
                drop = [50, 50, (-80 - inc)]

                new_step[i] = rise
                new_step[(i + 2) % 4] = drop
                new_step[(i + 1) % 4] = rise
                new_step[(i - 1) % 4] = drop

                crawler.do_step(new_step, speed)
                sleep(0.02)

    def pushup(speed):
        # Two poses used to simulate a push-up motion
        up = [[80, 0, -100], [80, 0, -100], [0, 120, -60], [0, 120, -60]]
        down = [[80, 0, -30], [80, 0, -30], [0, 120, -60], [0, 120, -60]]

        crawler.do_step(up, speed)
        sleep(0.6)

        crawler.do_step(down, speed)
        sleep(0.6)

    def swimming(speed, loops=100):
        # Simulate a swimming-like motion by gradually adjusting leg coordinates
        for i in range(loops):
            crawler.do_step(
                [
                    [100 - i, i, 0],
                    [100 - i, i, 0],
                    [0, 120, -60 + i / 5],
                    [0, 100, -40 - i / 5]
                ],
                speed
            )
            sleep(0.01)

    def main():
        speed = 100

        try:
            # Stand up slowly before performing actions
            crawler.do_step('stand', 40)
            sleep(1.0)

            swimming(speed)
            pushup(speed)
            handwork(speed)
            twist(speed)

        except KeyboardInterrupt:
            print("\nCtrl+C detected, exiting...")

        finally:
            # Return to a sitting posture before exiting
            try:
                crawler.do_step('sit', 40)
                sleep(1.0)
            except Exception:
                pass

    if __name__ == "__main__":
        main()

    
**¿Cómo funciona?**

#. Cuando el programa comienza, el robot primero se pone de pie lentamente para alcanzar una postura estable.

   .. code-block:: python
   
      crawler.do_step('stand', 40)
      sleep(1.0)

   Después de ponerse de pie, el programa ejecuta varios movimientos predefinidos en secuencia.

#. Movimiento de Natación

   El robot realiza un movimiento similar a nadar ajustando gradualmente las coordenadas de las patas.

   .. code-block:: python

      for i in range(loops):
          crawler.do_step([
              [100-i, i, 0],
              [100-i, i, 0],
              [0,120,-60+i/5],
              [0,100,-40-i/5]
          ], speed)

#. Movimiento de Flexiones

   Se definen dos posturas para simular un movimiento de flexión.

   .. code-block:: python

      up = [[80,0,-100],[80,0,-100],[0,120,-60],[0,120,-60]]
      down = [[80,0,-30],[80,0,-30],[0,120,-60],[0,120,-60]]

      crawler.do_step(up, speed)
      crawler.do_step(down, speed)

#. Movimiento de Saludo con la Mano

   El programa modifica las coordenadas de las patas delanteras usando ``mix_step()`` para crear un gesto de saludo.

   .. code-block:: python

      left_hand = crawler.mix_step(base,0,[0,50,80])
      right_hand = crawler.mix_step(base,1,[0,50,80])

#. Movimiento de Giro

   El robot gira su cuerpo levantando y bajando patas diagonales.

   .. code-block:: python

      rise = [50,50,(-80+inc*0.5)]
      drop = [50,50,(-80-inc)]
      crawler.do_step(new_step, speed)

#. Si se presiona **Ctrl+C**, el programa se cierra de forma segura y el robot vuelve a una posición sentada.

   .. code-block:: python
   
      crawler.do_step('sit', 40)
