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

Después de ejecutar el código, PiCrawler realizará las siguientes acciones en secuencia: avanzar, retroceder, girar a la izquierda, girar a la derecha, y mantenerse de pie.

**Código**

.. note::
    Puedes **Modificar/Restablecer/Copiar/Ejecutar/Detener** el código a continuación. Pero antes de eso, debes dirigirte a la ruta del código fuente, como ``pisloth\examples``. Después de modificar el código, puedes ejecutarlo directamente para ver el efecto.

.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep
    
    crawler = Picrawler() 
    
    def main():  
        
        speed = 80
              
        while True:
           
            crawler.do_action('forward',2,speed)
            sleep(0.05)     
            crawler.do_action('backward',2,speed)
            sleep(0.05)          
            crawler.do_action('turn left',2,speed)
            sleep(0.05)           
            crawler.do_action('turn right',2,speed)
            sleep(0.05)  
            crawler.do_action('turn left angle',2,speed)
            sleep(0.05)  
            crawler.do_action('turn right angle',2,speed)
            sleep(0.05) 
            crawler.do_step('stand',speed)
            sleep(1)
    
    if __name__ == "__main__":
        main()


**¿Cómo funciona?**

Primero, importa la clase ``Picrawler`` desde la biblioteca ``picrawler`` que has instalado, la cual contiene todas las acciones de PiCrawler y las funciones que las implementan.

.. code-block:: python

    from picrawler import Picrawler

Luego, instancia la clase ``crawler``.

.. code-block:: python

    crawler = Picrawler() 

Finalmente, utiliza la función ``crawler.do_action()`` para hacer que PiCrawler se mueva.

.. code-block:: python
    
    crawler.do_action('forward',2,speed)    
    crawler.do_action('backward',2,speed)         
    crawler.do_action('turn left',2,speed)          
    crawler.do_action('turn right',2,speed) 
    crawler.do_action('turn left angle',2,speed) 
    crawler.do_action('turn right angle',2,speed)

En general, todo el movimiento de PiCrawler puede implementarse con la función ``do_action()``. Esta tiene 3 parámetros:

* ``motion_name`` es el nombre de las acciones específicas, incluyendo: ``forward``, ``turn right``, ``turn left``, ``backward``, ``turn left angle``, ``turn right angle``.
* ``step`` representa el número de veces que se realiza cada acción, el valor predeterminado es 1.
* ``speed`` indica la velocidad de la acción, el valor predeterminado es 50 y el rango es de 0~100.

Además, aquí también se utiliza ``crawler.do_step('stand',speed)`` para hacer que PiCrawler se mantenga de pie. El uso de esta función se explicará en el siguiente ejemplo.
