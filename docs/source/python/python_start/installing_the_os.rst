.. note:: 

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook. ¡Explora más a fondo Raspberry Pi, Arduino y ESP32 con otros entusiastas!

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y vistas previas.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _install_os_sd:

2. Instalación del Sistema Operativo
============================================================


**Componentes Necesarios**

* Un ordenador personal
* Una tarjeta Micro SD y un lector

1. Instalar Raspberry Pi Imager
----------------------------------

#. Visita la página de descarga de software de Raspberry Pi en `Raspberry Pi Imager <https://www.raspberrypi.org/software/>`_. Selecciona la versión de Imager compatible con tu sistema operativo. Descarga y abre el archivo para iniciar la instalación.

    .. image:: img/os_install_imager.png
        :align: center

#. Durante la instalación, podría aparecer un mensaje de seguridad dependiendo de tu sistema operativo. Por ejemplo, Windows podría mostrar una advertencia. En ese caso, selecciona **Más información** y luego **Ejecutar de todas formas**. Sigue las instrucciones en pantalla para completar la instalación de Raspberry Pi Imager.

    .. image:: img/os_info.png
        :align: center

#. Inicia la aplicación Raspberry Pi Imager haciendo clic en su icono o escribiendo ``rpi-imager`` en tu terminal.

    .. image:: img/os_open_imager.png
        :align: center

2. Instalar el Sistema Operativo en la Tarjeta Micro SD
-----------------------------------------------------------

#. Inserta tu tarjeta SD en tu ordenador o portátil utilizando un lector.

#. Dentro de Imager, haz clic en **Raspberry Pi Device** y selecciona el modelo de Raspberry Pi desde el menú desplegable.

    .. image:: img/os_choose_device.png
        :align: center

#. Selecciona **Sistema Operativo** y elige la versión recomendada del sistema operativo.

    .. image:: img/os_choose_os.png
        :align: center

#. Haz clic en **Elegir Almacenamiento** y selecciona el dispositivo de almacenamiento adecuado para la instalación.

    .. note::

        Asegúrate de seleccionar el dispositivo de almacenamiento correcto. Para evitar confusiones, desconecta cualquier dispositivo de almacenamiento adicional si hay varios conectados.

    .. image:: img/os_choose_sd.png
        :align: center

#. Haz clic en **SIGUIENTE** y luego en **EDITAR CONFIGURACIONES** para personalizar la configuración del sistema operativo.

    .. note::

        Si tienes un monitor para tu Raspberry Pi, puedes omitir los siguientes pasos y hacer clic en "Sí" para comenzar la instalación. Ajusta otras configuraciones más tarde en el monitor.

    .. image:: img/os_enter_setting.png
        :align: center

#. Define un **nombre de host** para tu Raspberry Pi.

    .. note::

        El nombre de host es el identificador de red de tu Raspberry Pi. Puedes acceder a tu Pi utilizando ``<hostname>.local`` o ``<hostname>.lan``.

    .. image:: img/os_set_hostname.png
        :align: center

#. Crea un **Nombre de Usuario** y una **Contraseña** para la cuenta de administrador de la Raspberry Pi.

    .. note::

        Establecer un nombre de usuario y contraseña únicos es vital para asegurar tu Raspberry Pi, ya que no tiene una contraseña predeterminada.

    .. image:: img/os_set_username.png
        :align: center

#. Configura la red inalámbrica proporcionando el **SSID** y la **Contraseña** de tu red.

    .. note::

        Ajusta el campo ``País de LAN inalámbrica`` con el código de dos letras `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ correspondiente a tu ubicación.

    .. image:: img/os_set_wifi.png
        :align: center

#. Para conectarte remotamente a tu Raspberry Pi, habilita SSH en la pestaña de Servicios.

    * Para **autenticación por contraseña**, utiliza el nombre de usuario y contraseña de la pestaña General.
    * Para autenticación con clave pública, selecciona "Permitir autenticación solo con clave pública". Si tienes una clave RSA, se utilizará. Si no, haz clic en "Ejecutar SSH-keygen" para generar un nuevo par de claves.

    .. image:: img/os_enable_ssh.png
        :align: center

#. El menú **Opciones** te permite configurar el comportamiento de Imager durante la escritura, incluyendo reproducir un sonido al finalizar, expulsar el medio al terminar y habilitar la telemetría.

    .. image:: img/os_options.png
        :align: center

#. Cuando termines de ingresar las configuraciones de personalización del sistema operativo, haz clic en **Guardar** para guardar tus ajustes. Luego, haz clic en **Sí** para aplicarlos al escribir la imagen.

    .. image:: img/os_click_yes.png
        :align: center

#. Si la tarjeta SD contiene datos existentes, asegúrate de hacer una copia de seguridad para evitar la pérdida de datos. Haz clic en **Sí** para continuar si no necesitas realizar un respaldo.

    .. image:: img/os_continue.png
        :align: center

#. Cuando veas la ventana emergente "Escritura Exitosa", la imagen se ha escrito y verificado completamente. ¡Ahora estás listo para iniciar una Raspberry Pi desde la Tarjeta Micro SD!

    .. image:: img/os_finish.png
        :align: center

#. Ahora puedes insertar la tarjeta SD configurada con Raspberry Pi OS en la ranura microSD ubicada en la parte inferior de la Raspberry Pi.

    .. image:: img/insert_sd_card.png
        :width: 500
        :align: center