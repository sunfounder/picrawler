.. note:: 

    Bonjour, bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 sur Facebook ! Explorez plus en profondeur l'univers de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes post-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et d'aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_sound:

Effet Sonore
=====================

Dans cet exemple, nous utilisons les effets sonores de PiCrawler (plus précisément, ceux du Robot HAT). Cela se compose de trois parties : **Musique**, **Son**, et **Texte à la parole**.

.. image:: img/tts.png

**Installer i2samp**

Avant d'utiliser ces fonctions, commencez par activer le haut-parleur pour qu'il soit activé et puisse émettre des sons.

Exécutez ``i2samp.sh``, ce script installera tout ce qui est nécessaire pour utiliser l'amplificateur i2s.

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/
    sudo bash i2samp.sh 

Plusieurs invites apparaîtront vous demandant de confirmer l'action. Répondez à toutes les invites par **Y**. Après avoir effectué les modifications sur le système Raspberry Pi, un redémarrage sera nécessaire pour que ces changements prennent effet.

Après le redémarrage, exécutez à nouveau le script ``i2samp.sh`` pour tester l'amplificateur. Si un son est émis par le haut-parleur, la configuration est terminée.

**Exécuter le Code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 sound_effect.py

Une fois le code exécuté, suivez les instructions qui s'affichent dans le terminal.

Appuyez sur une touche pour appeler la fonction !
* ``q`` : Lire la musique de fond
* ``1`` : Lire un effet sonore
* ``2`` : Lire un effet sonore avec des fils d'exécution
* ``t`` : Texte à parler
* Pour quitter le programme, appuyez sur ``Ctrl+C``.

**Code**

.. code-block:: python

    '''
        Sorry, currently there is only sound when running with sudo
    '''

    from time import sleep
    from robot_hat import Music,TTS

    music = Music()
    tts = TTS()

    manual = '''
    Input key to call the function!
        q: Play background music
        1: Play sound effect
        2: Play sound effect with threads
        t: Text to speak

        Ctrl^C: quit
    '''

    def main():  
        print(manual)

        flag_bgm = False
        music.music_set_volume(20)
        tts.lang("en-US")


        while True:
            key = input() 
            key = key.lower() 
            if key == "q":
                flag_bgm = not flag_bgm
                if flag_bgm is True:
                    music.music_play('./musics/sports-Ahjay_Stelino.mp3')
                else:
                    music.music_stop()

            elif key == "1":
                music.sound_play('./sounds/talk1.wav')
                sleep(0.05)
                music.sound_play('./sounds/talk3.wav')
                sleep(0.05)
                music.sound_play('./sounds/sign.wav')
                sleep(0.5)

            elif key =="2":
                music.sound_play_threading('./sounds/talk1.wav')
                sleep(0.05)
                music.sound_play_threading('./sounds/talk3.wav')
                sleep(0.05)
                music.sound_play_threading('./sounds/sign.wav')
                sleep(0.5)

            elif key == "t":
                words = "Hello"
                tts.say(words)

    if __name__ == "__main__":
        main()

**Comment ça fonctionne ?**

Les fonctions liées à la musique de fond comprennent :

* ``music = Music()`` : Déclare l'objet.
* ``music.music_set_volume(20)`` : Définit le volume, avec une plage de 0 à 100.
* ``music.music_play(./musics/sports-Ahjay_Stelino.mp3)`` : Joue le fichier musical, ici le fichier **sports-Ahjay_Stelino.mp3** situé sous le chemin ``./musics``.
* ``music.music_stop()`` : Arrête la musique de fond.

.. note::

    Vous pouvez ajouter différents effets sonores ou musiques dans les dossiers ``musics`` ou ``sounds`` via :ref:`filezilla`.

Les fonctions liées aux effets sonores comprennent :

* ``music = Music()``
* ``music.sound_play('./sounds/talk1.wav')`` : Joue le fichier d'effet sonore, ici le fichier **talk1.wav** situé sous le chemin ``./musics``.
* ``music.sound_play_threading('./sounds/talk1.wav')`` : Joue le fichier d'effet sonore en mode fil d'exécution, sans suspendre le fil principal.

Les fonctions liées au texte à la parole comprennent :

* ``tts = TTS()``
* ``tts.say(words)`` : Lecture audio du texte.
* ``tts.lang("en-US")`` : Définit la langue.

.. note::

    Vous pouvez définir la langue en ajustant les paramètres de ``lang("")`` avec les caractères suivants.

.. list-table:: Language
    :widths: 15 50

    *   - zh-CN 
        - Mandarin (Chinois)
    *   - en-US 
        - Anglais - États-Unis
    *   - en-GB     
        - Anglais - Royaume-Uni
    *   - de-DE     
        - Allemand - Allemagne
    *   - es-ES     
        - Espagnol - Espagne
    *   - fr-FR  
        - Français - France
    *   - it-IT  
        - Italien - Italie
