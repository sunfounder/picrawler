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


**Código**

.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep

    crawler = Picrawler() 

    ## [delantera derecha], [delantera izquierda], [trasera izquierda], [trasera derecha]
    new_step=[[45, 45, -75], [45, 0, -75], [45, 0, -30], [45, 45, -75]]
    stand_step = crawler.move_list['stand'][0]

    def main():  
        while True:
            speed = 80

            print(f"stand step: {stand_step}")
            crawler.do_step(stand_step, speed)
            sleep(3)
            print(f"new step: {new_step}")
            crawler.do_step(new_step,speed)
            sleep(3)

    
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





