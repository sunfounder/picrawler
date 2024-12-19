.. note:: 

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Adéntrate más en Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y avances.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _ezb_avoid:

Evitación de obstáculos
=============================

En este proyecto, PiCrawler usará un módulo ultrasónico para detectar obstáculos al frente. 
Cuando PiCrawler detecte un obstáculo, enviará una señal y buscará otra dirección para avanzar.

.. image:: ../python/img/avoid1.png

**Programa**

.. note::

    * Puedes escribir el programa según la siguiente imagen. Consulta el tutorial: :ref:`ezblock:create_project_latest`.
    * O encuentra el código con el mismo nombre en la página de **Ejemplos** de EzBlock Studio y haz clic en **Ejecutar** o **Editar** directamente.

.. image:: img/avoid.png


**¿Cómo funciona?**

Puedes encontrar los siguientes bloques en la categoría **Módulo** para lograr la detección de distancia:

.. image:: img/sp210928_103046.png
    :width: 600

Es importante destacar que los dos pines del bloque deben corresponder al cableado real, es decir, trig-D2, echo-D3.

Aquí está el programa principal:

* Lee la ``distancia`` detectada por el módulo ultrasónico y filtra los valores menores que 0 (cuando el módulo ultrasónico está demasiado lejos del obstáculo o no puede leer los datos correctamente, aparecerá ``distance<0``).
* Cuando la ``distancia`` es menor que ``alert_distance`` (el valor umbral establecido previamente, que es 10), reproduce el efecto de sonido ``sign.wav``. PiCrawler realiza un ``giro a la izquierda``.
* Cuando la ``distancia`` es mayor que ``alert_distance``, PiCrawler avanzará hacia ``adelante``.
