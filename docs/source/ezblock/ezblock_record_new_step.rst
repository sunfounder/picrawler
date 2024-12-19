.. note:: 

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Adéntrate más en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _ezb_record:

Grabar un Nuevo Paso
==============================

Usamos la función remota para controlar a PiCrawler, haciéndolo realizar varias posturas en secuencia, y grabamos estas posturas para reproducirlas más tarde.

**Programa**

.. note::

    * Puedes escribir el programa según la siguiente imagen, consulta el tutorial: :ref:`ezblock:create_project_latest`.
    * O encuentra el código con el mismo nombre en la página de **Ejemplos** de EzBlock Studio y haz clic en **Ejecutar** o **Editar** directamente.

.. image:: img/record.png
    :width: 800

Cambia a la interfaz de Control Remoto y verás los siguientes widgets.

.. image:: img/sp210928_164343-1.png
    :width: 600

**¿Cómo funciona?**


Este proyecto se basa en :ref:`ezb_posture`, añadiendo funciones de grabación y reproducción.

La función de grabación se implementa con el siguiente código:

.. image:: img/sp210928_164449.png

La función de reproducción se implementa con el siguiente código:

.. image:: img/sp210928_164500.png