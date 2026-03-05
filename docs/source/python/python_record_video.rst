.. note:: 

    Bonjour, bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 sur Facebook ! Explorez plus en profondeur l'univers de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes post-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et d'aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_video:

Enregistrement Vidéo
========================

Cet exemple vous guide sur la façon d'utiliser la fonction d'enregistrement vidéo.

**Exécuter le Code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 record_video.py

Une fois le code exécuté, vous pouvez entrer ``http://<votre IP>:9000/mjpg`` dans le navigateur pour afficher l'écran vidéo, par exemple :  ``http://192.168.18.113:9000/mjpg``

.. image:: img/display.png

L'enregistrement peut être démarré ou arrêté en appuyant sur les touches du clavier.

* Appuyez sur ``q`` pour commencer l'enregistrement ou mettre en pause/reprendre, ``e`` pour arrêter l'enregistrement ou enregistrer.
* Pour quitter le programme, appuyez sur ``Ctrl+C``.

**Code**

.. code-block:: python

    from time import sleep, strftime, localtime
    from vilib import Vilib
    import readchar
    from os import getlogin
    import os

    USERNAME = getlogin()
    VIDEO_PATH = f"/home/{USERNAME}/Videos/"

    MANUAL = '''
    Press keys on keyboard to control recording:
        Q: record/pause/continue
        E: stop
        Ctrl+C: Quit
    '''

    def print_overwrite(msg, end='', flush=True):
        """Overwrite the current terminal line."""
        print('\r\033[2K', end='', flush=True)
        print(msg, end=end, flush=True)

    def safe_stop_recording():
        """Stop recording safely (avoid exceptions during exit)."""
        try:
            Vilib.rec_video_stop()
        except Exception:
            pass

    def safe_close_camera():
        """Close camera safely (avoid exceptions during exit)."""
        try:
            Vilib.camera_close()
        except Exception:
            pass

    def main():
        rec_flag = 'stop'  # Possible states: start, pause, stop
        vname = None

        # Ensure the video directory exists
        os.makedirs(VIDEO_PATH, exist_ok=True)

        # Set save path for recorded videos
        Vilib.rec_video_set["path"] = VIDEO_PATH

        # Start camera and preview
        Vilib.camera_start(vflip=False, hflip=False)
        Vilib.display(local=False, web=True)
        sleep(0.8)  # Wait for camera startup

        print(MANUAL)

        try:
            while True:
                # Read keyboard input (no Enter needed)
                key = readchar.readkey().lower()

                # Q: start / pause / continue
                if key == 'q':
                    if rec_flag == 'stop':
                        rec_flag = 'start'

                        # Generate filename based on timestamp
                        vname = strftime("%Y-%m-%d-%H.%M.%S", localtime())
                        Vilib.rec_video_set["name"] = vname

                        # Start recording
                        Vilib.rec_video_run()
                        Vilib.rec_video_start()
                        print_overwrite('rec start ...')

                    elif rec_flag == 'start':
                        rec_flag = 'pause'
                        Vilib.rec_video_pause()
                        print_overwrite('pause')

                    elif rec_flag == 'pause':
                        rec_flag = 'start'
                        Vilib.rec_video_start()
                        print_overwrite('continue')

                # E: stop recording
                elif key == 'e' and rec_flag != 'stop':
                    rec_flag = 'stop'
                    safe_stop_recording()
                    print_overwrite(
                        "The video saved as %s%s.avi" % (Vilib.rec_video_set["path"], vname),
                        end='\n'
                    )

                # Ctrl+C (readchar special key): quit
                elif key == readchar.key.CTRL_C:
                    print('\nquit')
                    break

                sleep(0.1)

        except KeyboardInterrupt:
            # Handle Ctrl+C from terminal as well
            print('\nquit')

        finally:
            # If recording is still active, stop it before closing camera
            if rec_flag != 'stop':
                safe_stop_recording()
            safe_close_camera()
            sleep(0.1)

    if __name__ == "__main__":
        main()

**Comment ça fonctionne ?**

#. Ce que fait ce programme

   Ce programme vous permet de contrôler l’enregistrement vidéo à l’aide du clavier.

   • Q → Démarrer / Mettre en pause / Reprendre l’enregistrement  
   • E → Arrêter l’enregistrement  
   • Ctrl+C → Quitter le programme  

   La vidéo enregistrée sera sauvegardée dans le dossier Videos.

#. Préparer le dossier vidéo

   .. code-block:: python

      USERNAME = getlogin()
      VIDEO_PATH = f"/home/{USERNAME}/Videos/"
      os.makedirs(VIDEO_PATH, exist_ok=True)

   Le programme récupère votre nom d’utilisateur actuel
   et crée un dossier Videos s’il n’existe pas déjà.

   Toutes les vidéos enregistrées seront sauvegardées ici.

#. Démarrer la caméra

   .. code-block:: python

      Vilib.camera_start(vflip=False, hflip=False)
      Vilib.display(local=False, web=True)
      sleep(0.8)

   La caméra est activée.
   L’aperçu web est activé afin que vous puissiez voir le flux vidéo en direct dans votre navigateur.

   Le court délai permet à la caméra de démarrer correctement.

#. Configuration de l’état d’enregistrement

   .. code-block:: python

      rec_flag = 'stop'
      vname = None

   Le programme utilise une variable appelée ``rec_flag``
   pour mémoriser l’état actuel de l’enregistrement :

   • stop  → pas d’enregistrement  
   • start → enregistrement en cours  
   • pause → en pause

#. Attendre une entrée clavier

   .. code-block:: python

      key = readchar.readkey().lower()

   Le programme attend qu’une touche soit pressée.

#. Appuyer sur Q pour démarrer l’enregistrement

   .. code-block:: python

      if rec_flag == 'stop':
          vname = strftime("%Y-%m-%d-%H.%M.%S", localtime())
          Vilib.rec_video_set["name"] = vname
          Vilib.rec_video_run()
          Vilib.rec_video_start()

   Lorsque vous appuyez sur Q pour la première fois :

   • Un nom de fichier est généré à partir de la date et de l’heure actuelles  
   • L’enregistrement démarre immédiatement  

   Exemple de nom de fichier :
   2026-03-03-15.30.21.avi

#. Appuyer de nouveau sur Q pour mettre en pause

   .. code-block:: python

      elif rec_flag == 'start':
          Vilib.rec_video_pause()

   Si l’enregistrement est déjà en cours,
   appuyer sur Q mettra l’enregistrement en pause.

#. Appuyer encore sur Q pour continuer

   .. code-block:: python

      elif rec_flag == 'pause':
          Vilib.rec_video_start()

   Si l’enregistrement est en pause,
   appuyer à nouveau sur Q reprendra l’enregistrement.

#. Appuyer sur E pour arrêter l’enregistrement

   .. code-block:: python

      elif key == 'e' and rec_flag != 'stop':
          Vilib.rec_video_stop()

   Appuyer sur E arrêtera complètement l’enregistrement.

   Le fichier vidéo sera enregistré dans :
   ``/home/your_username/Videos/``

#. Quitter le programme en toute sécurité

   .. code-block:: python

      finally:
          if rec_flag != 'stop':
              Vilib.rec_video_stop()
          Vilib.camera_close()

   Lorsque le programme se termine :

   • L’enregistrement est arrêté (s’il est encore actif)  
   • La caméra est fermée correctement  

   Cela évite les fichiers vidéo corrompus ou les erreurs de caméra.