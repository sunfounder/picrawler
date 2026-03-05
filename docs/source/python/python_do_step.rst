.. note:: 

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook. ¡Explora más a fondo Raspberry Pi, Arduino y ESP32 con otros entusiastas!

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y vistas previas.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _py_pose:

Postura
=============

PiCrawler puede asumir una postura específica escribiendo un array de coordenadas. Aquí asume una postura con la pata trasera derecha levantada.

.. image:: img/4cood.A.png

**Ejecutar el Código**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 do_step.py

Después de ejecutar el programa, el robot primero se pone de pie lentamente para alcanzar una postura estable.

Una vez de pie, el robot realiza repetidamente dos acciones en un bucle. Primero se mueve a una postura de paso de pie y mantiene la posición durante unos segundos, luego cambia a un paso personalizado donde las patas se mueven a diferentes coordenadas. Esto crea un movimiento repetido de cambio de postura.

El robot continúa alternando entre estas dos poses hasta que el programa se detiene. Si se presiona **Ctrl+C**, el programa se cierra de forma segura y el robot vuelve a una posición sentada.

**Código**

.. raw:: html

    <run></run>

.. code-block:: python

    #!/usr/bin/env python3
    from picrawler import Picrawler
    from time import sleep

    # Create Picrawler instance
    crawler = Picrawler()

    # Leg order:
    # [right front], [left front], [left rear], [right rear]
    new_step = [[45, 45, -75], [45, 0, -75], [45, 0, -30], [45, 45, -75]]

    # Get the default stand step from the move list
    stand_step = crawler.move_list['stand'][0]


    def main():
        action_speed = 80  # Speed for movement actions

        try:
            # Stand up slowly at 40% speed to reduce current spikes
            crawler.do_step('stand', 40)
            sleep(1.0)

            # Continuous action loop
            while True:
                crawler.do_step(stand_step, action_speed)
                sleep(3)

                crawler.do_step(new_step, action_speed)
                sleep(3)

        except KeyboardInterrupt:
            # Handle Ctrl+C for safe exit
            print("\nExiting safely...")

        finally:
            # Return to sitting position before shutting down
            try:
                crawler.do_step('sit', 40)
                sleep(1.0)
            except Exception:
                pass


    if __name__ == "__main__":
        main()

**Cómo funciona**

En este código, la línea que debes observar es ``crawler.do_step()``.

Similar a ``do_action()``, ``do_step()`` también puede manipular el comportamiento de PiCrawler.
La diferencia es que el primero puede realizar comportamientos continuos como ``mover hacia adelante``, mientras que el segundo se utiliza para realizar gestos separados como ``pararse`` y ``sentarse``.


Tiene dos usos:

Uno: Puede escribir cadenas y utilizar directamente el diccionario ``step_list`` de la biblioteca ``picrawler``.

.. code-block:: python

    crawler.do_step('stand', speed) 
    # "speed" indica la velocidad del paso, el rango es de 0~100.

Segundo: También puede escribir un array con 4 valores de coordenadas.

.. code-block:: python

    new_step=[[45, 45, -75], [45, 0, -75], [45, 0, -30], [45, 45, -75]]
    # Estas cuatro coordenadas se utilizan para controlar las patas delantera derecha, delantera izquierda, trasera izquierda y trasera derecha, respectivamente.

Cada pata tiene un sistema de coordenadas independiente. Como se muestra a continuación:

.. image:: img/4cood.png

Necesitas medir las coordenadas de cada pata individualmente. Como se muestra a continuación:

.. image:: img/1cood.png

Por cierto: el ``step_list`` llamado en el primer método también consiste en un array que contiene 4 valores de coordenadas.

.. code-block:: python

    step_list = {

        "stand":[
            [45, 45, -50], 
            [45, 45, -50], 
            [45, 45, -50], 
            [45, 45, -50]
        ],
        "sit":[
            [45, 45, -30], 
            [45, 45, -30], 
            [45, 45, -30], 
            [45, 45, -30]
        ],
              
    }





