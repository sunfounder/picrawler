.. note:: 

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook. ¡Explora más a fondo Raspberry Pi, Arduino y ESP32 con otros entusiastas!

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y vistas previas.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _py_twist:

Twist
==============

Ya sabemos cómo hacer que PiCrawler asuma una pose específica. El siguiente paso es combinar las poses para formar una acción continua.

Aquí, las cuatro patas de PiCrawler se levantan y bajan de dos en dos, saltando al ritmo de la música.

**Ejecutar el Código**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 twist.py

**Código**

.. note::
    Puedes **Modificar/Restablecer/Copiar/Ejecutar/Detener** el código a continuación. Pero antes, necesitas ir a la ruta del código fuente como ``picrawler\examples``. Después de modificar el código, puedes ejecutarlo directamente para ver el efecto.

.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from robot_hat import Music

    music = Music()
    crawler = Picrawler()


    def twist(speed):
        new_step=[[50, 50, -80], [50, 50, -80],[50, 50, -80], [50, 50, -80]]
        for i in range(4):
            for inc in range(30, 60, 5): 
                rise = [50,50,(-80+inc*0.5)]
                drop = [50,50,(-80-inc)]

                new_step[i]=rise
                new_step[(i+2)%4] = drop
                new_step[(i+1)%4] = rise
                new_step[(i-1)%4] = drop
                # print(new_step)
                crawler.do_step(new_step,speed)


    def main():  

        music.music_play('./musics/sports-Ahjay_Stelino.mp3')
        music.music_set_volume(20)

        while True:
            twist(speed=100) 

    
    if __name__ == "__main__":
        main()

**¿Cómo funciona?**

En este código, debes prestar atención a esta parte:

.. code-block:: python

    def twist(speed):
        ## [derecha delantera],[izquierda delantera],[izquierda trasera],[derecha trasera]
        new_step=[[50, 50, -80], [50, 50, -80],[50, 50, -80], [50, 50, -80]]
        for i in range(4):
            for inc in range(30,60,5):  
                rise = [50,50,(-80+inc*0.5)]
                drop = [50,50,(-80-inc)]

                new_step[i]=rise
                new_step[(i+2)%4] = drop
                new_step[(i+1)%4] = rise
                new_step[(i-1)%4] = drop
                crawler.do_step(new_step,speed)

En resumen, utiliza dos capas de bucles for para que el array ``new_step`` produzca cambios continuos y regulares. Al mismo tiempo, ``crawler.do_step()`` ejecuta la pose para formar una acción continua.

Puedes obtener intuitivamente el array de valores de coordenadas correspondiente a cada pose desde :ref:`py_posture`.

Además, el ejemplo también reproduce música de fondo. El método de implementación es el siguiente.

Reproduce música importando las siguientes bibliotecas:

.. code-block:: python

    from robot_hat import Music

Declara un objeto Music:

.. code-block:: python

    music = Music()

Reproduce la música de fondo en el directorio ``picrawler/examples/musics`` y establece el volumen en 20. También puedes añadir música a la carpeta ``musics`` mediante :ref:`filezilla`.

.. code-block:: python

    music.music_play('./musics/sports-Ahjay_Stelino.mp3')
    music.music_set_volume(20)

.. note::

    Puedes agregar diferentes efectos de sonido o música a las carpetas ``musics`` o ``sounds`` a través de :ref:`filezilla`.
