.. note:: 

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook. ¡Explora más a fondo Raspberry Pi, Arduino y ESP32 con otros entusiastas!

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y vistas previas.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _py_video:

Grabar Video
==================

Este ejemplo te guiará sobre cómo utilizar la función de grabación.

**Ejecutar el Código**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 record_video.py

Después de ejecutar el código, puedes ingresar ``http://<tu IP>:9000/mjpg`` en el navegador para ver la pantalla de video, por ejemplo: ``http://192.168.18.113:9000/mjpg``.

.. image:: img/display.png

La grabación se puede detener o iniciar presionando teclas en el teclado.

* Pulsa ``q`` para comenzar la grabación, pausar/continuar, y ``e`` para detener la grabación o guardar.
* Si deseas salir del programa, presiona ``Ctrl+C``.

**Código**

.. code-block:: python

    from time import sleep,strftime,localtime
    from vilib import Vilib
    import readchar 
    from os import getlogin
    
    USERNAME = getlogin()
    VIDEO_PATH = f"/home/{USERNAME}/Videos/"
    
    MANUAL = '''
    Press keys on keyboard to control recording:
        Q: record/pause/continue
        E: stop
        Ctrl^C: Quit
    '''
    
    def print_overwrite(msg,  end='', flush=True):
        print('\r\033[2K', end='',flush=True)
        print(msg, end=end, flush=True)
    
    def main():
        rec_flag = 'stop' # start, pause, stop
        vname = None
        Vilib.rec_video_set["path"] = VIDEO_PATH
    
        Vilib.camera_start(vflip=False,hflip=False) 
        Vilib.display(local=True,web=True)
        sleep(0.8)  # esperar a que inicie
    
        print(MANUAL)
        while True:
            # leer teclado
            key = readchar.readkey()
            key = key.lower()
            # iniciar/pausar
            if key == 'q':
                key = None
                if rec_flag == 'stop':            
                    rec_flag = 'start'
                    # establecer nombre
                    vname = strftime("%Y-%m-%d-%H.%M.%S", localtime())
                    Vilib.rec_video_set["name"] = vname
                    # iniciar grabación
                    Vilib.rec_video_run()
                    Vilib.rec_video_start()
                    print_overwrite('rec start ...')
                elif rec_flag == 'start':
                    rec_flag = 'pause'
                    Vilib.rec_video_pause()
                    print_overwrite('pause')
                elif rec_flag == 'pause':
                    rec_flag = 'start'
                    Vilib.rec_video_start()
                    print_overwrite('continue')
            # detener
            elif key == 'e' and rec_flag != 'stop':
                key = None
                rec_flag = 'stop'
                Vilib.rec_video_stop()
                print_overwrite("The video saved as %s%s.avi"%(Vilib.rec_video_set["path"],vname),end='\n')  
            # salir
            elif key == readchar.key.CTRL_C:
                Vilib.camera_close()
                print('\nquit')
                break 
    
            sleep(0.1)
    
    if __name__ == "__main__":
        main()

**¿Cómo funciona?**


Las funciones relacionadas con la grabación incluyen las siguientes:


* ``Vilib.rec_video_run(video_name)``: Inicia el hilo para grabar el video. ``video_name`` es el nombre del archivo de video, debe ser una cadena de texto.
* ``Vilib.rec_video_start()``: Inicia o continúa la grabación del video.
* ``Vilib.rec_video_pause()``: Pausa la grabación.
* ``Vilib.rec_video_stop()``: Detiene la grabación.

``Vilib.rec_video_set["path"] = "~/video/test/"`` establece la ubicación de almacenamiento de los archivos de video.
