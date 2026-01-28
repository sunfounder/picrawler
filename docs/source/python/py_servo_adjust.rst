.. note:: 

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook. ¡Explora más a fondo Raspberry Pi, Arduino y ESP32 con otros entusiastas!

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y vistas previas.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

Ajuste del Servo (Importante)
===================================

.. note::

    Si tu Robot HAT es versión V44 o superior (con el altavoz ubicado en la parte superior de la placa) e incluye un botón **Zero** integrado, puedes omitir este paso y simplemente presionar el botón **Zero** para activar el programa de calibración de servos.

    .. image:: img/robot_hat_v44.png
        :width: 500
        :align: center


El rango de ángulo del servo es de -90° a 90°, pero el ángulo configurado en fábrica es aleatorio, puede ser 0°, 45°, etc. Si ensamblamos el robot con este ángulo directamente, podría causar un estado caótico al ejecutar el código o, peor aún, bloquear y dañar el servo.

Por lo tanto, necesitamos configurar todos los servos en 0° antes de instalarlos, asegurándonos de que estén centrados, sin importar hacia qué dirección giren.

#. Para garantizar que el servo esté correctamente configurado en 0°, primero inserta el brazo del servo en el eje del servo y luego gira suavemente el brazo hacia un ángulo diferente. Este brazo del servo se utiliza solo para verificar visualmente la rotación del servo.

    .. image:: img/servo_arm.png
        :align: center

#. Ahora, ejecuta ``servo_zeroing.py`` en la carpeta ``examples/``.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/picrawler/examples
        sudo python3 servo_zeroing.py

#. A continuación, conecta el cable del servo al puerto P11 como se muestra. Al mismo tiempo, observarás que el brazo del servo gira hacia una posición (esta es la posición de 0°, que puede no ser completamente vertical o paralela).

    .. image:: img/servo_pin11.jpg

#. Retira ahora el brazo del servo, asegurándote de que el cable del servo permanezca conectado, y no apagues la energía. Continúa con el ensamblaje siguiendo las instrucciones del manual.

.. note::

    * No desconectes el cable del servo antes de fijarlo con el tornillo del servo; puedes desconectarlo después de fijarlo.
    * No gires el servo mientras está encendido para evitar daños; si el eje del servo no está insertado en el ángulo correcto, retira el servo e insértalo nuevamente.
    * Antes de ensamblar cada servo, debes conectar el cable del servo al pin PWM y encender la energía para configurar su ángulo en 0°.
