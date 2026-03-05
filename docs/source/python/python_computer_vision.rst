.. note:: 

    Bonjour, bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et obtenez des aperçus exclusifs.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions et concours festifs** : Participez à des concours et à des promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_vision:

Vision par ordinateur
=======================

Ce projet entre officiellement dans le domaine de la vision par ordinateur !

**Exécuter le code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 display.py

**Voir l'image**

Après l'exécution du code, le terminal affichera l'invite suivante :

.. code-block::

    No desktop !
    * Serving Flask app "vilib.vilib" (lazy loading)
    * Environment: production
    WARNING: Do not use the development server in a production environment.
    Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)

Vous pouvez alors entrer ``http://<votre IP>:9000/mjpg`` dans le navigateur pour afficher l'écran vidéo. Par exemple : ``http://192.168.18.113:9000/mjpg``

.. image:: img/display.png


Après l'exécution du programme, vous verrez les informations suivantes à la fin :


* Tapez une touche pour appeler la fonction !
* ``q`` : Prendre une photo
* ``1`` : Détection de couleur : rouge
* ``2`` : Détection de couleur : orange
* ``3`` : Détection de couleur : jaune
* ``4`` : Détection de couleur : vert
* ``5`` : Détection de couleur : bleu
* ``6`` : Détection de couleur : violet
* ``0`` : Désactiver la détection de couleur
* ``r`` : Scanner le QR code
* ``f`` : Activer/Désactiver la détection faciale
* ``s`` : Afficher les informations des objets détectés

Veuillez suivre les instructions pour activer les fonctions correspondantes.

    *  **Prendre une photo**

        Tapez ``q`` dans le terminal. L'image actuellement vue par la caméra sera sauvegardée (si la fonction de détection de couleur est activée, le cadre sera également visible dans l'image enregistrée). Vous pouvez voir ces photos dans le répertoire ``~/Pictures/PiCrawler/`` de votre Raspberry Pi.
        Vous pouvez utiliser des outils comme :ref:`filezilla` pour transférer les photos vers votre PC.
        

    *  **Détection de couleur**

        En entrant un chiffre entre ``1~6``, l'une des couleurs suivantes sera détectée : "rouge, orange, jaune, vert, bleu, violet". Entrez ``0`` pour désactiver la détection de couleur.

        .. image:: img/DTC2.png

        .. note:: Vous pouvez télécharger et imprimer les :download:`Cartes de couleur PDF <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>` pour la détection de couleur.


    *  **Détection faciale**

        Tapez ``f`` pour activer la détection faciale.

        .. image:: img/DTC5.png

    *  **Détection de QR Code**

        Tapez ``r`` pour activer la reconnaissance des QR codes. Aucune autre opération ne peut être effectuée tant que le QR code n'est pas reconnu. Les informations décodées du QR code seront affichées dans le terminal.

        .. image:: img/DTC4.png

    *  **Afficher les informations**

        En entrant ``s``, les informations sur la détection faciale (et de couleur) seront affichées dans le terminal. Cela inclut les coordonnées du centre (X, Y) et la taille (Largeur, Hauteur) de l'objet mesuré.


**Code**

.. code-block:: python

    from vilib import Vilib
    from time import sleep, time, strftime, localtime
    import threading
    import readchar
    from os import getlogin

    USERNAME = getlogin()
    PICTURE_PATH = f"/home/{USERNAME}/Pictures/"

    flag_face = False
    flag_color = False
    qr_code_flag = False

    MANUAL = '''
    Press a key to call the function:
        q: Take photo
        1: Color detect : red
        2: Color detect : orange
        3: Color detect : yellow
        4: Color detect : green
        5: Color detect : blue
        6: Color detect : purple
        0: Switch off Color detect
        r: Scan the QR code (toggle)
        f: Switch ON/OFF face detect
        s: Display detected object information
        Ctrl+C: Quit
    '''

    color_list = ['close', 'red', 'orange', 'yellow', 'green', 'blue', 'purple']

    def face_detect(flag):
        print("Face Detect:", flag)
        Vilib.face_detect_switch(flag)

    def qrcode_detect():
        global qr_code_flag
        Vilib.qrcode_detect_switch(True)
        print("Waiting for QR code...")

        text = None
        while qr_code_flag:
            temp = Vilib.detect_obj_parameter.get('qr_data', "None")
            if temp != "None" and temp != text:
                text = temp
                print("QR code:", text)
            sleep(0.2)

        Vilib.qrcode_detect_switch(False)

    def take_photo():
        _time = strftime('%Y-%m-%d-%H-%M-%S', localtime(time()))
        name = f'photo_{_time}'
        Vilib.take_photo(name, PICTURE_PATH)
        print(f'Photo saved as {PICTURE_PATH}{name}.jpg')

    def object_show():
        global flag_color, flag_face

        if flag_color:
            if Vilib.detect_obj_parameter.get('color_n', 0) == 0:
                print('Color Detect: None')
            else:
                x = Vilib.detect_obj_parameter.get('color_x')
                y = Vilib.detect_obj_parameter.get('color_y')
                w = Vilib.detect_obj_parameter.get('color_w')
                h = Vilib.detect_obj_parameter.get('color_h')
                print("[Color Detect] Coordinate:", (x, y), "Size:", (w, h))

        if flag_face:
            if Vilib.detect_obj_parameter.get('human_n', 0) == 0:
                print('Face Detect: None')
            else:
                x = Vilib.detect_obj_parameter.get('human_x')
                y = Vilib.detect_obj_parameter.get('human_y')
                w = Vilib.detect_obj_parameter.get('human_w')
                h = Vilib.detect_obj_parameter.get('human_h')
                print("[Face Detect] Coordinate:", (x, y), "Size:", (w, h))

    def main():
        global flag_face, flag_color, qr_code_flag
        qrcode_thread = None

        Vilib.camera_start(vflip=False, hflip=False)
        Vilib.display(local=True, web=True)
        print(MANUAL)

        try:
            while True:
                key = readchar.readkey().lower()

                if key == 'q':
                    take_photo()

                elif key in '0123456':
                    index = int(key)
                    if index == 0:
                        flag_color = False
                        Vilib.color_detect('close')
                    else:
                        flag_color = True
                        Vilib.color_detect(color_list[index])
                    print('Color detect:', color_list[index])

                elif key == 'f':
                    flag_face = not flag_face
                    face_detect(flag_face)

                elif key == 'r':
                    qr_code_flag = not qr_code_flag
                    if qr_code_flag:
                        if qrcode_thread is None or not qrcode_thread.is_alive():
                            qrcode_thread = threading.Thread(target=qrcode_detect, daemon=True)
                            qrcode_thread.start()
                    else:
                        print('QRcode Detect: close')

                elif key == 's':
                    object_show()

                sleep(0.05)

        except KeyboardInterrupt:
            print("\nQuit.")

        finally:
            # Stop QR thread and switches
            qr_code_flag = False
            try:
                Vilib.qrcode_detect_switch(False)
            except Exception:
                pass

            try:
                Vilib.color_detect('close')
            except Exception:
                pass

            try:
                Vilib.face_detect_switch(False)
            except Exception:
                pass

            # Close camera
            try:
                Vilib.camera_close()
            except Exception:
                pass

    if __name__ == "__main__":
        main()

**Comment ça fonctionne ?**

La première chose à noter ici est la fonction suivante. Ces deux fonctions vous permettent de démarrer la caméra.

.. code-block:: python

    Vilib.camera_start()
    Vilib.display()

Fonctions liées à la "détection d'objets" :

* ``Vilib.face_detect_switch(True)`` : Activer/Désactiver la détection faciale
* ``Vilib.color_detect(color)`` : Pour la détection de couleur, une seule couleur peut être détectée à la fois. Les paramètres à entrer sont : ``"rouge"``, ``"orange"``, ``"jaune"``, ``"vert"``, ``"bleu"``, ``"violet"``
* ``Vilib.color_detect_switch(False)`` : Désactiver la détection de couleur
* ``Vilib.qrcode_detect_switch(False)`` : Activer/Désactiver la détection de QR code, renvoie les données décodées du QR code.
* ``Vilib.gesture_detect_switch(False)`` : Activer/Désactiver la détection de gestes
* ``Vilib.traffic_sign_detect_switch(False)`` : Activer/Désactiver la détection de panneaux de signalisation

Les informations détectées par l'objet seront stockées dans le dictionnaire ``detect_obj_parameter = Manager().dict()``.

Dans le programme principal, vous pouvez y accéder comme ceci :

.. code-block:: python

    Vilib.detect_obj_parameter['color_x']

Les clés du dictionnaire et leur utilisation sont les suivantes :

* ``color_x`` : la valeur x de la coordonnée du centre du bloc de couleur détecté, la plage est de 0 à 320
* ``color_y`` : la valeur y de la coordonnée du centre du bloc de couleur détecté, la plage est de 0 à 240
* ``color_w`` : la largeur du bloc de couleur détecté, la plage est de 0 à 320
* ``color_h`` : la hauteur du bloc de couleur détecté, la plage est de 0 à 240
* ``color_n`` : le nombre de zones de couleur détectées
* ``human_x`` : la valeur x de la coordonnée du centre du visage humain détecté, la plage est de 0 à 320
* ``human_y`` : la valeur y de la coordonnée du centre du visage détecté, la plage est de 0 à 240
* ``human_w`` : la largeur du visage humain détecté, la plage est de 0 à 320
* ``human_h`` : la hauteur du visage humain détecté, la plage est de 0 à 240
* ``human_n`` : le nombre de visages détectés
* ``traffic_sign_x`` : la valeur x de la coordonnée centrale du panneau de signalisation détecté, la plage est de 0 à 320
* ``traffic_sign_y`` : la valeur y de la coordonnée centrale du panneau de signalisation détecté, la plage est de 0 à 240
* ``traffic_sign_w`` : la largeur du panneau de signalisation détecté, la plage est de 0 à 320
* ``traffic_sign_h`` : la hauteur du panneau de signalisation détecté, la plage est de 0 à 240
* ``traffic_sign_t`` : le contenu du panneau de signalisation détecté, la liste des valeurs est `['stop','right','left','forward']`
* ``gesture_x`` : la valeur x de la coordonnée centrale du geste détecté, la plage est de 0 à 320
* ``gesture_y`` : la valeur y de la coordonnée centrale du geste détecté, la plage est de 0 à 240
* ``gesture_w`` : la largeur du geste détecté, la plage est de 0 à 320
* ``gesture_h`` : la hauteur du geste détecté, la plage est de 0 à 240
* ``gesture_t`` : le contenu du geste détecté, la liste des valeurs est `["paper","scissor","rock"]`
* ``qr_data`` : le contenu du QR code détecté
* ``qr_x`` : la valeur x de la coordonnée centrale du QR code détecté, la plage est de 0 à 320
* ``qr_y`` : la valeur y de la coordonnée centrale du QR code détecté, la plage est de 0 à 240
* ``qr_w`` : la largeur du QR code détecté, la plage est de 0 à 320
* ``qr_h`` : la hauteur du QR code détecté, la plage est de 0 à 320
