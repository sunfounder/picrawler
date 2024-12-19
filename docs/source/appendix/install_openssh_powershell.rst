.. note:: 

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Adéntrate más en Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y avances.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _openssh_powershell:

Instalar OpenSSH a través de PowerShell
=============================================

Cuando intentas usar ``ssh <nombre_usuario>@<nombre_host>.local`` (o ``ssh <nombre_usuario>@<dirección_IP>``) para conectarte a tu Raspberry Pi y aparece el siguiente mensaje de error:

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.


Significa que tu sistema operativo es demasiado antiguo y no tiene `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ preinstalado. Necesitas seguir el tutorial a continuación para instalarlo manualmente.

#. Escribe ``powershell`` en el cuadro de búsqueda de tu escritorio de Windows, haz clic derecho sobre ``Windows PowerShell`` y selecciona ``Ejecutar como administrador`` en el menú que aparece.

    .. image:: img/powershell_ssh.png
        :align: center

#. Usa el siguiente comando para instalar ``OpenSSH.Client``:

    .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. Después de la instalación, se mostrará el siguiente resultado:

    .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. Verifica la instalación usando el siguiente comando:

    .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. Ahora te indicará que ``OpenSSH.Client`` se ha instalado correctamente.

    .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

    .. warning:: 
        Si no aparece el mensaje anterior, significa que tu sistema Windows es demasiado antiguo y se recomienda instalar una herramienta SSH de terceros, como PuTTY.

#. Reinicia PowerShell y continúa ejecutándolo como administrador. En este punto, podrás iniciar sesión en tu Raspberry Pi usando el comando ``ssh``, donde se te pedirá que ingreses la contraseña que configuraste previamente.

    .. image:: img/powershell_login.png