.. note:: 

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook. ¡Explora más a fondo Raspberry Pi, Arduino y ESP32 con otros entusiastas!

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y vistas previas.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

Para Usuarios de Windows
============================

Para usuarios de Windows 10 o superior, el acceso remoto a una Raspberry Pi se puede realizar siguiendo los siguientes pasos:

#. Busca ``powershell`` en el cuadro de búsqueda de Windows. Haz clic derecho en ``Windows PowerShell`` y selecciona ``Ejecutar como administrador``.

    .. image:: img/powershell_ssh.png
        :align: center

#. Determina la dirección IP de tu Raspberry Pi escribiendo ``ping -4 <hostname>.local`` en PowerShell.

    .. code-block::

        ping -4 raspberrypi.local

    .. image:: img/sp221221_145225.png
        :width: 550
        :align: center

    La dirección IP de la Raspberry Pi se mostrará una vez que esté conectada a la red.

    * Si el terminal muestra ``Ping request could not find host pi.local. Please check the name and try again.``, verifica que el nombre de host que ingresaste sea correcto.
    * Si aún no puedes obtener la dirección IP, revisa la configuración de red o WiFi en la Raspberry Pi.

#. Una vez confirmada la dirección IP, inicia sesión en tu Raspberry Pi utilizando ``ssh <username>@<hostname>.local`` o ``ssh <username>@<IP address>``.

    .. code-block::

        ssh pi@raspberrypi.local

    .. warning::

        Si aparece un error indicando ``The term 'ssh' is not recognized as the name of a cmdlet...``, es posible que tu sistema no tenga las herramientas SSH preinstaladas. En este caso, necesitas instalar manualmente OpenSSH siguiendo :ref:`openssh_powershell`, o usar una herramienta de terceros como PuTTY.

#. Durante tu primer inicio de sesión, aparecerá un mensaje de seguridad. Ingresa ``yes`` para continuar.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Ingresa la contraseña que configuraste previamente. Ten en cuenta que los caracteres de la contraseña no se mostrarán en pantalla, lo cual es una medida de seguridad estándar.

    .. note::
        La ausencia de caracteres visibles al escribir la contraseña es normal. Asegúrate de ingresar la contraseña correcta.

#. Una vez conectado, tu Raspberry Pi estará lista para operaciones remotas.

    .. image:: img/sp221221_140628.png
        :width: 550
        :align: center
