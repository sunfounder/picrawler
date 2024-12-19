.. note:: 

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Adéntrate más en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _ezb_remote:

Control Remoto
=========================

En este proyecto, aprenderemos a controlar remotamente el PiCrawler. 
Puedes controlar el PiCrawler para que avance, retroceda, gire a la izquierda o a la derecha.

.. image:: img/remote_control.png

.. note:: 

    Puedes consultar :ref:`ezblock:remote_control_latest`. ¡Realiza este proyecto sin problemas!

**Programa**

.. note::

    * Puedes escribir el programa según la siguiente imagen, consulta el tutorial: :ref:`ezblock:create_project_latest`.
    * O encuentra el código con el mismo nombre en la página de **Ejemplos** de EzBlock Studio y haz clic en **Ejecutar** o **Editar** directamente.

.. image:: img/remote.png

Cambia a la interfaz de Control Remoto, y verás los siguientes widgets.

.. image:: img/remote_B.png

Después de que el programa esté en ejecución, puedes activar el PiCrawler mediante el D-Pad.

**¿Cómo funciona?**

Después de arrastrar el widget a la interfaz de Control Remoto, aparecerá una categoría llamada **Remote** en la columna de categorías de bloques de la interfaz de programación.

Aquí agregamos el widget D-Pad, por lo que el bloque **D-Pad get value** aparece aquí.

.. image:: img/sp210927_180739.png

El D-Pad puede considerarse como un botón cuatro en uno. Puedes elegir qué botón leer en la segunda ranura del bloque.

Cuando se presiona el botón, el valor es "1"; cuando no se presiona, el valor es "0".

.. image:: img/sp210927_182447.png
    :width: 200

Usamos un bloque **if** (puedes encontrarlo en la categoría **Lógica** a la izquierda) para hacer que el PiCrawler avance una vez cuando se presiona el botón **UP** del D-Pad.

.. image:: img/sp210927_182828.png
    :width: 600

Puedes hacer clic en el ícono de engranaje en la esquina superior izquierda del bloque para modificar la forma del bloque **if** y realizar múltiples ramas de juicio.

.. image:: img/sp210927_183237.png
    :width: 300

El bloque **if** generalmente se usa con el bloque **=**, el cual puede modificarse a **>**, **<** y otras condiciones a través del menú desplegable. Úsalo de manera flexible.
