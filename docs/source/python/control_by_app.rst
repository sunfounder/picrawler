.. note:: 

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook. ¡Explora más a fondo Raspberry Pi, Arduino y ESP32 con otros entusiastas!

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y vistas previas.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _control_by_app:

Controlado por la APP
=======================

El controlador SunFounder se utiliza para controlar robots basados en Raspberry Pi/Pico.

La APP integra widgets como Botón, Interruptor, Joystick, D-pad, Slider y Slider de Potencia; widgets de entrada como Pantalla Digital, Radar Ultrasónico, Detección de Escala de Grises y Velocímetro.

Existen 17 áreas (A-Q) donde puedes colocar diferentes widgets para personalizar tu propio controlador.

Además, esta aplicación proporciona un servicio de transmisión de video en vivo.

Vamos a personalizar un controlador para PiCrawler usando esta app.

**¿Cómo hacerlo?**

#. Instala el módulo ``sunfounder-controller``.

    Primero deben instalarse los módulos ``robot-hat``, ``vilib`` y ``picrawler``. Para más detalles, consulta: :ref:`install_all_modules`.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~
        git clone https://github.com/sunfounder/sunfounder-controller.git
        cd ~/sunfounder-controller
        sudo python3 setup.py install

#. Ejecuta el código.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/sunfounder-controller/examples
        sudo python3 picrawler_control.py

#. Instala `SunFounder Controller <https://docs.sunfounder.com/projects/sf-controller/en/latest/>`_ desde **APP Store(iOS)** o **Google Play(Android)**.


#. Abre y crea un nuevo controlador.

    Crea un nuevo controlador haciendo clic en el signo + en la APP SunFounder Controller.

    .. image:: img/app1.PNG

    Hay controladores predefinidos para algunos productos en la sección Preset. Aquí seleccionamos PiCrawler.

    .. image:: img/app_control1.jpg

    Asigna un nombre y selecciona el tipo de Controlador. 

    .. image:: img/app_control2.jpg

    Dentro del controlador predefinido, verás que ya tiene algunos widgets. Si no necesitas realizar más cambios, haz clic en el botón |app_save|.

    .. image:: img/app_control3.jpg

#. Conéctate a PiCrawler.

    Cuando hagas clic en el botón **Connect**, buscará automáticamente robots cercanos. Su nombre está definido en ``picrawler_control.py`` y debe estar en ejecución en todo momento.

    .. image:: img/app_control6.jpg
    
    Una vez que hagas clic en el nombre del producto, aparecerá el mensaje "Connected Successfully" y el nombre del producto se mostrará en la esquina superior derecha.

    .. image:: img/app_control7.jpg

    .. note::

        * Asegúrate de que tu dispositivo móvil esté conectado a la misma red LAN que PiCrawler.
        * Si no se busca automáticamente, también puedes ingresar manualmente la IP para conectarte.

        .. image:: img/app11.PNG

#. Ejecuta este controlador.

    Haz clic en el botón **Run** para iniciar el controlador. Verás la transmisión de video del auto y ahora puedes controlar tu PiCrawler con estos widgets.

    .. image:: img/app_control8.jpg
    
    Estas son las funciones de los widgets:

    * **A**: Ajusta la potencia del PiCrawler.
    * **B**: Muestra la velocidad de movimiento del robot.
    * **C**: Función igual al widget B.
    * **D**: Muestra los obstáculos detectados como puntos rojos.
    * **G**: Reconocimiento de voz. Presiona y mantén este widget para hablar. Mostrará el reconocimiento de voz al soltarlo. En el código hemos configurado 4 comandos: ``forward``, ``backard``, ``left`` y ``right`` para controlar el auto.
    * **K**: Controla los movimientos de avance, retroceso, izquierda y derecha del auto.
    * **Q**: Gira la cabeza (cámara) hacia arriba, abajo, izquierda y derecha.
    * **N**: Activa la función de reconocimiento de color.
    * **O**: Activa la función de reconocimiento facial.
    * **P**: Activa la función de reconocimiento de objetos. Puede reconocer casi 90 tipos de objetos. Para la lista de modelos, consulta: https://github.com/sunfounder/vilib/blob/master/workspace/coco_labels.txt.
