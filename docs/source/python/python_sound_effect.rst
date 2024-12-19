.. note:: 

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook. ¡Explora más a fondo Raspberry Pi, Arduino y ESP32 con otros entusiastas!

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y vistas previas.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _py_sound:

Efectos de Sonido
=====================

En este ejemplo, utilizaremos los efectos de sonido de PiCrawler (o, más específicamente, de Robot HAT). Consiste en tres partes: **Música**, **Sonido**, y **Texto a Voz**.

.. image:: img/tts.png

**Instalar i2samp**

Antes de usar estas funciones, primero activa el altavoz para habilitarlo y que pueda emitir sonidos.

Ejecuta ``i2samp.sh``, este script instalará todo lo necesario para utilizar el amplificador i2s.

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/
    sudo bash i2samp.sh 

Se te pedirá que confirmes varias solicitudes. Responde a todas con una **Y**. Después de aplicar los cambios al sistema Raspberry Pi, será necesario reiniciar para que surtan efecto.

Después de reiniciar, ejecuta nuevamente el script ``i2samp.sh`` para probar el amplificador. Si el sonido se reproduce correctamente desde el altavoz, la configuración está completa.

**Ejecutar el Código**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 sound_effect.py

Después de ejecutar el código, sigue las indicaciones que aparecen en la terminal.

Introduce una tecla para llamar a la función correspondiente:
* ``q``: Reproducir música de fondo.
* ``1``: Reproducir efecto de sonido.
* ``2``: Reproducir efecto de sonido en hilos.
* ``t``: Convertir texto a voz.
* Para salir del programa, presiona ``Ctrl+C``.

**Código**

.. code-block:: python

    '''
        Sorry, currently there is only sound when running with sudo
    '''

    from time import sleep
    from robot_hat import Music,TTS

    music = Music()
    tts = TTS()

    manual = '''
    Input key to call the function!
        q: Play background music
        1: Play sound effect
        2: Play sound effect with threads
        t: Text to speak

        Ctrl^C: quit
    '''

    def main():  
        print(manual)

        flag_bgm = False
        music.music_set_volume(20)
        tts.lang("en-US")


        while True:
            key = input() 
            key = key.lower() 
            if key == "q":
                flag_bgm = not flag_bgm
                if flag_bgm is True:
                    music.music_play('./musics/sports-Ahjay_Stelino.mp3')
                else:
                    music.music_stop()

            elif key == "1":
                music.sound_play('./sounds/talk1.wav')
                sleep(0.05)
                music.sound_play('./sounds/talk3.wav')
                sleep(0.05)
                music.sound_play('./sounds/sign.wav')
                sleep(0.5)

            elif key =="2":
                music.sound_play_threading('./sounds/talk1.wav')
                sleep(0.05)
                music.sound_play_threading('./sounds/talk3.wav')
                sleep(0.05)
                music.sound_play_threading('./sounds/sign.wav')
                sleep(0.5)

            elif key == "t":
                words = "Hello"
                tts.say(words)

    if __name__ == "__main__":
        main()

**¿Cómo funciona?**

Las funciones relacionadas con la música de fondo incluyen:

* ``music = Music()`` : Declarar el objeto.
* ``music.music_set_volume(20)`` : Configurar el volumen, el rango es de 0 a 100.
* ``music.music_play('./musics/sports-Ahjay_Stelino.mp3')`` : Reproducir archivos de música, en este caso el archivo **sports-Ahjay_Stelino.mp3** en la ruta ``./musics``.
* ``music.music_stop()`` : Detener la reproducción de música de fondo.

.. note::

    Puedes añadir diferentes efectos de sonido o música a las carpetas ``musics`` o ``sounds`` mediante :ref:`filezilla`.

Las funciones relacionadas con los efectos de sonido incluyen:

* ``music = Music()``
* ``music.sound_play('./sounds/talk1.wav')`` : Reproducir el archivo de efecto de sonido, en este caso el archivo **talk1.wav** en la ruta ``./sounds``.
* ``music.sound_play_threading('./sounds/talk1.wav')`` : Reproducir el archivo de efecto de sonido en un modo de hilo nuevo sin suspender el hilo principal.

Las funciones relacionadas con Texto a Voz incluyen:

* ``tts = TTS()``
* ``tts.say(words)`` : Convertir texto a audio.
* ``tts.lang("en-US")`` : Configurar el idioma.

.. note:: 

    Configura el idioma mediante el parámetro de ``lang("")`` con los siguientes códigos:

.. list-table:: Idiomas
    :widths: 15 50

    *   - zh-CN 
        - Mandarín (Chino)
    *   - en-US 
        - Inglés-Estados Unidos
    *   - en-GB     
        - Inglés-Reino Unido
    *   - de-DE     
        - Alemán-Deutsch
    *   - es-ES     
        - Español-España
    *   - fr-FR  
        - Francés-Le français
    *   - it-IT  
        - Italiano-Lingua italiana
