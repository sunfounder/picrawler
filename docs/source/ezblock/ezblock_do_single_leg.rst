.. note:: 

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Adéntrate más en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _ezb_posture:

Ajustar Postura
==========================

En este ejemplo, utilizamos la función remota para controlar pie por pie al PiCrawler y asumir la postura deseada.

Puedes presionar el botón para imprimir los valores de las coordenadas actuales. Estos valores son útiles cuando creas acciones únicas para el PiCrawler.

.. image:: ../python/img/1cood.A.png


**Programa**

.. note::

    * Puedes escribir el programa según la siguiente imagen. Consulta el tutorial: :ref:`ezblock:create_project_latest`.
    * O encuentra el código con el mismo nombre en la página de **Ejemplos** de EzBlock Studio y haz clic en **Ejecutar** o **Editar** directamente.

.. image:: img/do_single_leg.png
    :width: 800

Cambia a la interfaz de Control Remoto y verás los siguientes widgets.

.. image:: img/do_single_leg_B-1.png
    :width: 600

**¿Cómo funciona?**

Lo que necesitas prestar atención en este proyecto son los siguientes tres bloques:

.. image:: img/sp210928_115847.png

Modifica individualmente el valor de coordenada de una pierna específica.

.. image:: img/sp210928_115908.png

Devuelve el valor de coordenada de la pierna correspondiente.

.. image:: img/sp210928_115958.png


Podrías simplificar el programa con Funciones, especialmente cuando realizas la misma operación varias veces. Incluir estas operaciones en una función recién declarada puede facilitar en gran medida su uso.

.. image:: img/sp210928_135733.png
    :width: 500