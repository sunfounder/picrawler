.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti Speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a promozioni e concorsi durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_avoid:

Evitamento Ostacoli
=====================

In questo progetto, PiCrawler utilizzerà un modulo ultrasonico per rilevare gli ostacoli davanti a sé. 
Quando PiCrawler rileva un ostacolo, invierà un segnale e cercherà un'altra direzione per proseguire.

.. .. image:: img/avoid1.png

**Esegui il Codice**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 avoid.py

Quando il programma si avvia, PiCrawler si alza.

Misura continuamente la distanza utilizzando il sensore a ultrasuoni
e stampa il valore nel terminale.

Se viene rilevato un ostacolo entro 15 cm:
- Viene riprodotto un suono di avviso.
- Il robot esegue una piccola rotazione verso sinistra.

Se il percorso è libero:
- Il robot si muove in avanti.

Il robot continua a evitare gli ostacoli automaticamente finché non si preme Ctrl+C.

Prima di uscire, si siede in modo sicuro.

**Codice**

.. note::
    Puoi **Modificare/Reimpostare/Copiare/Eseguire/Fermare** il codice qui sotto. Prima di farlo, devi accedere al percorso del codice sorgente come ``picrawler\examples``. Dopo aver modificato il codice, puoi eseguirlo direttamente per vedere il risultato.

.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from robot_hat import Music, Ultrasonic, Pin
    import time
    import signal

    music = Music()
    crawler = Picrawler()
    sonar = Ultrasonic(Pin("D2"), Pin("D3"))  # Ultrasonic trigger/echo pins

    music.music_set_volume(100)  # Set speaker volume

    alert_distance = 15  # Obstacle warning distance (cm)
    speed = 80           # Movement speed

    # ----------------------------
    # Add hardware timeout to sonar.read()
    # Prevent program from freezing
    # ----------------------------
    class Timeout(Exception):
        pass

    def _alarm_handler(signum, frame):
        raise Timeout()

    signal.signal(signal.SIGALRM, _alarm_handler)

    # Read distance once with timeout protection
    def safe_read_once(timeout_s=1):
        try:
            signal.alarm(timeout_s)
            d = sonar.read()
            signal.alarm(0)
            return d
        except Timeout:
            signal.alarm(0)
            return None
        except Exception:
            signal.alarm(0)
            return None

    # Read multiple times and return median value (anti-noise)
    def read_distance_filtered(n=5, gap=0.03, timeout_s=1):
        vals = []
        for _ in range(n):
            d = safe_read_once(timeout_s=timeout_s)
            if d is not None and d > 0:
                vals.append(d)
            time.sleep(gap)

        if not vals:
            return None

        vals.sort()
        return vals[len(vals)//2]  # Median filter

    def main():
        distance = read_distance_filtered(n=5, gap=0.03, timeout_s=1)
        print("distance:", distance)

        if distance is None:
            time.sleep(0.15)  # Wait if read failed
            return

        if distance <= alert_distance:
            # Obstacle detected → play sound and turn
            try:
                music.sound_play_threading('./sounds/sign.wav', volume=100)
            except Exception as e:
                print("sound error:", e)

            crawler.do_action('turn left angle', 1, speed)
            time.sleep(0.5)  # Quiet window after movement
        else:
            # Path clear → move forward
            crawler.do_action('forward', 1, speed)
            time.sleep(0.4)

    if __name__ == "__main__":
        try:
            crawler.do_step('stand', 40)  # Stand before starting
            time.sleep(1.0)

            while True:
                main()

        except KeyboardInterrupt:
            print("\nStop.")
        finally:
            try:
                crawler.do_step('sit', 40)  # Sit before exit
                time.sleep(1.0)
            except Exception:
                pass

**Come funziona?**

#. Blocco di inizializzazione

   .. code-block:: python

      music = Music()
      crawler = Picrawler()
      sonar = Ultrasonic(Pin("D2"), Pin("D3"))

      music.music_set_volume(100)
      alert_distance = 15
      speed = 80

   Questo blocco inizializza i tre moduli principali:
   - ``music``: controlla la riproduzione dei suoni.
   - ``crawler``: controlla i movimenti del PiCrawler.
   - ``sonar``: legge la distanza tramite il sensore a ultrasuoni.

   Imposta inoltre il volume dell'altoparlante, la soglia di rilevamento degli ostacoli (cm)
   e la velocità di movimento.

#. Blocco di configurazione del timeout (evita che ``sonar.read()`` si blocchi)

   .. code-block:: python

      class Timeout(Exception):
          pass

      def _alarm_handler(signum, frame):
          raise Timeout()

      signal.signal(signal.SIGALRM, _alarm_handler)

   Il driver del sensore a ultrasuoni può bloccarsi mentre attende il segnale di eco.
   Questo blocco installa un gestore di segnale in modo che il programma possa interrompere
   una chiamata bloccata a ``sonar.read()`` e continuare a funzionare.

#. Funzione: safe_read_once()

   .. code-block:: python

      def safe_read_once(timeout_s=1):
          try:
              signal.alarm(timeout_s)
              d = sonar.read()
              signal.alarm(0)
              return d
          except Timeout:
              signal.alarm(0)
              return None
          except Exception:
              signal.alarm(0)
              return None

   Questa funzione legge una volta la distanza a ultrasuoni con protezione di timeout.
   - Se la lettura ha successo, restituisce il valore della distanza.
   - Se scade il timeout o si verifica un errore, restituisce ``None`` invece di bloccarsi.

#. Funzione: read_distance_filtered()

   .. code-block:: python

      def read_distance_filtered(n=5, gap=0.03, timeout_s=1):
          vals = []
          for _ in range(n):
              d = safe_read_once(timeout_s=timeout_s)
              if d is not None and d > 0:
                  vals.append(d)
              time.sleep(gap)

          if not vals:
              return None

          vals.sort()
          return vals[len(vals)//2]

   Questa funzione migliora l'affidabilità effettuando più letture:
   - I valori non validi (``None`` oppure ``<= 0``) vengono ignorati.
   - I valori rimanenti vengono ordinati.
   - Viene restituito il valore mediano per ridurre il rumore.

#. Funzione: main() (logica principale di decisione e azione)

   .. code-block:: python

      def main():
          distance = read_distance_filtered(...)
          if distance is None:
              return

          if distance <= alert_distance:
              music.sound_play_threading(...)
              crawler.do_action('turn left angle', 1, speed)
          else:
              crawler.do_action('forward', 1, speed)

   Questa è la logica di controllo principale:

   - Legge un valore di distanza filtrato.
   - Se la lettura fallisce, salta questo ciclo.
   - Se un ostacolo è più vicino di ``alert_distance``, riproduce un suono di avviso e gira a sinistra.
   - Altrimenti, si muove in avanti.

#. Blocco di avvio del programma (ciclo continuo + uscita sicura)

   .. code-block:: python

      if __name__ == "__main__":
          try:
              crawler.do_step('stand', 40)
              while True:
                  main()
          except KeyboardInterrupt:
              print("\nStop.")
          finally:
              crawler.do_step('sit', 40)

   Questo blocco controlla il flusso generale del programma:
   - Il crawler si alza prima di iniziare.
   - Il programma esegue ``main()`` ripetutamente in un ciclo infinito.
   - Premendo Ctrl+C si interrompe il ciclo.
   - Il crawler si siede prima che il programma termini.