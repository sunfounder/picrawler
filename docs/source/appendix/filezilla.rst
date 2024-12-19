.. note:: 

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Adéntrate más en Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones exclusivas**: Accede anticipadamente a anuncios de nuevos productos y avances exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _filezilla:

Software Filezilla
==========================

.. image:: img/filezilla_icon.png

El Protocolo de Transferencia de Archivos (FTP) es un protocolo estándar de comunicación utilizado para la transferencia de archivos de un servidor a un cliente en una red informática.

Filezilla es un software de código abierto que no solo admite FTP, sino también FTP sobre TLS (FTPS) y SFTP. Podemos usar Filezilla para cargar archivos locales (como imágenes y audio, etc.) al Raspberry Pi, o descargar archivos desde el Raspberry Pi al ordenador local.

**Paso 1**: Descarga Filezilla.

Descarga el cliente desde `el sitio web oficial de Filezilla <https://filezilla-project.org/>`_. Filezilla cuenta con un tutorial muy útil, por favor consulta: `Documentación - Filezilla <https://wiki.filezilla-project.org/Documentation>`_.

**Paso 2**: Conectar al Raspberry Pi

Después de una instalación rápida, ábrelo y ahora `conéctalo a un servidor FTP <https://wiki.filezilla-project.org/Using#Connecting_to_an_FTP_server>`_. Tiene 3 formas de conectarse, aquí usamos la barra **Conexión rápida**. Ingresa el **nombre de host/IP**, **nombre de usuario**, **contraseña** y **puerto (22)**, luego haz clic en **Conexión rápida** o presiona **Enter** para conectarte al servidor.

.. image:: img/filezilla_connect.png

.. note::

    Conexión rápida es una buena forma de probar tu información de inicio de sesión. Si deseas crear una entrada permanente, puedes seleccionar **Archivo** -> **Copiar conexión actual al Administrador de sitios** después de una conexión rápida exitosa, ingresa el nombre y haz clic en **OK**. La próxima vez podrás conectarte seleccionando el sitio previamente guardado dentro de **Archivo** -> **Administrador de sitios**.
    
    .. image:: img/ftp_site.png

**Paso 3**: Subir/descargar archivos.

Puedes cargar archivos locales al Raspberry Pi arrastrándolos y soltándolos, o descargar archivos desde el Raspberry Pi al ordenador local.

.. image:: img/upload_ftp.png
