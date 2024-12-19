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

.. image:: img/avoid1.png

**Ejecutar el Código**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 avoid.py

Después de ejecutar el código, PiCrawler caminará hacia adelante. Si detecta que la distancia al obstáculo delante es menor a 10 cm, se detendrá y emitirá una advertencia sonora, luego girará a la izquierda y se detendrá. Si no hay obstáculos en la dirección después de girar a la izquierda o la distancia al obstáculo es mayor a 10 cm, continuará avanzando.

**Código**

.. note::
    Puedes **Modificar/Restablecer/Copiar/Ejecutar/Detener** el código a continuación. Pero antes de eso, necesitas ir a la ruta del código fuente como ``picrawler\examples``. Después de modificar el código, puedes ejecutarlo directamente para ver el efecto.

.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from robot_hat import TTS, Music
    from robot_hat import Ultrasonic
    from robot_hat import Pin
    import time

    tts = TTS()
    music = Music()

    crawler = Picrawler() 
    sonar = Ultrasonic(Pin("D2") ,Pin("D3"))
    music.music_set_volume(100)

    alert_distance = 15
    speed = 80

    def main():
        distance = sonar.read()
        print(distance)
        if distance < 0:
            pass
        elif distance <= alert_distance:
            try:
                music.sound_play_threading('./sounds/sign.wav', volume=100)
            except Exception as e:
                print(e)
            crawler.do_action('turn left angle',3,speed)
            time.sleep(0.2)
        else :
            crawler.do_action('forward', 1,speed)
            time.sleep(0.2)

    if __name__ == "__main__":
        while True:
            main()

**¿Cómo funciona?**

Puedes obtener la distancia importando la clase ``Ultrasonic``.

.. code-block:: python

    from robot_hat import Ultrasonic

Luego, inicializa los pines del sensor ultrasónico.

.. code-block:: python

    sonar = Ultrasonic(Pin("D2") ,Pin("D3"))

Aquí está el programa principal:

* Lee la ``distance`` detectada por el módulo ultrasónico y filtra los valores menores a 0 (cuando el módulo ultrasónico está demasiado lejos del obstáculo o no puede leer los datos correctamente, aparece ``distance<0``).
* Cuando la ``distance`` es menor o igual a ``alert_distance`` (el valor de umbral establecido previamente, que es 10), reproduce el efecto de sonido ``sign.wav``. PiCrawler ejecuta ``turn left angle``.
* Cuando la ``distance`` es mayor a ``alert_distance``, PiCrawler avanzará con la acción ``forward``.

.. code-block:: python

    distance = sonar.read()
    print(distance)
    if distance < 0:
        pass
    elif distance <= alert_distance:
        try:
            music.sound_play_threading('./sounds/sign.wav', volume=100)
        except Exception as e:
            print(e)
        crawler.do_action('turn left angle',3,speed)
        time.sleep(0.2)
    else :
        crawler.do_action('forward', 1,speed)
        time.sleep(0.2)

.. note::

    Puedes agregar diferentes efectos de sonido o música a la carpeta ``musics`` o ``sounds`` a través de :ref:`filezilla`.
