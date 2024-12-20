.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti Speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a promozioni e concorsi durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_treasure:

Caccia al Tesoro
============================

Organizza un labirinto nella tua stanza e posiziona sei cartellini di colori diversi in sei angoli. Poi controlla PiCrawler per cercare questi cartellini uno alla volta!

.. note:: Puoi scaricare e stampare i :download:`PDF Color Cards <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>` per il rilevamento dei colori.

**Esegui il Codice**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 treasure_hunt.py


**Visualizza le Immagini**

Dopo aver eseguito il codice, il terminale mostrerà il seguente messaggio:

.. code-block::

    No desktop !
    * Serving Flask app "vilib.vilib" (lazy loading)
    * Environment: production
    WARNING: Do not use the development server in a production environment.
    Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)

Inserisci quindi ``http://<il tuo IP>:9000/mjpg`` nel browser per visualizzare il feed video. Ad esempio: ``http://192.168.18.113:9000/mjpg``.

.. image:: img/display.png

**Codice**

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


**Come funziona?**

In generale, questo progetto combina i punti chiave di :ref:`py_keyboard`, :ref:`py_vision` e :ref:`py_sound`.

Il flusso del progetto è mostrato nella figura seguente:

.. image:: img/treasure_hunt-f.png

