.. note:: 

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook. ¡Explora más a fondo Raspberry Pi, Arduino y ESP32 con otros entusiastas!

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y vistas previas.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _py_keyboard:

Control con Teclado
=======================

En este proyecto, aprenderemos a usar el teclado para controlar remotamente el PiCrawler. Podrás controlar al PiCrawler para que se mueva hacia adelante, hacia atrás, a la izquierda y a la derecha.


**Ejecutar el Código**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 keyboard_control.py

Cuando el programa comienza, PiCrawler se inicializa y se muestra una interfaz de control por teclado en la terminal.

¡Presione las teclas del teclado para controlar PiCrawler!

* ``w``: Avanzar
* ``a``: Girar a la izquierda
* ``s``: Retroceder
* ``d``: Girar a la derecha
* ``Ctrl+C``: Salir

La velocidad actual se muestra y puede ajustarse usando:

- + / ] para aumentar la velocidad
- - / [ para disminuir la velocidad

Después de cada acción, se aplica un pequeño retraso para mejorar la estabilidad.

Presione Ctrl+C para salir.
Antes de apagarse, el crawler realiza una acción segura de "sentarse".


**Código**

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep
    import readchar

    crawler = Picrawler()

    SPEED_MIN = 20
    SPEED_MAX = 70
    speed = 60

    STEP = 1            # Number of action steps per key press
    ACTION_GAP = 0.25   # Delay after each action to reduce current spikes

    manual = """
    Keyboard Control - PiCrawler

    Movement:
    W: Forward
    A: Turn left
    S: Backward
    D: Turn right

    Speed Control:
    + / ] : Increase speed
    - / [ : Decrease speed

    Other:
    Space  : Stop (no action)
    Ctrl+C : Quit (auto sit)
    """

    def clamp(value, min_value, max_value):
        """Limit value within a specified range."""
        return max(min_value, min(max_value, value))

    def show_info():
        """Clear terminal and display control instructions."""
        print("\033[H\033[J", end="")  # Clear terminal screen
        print(manual)
        print(f"Current speed: {speed}  (range {SPEED_MIN}-{SPEED_MAX})")
        print(f"Action gap: {ACTION_GAP:.2f}s")

    def do_move(action_name):
        """Execute movement action with safety delay."""
        crawler.do_action(action_name, STEP, speed)
        sleep(ACTION_GAP)

    def safe_sit():
        """Safely sit down before program exit."""
        try:
            crawler.do_step("sit", clamp(speed, 20, 40))
            sleep(1.0)
        except Exception:
            pass

    def main():
        show_info()

        try:
            while True:
                key = readchar.readkey()
                k = key.lower()

                if k == "w":
                    do_move("forward")
                elif k == "s":
                    do_move("backward")
                elif k == "a":
                    do_move("turn left")
                elif k == "d":
                    do_move("turn right")

                # Speed increase
                elif k in ("+", "]"):
                    global speed
                    speed = clamp(speed + 5, SPEED_MIN, SPEED_MAX)

                # Speed decrease
                elif k in ("-", "["):
                    speed = clamp(speed - 5, SPEED_MIN, SPEED_MAX)

                # Stop (no movement)
                elif k == " ":
                    pass

                # Quit using readchar special key
                elif key == readchar.key.CTRL_C:
                    print("\nQuit.")
                    break

                show_info()
                sleep(0.02)

        except KeyboardInterrupt:
            print("\nQuit (KeyboardInterrupt).")

        finally:
            safe_sit()

    if __name__ == "__main__":
        main()

**¿Cómo funciona?**

#. Creación del Objeto del Robot

   .. code-block:: python

      crawler = Picrawler()

   Esta línea crea un objeto ``Picrawler``.
   Permite que el programa controle los movimientos del robot.

#. Definición del Rango de Velocidad Seguro

   .. code-block:: python

      SPEED_MIN = 20
      SPEED_MAX = 70
      speed = 60

   Estas variables definen el rango de velocidad permitido.
   ``speed`` almacena la velocidad de movimiento actual.
   El robot no se moverá más rápido que el valor máximo.

#. Limitación de Velocidad con clamp()

   .. code-block:: python

      def clamp(value, min_value, max_value):
          return max(min_value, min(max_value, value))

   Esta función asegura que la velocidad se mantenga dentro del rango seguro.
   Evita movimientos inestables causados por valores extremos.

#. Ejecución de un Movimiento

   .. code-block:: python

      def do_move(action_name):
          crawler.do_action(action_name, STEP, speed)
          sleep(ACTION_GAP)

   Esta función envía un comando de movimiento al robot.
   ``ACTION_GAP`` agrega un pequeño retraso para mejorar la estabilidad.

#. Lectura de Entrada del Teclado

   .. code-block:: python

      key = readchar.readkey()
      k = key.lower()

   El programa espera a que se presione una tecla.
   La tecla se convierte a minúsculas para mantener consistencia.

#. Lógica de Control de Movimiento

   .. code-block:: python

      if k == "w":
          do_move("forward")
      elif k == "s":
          do_move("backward")

   Cuando se presiona una tecla, el movimiento correspondiente se ejecuta inmediatamente.
   No es necesario presionar Enter.

#. Salida Segura

   .. code-block:: python

      finally:
          safe_sit()

   Antes de que el programa finalice, el robot ejecuta una acción segura de "sentarse".
   Esto evita posturas inestables o apagados repentinos.