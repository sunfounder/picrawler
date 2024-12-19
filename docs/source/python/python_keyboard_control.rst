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

¡Presiona las teclas en el teclado para controlar el PiCrawler!

* ``w``: Adelante
* ``a``: Girar a la izquierda
* ``s``: Atrás
* ``d``: Girar a la derecha
* ``Ctrl+C``: Salir


**Código**

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep
    import readchar

    crawler = Picrawler() 
    speed = 90

    manual = '''
    Press keys on keyboard to control PiCrawler!
        W: Forward
        A: Turn left
        S: Backward
        D: Turn right

        Ctrl^C: Quit
    '''

    def show_info():
        print("\033[H\033[J",end='')  # limpiar ventana del terminal 
        print(manual)


    def main(): 
        show_info()   
        while True:
            key = readchar.readkey()
            key = key.lower()
            if key in('wsad'):
                if 'w' == key:
                    crawler.do_action('forward',1,speed)     
                elif 's' == key:
                    crawler.do_action('backward',1,speed)          
                elif 'a' == key:
                    crawler.do_action('turn left',1,speed)           
                elif 'd' == key:
                    crawler.do_action('turn right',1,speed)
                sleep(0.05)
                show_info()  
            elif key == readchar.key.CTRL_C:
                print("\n Quit") 
                break    

            sleep(0.02)          

    
    if __name__ == "__main__":
        main()

**¿Cómo funciona?**

PiCrawler debe realizar una acción adecuada en función de los caracteres leídos del teclado. La función ``lower()`` convierte los caracteres en mayúsculas a minúsculas, de modo que la letra sea válida independientemente del caso.

.. code-block:: python

    def main(): 
        show_info()   
        while True:
            key = readchar.readkey()
            key = key.lower()
            if key in('wsad'):
                if 'w' == key:
                    crawler.do_action('forward',1,speed)     
                elif 's' == key:
                    crawler.do_action('backward',1,speed)          
                elif 'a' == key:
                    crawler.do_action('turn left',1,speed)           
                elif 'd' == key:
                    crawler.do_action('turn right',1,speed)
                sleep(0.05)
                show_info()  
            elif key == readchar.key.CTRL_C:
                print("\n Quit") 
                break    
            
            sleep(0.02)  
