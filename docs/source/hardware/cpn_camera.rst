.. note:: 

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook. ¡Explora más a fondo Raspberry Pi, Arduino y ESP32 con otros entusiastas!

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y vistas previas.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

Módulo de Cámara
=========================

**Descripción**

.. image:: img/camera_module_pic.png
   :width: 200
   :align: center

Este es un módulo de cámara Raspberry Pi de 5MP con sensor OV5647. Es plug and play: conecta el cable de cinta incluido al puerto CSI (Interfaz Serial de Cámara) de tu Raspberry Pi y estará listo para usarse.

La placa es pequeña, mide aproximadamente 25mm x 23mm x 9mm y pesa 3g, lo que la hace ideal para aplicaciones móviles u otras donde el tamaño y el peso son críticos. El módulo de cámara tiene una resolución nativa de 5 megapíxeles y cuenta con una lente de enfoque fijo a bordo que captura imágenes estáticas a 2592 x 1944 píxeles. También soporta video en resoluciones de 1080p30, 720p60 y 640x480p90.

.. note:: 

   El módulo solo es capaz de capturar imágenes y videos, no sonido.

**Especificaciones**

* **Resolución de Imágenes Estáticas**: 2592×1944 
* **Resolución de Video Soportada**: 1080p/30 fps, 720p/60 fps y 640 x 480p 60/90 grabación de video 
* **Apertura (F)**: 1.8 
* **Ángulo Visual**: 65 grados 
* **Dimensiones**: 24mm x 23.5mm x 8mm 
* **Peso**: 3g 
* **Interfaz**: Conector CSI 
* **Sistema Operativo Compatible**: Raspberry Pi OS (se recomienda la versión más reciente)


**Ensamblar el Módulo de Cámara**



En el módulo de cámara o en la Raspberry Pi, encontrarás un conector de plástico plano. Tira cuidadosamente del interruptor negro de fijación hasta que esté parcialmente extraído. Inserta el cable FFC en el conector de plástico en la dirección indicada y empuja el interruptor de fijación nuevamente en su lugar.

Si el cable FFC está instalado correctamente, quedará recto y no se saldrá al tirar suavemente de él. Si no es así, vuelve a instalarlo.

.. image:: img/connect_ffc.png
.. image:: img/1.10_camera.png
   :width: 700

.. warning::

   No instales la cámara con la alimentación encendida, ya que esto podría dañar tu cámara.
