.. note:: 

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Adéntrate más en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _ezb_move:

Moverse
=================

Este es el primer proyecto de PiCrawler. Realiza su función más básica: moverse.

.. .. image:: ../python/img/move.png

**Programa**

.. note::

    * Puedes escribir el programa según la siguiente imagen, consulta el tutorial: :ref:`ezblock:create_project_latest`.
    * O encuentra el código con el mismo nombre en la página de **Ejemplos** de EzBlock Studio y haz clic en **Ejecutar** o **Editar** directamente.

.. image:: img/move.png

Haz clic en el botón **Subir y Ejecutar** en la parte inferior derecha de la pantalla, y PiCrawler ejecutará las acciones de "adelante" y "atrás" en secuencia.


**¿Cómo funciona?**

Primero, necesitas comprender la estructura del programa en Ezblock, como se muestra a continuación:

.. image:: img/sp210927_162828.png
    :width: 200

Todos los proyectos de Ezblock contienen estos dos bloques. El bloque **Inicio** se ejecuta al comienzo del programa y solo una vez; a menudo se utiliza para establecer variables. El bloque **Siempre** se ejecuta después de **Inicio** y se ejecutará repetidamente, generalmente para implementar las funciones principales.
Si eliminas estos dos bloques, puedes arrastrarlos nuevamente desde la categoría **Básico** a la izquierda.

A continuación, debes comprender los siguientes bloques:

.. image:: img/sp210927_165133.png

**do action** permite que PiCrawler realice acciones básicas. Puedes modificar las opciones en la primera ranura, por ejemplo, seleccionar "Girar a la izquierda", "Retroceder", entre otras.
La segunda ranura puede establecer el número de ejecuciones de la acción, y solo se pueden escribir números enteros mayores a 0.
La tercera ranura puede establecer la velocidad de la acción, y solo se pueden escribir números enteros dentro del rango 0~100.

.. image:: img/sp210927_170717.png
    :width: 500

**do step** es similar a **do action**, pero no es una acción sino una postura estática, como "pararse" o "sentarse".


Ambos bloques se pueden arrastrar desde la categoría **PiCrawler** a la izquierda.
