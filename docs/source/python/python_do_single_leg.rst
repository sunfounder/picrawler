.. note:: 

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook. ¡Explora más a fondo Raspberry Pi, Arduino y ESP32 con otros entusiastas!

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y vistas previas.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _py_posture:

Ajustar Postura
=====================

En este ejemplo, utilizamos el teclado para controlar cada pata del PiCrawler y lograr la postura deseada.

Puedes presionar la barra espaciadora para imprimir los valores actuales de las coordenadas. Estos valores son útiles cuando deseas crear acciones únicas para el PiCrawler.

.. image:: img/1cood.A.png

**Ejecutar el Código**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 do_single_leg.py

Después de ejecutar el código, por favor opera según las instrucciones que aparecen en el terminal.

* Presiona ``1234`` para seleccionar las patas individualmente: ``1``: pata delantera derecha, ``2``: pata delantera izquierda, ``3``: pata trasera izquierda, ``4``: pata trasera derecha.
* Presiona ``w``, ``a``, ``s``, ``d``, ``r``, y ``f`` para controlar lentamente los valores de las coordenadas del PiCrawler.
* Presiona ``Ctrl+C`` para salir.

**Código**

.. code-block:: python

    #!/usr/bin/env python3
    from picrawler import Picrawler
    from time import sleep
    import readchar

    crawler = Picrawler()

    SPEED = 80
    STEP_SIZE = 2

    manual = '''
    -------- PiCrawler Controller ---------
        .......          .......
        <=|   2   |┌-┌┐┌┐-┐|   1   |=>
        ``````` ├      ┤ ```````
        ....... ├      ┤ .......
        <=|   3   |└------┘|   4   |=>
        ```````          ```````
        1: Select right front leg
        2: Select left front leg
        3: Select left rear leg
        4: Select right rear leg

        W: Y++          R: Z++
        A: X--          F: Z--
        S: Y--
        D: X++          Ctrl+C: Quit
    '''

    legs_list = ['right front', 'left front', 'left rear', 'right rear']

    # Axis mapping for cleaner logic
    move_map = {
        'w': (1, +STEP_SIZE),  # Y++
        's': (1, -STEP_SIZE),  # Y--
        'a': (0, -STEP_SIZE),  # X--
        'd': (0, +STEP_SIZE),  # X++
        'r': (2, +STEP_SIZE),  # Z++
        'f': (2, -STEP_SIZE),  # Z--
    }


    def clear_screen():
        print("\033[H\033[J", end='')


    def show_info(selected_leg, coordinate):
        clear_screen()
        print(manual)
        print(f"Selected leg: {selected_leg + 1} - {legs_list[selected_leg]}")
        print(f"Coordinate: {coordinate}")


    def main():
        selected_leg = 0

        try:
            print(manual)

            # Stand up first
            crawler.do_step('stand', 40)
            sleep(0.5)

            # Get current coordinates
            coordinate = crawler.current_step_all_leg_value()
            show_info(selected_leg, coordinate)

            while True:
                key = readchar.readkey().lower()

                # Select leg
                if key in ('1', '2', '3', '4'):
                    selected_leg = int(key) - 1
                    show_info(selected_leg, coordinate)

                # Move selected leg
                elif key in move_map:
                    axis, delta = move_map[key]

                    # Update coordinate
                    coordinate[selected_leg][axis] += delta

                    # Send updated position
                    crawler.do_single_leg(selected_leg, coordinate[selected_leg], SPEED)
                    sleep(0.1)

                    show_info(selected_leg, coordinate)

                sleep(0.05)

        except KeyboardInterrupt:
            print("\nExiting safely...")

        finally:
            # Return to sitting position on exit
            try:
                crawler.do_step('sit', 40)
                sleep(1)
            except Exception:
                pass

            print("Robot is now sitting. Program ended.")


    if __name__ == "__main__":
        main()
        
* ``current_step_all_leg_value()``: Devuelve los valores de coordenadas de todas las patas.
* ``do_single_leg(leg,coordinate[leg],speed)``: Modifica el valor de coordenadas de una pata individualmente.
