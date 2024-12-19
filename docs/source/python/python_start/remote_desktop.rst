.. note:: 

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook. ¡Explora más a fondo Raspberry Pi, Arduino y ESP32 con otros entusiastas!

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y vistas previas.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _remote_desktop:

Acceso Remoto al Escritorio de Raspberry Pi
==================================================

Para aquellos que prefieren una interfaz gráfica de usuario (GUI) en lugar de acceso por línea de comandos, Raspberry Pi admite funcionalidad de escritorio remoto. Esta guía te explicará cómo configurar y usar VNC (Computación en Red Virtual) para el acceso remoto.

Recomendamos usar `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ para este propósito.

**Habilitar el servicio VNC en Raspberry Pi**

El servicio VNC viene preinstalado en Raspberry Pi OS, pero está deshabilitado por defecto. Sigue estos pasos para activarlo:

#. Ingresa el siguiente comando en el terminal de Raspberry Pi:

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. Navega a **Interfacing Options** usando la tecla de flecha hacia abajo y presiona **Enter**.

    .. image:: img/config_interface.png
        :align: center

#. Selecciona **VNC** de las opciones.

    .. image:: img/vnc.png
        :align: center

#. Usa las teclas de flecha para elegir **<Yes>** -> **<OK>** -> **<Finish>** y finaliza la activación del servicio VNC.

    .. image:: img/vnc_yes.png
        :align: center

**Iniciar sesión a través de VNC Viewer**

#. Descarga e instala `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ en tu computadora personal.

#. Una vez instalado, lanza VNC Viewer. Ingresa el nombre del host o la dirección IP de tu Raspberry Pi y presiona Enter.

    .. image:: img/vnc_viewer1.png
        :align: center

#. Cuando se te solicite, ingresa el nombre de usuario y la contraseña de tu Raspberry Pi, luego haz clic en **OK**.

    .. image:: img/vnc_viewer2.png
        :align: center

#. Después de unos segundos, se mostrará el escritorio de Raspberry Pi OS. Ahora puedes abrir el Terminal para comenzar a ingresar comandos.

    .. image:: img/bookwarm.png
        :align: center
