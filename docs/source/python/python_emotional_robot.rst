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


**Código**

.. note::
    Puedes **Modificar/Restablecer/Copiar/Ejecutar/Detener** el código a continuación. Pero antes de eso, necesitas ir a la ruta del código fuente como ``picrawler\examples``. Después de modificar el código, puedes ejecutarlo directamente para ver el efecto.


.. raw:: html

    <run></run>


.. code-block:: python

    from picrawler import Picrawler
    from time import sleep

    crawler = Picrawler() 

    def handwork(speed):

        basic_step = []
        basic_step = crawler.step_list.get("sit")
        left_hand  = crawler.mix_step(basic_step,0,[0,50,80])
        right_hand  = crawler.mix_step(basic_step,1,[0,50,80])
        two_hand = crawler.mix_step(left_hand,1,[0,50,80])

        crawler.do_step('sit',speed)
        sleep(0.6)    
        crawler.do_step(left_hand,speed)
        sleep(0.6)
        crawler.do_step(two_hand,speed)
        sleep(0.6)
        crawler.do_step(right_hand,speed)
        sleep(0.6)
        crawler.do_step('sit',speed)
        sleep(0.6)

    def twist(speed):
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

    ##"[[delantera derecha], [delantera izquierda], [trasera izquierda], [trasera derecha]]")

    def pushup(speed):
        up=[[80, 0, -100], [80, 0, -100],[0, 120, -60], [0, 120, -60]]
        down=[[80, 0, -30], [80, 0, -30],[0, 120, -60], [0, 120, -60]]
        crawler.do_step(up,speed)
        sleep(0.6)
        crawler.do_step(down,speed)
        sleep(0.6)

    def swimming(speed):
        for i in range(100):
            crawler.do_step([[100-i,i,0],[100-i,i,0],[0,120,-60+i/5],[0,100,-40-i/5]],speed)

    # main
    def main():
        speed = 100

        swimming(speed)
        pushup(speed)
        handwork(speed)
        twist(speed)

        sleep(0.05)

    if __name__ == "__main__":
        main()

    
 
