.. note:: 

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Adéntrate más en Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y avances.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

Calibrar el PiCrawler
================================

Después de conectar el PiCrawler, habrá un paso de calibración. Esto se debe a posibles desviaciones durante el proceso de instalación o limitaciones de los servomotores, lo que hace que algunos ángulos estén ligeramente inclinados. Por lo tanto, puedes calibrarlos en este paso.

Sin embargo, si crees que el ensamblaje es perfecto y no se necesita calibración, también puedes omitir este paso.

.. note::
    Si deseas recalibrar el robot durante su uso, sigue los pasos a continuación.
    
    Puedes abrir la página de detalles del producto haciendo clic en el icono de conexión en la esquina superior izquierda.

    .. image:: img/calibrate0.png

    Haz clic en el botón **Configuración**.

    .. image:: img/calibrate1.png

    En esta página, puedes cambiar el nombre del producto, el tipo de producto, ver la versión de la aplicación o calibrar el robot. Una vez que hagas clic en **Calibrar**, accederás a la página de calibración.

    .. image:: img/calibrate2.png


Los pasos de calibración son los siguientes:

#. Toma el folleto de ensamblaje, gíralo a la última página y colócalo plano sobre la mesa. Luego, coloca el PiCrawler como se muestra a continuación, alineando su parte inferior con el contorno del gráfico de calibración.

    .. image:: img/calibration2.png
        :align: center

#. Vuelve a EzBlock Studio, selecciona una pata izquierda, luego haz clic en los 3 botones de los ejes X, Y y Z, y deja que las patas se alineen lentamente con el punto de calibración.

   * Los botones de calibración se usan para ajustes finos y es necesario presionarlos varias veces para observar el cambio de posición del pin.
   * Se recomienda hacer clic primero en el botón de subida del eje Z para levantar la pata, y luego ajustar los ejes X e Y.

    .. image:: img/calibration4.jpg
        :align: center

#. Alinea la otra pata izquierda de la misma manera.

    .. image:: img/calibration3.png
        :align: center

#. Después de calibrar las dos patas izquierdas, cambia el papel de calibración al lado derecho y calibra las dos patas derechas siguiendo el método anterior.

    .. image:: img/calibration4.png
        :align: center