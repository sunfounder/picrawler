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

    from picrawler import Picrawler
    from time import sleep
    import readchar

    crawler = Picrawler()
    speed = 80


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

    def main():  
        leg = 0
        speed = 80
        step = 2
        print(manual)
        crawler.do_step('stand', speed)
        sleep(0.2)
        coordinate=crawler.current_step_all_leg_value()  

        def show_info():
            print("\033[H\033[J", end='')  # limpiar ventana del terminal
            print(manual)   
            print('%s : %s'%(leg+1, legs_list[leg])) 
            print('coordinate: %s'%(coordinate))  

        show_info()

        while True:
            # leer tecla
            key = readchar.readkey()
            key = key.lower()
            # seleccionar pata
            if key in ('1234'):
                leg = int(key) - 1
                show_info()
            # mover
            elif key in ('wsadrf'):         
                if 'w' == key:
                    coordinate[leg][1]=coordinate[leg][1] + step    
                elif 's' == key:
                    coordinate[leg][1]=coordinate[leg][1] - step           
                elif 'a' == key:
                    coordinate[leg][0]=coordinate[leg][0] - step         
                elif 'd' == key:
                    coordinate[leg][0]=coordinate[leg][0] + step   
                elif 'r' == key:
                    coordinate[leg][2]=coordinate[leg][2] + step         
                elif 'f' == key:
                    coordinate[leg][2]=coordinate[leg][2] - step 

                crawler.do_single_leg(leg,coordinate[leg],speed) 
                sleep(0.1)  
                # coordinate=crawler.current_step_all_leg_value()
                show_info()

            sleep(0.05)

    
    if __name__ == "__main__":
        main()

* ``current_step_all_leg_value()``: Devuelve los valores de coordenadas de todas las patas.
* ``do_single_leg(leg,coordinate[leg],speed)``: Modifica el valor de coordenadas de una pata individualmente.
