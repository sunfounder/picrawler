.. note:: 

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook. ¡Explora más a fondo Raspberry Pi, Arduino y ESP32 con otros entusiastas!

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y vistas previas.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

Módulo Ultrasónico
================================

.. image:: img/ultrasonic_pic.png
    :width: 400
    :align: center

* **TRIG**: Entrada de pulso de activación
* **ECHO**: Salida de pulso de eco
* **GND**: Tierra
* **VCC**: Suministro de 5V

Este es el sensor ultrasónico de distancia HC-SR04, que proporciona medición sin contacto desde 2 cm hasta 400 cm con una precisión de hasta 3 mm. Incluye un transmisor ultrasónico, un receptor y un circuito de control.

Solo necesitas conectar 4 pines: VCC (alimentación), Trig (disparador), Echo (recepción) y GND (tierra) para facilitar su uso en proyectos de medición.

**Características**

* Voltaje de trabajo: DC5V
* Corriente de trabajo: 16mA
* Frecuencia de trabajo: 40Hz
* Rango máximo: 500cm
* Rango mínimo: 2cm
* Señal de entrada de activación: Pulso TTL de 10uS
* Señal de salida de eco: Señal de nivel TTL proporcional al rango
* Conector: XH2.54-4P
* Dimensiones: 46x20.5x15 mm

**Principio**

Los principios básicos son los siguientes:

* Usar el disparador IO para enviar una señal de nivel alto durante al menos 10us.
* El módulo emite una ráfaga de 8 ciclos de ultrasonido a 40 kHz y detecta si se recibe una señal de pulso.
* Echo enviará un nivel alto si se devuelve una señal; la duración del nivel alto es el tiempo desde la emisión hasta el retorno.
* Distancia = (tiempo de nivel alto x velocidad del sonido (340M/S)) / 2

    .. image:: img/ultrasonic_prin.jpg
        :width: 800

Fórmula: 

* us / 58 = distancia en centímetros
* us / 148 = distancia en pulgadas
* distancia = tiempo de nivel alto x velocidad (340M/S) / 2


**Notas de Aplicación**

* Este módulo no debe conectarse mientras esté encendido; si es necesario, conecta primero el GND del módulo. De lo contrario, afectará su funcionamiento.
* El área del objeto a medir debe ser al menos de 0.5 metros cuadrados y lo más plana posible. De lo contrario, afectará los resultados.
