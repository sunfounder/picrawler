.. note:: 

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook. ¡Explora más a fondo Raspberry Pi, Arduino y ESP32 con otros entusiastas!

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y vistas previas.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _install_all_modules:

5. Instalar Todos los Módulos (Importante)
===============================================

Asegúrate de estar conectado a Internet y actualiza tu sistema:

.. raw:: html

    <run></run>

.. code-block::

    sudo apt update
    sudo apt upgrade

.. note::

    Los paquetes relacionados con Python3 deben estar instalados si estás utilizando la versión Lite del sistema operativo.

    .. raw:: html

        <run></run>

    .. code-block::
    
        sudo apt install git python3-pip python3-setuptools python3-smbus

Instala el módulo ``robot-hat``.

.. raw:: html

    <run></run>

.. code-block::

    cd ~/
    git clone -b v2.0 https://github.com/sunfounder/robot-hat.git
    cd robot-hat
    sudo python3 setup.py install

Luego descarga el código e instala el módulo ``vilib``.

.. raw:: html

    <run></run>

.. code-block::

    cd ~/
    git clone -b picamera2 https://github.com/sunfounder/vilib.git
    cd vilib
    sudo python3 install.py

Luego descarga el código e instala el módulo ``picrawler``.

.. raw:: html

    <run></run>

.. code-block::

    cd ~/
    git clone https://github.com/sunfounder/picrawler.git
    cd picrawler
    sudo python3 setup.py install

Este paso tomará un poco de tiempo, así que por favor ten paciencia.

Finalmente, necesitas ejecutar el script ``i2samp.sh`` para instalar los componentes requeridos por el amplificador i2s; de lo contrario, el PiSlot no tendrá sonido.

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler
    sudo bash i2samp.sh
	
.. image:: img/i2s.png

Escribe ``y`` y presiona ``Enter`` para continuar ejecutando el script.

.. image:: img/i2s2.png

Escribe ``y`` y presiona ``Enter`` para ejecutar ``/dev/zero`` en segundo plano.

.. image:: img/i2s3.png

Escribe ``y`` y presiona ``Enter`` para reiniciar la máquina.

.. note::
    Si no hay sonido después de reiniciar, es posible que necesites ejecutar el script ``i2samp.sh`` varias veces.
