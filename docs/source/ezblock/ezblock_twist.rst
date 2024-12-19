.. note:: 

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Adéntrate más en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _ezb_twist:

Giro
==================

Ya sabemos cómo hacer que PiCrawler asuma una postura específica; el siguiente paso es combinar las posturas para formar una acción continua.

Aquí, las cuatro patas de PiCrawler se mueven arriba y abajo en pares, saltando al ritmo de la música.

**Programa**

.. note::

    * Puedes escribir el programa según la siguiente imagen, consulta el tutorial: :ref:`ezblock:create_project_latest`.
    * O encuentra el código con el mismo nombre en la página de **Ejemplos** de EzBlock Studio y haz clic en **Ejecutar** o **Editar** directamente.

.. image:: img/twist.png
    :width: 800

**¿Cómo funciona?**

Utiliza dos capas de bucles for para que la matriz ``new_step`` produzca cambios continuos y regulares, y al mismo tiempo, **do step** ejecuta las posturas para formar una acción continua.

Puedes obtener intuitivamente la matriz de valores de coordenadas correspondiente a cada postura desde :ref:`ezb_posture`.

Un aspecto que necesitas tener en cuenta es este bloque de matriz de coordenadas:

.. image:: img/sp210928_154257.png
    
Es esencialmente una matriz bidimensional, que se puede procesar mediante bloques en la categoría **Lista**. Su estructura es ``[[frontal derecha],[frontal izquierda],[trasera izquierda],[trasera derecha]]``.
En otras palabras, en este ejemplo, ``new_step#1`` corresponde a la pata frontal derecha; ``new_step#2`` corresponde a la pata frontal izquierda; ``new_step#3`` corresponde a la pata trasera izquierda; y ``new_step#4`` corresponde a la pata trasera derecha.
