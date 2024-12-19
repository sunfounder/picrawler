Interacción con IA Usando GPT-4O
=====================================

En nuestros proyectos anteriores, utilizamos programación para dirigir a PiCrawler en tareas predeterminadas, lo que podría parecer un poco tedioso. Este proyecto introduce un emocionante salto hacia una interacción dinámica. ¡Cuidado con intentar engañar a nuestro robot, ahora puede comprender mucho más que antes!

Esta iniciativa detalla todos los pasos técnicos necesarios para integrar GPT-4O en tu sistema, incluyendo la configuración de entornos virtuales necesarios, instalación de bibliotecas cruciales y configuración de claves API e IDs de asistentes.

.. note::

   Este proyecto requiere el uso de |link_openai_platform|, y es necesario pagar por OpenAI. Además, la API de OpenAI se factura por separado de ChatGPT, con precios disponibles en https://openai.com/api/pricing/.

   Por lo tanto, debes decidir si continuar con este proyecto o asegurarte de haber financiado la API de OpenAI.

Ya sea que tengas un micrófono para comunicarte directamente o prefieras escribir en una ventana de comandos, las respuestas de PiCrawler impulsadas por GPT-4O seguramente te sorprenderán.

¡Vamos a sumergirnos en este proyecto y desatar un nuevo nivel de interacción con PiCrawler!


1. Instalación de Paquetes y Dependencias Requeridas
-------------------------------------------------------

.. note::

   Primero necesitas instalar los módulos necesarios para PiCrawler. Para más detalles, consulta: :ref:`install_all_modules`.
   
En esta sección, crearemos y activaremos un entorno virtual, instalando los paquetes y dependencias requeridos dentro de él. Esto asegura que los paquetes instalados no interfieran con el resto del sistema, manteniendo el aislamiento de dependencias del proyecto y previniendo conflictos con otros proyectos o paquetes del sistema.

#. Usa el comando ``python -m venv`` para crear un entorno virtual llamado ``my_venv``, incluyendo paquetes a nivel de sistema. La opción ``--system-site-packages`` permite al entorno virtual acceder a paquetes instalados a nivel de sistema, útil cuando se necesitan bibliotecas del sistema.

   .. code-block:: shell

      python -m venv --system-site-packages my_venv

#. Cambia al directorio ``my_venv`` y activa el entorno virtual usando el comando ``source bin/activate``. El indicador del terminal cambiará para indicar que el entorno virtual está activo.

   .. code-block:: shell

      cd my_venv
      source bin/activate

#. Ahora, instala los paquetes de Python requeridos dentro del entorno virtual activado. Estos paquetes estarán aislados en el entorno virtual y no afectarán otros paquetes del sistema.

   .. code-block:: shell

      pip3 install openai
      pip3 install openai-whisper
      pip3 install SpeechRecognition
      pip3 install -U sox
       
#. Finalmente, usa el comando ``apt`` para instalar dependencias a nivel de sistema, lo que requiere privilegios de administrador.

   .. code-block:: shell

      sudo apt install python3-pyaudio
      sudo apt install sox


2. Obtención de Clave API e ID de Asistente
--------------------------------------------

**Obtener la Clave API**

#. Visita |link_openai_platform| y haz clic en el botón **Create new secret key** en la esquina superior derecha.

   .. image:: img/apt_create_api_key.png
      :width: 700
      :align: center

#. Selecciona el Propietario, Nombre, Proyecto y permisos según sea necesario, luego haz clic en **Create secret key**.

   .. image:: img/apt_create_api_key2.png
      :width: 700
      :align: center

#. Una vez generada, guarda esta clave secreta en un lugar seguro y accesible. Por razones de seguridad, no podrás verla nuevamente en tu cuenta de OpenAI. Si pierdes esta clave secreta, tendrás que generar una nueva.

   .. image:: img/apt_create_api_key_copy.png
      :width: 700
      :align: center

**Obtener el ID del Asistente**

#. A continuación, haz clic en **Assistants**, luego haz clic en **Create**, asegurándote de estar en la página de **Dashboard**.

   .. image:: img/apt_create_assistant.png
      :width: 700
      :align: center

#. Mueve tu cursor aquí para copiar el **ID del asistente**, luego pégalo en un cuadro de texto o en otro lugar. Este es el identificador único de este Asistente.

   .. image:: img/apt_create_assistant_id.png
      :width: 700
      :align: center

#. Asigna un nombre aleatorio, luego copia el siguiente contenido en el cuadro **Instructions** para describir a tu Asistente.

   .. image:: img/apt_create_assistant_instructions.png
      :width: 700
      :align: center

   .. code-block::

      You are an AI spider robot named PaiCrawler. With four legs, a camera, and an ultrasonic distance sensor, you can interact with people through conversations and respond appropriately to different scenarios.

      ## Response with Json Format, eg:
      {"actions": ["wave"], "answer": "Hello, I am PaiCrawler, your good friend."}

      ## Response Style
      Tone: Cheerful, optimistic, humorous, childlike
      Preferred Style: Enjoys incorporating jokes, metaphors, and playful banter; prefers responding from a robotic perspective
      Answer Elaboration: Moderately detailed

      ## Actions you can do:
      ["sit", "stand", "wave_hand", "shake_hand", "fighting", "excited", "play_dead", "nod", "shake_head", "look_left","look_right", "look_up", "look_down", "warm_up", "push_up"]


#. PiCrawler está equipado con un módulo de cámara que puedes habilitar para capturar imágenes de lo que ve y cargarlas en GPT usando nuestro código de ejemplo. Por lo tanto, recomendamos elegir GPT-4O, que tiene capacidades de análisis de imágenes. Por supuesto, también puedes elegir gpt-3.5-turbo u otros modelos.

   .. image:: img/apt_create_assistant_model.png
      :width: 700
      :align: center

#. Ahora, haz clic en **Playground** para verificar si tu cuenta funciona correctamente.

   .. image:: img/apt_playground.png

#. Si tus mensajes o imágenes cargadas se envían con éxito y recibes respuestas, significa que tu cuenta no ha alcanzado el límite de uso.

   .. image:: img/apt_playground_40.png
      :width: 700
      :align: center

#. Si encuentras un mensaje de error después de ingresar información, es posible que hayas alcanzado tu límite de uso. Por favor verifica el panel de uso o la configuración de facturación.

   .. image:: img/apt_playground_40mini_3.5.png
      :width: 700
      :align: center

3. Completar la clave API y el ID del asistente
--------------------------------------------------

#. Usa el siguiente comando para abrir el archivo ``keys.py``.

   .. code-block:: shell

      nano ~/picrawler/gpt_examples/keys.py

#. Completa la clave API y el ID del asistente que acabas de copiar.

   .. code-block:: shell

      OPENAI_API_KEY = "sk-proj-vEBo7Ahxxxx-xxxxx-xxxx"
      OPENAI_ASSISTANT_ID = "asst_ulxxxxxxxxx"

#. Presiona ``Ctrl + X``, ``Y`` y luego ``Enter`` para guardar el archivo y salir.

4. Ejecutar el Ejemplo
----------------------------------
Comunicación por Texto
^^^^^^^^^^^^^^^^^^^^^^^^^^

Si tu PiCrawler no tiene un micrófono, puedes usar texto ingresado con teclado para interactuar con él ejecutando los siguientes comandos.

#. Ahora, ejecuta los siguientes comandos usando sudo, ya que el altavoz de PiCrawler no funcionará sin él. El proceso tomará algún tiempo en completarse.

   .. code-block:: shell

      cd ~/picrawler/gpt_examples/
      sudo ~/my_venv/bin/python3 gpt_spider.py --keyboard

#. Una vez que los comandos se hayan ejecutado con éxito, verás la siguiente salida, indicando que todos los componentes de PiCrawler están listos.

   .. code-block:: shell

      vilib 0.3.8 launching ...
      picamera2 0.3.19

      Web display on:
         http://rpi_ip:9000/mjpg

      Starting web streaming ...
      * Serving Flask app 'vilib.vilib'
      * Debug mode: off

      input:

#. También se te proporcionará un enlace para ver la transmisión de la cámara de PiCrawler en tu navegador web: ``http://rpi_ip:9000/mjpg``.

   .. image:: img/apt_ip_camera.png
      :width: 700
      :align: center

#. Ahora puedes escribir tus comandos en la ventana del terminal y presionar Enter para enviarlos. Las respuestas de PiCrawler pueden sorprenderte.

   .. note::
      
      PiCrawler necesita recibir tu entrada, enviarla a GPT para procesarla, recibir la respuesta y luego reproducirla mediante síntesis de voz. Todo este proceso toma tiempo, así que por favor ten paciencia.

   .. image:: img/apt_keyboard_input.png
      :width: 700
      :align: center

#. Si estás usando el modelo GPT-4O, también puedes hacer preguntas basadas en lo que PiCrawler ve.

Comunicación por Voz
^^^^^^^^^^^^^^^^^^^^^^^^

Si tu PiCrawler está equipado con un micrófono, o puedes adquirir uno haciendo clic en |link_microphone|, puedes interactuar con PiCrawler usando comandos de voz.

#. Primero, verifica que la Raspberry Pi haya detectado el micrófono.

   .. code-block:: shell

      arecord -l

   Si tiene éxito, recibirás la siguiente información, indicando que tu micrófono ha sido detectado.

   .. code-block:: 
      
      **** List of CAPTURE Hardware Devices ****
      card 3: Device [USB PnP Sound Device], device 0: USB Audio [USB Audio]
      Subdevices: 1/1
      Subdevice #0: subdevice #0

#. Ejecuta el siguiente comando, luego habla con PiCrawler o haz algunos sonidos. El micrófono grabará los sonidos en el archivo ``op.wav``. Presiona ``Ctrl + C`` para detener la grabación.

   .. code-block:: shell

      rec op.wav

#. Finalmente, usa el siguiente comando para reproducir el sonido grabado, confirmando que el micrófono funciona correctamente.

   .. code-block:: shell

      sudo play op.wav

#. Ahora, ejecuta los siguientes comandos usando sudo, ya que el altavoz de PiCrawler no funcionará sin él. El proceso tomará algún tiempo en completarse.

   .. code-block:: shell

      cd ~/picrawler/gpt_examples/
      sudo ~/my_venv/bin/python3 gpt_spider.py

#. Una vez que los comandos se hayan ejecutado con éxito, verás la siguiente salida, indicando que todos los componentes de PiCrawler están listos.

   .. code-block:: shell
      
      vilib 0.3.8 launching ...
      picamera2 0.3.19

      Web display on:
         http://rpi_ip:9000/mjpg

      Starting web streaming ...
      * Serving Flask app 'vilib.vilib'
      * Debug mode: off

      listening ...

#. También se te proporcionará un enlace para ver la cámara de PiCrawler en tu navegador web: ``http://rpi_ip:9000/mjpg``.

   .. image:: img/apt_ip_camera.png
      :width: 700
      :align: center

#. Ahora puedes hablar con PiCrawler, y sus respuestas pueden sorprenderte.

   .. note::
      
      PiCrawler necesita recibir tu entrada, convertirla a texto, enviarla a GPT para su procesamiento, recibir la respuesta y luego reproducirla mediante síntesis de voz. Todo este proceso toma tiempo, así que por favor ten paciencia.

   .. image:: img/apt_speech_input.png
      :width: 700
      :align: center

#. Si estás usando el modelo GPT-4O, también puedes hacer preguntas basadas en lo que PiCrawler ve.

5. Modificar parámetros [opcional]
-------------------------------------------

En el archivo ``gpt_spider.py``, localiza las siguientes líneas. Puedes modificar estos parámetros para configurar el idioma de STT, la ganancia de volumen de TTS y el rol de voz.

* **STT (Speech to Text)** se refiere al proceso donde el micrófono de PiCrawler captura el habla y la convierte en texto para ser enviada a GPT. Puedes especificar el idioma para una mayor precisión y menor latencia en esta conversión.

* **TTS (Text to Speech)** es el proceso de convertir las respuestas de texto de GPT en voz, que se reproduce a través del altavoz de PiCrawler. Puedes ajustar la ganancia de volumen y seleccionar un rol de voz para la salida de TTS.

.. code-block:: python

   # inicialización del asistente de OpenAI
   # =================================================================
   openai_helper = OpenAiHelper(OPENAI_API_KEY, OPENAI_ASSISTANT_ID, 'picrawler')

   # LANGUAGE = ['zh', 'en'] # configura el código de idioma STT, https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes
   LANGUAGE = []

   VOLUME_DB = 3 # ganancia de volumen TTS, preferentemente menor a 5db

   # selecciona el rol de voz TTS, podría ser "alloy, echo, fable, onyx, nova, y shimmer"
   # https://platform.openai.com/docs/guides/text-to-speech/supported-languages
   TTS_VOICE = 'nova'


* Variable ``LANGUAGE``: 

  * Mejora la precisión y el tiempo de respuesta del Speech-to-Text (STT).
  * ``LANGUAGE = []`` significa que admite todos los idiomas, pero esto puede reducir la precisión de STT y aumentar la latencia.
  * Se recomienda configurar el(los) idioma(s) específico(s) usando códigos de idioma de |link_iso_language_code| para mejorar el rendimiento.

* Variable ``VOLUME_DB``:

  * Controla la ganancia aplicada a la salida de Text-to-Speech (TTS).
  * Aumentar el valor aumentará el volumen, pero es mejor mantenerlo por debajo de 5dB para evitar distorsiones de audio.

* Variable ``TTS_VOICE``:

  * Selecciona el rol de voz para la salida de Text-to-Speech (TTS).
  * Opciones disponibles: ``alloy, echo, fable, onyx, nova, shimmer``.
  * Puedes experimentar con diferentes voces desde |link_voice_options| para encontrar una que se adapte al tono y público deseado. Las voces disponibles están actualmente optimizadas para inglés.
