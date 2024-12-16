.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein und verbinden Sie sich mit anderen Technikbegeisterten.

    **Warum mitmachen?**

    - **Expertenunterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Einblicken.
    - **Exklusive Rabatte**: Genießen Sie besondere Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und saisonalen Angeboten teil.

    👉 Bereit, mit uns zu entdecken und zu schaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _py_treasure:

Schatzsuche
============================

Richten Sie ein Labyrinth in Ihrem Raum ein und platzieren Sie sechs verschiedene Farbkarte in den sechs Ecken. Steuern Sie dann PiCrawler, um diese Farbkarte nacheinander zu suchen!

.. note:: Sie können die :download:`PDF Farbkarte <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>` für die Farberkennung herunterladen und ausdrucken.

**Code ausführen**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 treasure_hunt.py


**Bild anzeigen**

Nachdem der Code ausgeführt wurde, wird im Terminal die folgende Aufforderung angezeigt:

.. code-block::

    No desktop !
    * Serving Flask app "vilib.vilib" (lazy loading)
    * Environment: production
    WARNING: Do not use the development server in a production environment.
    Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)

Nun können Sie ``http://<Ihre IP>:9000/mjpg`` im Browser eingeben, um das Video anzuzeigen, z. B. ``http://192.168.18.113:9000/mjpg``

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


**Wie funktioniert es?**

Dieses Projekt kombiniert im Allgemeinen die Wissensbereiche von :ref:`py_keyboard`, :ref:`py_vision` und :ref:`py_sound`.

Der Ablauf ist wie folgt dargestellt:

.. image:: img/treasure_hunt-f.png

