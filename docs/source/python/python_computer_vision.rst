.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti Speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a promozioni e concorsi durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_vision:

Visione Artificiale
=======================

In questo progetto, entreremo ufficialmente nel campo della visione artificiale!

**Esegui il Codice**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 display.py

**Visualizza l'Immagine**

Dopo aver eseguito il codice, il terminale mostrerà il seguente messaggio:

.. code-block::

    No desktop !
    * Serving Flask app "vilib.vilib" (lazy loading)
    * Environment: production
    WARNING: Do not use the development server in a production environment.
    Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)

Puoi quindi inserire ``http://<il tuo IP>:9000/mjpg`` nel browser per visualizzare il feed video, ad esempio: ``https://192.168.18.113:9000/mjpg``

.. image:: img/display.png


Dopo l'avvio del programma, vedrai le seguenti informazioni:

* Inserisci un tasto per attivare la funzione!
* ``q``: Scatta una foto
* ``1``: Rileva colore: rosso
* ``2``: Rileva colore: arancione
* ``3``: Rileva colore: giallo
* ``4``: Rileva colore: verde
* ``5``: Rileva colore: blu
* ``6``: Rileva colore: viola
* ``0``: Disattiva rilevamento colori
* ``r``: Scansiona il codice QR
* ``f``: Attiva/Disattiva rilevamento volti
* ``s``: Mostra informazioni sugli oggetti rilevati

Segui i suggerimenti per attivare le funzioni corrispondenti.

    * **Scatta Foto**

        Digita ``q`` nel terminale e premi Invio. L'immagine attualmente visibile dalla fotocamera sarà salvata (se il rilevamento del colore è attivato, la casella di marcatura apparirà anche nella foto salvata). Puoi trovare queste foto nella directory ``~/Pictures/PiCrawler/`` del Raspberry Pi.
        Puoi usare strumenti come :ref:`filezilla` per trasferire le foto sul tuo PC.
        
    * **Rileva Colore**

        Inserendo un numero tra ``1~6`` rileverai uno dei colori "rosso, arancione, giallo, verde, blu, viola". Inserisci ``0`` per disattivare il rilevamento del colore.

        .. image:: img/DTC2.png

        .. note:: Puoi scaricare e stampare le :download:`Carte dei Colori PDF <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>` per il rilevamento dei colori.


    * **Rileva Volto**

        Digita ``f`` per attivare il rilevamento del volto.

        .. image:: img/DTC5.png

    * **Rileva Codice QR**

        Inserisci ``r`` per avviare il riconoscimento del codice QR. Nessuna altra operazione può essere eseguita finché il codice QR non è stato riconosciuto. Le informazioni decodificate del codice QR saranno stampate nel terminale.

        .. image:: img/DTC4.png

    * **Mostra Informazioni**

        Inserendo ``s`` verranno stampate nel terminale le informazioni sul volto rilevato (e sull'oggetto rilevato). Incluse le coordinate centrali (X, Y) e la dimensione (Larghezza, Altezza) dell'oggetto misurato.

**Codice**

.. code-block:: python

    from vilib import Vilib
    from time import sleep, time, strftime, localtime
    import threading
    from os import getlogin
    
    USERNAME = getlogin()
    PICTURE_PATH = f"/home/{USERNAME}/Pictures/"
    
    
    flag_face = False
    flag_color = False
    qr_code_flag = False
    
    MANUAL = '''
    Input key to call the function!
        q: Take photo
        1: Color detect : red
        2: Color detect : orange
        3: Color detect : yellow
        4: Color detect : green
        5: Color detect : blue
        6: Color detect : purple
        0: Switch off Color detect
        r: Scan the QR code
        f: Switch ON/OFF face detect
        s: Display detected object information
    '''
    
    color_list = ['close', 'red', 'orange', 'yellow', 
            'green', 'blue', 'purple',
    ]
    
    def face_detect(flag):
        print("Face Detect:" + str(flag))
        Vilib.face_detect_switch(flag)
    
    
    def qrcode_detect():
        global qr_code_flag
        if qr_code_flag == True:
            Vilib.qrcode_detect_switch(True)
            print("Waitting for QR code")
    
        text = None
        while True:
            temp = Vilib.detect_obj_parameter['qr_data']
            if temp != "None" and temp != text: 
                text = temp         
                print('QR code:%s'%text)
            if qr_code_flag == False:          
                break
            sleep(0.5)
        Vilib.qrcode_detect_switch(False)
    
    
    def take_photo():
        _time = strftime('%Y-%m-%d-%H-%M-%S',localtime(time()))
        name = 'photo_%s'%_time
        Vilib.take_photo(name, PICTURE_PATH)
        print('photo save as %s%s.jpg'%(PICTURE_PATH, name))
    
    
    def object_show():
        global flag_color, flag_face
    
        if flag_color is True:
            if Vilib.detect_obj_parameter['color_n'] == 0:
                print('Color Detect: None')
            else:
                color_coodinate = (Vilib.detect_obj_parameter['color_x'],Vilib.detect_obj_parameter['color_y'])
                color_size = (Vilib.detect_obj_parameter['color_w'],Vilib.detect_obj_parameter['color_h'])
                print("[Color Detect] ","Coordinate:",color_coodinate,"Size",color_size)
    
        if flag_face is True:
            if Vilib.detect_obj_parameter['human_n'] == 0:
                print('Face Detect: None')
            else:
                human_coodinate = (Vilib.detect_obj_parameter['human_x'],Vilib.detect_obj_parameter['human_y'])
                human_size = (Vilib.detect_obj_parameter['human_w'],Vilib.detect_obj_parameter['human_h'])
                print("[Face Detect] ","Coordinate:",human_coodinate,"Size",human_size)
    
    
    def main():
        global flag_face, flag_color, qr_code_flag
        qrcode_thread = None
    
        Vilib.camera_start(vflip=False,hflip=False)
        Vilib.display(local=True,web=True)
        print(MANUAL)
    
        while True:
            # readkey
            key = input()
            key = key.lower()
            # take photo
            if key == 'q':
                take_photo()
            # color detect         
            elif key != '' and key in ('0123456'):  # '' in ('0123') -> True
                index = int(key)
                if index == 0:
                    flag_color = False
                    Vilib.color_detect('close')
                else:
                    flag_color = True
                    Vilib.color_detect(color_list[index]) # color_detect(color:str -> color_name/close)
                print('Color detect : %s'%color_list[index])  
            # face detection
            elif key =="f":
                flag_face = not flag_face
                face_detect(flag_face)
            # qrcode detection
            elif key =="r":
                qr_code_flag = not qr_code_flag
                if qr_code_flag == True:
                    if qrcode_thread == None or not qrcode_thread.is_alive():
                    qrcode_thread = threading.Thread(target=qrcode_detect)
                    qrcode_thread.setDaemon(True)
                    qrcode_thread.start()
                else:
                    if qrcode_thread != None and qrcode_thread.is_alive(): 
                       # wait for thread to end 
                    qrcode_thread.join()
                        print('QRcode Detect: close')
            # show detected object information
            elif key == "s":
                object_show()
    
            sleep(0.5)
    
    
    if __name__ == "__main__":
        main()

**Come Funziona?**

La parte fondamentale è l'avvio della fotocamera e il display:

.. code-block:: python

    Vilib.camera_start()
    Vilib.display()

Funzioni correlate alla "rilevazione degli oggetti":

* ``Vilib.face_detect_switch(True)`` : Attiva/Disattiva il rilevamento volti
* ``Vilib.color_detect(color)`` : Rileva un colore, specifica tra ``"rosso"``, ``"arancione"``, ``"giallo"``, ``"verde"``, ``"blu"``, ``"viola"``
* ``Vilib.color_detect_switch(False)`` : Disattiva rilevamento colori
* ``Vilib.qrcode_detect_switch(False)`` : Attiva/Disattiva il rilevamento QR code
* ``Vilib.gesture_detect_switch(False)`` : Attiva/Disattiva rilevamento gesti
* ``Vilib.traffic_sign_detect_switch(False)`` : Attiva/Disattiva rilevamento segnali stradali

Informazioni rilevate archiviate nel dizionario ``detect_obj_parameter = Manager().dict()``.

Esempio d'uso:

.. code-block:: python

    Vilib.detect_obj_parameter['color_x']

Chiavi del dizionario e loro utilizzo:

* ``color_x``: il valore x della coordinata centrale del blocco di colore rilevato, con un intervallo di 0~320
* ``color_y``: il valore y della coordinata centrale del blocco di colore rilevato, con un intervallo di 0~240
* ``color_w``: la larghezza del blocco di colore rilevato, con un intervallo di 0~320
* ``color_h``: l'altezza del blocco di colore rilevato, con un intervallo di 0~240
* ``color_n``: il numero di blocchi di colore rilevati
* ``human_x``: il valore x della coordinata centrale del volto umano rilevato, con un intervallo di 0~320
* ``human_y``: il valore y della coordinata centrale del volto umano rilevato, con un intervallo di 0~240
* ``human_w``: la larghezza del volto umano rilevato, con un intervallo di 0~320
* ``human_h``: l'altezza del volto umano rilevato, con un intervallo di 0~240
* ``human_n``: il numero di volti rilevati
* ``traffic_sign_x``: il valore x della coordinata centrale del segnale stradale rilevato, con un intervallo di 0~320
* ``traffic_sign_y``: il valore y della coordinata centrale del segnale stradale rilevato, con un intervallo di 0~240
* ``traffic_sign_w``: la larghezza del segnale stradale rilevato, con un intervallo di 0~320
* ``traffic_sign_h``: l'altezza del segnale stradale rilevato, con un intervallo di 0~240
* ``traffic_sign_t``: il contenuto del segnale stradale rilevato; l'elenco dei valori è `['stop','right','left','forward']`
* ``gesture_x``: il valore x della coordinata centrale del gesto rilevato, con un intervallo di 0~320
* ``gesture_y``: il valore y della coordinata centrale del gesto rilevato, con un intervallo di 0~240
* ``gesture_w``: la larghezza del gesto rilevato, con un intervallo di 0~320
* ``gesture_h``: l'altezza del gesto rilevato, con un intervallo di 0~240
* ``gesture_t``: il contenuto del gesto rilevato; l'elenco dei valori è `["paper","scissor","rock"]`
* ``qr_date``: il contenuto del codice QR rilevato
* ``qr_x``: il valore x della coordinata centrale del codice QR rilevato, con un intervallo di 0~320
* ``qr_y``: il valore y della coordinata centrale del codice QR rilevato, con un intervallo di 0~240
* ``qr_w``: la larghezza del codice QR rilevato, con un intervallo di 0~320
* ``qr_h``: l'altezza del codice QR rilevato, con un intervallo di 0~320
