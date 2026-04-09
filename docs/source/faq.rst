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

P5: Sobre el cargador de batería
-------------------------------------------------------------------

Para cargar la batería, simplemente conecta una fuente de alimentación Type-C de 5V/2A al puerto de alimentación del Robot Hat. No es necesario encender el interruptor de alimentación del Robot Hat durante la carga.
También puedes usar el dispositivo mientras cargas la batería.

.. image:: img/robot_hat_pic.png
    :align: center
    :width: 500

Durante la carga, la energía de entrada es amplificada por el chip de carga para cargar la batería y, al mismo tiempo, alimentar el convertidor DC-DC para uso externo, con una potencia de carga de aproximadamente 10W.
Si el consumo de energía externa se mantiene alto durante un período prolongado, la batería puede complementar el suministro de energía, de manera similar a usar un teléfono mientras se carga. Sin embargo, ten en cuenta la capacidad de la batería para evitar que se agote por completo durante el uso y la carga simultáneos.

P6: Sobre la instalación de la PiCamera
-----------------------------------------------------

Instala la PiCamera según tu modelo de Raspberry Pi (Modelo Raspberry Pi 5/4/Zero 2 W).

.. raw:: html

    <iframe width="600" height="400" src="https://www.youtube.com/embed/vwsna5zb9o8?si=oNH6fxpg_XW0tS15" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>