.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti Speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a promozioni e concorsi durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _control_by_app:

Controllo tramite l'APP
========================

Il controller SunFounder è utilizzato per controllare i robot basati su Raspberry Pi/Pico.

L'APP integra widget come Pulsante, Interruttore, Joystick, D-pad, Slider e Slider per accelerazione; widget di input come Display Digitale, Radar Ultrasonico, Rilevamento di Scala di Grigi e Tachimetro.

Sono disponibili 17 aree A-Q dove puoi posizionare diversi widget per personalizzare il tuo controller.

Inoltre, questa applicazione offre un servizio di streaming video in diretta.

Personalizziamo un controller PiCrawler utilizzando questa app.

**Come fare?**

#. Installa il modulo ``sunfounder-controller``.

    I moduli ``robot-hat``, ``vilib`` e ``picrawler`` devono essere installati prima. Per i dettagli, consulta: :ref:`install_all_modules`.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~
        git clone https://github.com/sunfounder/sunfounder-controller.git
        cd ~/sunfounder-controller
        sudo python3 setup.py install

#. Esegui il codice.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/sunfounder-controller/examples
        sudo python3 picrawler_control.py

#. Installa `SunFounder Controller <https://docs.sunfounder.com/projects/sf-controller/en/latest/>`_ da **APP Store (iOS)** o **Google Play (Android)**.


#. Apri e crea un nuovo controller.

    Crea un nuovo controller cliccando sul segno + nell'APP SunFounder Controller.

    .. image:: img/app1.PNG

    Ci sono controller preimpostati per alcuni prodotti nella sezione Preset. Qui scegliamo PiCrawler.

    .. image:: img/app_control1.jpg

    Dagli un nome e seleziona il tipo di Controller. 

    .. image:: img/app_control2.jpg

    Entrando nel controller preimpostato, noterai che ci sono già alcuni widget. Se non devi apportare modifiche, clicca il pulsante |app_save|.

    .. image:: img/app_control3.jpg

#. Connetti a PiCrawler.

    Cliccando il pulsante **Connect**, verranno cercati automaticamente i robot nelle vicinanze. Il nome è definito in ``picrawler_control.py`` e deve essere in esecuzione.

    .. image:: img/app_control6.jpg
    
    Una volta cliccato sul nome del prodotto, apparirà il messaggio "Connected Successfully" e il nome del prodotto apparirà nell'angolo in alto a destra.

    .. image:: img/app_control7.jpg

    .. note::

        * Assicurati che il tuo dispositivo mobile sia connesso alla stessa LAN di PiCrawler.
        * Se la ricerca non avviene automaticamente, puoi inserire manualmente l'IP per connetterti.

        .. image:: img/app11.PNG

#. Esegui questo controller.

    Clicca il pulsante **Run** per avviare il controller. Vedrai il filmato ripreso dall'auto e potrai controllare il tuo PiCrawler utilizzando questi widget.

    .. image:: img/app_control8.jpg
    
    Ecco le funzioni dei widget:

    * **A**: Imposta la potenza del PiCrawler.
    * **B**: Mostra la velocità di movimento del robot.
    * **C**: Stessa funzione del widget B.
    * **D**: Mostra gli ostacoli rilevati con punti rossi.
    * **G**: Riconoscimento vocale: premi e tieni premuto questo widget per iniziare a parlare, e verrà mostrato il comando riconosciuto quando lo rilasci. Nel codice sono impostati i comandi ``forward``, ``backward``, ``left`` e ``right`` per controllare l'auto.
    * **K**: Controlla i movimenti avanti, indietro, sinistra e destra dell'auto.
    * **Q**: Muove la testa (Camera) su, giù, sinistra e destra.
    * **N**: Attiva la funzione di riconoscimento dei colori.
    * **O**: Attiva la funzione di riconoscimento facciale.
    * **P**: Attiva la funzione di riconoscimento degli oggetti. Può riconoscere circa 90 tipi di oggetti. Per l'elenco dei modelli, consulta: https://github.com/sunfounder/vilib/blob/master/workspace/coco_labels.txt.
