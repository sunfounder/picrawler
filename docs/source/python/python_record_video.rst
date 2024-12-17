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

    from time import sleep,strftime,localtime
    from vilib import Vilib
    import readchar
    from os import getlogin
    
    USERNAME = getlogin()
    VIDEO_PATH = f"/home/{USERNAME}/Videos/"
    
    MANUAL = '''
    Press keys on keyboard to control recording:
        Q: record/pause/continue
        E: stop
        Ctrl^C: Quit
    '''

    def print_overwrite(msg,  end='', flush=True):
        print('\r\033[2K', end='',flush=True)
        print(msg, end=end, flush=True)
    
    def main():
        rec_flag = 'stop'  # start, pause, stop
        vname = None
        Vilib.rec_video_set["path"] = VIDEO_PATH
    
        Vilib.camera_start(vflip=False,hflip=False) 
        Vilib.display(local=True,web=True)
        sleep(0.8)  # attendre le démarrage
    
        print(MANUAL)
        while True:
            # lire le clavier
            key = readchar.readkey()
            key = key.lower()
            # démarrer, mettre en pause
            if key == 'q':
                key = None
                if rec_flag == 'stop':            
                    rec_flag = 'start'
                    # définir le nom
                    vname = strftime("%Y-%m-%d-%H.%M.%S", localtime())
                    Vilib.rec_video_set["name"] = vname
                    # démarrer l'enregistrement
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
            # arrêter       
            elif key == 'e' and rec_flag != 'stop':
                key = None
                rec_flag = 'stop'
                Vilib.rec_video_stop()
                print_overwrite("The video saved as %s%s.avi"%(Vilib.rec_video_set["path"],vname),end='\n')  
            # quitter
            elif key == readchar.key.CTRL_C:
                Vilib.camera_close()
                print('\nquit')
                break 
    
            sleep(0.1)
    
    if __name__ == "__main__":
        main()

**Comment ça fonctionne ?**


Les fonctions liées à l'enregistrement incluent :


* ``Vilib.rec_video_run(video_name)`` : Lance le thread pour enregistrer la vidéo. ``video_name`` est le nom du fichier vidéo, il doit s'agir d'une chaîne de caractères.
* ``Vilib.rec_video_start()`` : Démarre ou reprend l'enregistrement vidéo.
* ``Vilib.rec_video_pause()`` : Met l'enregistrement en pause.
* ``Vilib.rec_video_stop()`` : Arrête l'enregistrement.

``Vilib.rec_video_set["path"] = "~/video/test/"`` définit le répertoire de stockage des fichiers vidéo.
