.. note:: 

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook. ¡Explora más a fondo Raspberry Pi, Arduino y ESP32 con otros entusiastas!

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y vistas previas.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _ezb_servo_adjust:

Guía rápida sobre EzBlock
=============================

.. note::

    Si estás usando una Raspberry Pi 5, nuestro software de programación gráfica, EzBlock, no es compatible.

El rango de ángulo del servo es de -90° a 90°, pero el ángulo configurado en fábrica es aleatorio, podría ser 0°, 45° u otro valor; si ensamblamos el robot directamente con este ángulo, podría llevar a un estado caótico al ejecutar el código, o peor aún, podría causar que el servo se bloquee y se queme.

Por lo tanto, necesitamos configurar todos los ángulos del servo en 0° antes de instalarlos, de manera que el ángulo del servo quede en el centro, sin importar hacia qué dirección gire.

#. Primero, sigue el tutorial :ref:`ezblock:install_ezblock_os_latest` (tutorial propio de EzBlock) para instalar EzBlock en una tarjeta Micro SD. Una vez completada la instalación, insértala en la Raspberry Pi.

    .. note::
        Después de completar la instalación, regresa a esta página.

    .. image:: img/insert_sd_card.png
        :width: 500
        :align: center

#. Para asegurarte de que el servo está correctamente configurado en 0°, primero inserta el brazo del servo en el eje del servo y luego gira suavemente el brazo a un ángulo diferente. Esto te permitirá observar claramente el movimiento del servo.

    .. image:: img/servo_arm.png

#. Sigue las instrucciones en el manual de ensamblaje, inserta el cable de la batería y enciende el interruptor de encendido. Luego conecta un cable USB-C alimentado para activar la batería. Espera de 1 a 2 minutos hasta que escuches un sonido indicando que la Raspberry Pi ha arrancado correctamente.

    .. image:: img/Z_BTR.JPG
        :width: 800
        :align: center

#. A continuación, conecta el cable del servo al puerto P11 como se muestra.

    .. image:: img/Z_P11.JPG

#. Mantén presionada la tecla **USR**, luego presiona la tecla **RST** para ejecutar el script de cero de servos en el sistema. Cuando veas que el brazo del servo gira hacia una posición (esta es la posición 0°, que podría no ser vertical o paralela), indica que el programa se ha ejecutado.

    .. note::

        Este paso solo necesita realizarse una vez; después, simplemente conecta otros cables de servo y se ajustarán automáticamente a cero.

    .. image:: img/Z_P11_BT.png
        :width: 400
        :align: center
    
#. Ahora, retira el brazo del servo, asegurándote de que el cable del servo permanezca conectado, y no apagues la energía. Luego continúa el ensamblaje siguiendo las instrucciones del manual.

.. note::

    * No desconectes este cable del servo antes de fijarlo con el tornillo, puedes desconectarlo después de fijarlo.
    * No gires el servo mientras está encendido para evitar daños; si el eje del servo no está insertado en el ángulo correcto, retira el servo y vuelve a insertarlo.
    * Antes de ensamblar cada servo, necesitas conectar el cable del servo al puerto P11 y encender la energía para configurar su ángulo a 0°.
    * Esta función de ajuste a cero se desactivará si descargas un programa al robot más adelante con la aplicación EzBlock.
