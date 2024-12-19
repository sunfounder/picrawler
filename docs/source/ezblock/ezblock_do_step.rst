.. note:: 

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Adéntrate más en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _ezb_pose:

Postura
===============

PiCrawler puede asumir una postura específica escribiendo un array de coordenadas. Aquí asume una postura con la pata trasera derecha levantada.

.. image:: ../python/img/4cood.A.png

**Programa**

.. note::

    * Puedes escribir el programa según la siguiente imagen, consulta el tutorial: :ref:`ezblock:create_project_latest`.
    * O encuentra el código con el mismo nombre en la página de **Ejemplos** de EzBlock Studio y haz clic en **Ejecutar** o **Editar** directamente.

.. image:: img/dostep.png


**¿Cómo funciona?**

En este código, lo que debes prestar atención es a este bloque **do step**.

Tiene dos usos:

Primero: Puede usarse directamente con **stand** o **sit**.

Segundo: También puede escribir un array de 4 valores de coordenadas.

Cada pata tiene un sistema de coordenadas independiente. Como se muestra a continuación:

.. image:: ../python/img/4cood.png

Debes medir las coordenadas de cada dedo individualmente. Como se muestra a continuación:

.. image:: ../python/img/1cood.png
