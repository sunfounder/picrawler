.. note:: 

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook. ¡Explora más a fondo Raspberry Pi, Arduino y ESP32 con otros entusiastas!

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y vistas previas.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

FAQ
===========================

P1: Después de instalar Ezblock OS, ¿el servo no puede girar a 0°?
----------------------------------------------------------------------

1) Verifica si el cable del servo está conectado correctamente y si la alimentación del Robot HAT está encendida.
2) Presiona el botón de reinicio.
3) Si ya ejecutaste el programa en Ezblock Studio, el programa personalizado para P11 ya no estará disponible. Puedes consultar la imagen a continuación para escribir manualmente un programa en Ezblock Studio que configure el ángulo del servo a 0°.

.. image:: img/faq_servo.png

P2: Al usar VNC, ¿me aparece un mensaje indicando que el escritorio no se puede mostrar en este momento?
---------------------------------------------------------------------------------------------------------------

En el Terminal, escribe ``sudo raspi-config`` para cambiar la resolución.

P3: ¿Por qué a veces el servo regresa a la posición central sin razón aparente?
------------------------------------------------------------------------------------

Cuando el servo está bloqueado por una estructura u otro objeto y no puede alcanzar su posición deseada, entra en modo de protección por apagado para evitar que se queme debido a un exceso de corriente.

Después de un período de apagado, si no se envía una señal PWM al servo, este volverá automáticamente a su posición original.

P4: ¿Dónde puedo encontrar el tutorial detallado sobre el Robot HAT?
------------------------------------------------------------------------

Puedes encontrar un tutorial completo sobre el Robot HAT aquí, que incluye información sobre su hardware y API.

* |link_robot_hat|