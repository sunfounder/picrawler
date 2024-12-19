.. note:: 

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook. ¡Explora más a fondo Raspberry Pi, Arduino y ESP32 con otros entusiastas!

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y vistas previas.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _i2c_spi_config:

6. Verificar la interfaz I2C
========================================

Usaremos la interfaz I2C del Raspberry Pi. Esta interfaz debió haberse habilitado al instalar el módulo ``robot-hat`` anteriormente. Para asegurarnos de que todo está en orden, verifiquemos si está habilitada.

#. Ingresa el siguiente comando:

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. Selecciona **Interfacing Options** presionando la tecla de flecha hacia abajo en tu teclado, luego presiona la tecla **Enter**.

    .. image:: img/image282.png
        :align: center

#. Luego selecciona **I2C**.

    .. image:: img/image283.png
        :align: center

#. Usa las teclas de flecha en el teclado para seleccionar **<Yes>** -> **<OK>** y completa la configuración del I2C.

    .. image:: img/image284.png
        :align: center