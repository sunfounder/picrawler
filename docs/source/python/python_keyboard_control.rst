.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti Speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a promozioni e concorsi durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_keyboard:

Controllo tramite Tastiera
============================

In questo progetto, impareremo come utilizzare la tastiera per controllare da remoto il PiCrawler. Potrai comandare il PiCrawler per avanzare, retrocedere, girare a sinistra o a destra.

**Esegui il Codice**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 keyboard_control.py

Quando il programma si avvia, PiCrawler viene inizializzato e nel terminale viene visualizzata un’interfaccia di controllo da tastiera.

Premi i tasti sulla tastiera per controllare PiCrawler!

* ``w``: Avanti
* ``a``: Gira a sinistra
* ``s``: Indietro
* ``d``: Gira a destra
* ``Ctrl+C``: Esci

La velocità corrente viene mostrata e può essere regolata tramite:

- + / ] per aumentare la velocità
- - / [ per diminuire la velocità

Dopo ogni azione, viene applicato un breve ritardo per migliorare la stabilità.

Premi Ctrl+C per uscire.
Prima di terminare, il crawler esegue in modo sicuro l’azione "sit".

**Codice**

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep
    import readchar

    crawler = Picrawler()

    SPEED_MIN = 20
    SPEED_MAX = 70
    speed = 60

    STEP = 1            # Number of action steps per key press
    ACTION_GAP = 0.25   # Delay after each action to reduce current spikes

    manual = """
    Keyboard Control - PiCrawler

    Movement:
    W: Forward
    A: Turn left
    S: Backward
    D: Turn right

    Speed Control:
    + / ] : Increase speed
    - / [ : Decrease speed

    Other:
    Space  : Stop (no action)
    Ctrl+C : Quit (auto sit)
    """

    def clamp(value, min_value, max_value):
        """Limit value within a specified range."""
        return max(min_value, min(max_value, value))

    def show_info():
        """Clear terminal and display control instructions."""
        print("\033[H\033[J", end="")  # Clear terminal screen
        print(manual)
        print(f"Current speed: {speed}  (range {SPEED_MIN}-{SPEED_MAX})")
        print(f"Action gap: {ACTION_GAP:.2f}s")

    def do_move(action_name):
        """Execute movement action with safety delay."""
        crawler.do_action(action_name, STEP, speed)
        sleep(ACTION_GAP)

    def safe_sit():
        """Safely sit down before program exit."""
        try:
            crawler.do_step("sit", clamp(speed, 20, 40))
            sleep(1.0)
        except Exception:
            pass

    def main():
        show_info()

        try:
            while True:
                key = readchar.readkey()
                k = key.lower()

                if k == "w":
                    do_move("forward")
                elif k == "s":
                    do_move("backward")
                elif k == "a":
                    do_move("turn left")
                elif k == "d":
                    do_move("turn right")

                # Speed increase
                elif k in ("+", "]"):
                    global speed
                    speed = clamp(speed + 5, SPEED_MIN, SPEED_MAX)

                # Speed decrease
                elif k in ("-", "["):
                    speed = clamp(speed - 5, SPEED_MIN, SPEED_MAX)

                # Stop (no movement)
                elif k == " ":
                    pass

                # Quit using readchar special key
                elif key == readchar.key.CTRL_C:
                    print("\nQuit.")
                    break

                show_info()
                sleep(0.02)

        except KeyboardInterrupt:
            print("\nQuit (KeyboardInterrupt).")

        finally:
            safe_sit()

    if __name__ == "__main__":
        main()

**Come funziona?**

#. Creazione dell'oggetto robot

   .. code-block:: python

      crawler = Picrawler()

   Questa riga crea un oggetto ``Picrawler``.
   Permette al programma di controllare i movimenti del robot.

#. Definizione dell'intervallo di velocità sicuro

   .. code-block:: python

      SPEED_MIN = 20
      SPEED_MAX = 70
      speed = 60

   Queste variabili definiscono l'intervallo di velocità consentito.
   ``speed`` memorizza la velocità di movimento corrente.
   Il robot non si muoverà più velocemente del valore massimo.

#. Limitazione della velocità con clamp()

   .. code-block:: python

      def clamp(value, min_value, max_value):
          return max(min_value, min(max_value, value))

   Questa funzione assicura che la velocità rimanga entro l'intervallo sicuro.
   Previene movimenti instabili causati da valori estremi.

#. Esecuzione di un movimento

   .. code-block:: python

      def do_move(action_name):
          crawler.do_action(action_name, STEP, speed)
          sleep(ACTION_GAP)

   Questa funzione invia un comando di movimento al robot.
   ``ACTION_GAP`` aggiunge un breve ritardo per migliorare la stabilità.

#. Lettura dell'input da tastiera

   .. code-block:: python

      key = readchar.readkey()
      k = key.lower()

   Il programma attende la pressione di un tasto.
   Il tasto viene convertito in minuscolo per garantire coerenza.

#. Logica di controllo del movimento

   .. code-block:: python

      if k == "w":
          do_move("forward")
      elif k == "s":
          do_move("backward")

   Quando viene premuto un tasto, il movimento corrispondente viene eseguito immediatamente.
   Non è necessario premere Invio.

#. Uscita sicura

   .. code-block:: python

      finally:
          safe_sit()

   Prima che il programma termini, il robot esegue un'azione sicura di "sit".
   Questo previene posture instabili o uno spegnimento improvviso.