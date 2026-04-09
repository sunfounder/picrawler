.. note:: 

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook. ¡Explora más a fondo Raspberry Pi, Arduino y ESP32 con otros entusiastas!

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y vistas previas.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _install_all_modules:

Instalar todos los módulos (Importante)
=============================================

#. **Preparar el sistema**

   Asegúrate de que tu Raspberry Pi esté conectado a Internet y luego actualiza el sistema:

   .. raw:: html

      <run></run>

   .. code-block::

      sudo apt update
      sudo apt upgrade

   .. note::
      
      Si estás utilizando Raspberry Pi OS Lite, instala primero los paquetes necesarios de Python 3:

   .. raw:: html

      <run></run>

   .. code-block::

         sudo apt install git python3-pip python3-setuptools python3-smbus

#. **Instalar robot-hat**

   Descarga e instala el módulo ``robot-hat``:

   .. raw:: html

      <run></run>

   .. code-block::

      cd ~/
      git clone -b v2.0 https://github.com/sunfounder/robot-hat.git --depth 1
      cd robot-hat
      sudo python3 install.py

#. **Instalar vilib**

   Descarga e instala el módulo ``vilib``:

   .. raw:: html

      <run></run>

   .. code-block::

      cd ~/
      git clone https://github.com/sunfounder/vilib.git --depth 1
      cd vilib
      sudo python3 install.py


#. **Instalar picrawler**

   Luego descarga el código e instala el módulo ``picrawler``.
   
   .. raw:: html
   
       <run></run>
   
   .. code-block::
   
       cd ~/
       git clone https://github.com/sunfounder/picrawler.git --depth 1
       cd picrawler
       sudo python3 setup.py install
   
   Este paso tomará un poco de tiempo, así que por favor ten paciencia.

#. **Habilitar sonido (amplificador I2S)**

   Para habilitar la salida de audio, ejecuta el script ``i2samp.sh`` para instalar los componentes necesarios del amplificador I2S:

   .. raw:: html

      <run></run>

   .. code-block::

      cd ~/robot-hat
      sudo bash i2samp.sh

   Sigue las instrucciones en pantalla escribiendo ``y`` y presionando Enter para continuar, ejecuta ``/dev/zero`` en segundo plano y reinicia el Picar-X.

   .. note::
      Si no hay sonido después de reiniciar, intenta ejecutar el script ``i2samp.sh`` varias veces.
