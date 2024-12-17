.. note:: 

    Bonjour, bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 sur Facebook ! Explorez plus en profondeur l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes post-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et d'aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_treasure:

Chasse au Trésor
============================

Aménagez un labyrinthe dans votre pièce et placez six cartes de couleur différentes dans six coins. Ensuite, contrôlez PiCrawler pour rechercher ces cartes de couleur une par une !

.. note:: Vous pouvez télécharger et imprimer les :download:`cartes de couleur PDF <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>` pour la détection des couleurs.

**Exécuter le Code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 treasure_hunt.py


**Affichage de l'Image**

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

**Code**

.. code-block:: python

	from picrawler import Picrawler
	from time import sleep
	from robot_hat import Music,TTS
	from vilib import Vilib
	import readchar
	import random
	import threading
	
	crawler = Picrawler()
	
	
	music = Music()
	tts = TTS()
	
	manual = '''
	Press keys on keyboard to control Picrawler!
	    w: Forward
	    a: Turn left
	    s: Backward
	    d: Turn right
	    space: Say the target again
	    Ctrl^C: Quit
	'''
	
	color = "red"
	color_list=["red","orange","yellow","green","blue","purple"]
	key_dict = {
	    'w': 'forward',
	    's': 'backward',
	    'a': 'turn_left',
	    'd': 'turn_right',
	}
	def renew_color_detect():
	    global color
	    color = random.choice(color_list)
	    Vilib.color_detect(color)
	    tts.say("Look for " + color)
	
	key = None
	lock = threading.Lock()
	def key_scan_thread():
	    global key
	    while True:
	        key_temp = readchar.readkey()
	        print('\r',end='')
	        with lock:
	            key = key_temp.lower()
	            if key == readchar.key.SPACE:
	                key = 'space'
	            elif key == readchar.key.CTRL_C:
	                key = 'quit'
	                break
	        sleep(0.01)
	
	def main():
	    global key
	    action = None
	    Vilib.camera_start(vflip=False,hflip=False)
	    Vilib.display(local=False,web=True)
	    sleep(0.8)
	    speed = 80
	    print(manual)
	
	    sleep(1)
	    _key_t = threading.Thread(target=key_scan_thread)
	    _key_t.setDaemon(True)
	    _key_t.start()
	
	    tts.say("game start")
	    sleep(0.05)   
	    renew_color_detect()
	    while True:
	
	        if Vilib.detect_obj_parameter['color_n']!=0 and Vilib.detect_obj_parameter['color_w']>100:
	            tts.say("will done")
	            sleep(0.05)   
	            renew_color_detect()
	
	        with lock:
	            if key != None and key in ('wsad'):
	                action = key_dict[str(key)]
	                key =  None
	            elif key == 'space':
	                tts.say("Look for " + color)
	                key =  None
	            elif key == 'quit':
	                _key_t.join()
	                Vilib.camera_close()
	                print("\n\rQuit") 
	                break 
	
	        if action != None:
	            crawler.do_action(action,1,speed)  
	            action = None
	
	        sleep(0.05)          
	
	
	if __name__ == "__main__":
	    main()


**Comment ça fonctionne ?**

En général, ce projet combine les points de connaissance des sections :ref:`py_keyboard`, :ref:`py_vision` et :ref:`py_sound`.

Voici le flux de ce projet, illustré dans la figure ci-dessous :

.. image:: img/treasure_hunt-f.png

