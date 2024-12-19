.. note:: 

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook. ¡Explora más a fondo Raspberry Pi, Arduino y ESP32 con otros entusiastas!

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y vistas previas.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _py_record:

Registrar Nuevo Paso
=======================

Utilizamos el teclado para controlar a PiCrawler para realizar varias posturas en secuencia y grabar estas posturas. Luego, las reproducimos.

**Ejecutar el Código**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 record_new_step_by_keyboard.py

Después de ejecutar el código, opera según las instrucciones que aparecen en el terminal.

* Pulsa ``1234`` para seleccionar cada pata por separado, ``1``: pata delantera derecha, ``2``: pata delantera izquierda, ``3``: pata trasera izquierda, ``4``: pata trasera derecha.
* Pulsa ``w``, ``a``, ``s``, ``d``, ``r`` y ``f`` para controlar lentamente los valores de las coordenadas de PiCrawler.
* Pulsa ``space`` para imprimir todos los valores de las coordenadas.
* Pulsa ``p`` para que PiCrawler reproduzca la acción grabada.
* Pulsa ``esc`` para salir.

**Código**

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep
    import sys
    import tty
    import termios
    import copy

    crawler = Picrawler() 
    speed = 80

    def readchar():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


    manual = '''
    Press keys on keyboard to control!
        w: Y++
        a: X--
        s: Y--
        d: X++
        r: Z++
        f: Z--
        1: Select right front leg
        2: Select left front leg
        3: Select left rear leg
        4: Select right rear leg
        Space: Print all leg coodinate & Save this step
        p: Play all saved step
        esc: Quit
    '''


    new_step=[]

    def save_new_step():
        new_step.append(copy.deepcopy(crawler.current_step_all_leg_value()))
        print(new_step)

    def play_all_new_step():
        for step in new_step:
            crawler.do_step(step,speed)
            sleep(0.6)

    def main():  

        speed = 80
        print(manual)
        crawler.do_step('sit',speed)
        leg = 0 
        coodinate=crawler.current_step_leg_value(leg)   
        while True:
            key = readchar()
            key = key.lower()
            # print(key)
            if 'w' == key:
                coodinate[1]=coodinate[1]+2    
            elif 's' == key:
                coodinate[1]=coodinate[1]-2           
            elif 'a' == key:
                coodinate[0]=coodinate[0]-2         
            elif 'd' == key:
                coodinate[0]=coodinate[0]+2   
            elif 'r' == key:
                coodinate[2]=coodinate[2]+2         
            elif 'f' == key:
                coodinate[2]=coodinate[2]-2       
            elif '1' == key:
                leg=0
                coodinate=crawler.current_step_leg_value(leg)           
            elif '2' == key:
                leg=1   
                coodinate=crawler.current_step_leg_value(leg)              
            elif '3' == key:
                leg=2  
                coodinate=crawler.current_step_leg_value(leg)     
            elif '4' == key:
                leg=3     
                coodinate=crawler.current_step_leg_value(leg)  
            elif chr(32) == key:
                print("[[right front],[left front],[left rear],[right rear]]")
                print("saved new step")
                print(crawler.current_step_all_leg_value())
                save_new_step()
            elif 'p' == key:
                play_all_new_step()
            elif chr(27) == key:# 27 para ESC
                break    

            sleep(0.05)
            crawler.do_single_leg(leg,coodinate,speed)          
        print("\n q Quit")  

    
    if __name__ == "__main__":
        main()

**¿Cómo funciona?**

Este proyecto surge de :ref:`py_posture`, con la adición de funciones de grabación y reproducción.

La función de grabación se implementa con el siguiente código.

.. code-block:: python

    new_step=[]

    def save_new_step():
        new_step.append(copy.deepcopy(crawler.current_step_all_leg_value()))
        print(new_step)

.. note:: 
    La asignación aquí necesita usar la función `Deep Copy <https://docs.python.org/3/library/copy.html>`_, de lo contrario, ``new_step`` no obtendrá un nuevo objeto de array al hacer append.

La función de reproducción se implementa con el siguiente código.

.. code-block:: python

    def play_all_new_step():
        for step in new_step:
            crawler.do_step(step,speed)
            sleep(0.6)