.. note:: 

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook. ¡Explora más a fondo Raspberry Pi, Arduino y ESP32 con otros entusiastas!

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y vistas previas.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _py_avoid:

Evitación de Obstáculos
===========================

En este proyecto, PiCrawler usará un módulo ultrasónico para detectar obstáculos frente a él. 
Cuando PiCrawler detecte un obstáculo, enviará una señal y buscará otra dirección para avanzar.

.. .. image:: img/avoid1.png

**Ejecutar el Código**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 avoid.py

Cuando el programa comienza, PiCrawler se pone de pie.

Mide continuamente la distancia utilizando el sensor ultrasónico
y muestra el valor en la terminal.

Si se detecta un obstáculo dentro de 15 cm:
- Se reproduce un sonido de advertencia.
- El robot realiza un pequeño giro hacia la izquierda.

Si el camino está despejado:
- El robot avanza hacia adelante.

El robot continúa evitando obstáculos automáticamente hasta que presione Ctrl+C.

Antes de salir, se sienta de forma segura.

**Código**

.. note::
    Puedes **Modificar/Restablecer/Copiar/Ejecutar/Detener** el código a continuación. Pero antes de eso, necesitas ir a la ruta del código fuente como ``picrawler\examples``. Después de modificar el código, puedes ejecutarlo directamente para ver el efecto.

.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from robot_hat import Music, Ultrasonic, Pin
    import time
    import signal

    music = Music()
    crawler = Picrawler()
    sonar = Ultrasonic(Pin("D2"), Pin("D3"))  # Ultrasonic trigger/echo pins

    music.music_set_volume(100)  # Set speaker volume

    alert_distance = 15  # Obstacle warning distance (cm)
    speed = 80           # Movement speed

    # ----------------------------
    # Add hardware timeout to sonar.read()
    # Prevent program from freezing
    # ----------------------------
    class Timeout(Exception):
        pass

    def _alarm_handler(signum, frame):
        raise Timeout()

    signal.signal(signal.SIGALRM, _alarm_handler)

    # Read distance once with timeout protection
    def safe_read_once(timeout_s=1):
        try:
            signal.alarm(timeout_s)
            d = sonar.read()
            signal.alarm(0)
            return d
        except Timeout:
            signal.alarm(0)
            return None
        except Exception:
            signal.alarm(0)
            return None

    # Read multiple times and return median value (anti-noise)
    def read_distance_filtered(n=5, gap=0.03, timeout_s=1):
        vals = []
        for _ in range(n):
            d = safe_read_once(timeout_s=timeout_s)
            if d is not None and d > 0:
                vals.append(d)
            time.sleep(gap)

        if not vals:
            return None

        vals.sort()
        return vals[len(vals)//2]  # Median filter

    def main():
        distance = read_distance_filtered(n=5, gap=0.03, timeout_s=1)
        print("distance:", distance)

        if distance is None:
            time.sleep(0.15)  # Wait if read failed
            return

        if distance <= alert_distance:
            # Obstacle detected → play sound and turn
            try:
                music.sound_play_threading('./sounds/sign.wav', volume=100)
            except Exception as e:
                print("sound error:", e)

            crawler.do_action('turn left angle', 1, speed)
            time.sleep(0.5)  # Quiet window after movement
        else:
            # Path clear → move forward
            crawler.do_action('forward', 1, speed)
            time.sleep(0.4)

    if __name__ == "__main__":
        try:
            crawler.do_step('stand', 40)  # Stand before starting
            time.sleep(1.0)

            while True:
                main()

        except KeyboardInterrupt:
            print("\nStop.")
        finally:
            try:
                crawler.do_step('sit', 40)  # Sit before exit
                time.sleep(1.0)
            except Exception:
                pass

**¿Cómo funciona?**

#. Bloque de Inicialización

   .. code-block:: python

      music = Music()
      crawler = Picrawler()
      sonar = Ultrasonic(Pin("D2"), Pin("D3"))

      music.music_set_volume(100)
      alert_distance = 15
      speed = 80

   Este bloque inicializa los tres módulos principales:
   - ``music``: controla la reproducción de sonido.
   - ``crawler``: controla el movimiento de PiCrawler.
   - ``sonar``: mide la distancia usando el sensor ultrasónico.

   También establece el volumen del altavoz, el umbral de detección de obstáculos (cm)
   y la velocidad de movimiento.

#. Bloque de Configuración de Timeout (evita que ``sonar.read()`` se congele)

   .. code-block:: python

      class Timeout(Exception):
          pass

      def _alarm_handler(signum, frame):
          raise Timeout()

      signal.signal(signal.SIGALRM, _alarm_handler)

   El controlador ultrasónico puede bloquearse mientras espera la señal de eco.
   Este bloque instala un manejador de señales para que el programa pueda interrumpir
   una llamada bloqueada de ``sonar.read()`` y continuar ejecutándose.

#. Función: safe_read_once()

   .. code-block:: python

      def safe_read_once(timeout_s=1):
          try:
              signal.alarm(timeout_s)
              d = sonar.read()
              signal.alarm(0)
              return d
          except Timeout:
              signal.alarm(0)
              return None
          except Exception:
              signal.alarm(0)
              return None

   Esta función lee la distancia ultrasónica una vez con protección de tiempo límite.
   - Si la lectura es exitosa, devuelve el valor de la distancia.
   - Si ocurre un timeout o falla, devuelve ``None`` en lugar de quedarse bloqueado.

#. Función: read_distance_filtered()

   .. code-block:: python

      def read_distance_filtered(n=5, gap=0.03, timeout_s=1):
          vals = []
          for _ in range(n):
              d = safe_read_once(timeout_s=timeout_s)
              if d is not None and d > 0:
                  vals.append(d)
              time.sleep(gap)

          if not vals:
              return None

          vals.sort()
          return vals[len(vals)//2]

   Esta función mejora la fiabilidad leyendo múltiples muestras:
   - Los valores inválidos (``None`` o ``<= 0``) se ignoran.
   - Los valores restantes se ordenan.
   - Se devuelve el valor mediano para reducir el ruido.

#. Función: main() (decisión y acción principal)

   .. code-block:: python

      def main():
          distance = read_distance_filtered(...)
          if distance is None:
              return

          if distance <= alert_distance:
              music.sound_play_threading(...)
              crawler.do_action('turn left angle', 1, speed)
          else:
              crawler.do_action('forward', 1, speed)

   Esta es la lógica principal de control:

   - Lee un valor de distancia filtrado.
   - Si la lectura falla, se omite este ciclo.
   - Si un obstáculo está más cerca que ``alert_distance``, reproduce un sonido de advertencia y gira a la izquierda.
   - De lo contrario, avanza hacia adelante.

#. Bloque de Entrada del Programa (bucle continuo + salida segura)

   .. code-block:: python

      if __name__ == "__main__":
          try:
              crawler.do_step('stand', 40)
              while True:
                  main()
          except KeyboardInterrupt:
              print("\nStop.")
          finally:
              crawler.do_step('sit', 40)

   Este bloque controla el flujo general del programa:
   - El crawler se pone de pie antes de comenzar.
   - El programa ejecuta ``main()`` repetidamente en un bucle infinito.
   - Presionar Ctrl+C detiene el bucle.
   - El crawler se sienta antes de que el programa finalice.