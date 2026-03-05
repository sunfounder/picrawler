.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie mit anderen Enthusiasten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Gewinnspielen und saisonalen Aktionen teil.

    👉 Bereit, mit uns zu entdecken und zu gestalten? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _py_vision:

Computer Vision
=======================

Dieses Projekt führt Sie offiziell in das Gebiet der Computer Vision ein!

**Code ausführen**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 display.py

**Bild anzeigen**

Nach dem Start des Codes wird im Terminal folgende Eingabeaufforderung angezeigt:

.. code-block::

    No desktop !
    * Serving Flask app "vilib.vilib" (lazy loading)
    * Environment: production
    WARNING: Do not use the development server in a production environment.
    Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)

Dann können Sie im Browser ``http://<Ihre IP>:9000/mjpg`` eingeben, um den Videostream anzuzeigen. Beispiel: ``http://192.168.18.113:9000/mjpg``

.. image:: img/display.png

Nach dem Start des Programms werden folgende Informationen angezeigt:

* Geben Sie eine Taste ein, um eine Funktion aufzurufen!
* ``q``: Foto aufnehmen
* ``1``: Farberkennung: Rot
* ``2``: Farberkennung: Orange
* ``3``: Farberkennung: Gelb
* ``4``: Farberkennung: Grün
* ``5``: Farberkennung: Blau
* ``6``: Farberkennung: Lila
* ``0``: Farberkennung ausschalten
* ``r``: QR-Code scannen
* ``f``: Gesichts- und Farberkennung ein-/ausschalten
* ``s``: Erfasste Objektinformationen anzeigen

Befolgen Sie die Anweisungen, um die entsprechenden Funktionen zu aktivieren.

    *  **Foto aufnehmen**

        Geben Sie ``q`` in das Terminal ein. Das aktuell von der Kamera gesehene Bild wird gespeichert (wenn die Farberkennungsfunktion aktiviert ist, wird auch der Markierungsrahmen im gespeicherten Bild angezeigt). Diese Fotos finden Sie im Verzeichnis ``~/Pictures/PiCrawler/`` auf dem Raspberry Pi.
        Sie können Tools wie :ref:`filezilla` verwenden, um die Fotos auf Ihren PC zu übertragen.

    *  **Farberkennung**

        Wenn Sie eine Zahl zwischen ``1~6`` eingeben, wird eine der Farben "Rot, Orange, Gelb, Grün, Blau, Lila" erkannt. Geben Sie ``0`` ein, um die Farberkennung auszuschalten.

        .. image:: img/DTC2.png

        .. note:: Sie können die :download:`PDF-Farbkarten <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>` für die Farberkennung herunterladen und ausdrucken.


    *  **Gesichtserkennung**

        Geben Sie ``f`` ein, um die Gesichtserkennung zu aktivieren.

        .. image:: img/DTC5.png

    *  **QR-Code-Erkennung**

        Geben Sie ``r`` ein, um die QR-Code-Erkennung zu aktivieren. Bevor der QR-Code erkannt wird, können keine weiteren Aktionen ausgeführt werden. Die Decodierungsinformationen des QR-Codes werden im Terminal angezeigt.

        .. image:: img/DTC4.png

    *  **Informationen anzeigen**

        Geben Sie ``s`` ein, um die Informationen des Gesichtserkennungs- (und Farberkennungs-) Ziels im Terminal anzuzeigen, einschließlich der Koordinaten (X, Y) und der Größe (Breite, Höhe) des gemessenen Objekts.

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

**Funktionsweise**

Zu Beginn sollten Sie folgende Funktionen beachten, die die Kamera starten:

.. code-block:: python

    Vilib.camera_start()
    Vilib.display()

Funktionen zur "Objekterkennung":

* ``Vilib.face_detect_switch(True)``: Aktiviert/deaktiviert die Gesichtserkennung.
* ``Vilib.color_detect(color)``: Erkennt Farben. Nur eine Farbe kann gleichzeitig erkannt werden. Eingabewerte: ``"red"``, ``"orange"``, ``"yellow"``, ``"green"``, ``"blue"``, ``"purple"``.
* ``Vilib.color_detect_switch(False)``: Deaktiviert die Farberkennung.
* ``Vilib.qrcode_detect_switch(False)``: Aktiviert/deaktiviert die QR-Code-Erkennung. Gibt dekodierte QR-Daten zurück.
* ``Vilib.gesture_detect_switch(False)``: Aktiviert/deaktiviert die Gestenerkennung.
* ``Vilib.traffic_sign_detect_switch(False)``: Aktiviert/deaktiviert die Verkehrsschilderkennung.

Die erkannten Informationen werden in ``detect_obj_parameter = Manager().dict()`` gespeichert.

Im Hauptprogramm können Sie auf diese Weise darauf zugreifen:

.. code-block:: python

    Vilib.detect_obj_parameter['color_x']

Die Schlüssel des Wörterbuchs und ihre Verwendungen sind in der folgenden Liste dargestellt:

* ``color_x``: Der x-Wert der zentralen Koordinate des erkannten Farbfeldes, der Bereich ist 0~320.
* ``color_y``: Der y-Wert der zentralen Koordinate des erkannten Farbfeldes, der Bereich ist 0~240.
* ``color_w``: Die Breite des erkannten Farbfeldes, der Bereich ist 0~320.
* ``color_h``: Die Höhe des erkannten Farbfeldes, der Bereich ist 0~240.
* ``color_n``: Die Anzahl der erkannten Farbfelder.
* ``human_x``: Der x-Wert der zentralen Koordinate des erkannten menschlichen Gesichts, der Bereich ist 0~320.
* ``human_y``: Der y-Wert der zentralen Koordinate des erkannten Gesichts, der Bereich ist 0~240.
* ``human_w``: Die Breite des erkannten menschlichen Gesichts, der Bereich ist 0~320.
* ``human_h``: Die Höhe des erkannten Gesichts, der Bereich ist 0~240.
* ``human_n``: Die Anzahl der erkannten Gesichter.
* ``traffic_sign_x``: Der x-Wert der zentralen Koordinate des erkannten Verkehrsschildes, der Bereich ist 0~320.
* ``traffic_sign_y``: Der y-Wert der zentralen Koordinate des erkannten Verkehrsschildes, der Bereich ist 0~240.
* ``traffic_sign_w``: Die Breite des erkannten Verkehrsschildes, der Bereich ist 0~320.
* ``traffic_sign_h``: Die Höhe des erkannten Verkehrsschildes, der Bereich ist 0~240.
* ``traffic_sign_t``: Der Inhalt des erkannten Verkehrsschildes, die Werteliste lautet `['stop','right','left','forward']`.
* ``gesture_x``: Der x-Wert der zentralen Koordinate der erkannten Geste, der Bereich ist 0~320.
* ``gesture_y``: Der y-Wert der zentralen Koordinate der erkannten Geste, der Bereich ist 0~240.
* ``gesture_w``: Die Breite der erkannten Geste, der Bereich ist 0~320.
* ``gesture_h``: Die Höhe der erkannten Geste, der Bereich ist 0~240.
* ``gesture_t``: Der Inhalt der erkannten Geste, die Werteliste lautet `["paper","scissor","rock"]`.
* ``qr_date``: Der Inhalt des erkannten QR-Codes.
* ``qr_x``: Der x-Wert der zentralen Koordinate des zu erkennenden QR-Codes, der Bereich ist 0~320.
* ``qr_y``: Der y-Wert der zentralen Koordinate des zu erkennenden QR-Codes, der Bereich ist 0~240.
* ``qr_w``: Die Breite des zu erkennenden QR-Codes, der Bereich ist 0~320.
* ``qr_h``: Die Höhe des zu erkennenden QR-Codes, der Bereich ist 0~320.

