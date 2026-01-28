.. note:: 

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook. ¡Explora más a fondo Raspberry Pi, Arduino y ESP32 con otros entusiastas!

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y vistas previas.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

Calibrar el PiCrawler
=============================

Debido a posibles desviaciones durante la instalación del PiCrawler o limitaciones de los propios servos, algunos ángulos de los servos pueden estar ligeramente desalineados, por lo que puedes calibrarlos.

Por supuesto, puedes omitir este capítulo si crees que el ensamblaje es perfecto y no requiere calibración.


Los pasos específicos son los siguientes:

1. Saca el folleto de ensamblaje, ábrelo en la última página y colócalo sobre la mesa. Luego coloca el PiCrawler como se muestra a continuación, alineando su base con el contorno en la tabla de calibración.

    .. image:: img/calibration2.png

#. Ejecuta el archivo ``calibration.py``.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/picrawler/examples/calibration
        sudo python3 calibration.py
        
    Después de ejecutar el código anterior, verás la siguiente interfaz mostrada en el terminal.

    .. image:: img/calibration1.png

#. Presiona las teclas ``2`` y ``3`` respectivamente para seleccionar las dos patas izquierdas. Luego presiona las teclas ``w``, ``a``, ``s``, ``d``, ``r`` y ``f`` para moverlas al punto de calibración.

    .. image:: img/calibration3.png

#. Ahora, cambia el papel de calibración hacia la derecha y presiona las teclas ``1`` y ``4`` para seleccionar las dos patas derechas. Luego, presiona las teclas ``w``, ``a``, ``s``, ``d``, ``r`` y ``f`` para moverlas al punto de calibración.

    .. image:: img/calibration4.png

#. Una vez completada la calibración, presiona la tecla ``espacio`` para guardar. Se te pedirá que ingreses ``Y`` para confirmar, y luego ``ctrl+c`` para salir del programa y completar la calibración.

    .. image:: img/calibration5.png



