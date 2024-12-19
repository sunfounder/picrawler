.. note:: 

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Adéntrate más en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _ezb_treasure:

Búsqueda del Tesoro
============================

Organiza un laberinto en tu habitación y coloca seis tarjetas de diferentes colores en seis esquinas. Luego, controla a PiCrawler para buscar estas tarjetas de colores una por una.

.. note:: Puedes descargar e imprimir las :download:`Tarjetas de Colores en PDF <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>` para la detección de colores.

**Programa**

.. note::

    * Puedes escribir el programa según la siguiente imagen, consulta el tutorial: :ref:`ezblock:create_project_latest`.
    * O encuentra el código con el mismo nombre en la página de **Ejemplos** de EzBlock Studio y haz clic en **Ejecutar** o **Editar** directamente.

.. image:: img/sp210928_181036.png
    :width: 800

Cambia a la interfaz de Control Remoto, y verás los siguientes widgets.

.. image:: img/sp210928_181134.png
    :width: 800


**¿Cómo funciona?**

En general, este proyecto combina los puntos de conocimiento de :ref:`ezb_remote`, :ref:`ezb_vision` y :ref:`ezb_sound`.

Su flujo se muestra en la siguiente figura:

.. image:: ../python/img/treasure_hunt-f.png
    :width: 600