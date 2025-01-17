Interaction avec l'IA utilisant GPT-4O
=====================================================

Dans nos projets précédents, nous avons utilisé la programmation pour diriger PiCrawler dans des tâches prédéfinies, ce qui pouvait sembler un peu répétitif. Ce projet introduit un saut passionnant vers une interaction dynamique. Attention à ne pas essayer de surpasser notre voiture, car elle est maintenant équipée pour comprendre bien plus que jamais !

Cette initiative détaille toutes les étapes techniques nécessaires pour intégrer GPT-4O dans votre système, y compris la configuration des environnements virtuels nécessaires, l'installation des bibliothèques essentielles et la configuration des clés API et des identifiants d'assistant.

.. note::

   Ce projet nécessite l'utilisation de |link_openai_platform| et l'abonnement à OpenAI. De plus, l'API OpenAI est facturée séparément de ChatGPT, avec sa propre tarification disponible sur https://openai.com/api/pricing/.

   Vous devez donc décider si vous souhaitez poursuivre ce projet ou vous assurer que vous avez financé l'API OpenAI.

Que vous ayez un microphone pour communiquer directement ou que vous préfériez taper dans une fenêtre de commande, les réponses de PiCrawler propulsées par GPT-4O ne manqueront pas de vous étonner !

Plongeons dans ce projet et libérons un nouveau niveau d'interaction avec PiCrawler !

1. Installation des packages et dépendances requis
--------------------------------------------------------------

.. note::

   Vous devez d'abord installer les modules nécessaires pour PiCrawler. Pour plus de détails, veuillez consulter :ref:`install_all_modules`.

Dans cette section, nous allons créer et activer un environnement virtuel, puis installer les packages et dépendances nécessaires à l'intérieur. Cela garantit que les packages installés n'interfèrent pas avec le reste du système, en maintenant l'isolation des dépendances du projet et en évitant les conflits avec d'autres projets ou packages système.

#. Utilisez la commande ``python -m venv`` pour créer un environnement virtuel nommé ``my_venv``, incluant les packages système. L'option ``--system-site-packages`` permet à l'environnement virtuel d'accéder aux packages installés au niveau du système, ce qui est utile lorsque des bibliothèques système sont nécessaires.

   .. code-block:: shell

      python -m venv --system-site-packages my_venv

#. Accédez au répertoire ``my_venv`` et activez l'environnement virtuel en utilisant la commande ``source bin/activate``. L'invite de commande changera pour indiquer que l'environnement virtuel est actif.

   .. code-block:: shell

      cd my_venv
      source bin/activate

#. Installez maintenant les packages Python nécessaires dans l'environnement virtuel activé. Ces packages seront isolés dans l'environnement virtuel et n'affecteront pas les autres packages système.

   .. code-block:: shell

      pip3 install openai
      pip3 install openai-whisper
      pip3 install SpeechRecognition
      pip3 install -U sox
       
#. Enfin, utilisez la commande ``apt`` pour installer les dépendances système, ce qui nécessite des privilèges administratifs.

   .. code-block:: shell

      sudo apt install python3-pyaudio
      sudo apt install sox


2. Obtenir la clé API et l'ID de l'assistant
------------------------------------------------

**Obtenir la clé API**

#. Allez sur |link_openai_platform| et cliquez sur le bouton **Créer une nouvelle clé secrète** dans le coin supérieur droit.

   .. image:: img/apt_create_api_key.png
      :width: 700
      :align: center

#. Sélectionnez le propriétaire, le nom, le projet et les autorisations nécessaires, puis cliquez sur **Créer une clé secrète**.

   .. image:: img/apt_create_api_key2.png
      :width: 700
      :align: center

#. Une fois générée, enregistrez cette clé secrète dans un endroit sûr et accessible. Pour des raisons de sécurité, vous ne pourrez plus la consulter à nouveau via votre compte OpenAI. Si vous perdez cette clé secrète, vous devrez en générer une nouvelle.

   .. image:: img/apt_create_api_key_copy.png
      :width: 700
      :align: center

**Obtenir l'ID de l'assistant**

#. Ensuite, cliquez sur **Assistants**, puis sur **Créer**, en vous assurant d'être sur la page **Tableau de bord**.

   .. image:: img/apt_create_assistant.png
      :width: 700
      :align: center

#. Déplacez votre curseur ici pour copier l'**ID de l'assistant**, puis collez-le dans une zone de texte ou ailleurs. Il s'agit de l'identifiant unique de cet assistant.

   .. image:: img/apt_create_assistant_id.png
      :width: 700
      :align: center

#. Définissez un nom aléatoire, puis copiez le contenu suivant dans la zone **Instructions** pour décrire votre assistant.

   .. image:: img/apt_create_assistant_instructions.png
      :width: 700
      :align: center

   .. code-block::

      Vous êtes un robot araignée IA nommé PaiCrawler. Avec ses quatre pattes, une caméra et un capteur de distance à ultrasons, vous pouvez interagir avec les gens par des conversations et répondre de manière appropriée à différents scénarios.

      ## Répondre au format Json, par exemple :
      {"actions": ["wave"], "answer": "Bonjour, je suis PaiCrawler, votre bon ami."}

      ## Style de réponse
      Ton : Joyeux, optimiste, humoristique, enfantin
      Style préféré : Aime incorporer des blagues, des métaphores et des plaisanteries ; préfère répondre du point de vue d'un robot
      Élaboration de la réponse : Modérément détaillée

      ## Actions que vous pouvez faire :
      ["sit", "stand", "wave_hand", "shake_hand", "fighting", "excited", "play_dead", "nod", "shake_head", "look_left", "look_right", "look_up", "look_down", "warm_up", "push_up"]

#. PiCrawler est équipé d'un module caméra que vous pouvez activer pour capturer des images de ce qu'il voit et les télécharger sur GPT à l'aide de notre code exemple. Nous vous recommandons donc de choisir GPT-4O-mini, qui dispose de capacités d'analyse d'images. Bien sûr, vous pouvez également choisir gpt-3.5-turbo ou d'autres modèles.

   .. image:: img/apt_create_assistant_model.png
      :width: 700
      :align: center

#. Maintenant, cliquez sur **Playground** pour vérifier si votre compte fonctionne correctement.

   .. image:: img/apt_playground.png

#. Si vos messages ou images téléchargées sont envoyés avec succès et que vous recevez des réponses, cela signifie que votre compte n'a pas atteint la limite d'utilisation.

   .. image:: img/apt_playground_40.png
      :width: 700
      :align: center

#. Si vous rencontrez un message d'erreur après avoir saisi des informations, il est possible que vous ayez atteint votre limite d'utilisation. Veuillez consulter votre tableau de bord d'utilisation ou les paramètres de facturation.

   .. image:: img/apt_playground_40mini_3.5.png
      :width: 700
      :align: center

3. Remplir la clé API et l'ID de l'assistant
--------------------------------------------------

#. Utilisez la commande pour ouvrir le fichier ``keys.py``.

   .. code-block:: shell

      nano ~/picrawler/gpt_examples/keys.py

#. Remplissez la clé API et l'ID de l'assistant que vous venez de copier.

   .. code-block:: shell

      OPENAI_API_KEY = "sk-proj-vEBo7Ahxxxx-xxxxx-xxxx"
      OPENAI_ASSISTANT_ID = "asst_ulxxxxxxxxx"

#. Appuyez sur ``Ctrl + X``, ``Y``, puis ``Enter`` pour enregistrer le fichier et quitter.

4. Exécution de l'exemple
----------------------------------

Communication par texte
^^^^^^^^^^^^^^^^^^^^^^^^^^

Si votre PiCrawler n'a pas de microphone, vous pouvez interagir avec lui en saisissant du texte via le clavier en exécutant les commandes suivantes.

#. Maintenant, exécutez les commandes suivantes en utilisant sudo, car le haut-parleur de PiCrawler ne fonctionnera pas sans cela. Le processus prendra un certain temps pour se terminer.

   .. code-block:: shell

      cd ~/picrawler/gpt_examples/
      sudo ~/my_venv/bin/python3 gpt_spider.py --keyboard

#. Une fois les commandes exécutées avec succès, vous verrez la sortie suivante, indiquant que tous les composants de PiCrawler sont prêts.

   .. code-block:: shell

      vilib 0.3.8 launching ...
      picamera2 0.3.19

      Web display on:
         http://rpi_ip:9000/mjpg

      Starting web streaming ...
      * Serving Flask app 'vilib.vilib'
      * Debug mode: off

      input:

#. Un lien vous sera également fourni pour afficher le flux caméra de PiCrawler dans votre navigateur web : ``http://rpi_ip:9000/mjpg``.

   .. image:: img/apt_ip_camera.png
      :width: 700
      :align: center

#. Vous pouvez maintenant taper vos commandes dans la fenêtre du terminal et appuyer sur Entrée pour les envoyer. Les réponses de PiCrawler pourraient bien vous surprendre.

   .. note::

      PiCrawler doit recevoir votre entrée, l'envoyer à GPT pour traitement, recevoir la réponse et ensuite la restituer via synthèse vocale. Tout ce processus prend un peu de temps, alors soyez patient.

   .. image:: img/apt_keyboard_input.png
      :width: 700
      :align: center

#. Si vous utilisez le modèle GPT-4O, vous pouvez également poser des questions basées sur ce que PiCrawler voit.
Communication vocale
^^^^^^^^^^^^^^^^^^^^^^^^

Si votre PiCrawler est équipé d'un microphone, ou si vous pouvez en acheter un en cliquant sur |link_microphone|, vous pouvez interagir avec PiCrawler en utilisant des commandes vocales.

#. Commencez par vérifier que le Raspberry Pi a bien détecté le microphone.

   .. code-block:: shell

      arecord -l

   Si l'opération est réussie, vous recevrez les informations suivantes, indiquant que votre microphone a été détecté.

   .. code-block::

      **** Liste des périphériques matériels de CAPTURE ****
      carte 3 : Appareil [USB PnP Sound Device], périphérique 0 : USB Audio [USB Audio]
      Sous-périphériques : 1/1
      Sous-périphérique #0 : sous-périphérique #0

#. Exécutez la commande suivante, puis parlez à PiCrawler ou produisez des sons. Le microphone enregistrera les sons dans le fichier ``op.wav``. Appuyez sur ``Ctrl + C`` pour arrêter l'enregistrement.

   .. code-block:: shell

      rec op.wav

#. Enfin, utilisez la commande ci-dessous pour lire le son enregistré, afin de vérifier que le microphone fonctionne correctement.

   .. code-block:: shell

      sudo play op.wav

#. Maintenant, exécutez les commandes suivantes avec sudo, car le haut-parleur de PiCrawler ne fonctionnera pas sans cela. Le processus prendra un certain temps pour se terminer.

   .. code-block:: shell

      cd ~/picrawler/gpt_examples/
      sudo ~/my_venv/bin/python3 gpt_spider.py

#. Une fois les commandes exécutées avec succès, vous verrez la sortie suivante, indiquant que tous les composants de PiCrawler sont prêts.

   .. code-block:: shell

      vilib 0.3.8 launching ...
      picamera2 0.3.19

      Web display on:
         http://rpi_ip:9000/mjpg

      Starting web streaming ...
      * Serving Flask app 'vilib.vilib'
      * Debug mode: off

      listening ...

#. Un lien vous sera également fourni pour visualiser le flux de la caméra de PiCrawler dans votre navigateur web : ``http://rpi_ip:9000/mjpg``.

   .. image:: img/apt_ip_camera.png
      :width: 700
      :align: center

#. Vous pouvez maintenant parler à PiCrawler, et ses réponses pourraient vous surprendre.

   .. note::

      PiCrawler doit recevoir votre entrée, la convertir en texte, l'envoyer à GPT pour traitement, recevoir la réponse, puis la restituer via synthèse vocale. Ce processus prend un certain temps, alors soyez patient.

   .. image:: img/apt_speech_input.png
      :width: 700
      :align: center

#. Si vous utilisez le modèle GPT-4O, vous pouvez également poser des questions basées sur ce que PiCrawler voit.

5. Modifier les paramètres [facultatif]
-------------------------------------------

Dans le fichier ``gpt_spider.py``, localisez les lignes suivantes. Vous pouvez modifier ces paramètres pour configurer la langue de la reconnaissance vocale (STT), le gain du volume de la synthèse vocale (TTS) et le rôle de la voix.

* **STT (Speech to Text)** fait référence au processus où le microphone de PiCrawler capte la parole et la convertit en texte, qui sera envoyé à GPT. Vous pouvez spécifier la langue pour améliorer la précision et réduire la latence de cette conversion.

* **TTS (Text to Speech)** est le processus qui consiste à convertir les réponses textuelles de GPT en discours, qui est ensuite restitué par le haut-parleur de PiCrawler. Vous pouvez ajuster le gain du volume et choisir un rôle de voix pour la sortie TTS.

.. code-block:: python

   # initialisation de l'assistant openai
   # =================================================================
   openai_helper = OpenAiHelper(OPENAI_API_KEY, OPENAI_ASSISTANT_ID, 'picrawler')

   # LANGUE = ['zh', 'en'] # configurer le code de langue STT, https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes
   LANGUE = []

   VOLUME_DB = 3 # gain du volume TTS, de préférence inférieur à 5db

   # choisir le rôle de la voix TTS, qui peut être "alloy", "echo", "fable", "onyx", "nova" ou "shimmer"
   # https://platform.openai.com/docs/guides/text-to-speech/supported-languages
   TTS_VOICE = 'nova'


* Variable ``LANGUE`` :

  * Améliore la précision de la reconnaissance vocale (STT) et réduit le temps de réponse.
  * ``LANGUE = []`` signifie que toutes les langues sont prises en charge, mais cela peut réduire la précision du STT et augmenter la latence.
  * Il est recommandé de spécifier la ou les langues à l'aide des codes de langue |link_iso_language_code| pour améliorer la performance.

* Variable ``VOLUME_DB`` :

  * Contrôle le gain appliqué à la sortie Text-to-Speech (TTS).
  * Augmenter cette valeur augmentera le volume, mais il est préférable de garder cette valeur en dessous de 5dB pour éviter la distorsion audio.

* Variable ``TTS_VOICE`` :

  * Choisissez le rôle de la voix pour la sortie Text-to-Speech (TTS).
  * Options disponibles : ``alloy``, ``echo``, ``fable``, ``onyx``, ``nova``, ``shimmer``.
  * Vous pouvez expérimenter différentes voix via |link_voice_options| pour trouver celle qui correspond à votre ton et à votre public. Les voix disponibles sont actuellement optimisées pour l'anglais.
