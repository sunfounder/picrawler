.. note:: 

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook. ¡Explora más a fondo Raspberry Pi, Arduino y ESP32 con otros entusiastas!

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y vistas previas.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _py_vision:

Visión por Computadora
==========================

¡Este proyecto te llevará oficialmente al campo de la visión por computadora!

**Ejecutar el Código**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 display.py

**Ver la Imagen**

Después de ejecutar el código, el terminal mostrará el siguiente mensaje:

.. code-block::

    No desktop !
    * Serving Flask app "vilib.vilib" (lazy loading)
    * Environment: production
    WARNING: Do not use the development server in a production environment.
    Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)

Luego puedes ingresar ``http://<tu IP>:9000/mjpg`` en el navegador para ver la pantalla de video. Por ejemplo: ``http://192.168.18.113:9000/mjpg``

.. image:: img/display.png

Después de ejecutar el programa, verás la siguiente información en el terminal:

* Ingresa una tecla para llamar a la función:
* ``q``: Tomar foto
* ``1``: Detección de color: rojo
* ``2``: Detección de color: naranja
* ``3``: Detección de color: amarillo
* ``4``: Detección de color: verde
* ``5``: Detección de color: azul
* ``6``: Detección de color: púrpura
* ``0``: Apagar detección de color
* ``r``: Escanear código QR
* ``f``: Activar/Desactivar detección de rostro
* ``s``: Mostrar información de objeto detectado

Por favor, sigue las indicaciones para activar las funciones correspondientes.

    * **Tomar Foto**

        Escribe ``q`` en el terminal. La imagen que actualmente ve la cámara se guardará (si la función de detección de color está activada, también aparecerá el cuadro de marca en la imagen guardada). Puedes ver estas fotos en el directorio ``~/Pictures/PiCrawler/`` de la Raspberry Pi. Usa herramientas como :ref:`filezilla` para transferir fotos a tu PC.

    * **Detección de Color**

        Ingresa un número entre ``1~6`` para detectar uno de los colores "rojo, naranja, amarillo, verde, azul, púrpura". Ingresa ``0`` para apagar la detección de color.

        .. image:: img/DTC2.png

        .. note:: Puedes descargar e imprimir las :download:`Tarjetas de Color en PDF <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>` para la detección de colores.


    * **Detección de Rostros**

        Escribe ``f`` para activar la detección de rostros.

        .. image:: img/DTC5.png

    * **Detección de Código QR**

        Ingresa ``r`` para abrir el reconocimiento de códigos QR. No se pueden realizar otras operaciones antes de que se reconozca el código QR. La información decodificada del código QR se imprimirá en el terminal.

        .. image:: img/DTC4.png

    * **Mostrar Información**

        Al ingresar ``s`` se imprimirá la información del objetivo detectado (detección de rostros y colores) en el terminal. Esto incluye las coordenadas centrales (X, Y) y el tamaño (ancho, altura) del objeto medido.

**Código** 

.. code-block:: python

    from vilib import Vilib
    from time import sleep, time, strftime, localtime
    import threading
    import readchar
    from os import getlogin

    USERNAME = getlogin()
    PICTURE_PATH = f"/home/{USERNAME}/Pictures/"

    flag_face = False
    flag_color = False
    qr_code_flag = False

    MANUAL = '''
    Press a key to call the function:
        q: Take photo
        1: Color detect : red
        2: Color detect : orange
        3: Color detect : yellow
        4: Color detect : green
        5: Color detect : blue
        6: Color detect : purple
        0: Switch off Color detect
        r: Scan the QR code (toggle)
        f: Switch ON/OFF face detect
        s: Display detected object information
        Ctrl+C: Quit
    '''

    color_list = ['close', 'red', 'orange', 'yellow', 'green', 'blue', 'purple']

    def face_detect(flag):
        print("Face Detect:", flag)
        Vilib.face_detect_switch(flag)

    def qrcode_detect():
        global qr_code_flag
        Vilib.qrcode_detect_switch(True)
        print("Waiting for QR code...")

        text = None
        while qr_code_flag:
            temp = Vilib.detect_obj_parameter.get('qr_data', "None")
            if temp != "None" and temp != text:
                text = temp
                print("QR code:", text)
            sleep(0.2)

        Vilib.qrcode_detect_switch(False)

    def take_photo():
        _time = strftime('%Y-%m-%d-%H-%M-%S', localtime(time()))
        name = f'photo_{_time}'
        Vilib.take_photo(name, PICTURE_PATH)
        print(f'Photo saved as {PICTURE_PATH}{name}.jpg')

    def object_show():
        global flag_color, flag_face

        if flag_color:
            if Vilib.detect_obj_parameter.get('color_n', 0) == 0:
                print('Color Detect: None')
            else:
                x = Vilib.detect_obj_parameter.get('color_x')
                y = Vilib.detect_obj_parameter.get('color_y')
                w = Vilib.detect_obj_parameter.get('color_w')
                h = Vilib.detect_obj_parameter.get('color_h')
                print("[Color Detect] Coordinate:", (x, y), "Size:", (w, h))

        if flag_face:
            if Vilib.detect_obj_parameter.get('human_n', 0) == 0:
                print('Face Detect: None')
            else:
                x = Vilib.detect_obj_parameter.get('human_x')
                y = Vilib.detect_obj_parameter.get('human_y')
                w = Vilib.detect_obj_parameter.get('human_w')
                h = Vilib.detect_obj_parameter.get('human_h')
                print("[Face Detect] Coordinate:", (x, y), "Size:", (w, h))

    def main():
        global flag_face, flag_color, qr_code_flag
        qrcode_thread = None

        Vilib.camera_start(vflip=False, hflip=False)
        Vilib.display(local=True, web=True)
        print(MANUAL)

        try:
            while True:
                key = readchar.readkey().lower()

                if key == 'q':
                    take_photo()

                elif key in '0123456':
                    index = int(key)
                    if index == 0:
                        flag_color = False
                        Vilib.color_detect('close')
                    else:
                        flag_color = True
                        Vilib.color_detect(color_list[index])
                    print('Color detect:', color_list[index])

                elif key == 'f':
                    flag_face = not flag_face
                    face_detect(flag_face)

                elif key == 'r':
                    qr_code_flag = not qr_code_flag
                    if qr_code_flag:
                        if qrcode_thread is None or not qrcode_thread.is_alive():
                            qrcode_thread = threading.Thread(target=qrcode_detect, daemon=True)
                            qrcode_thread.start()
                    else:
                        print('QRcode Detect: close')

                elif key == 's':
                    object_show()

                sleep(0.05)

        except KeyboardInterrupt:
            print("\nQuit.")

        finally:
            # Stop QR thread and switches
            qr_code_flag = False
            try:
                Vilib.qrcode_detect_switch(False)
            except Exception:
                pass

            try:
                Vilib.color_detect('close')
            except Exception:
                pass

            try:
                Vilib.face_detect_switch(False)
            except Exception:
                pass

            # Close camera
            try:
                Vilib.camera_close()
            except Exception:
                pass

    if __name__ == "__main__":
        main()

**¿Cómo funciona?**

El primer paso es utilizar las siguientes funciones para iniciar la cámara:

.. code-block:: python

    Vilib.camera_start()
    Vilib.display()

Funciones relacionadas con "detección de objetos":

* ``Vilib.face_detect_switch(True)``: Activar/Desactivar detección de rostros.
* ``Vilib.color_detect(color)``: Para la detección de colores; solo se puede realizar una detección de color a la vez. Los parámetros aceptados son: ``"red"``, ``"orange"``, ``"yellow"``, ``"green"``, ``"blue"``, ``"purple"``.
* ``Vilib.color_detect_switch(False)``: Apagar detección de color.
* ``Vilib.qrcode_detect_switch(False)``: Activar/Desactivar detección de códigos QR. Devuelve los datos decodificados del código QR.
* ``Vilib.gesture_detect_switch(False)``: Activar/Desactivar detección de gestos.
* ``Vilib.traffic_sign_detect_switch(False)``: Activar/Desactivar detección de señales de tráfico.

La información detectada se almacena en el diccionario ``detect_obj_parameter = Manager().dict()``.

En el programa principal, puedes usarlo de la siguiente manera:

.. code-block:: python

    Vilib.detect_obj_parameter['color_x']

Las claves del diccionario y sus usos se describen en la siguiente lista:

* ``color_x``: Valor x de la coordenada central del bloque de color detectado (rango: 0~320).
* ``color_y``: Valor y de la coordenada central del bloque de color detectado (rango: 0~240).
* ``color_w``: Ancho del bloque de color detectado (rango: 0~320).
* ``color_h``: Altura del bloque de color detectado (rango: 0~240).
* ``color_n``: Cantidad de bloques de color detectados.
* ``human_x``: Valor x de la coordenada central del rostro detectado (rango: 0~320).
* ``human_y``: Valor y de la coordenada central del rostro detectado (rango: 0~240).
* ``human_w``: Ancho del rostro detectado (rango: 0~320).
* ``human_h``: Altura del rostro detectado (rango: 0~240).
* ``human_n``: Cantidad de rostros detectados.
* ``traffic_sign_x``: Valor x de la coordenada central de la señal de tráfico detectada (rango: 0~320).
* ``traffic_sign_y``: Valor y de la coordenada central de la señal de tráfico detectada (rango: 0~240).
* ``traffic_sign_w``: Ancho de la señal de tráfico detectada (rango: 0~320).
* ``traffic_sign_h``: Altura de la señal de tráfico detectada (rango: 0~240).
* ``traffic_sign_t``: Contenido de la señal de tráfico detectada (valores posibles: `['stop','right','left','forward']`).
* ``gesture_x``: Valor x de la coordenada central del gesto detectado (rango: 0~320).
* ``gesture_y``: Valor y de la coordenada central del gesto detectado (rango: 0~240).
* ``gesture_w``: Ancho del gesto detectado (rango: 0~320).
* ``gesture_h``: Altura del gesto detectado (rango: 0~240).
* ``gesture_t``: Contenido del gesto detectado (valores posibles: `["paper","scissor","rock"]`).
* ``qr_date``: Contenido del código QR detectado.
* ``qr_x``: Valor x de la coordenada central del código QR detectado (rango: 0~320).
* ``qr_y``: Valor y de la coordenada central del código QR detectado (rango: 0~240).
* ``qr_w``: Ancho del código QR detectado (rango: 0~320).
* ``qr_h``: Altura del código QR detectado (rango: 0~240).
