.. note::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Adéntrate más en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y avances exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _ezb_vision:

Visión por Computadora
=============================

¡Este proyecto te permitirá entrar oficialmente en el campo de la visión por computadora!

.. note:: 
    
    Puedes leer :ref:`ezblock:video_latest`. Realiza este proyecto sin contratiempos.

**Programa**

.. note::

    * Puedes escribir el programa según la siguiente imagen. Consulta el tutorial: :ref:`ezblock:create_project_latest`.
    * O encuentra el código con el mismo nombre en la página de **Ejemplos** de EzBlock Studio y haz clic en **Ejecutar** o **Editar** directamente.

.. image:: img/sp210928_165255.png
    :width: 800

Cambia a la interfaz de Control Remoto y verás los siguientes widgets.

.. image:: img/sp210928_165642.png

Después de ejecutar el programa, puedes usar el control deslizante para activar/desactivar la detección facial; hacer clic en el D-Pad para seleccionar el color de la detección; o hacer clic en el botón para imprimir el resultado de la detección.

**¿Cómo funciona?**

.. image:: img/sp210928_170920.png

Este bloque se utiliza para activar el módulo de cámara.

.. image:: img/sp210928_171021.png
    :width: 400

Estos dos bloques se usan para habilitar la función de detección facial o detección de color.

.. image:: img/sp210928_171125.png
    :width: 400

Estos dos bloques se utilizan para generar información. El resultado de la detección contiene cinco valores de salida: coordenada x, coordenada y, ancho, altura y número.
