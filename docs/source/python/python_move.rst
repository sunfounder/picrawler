.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti Speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a promozioni e concorsi durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_move:

Movimento
=========

Questo è il primo progetto di PiCrawler. Realizza la sua funzione più basilare: il movimento.

.. .. image:: img/move.png

**Esegui il Codice**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 move.py

Quando il programma si avvia, PiCrawler si alza e attende brevemente.

Successivamente esegue continuamente un ciclo di movimenti:
avanti, indietro, gira a sinistra, gira a destra,
piccola rotazione a sinistra e piccola rotazione a destra.

Ogni azione è separata da brevi pause per rendere il movimento più fluido.

Premi Ctrl+C per interrompere il programma.
Prima di uscire, il crawler si siede in modo sicuro.

**Codice**

.. note::
    Puoi **Modificare/Reimpostare/Copiare/Eseguire/Interrompere** il codice seguente. Tuttavia, prima di farlo, devi accedere al percorso del codice sorgente come ``picrawler\examples``. Dopo aver modificato il codice, puoi eseguirlo direttamente per vedere l'effetto.

.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep

    crawler = Picrawler()  # Create PiCrawler object

    def main():
        speed = 80  # Movement speed

        try:
            crawler.do_step('stand', 40)  # Stand up
            sleep(1.0)

            while True:
                crawler.do_action('forward', 1, speed)   # Move forward
                sleep(0.25)

                crawler.do_action('backward', 1, speed)  # Move backward
                sleep(0.25)

                crawler.do_action('turn left', 1, speed)  # Turn left
                sleep(0.25)

                crawler.do_action('turn right', 1, speed)  # Turn right
                sleep(0.25)

                crawler.do_action('turn left angle', 1, speed)  # Small left turn
                sleep(0.3)

                crawler.do_action('turn right angle', 1, speed)  # Small right turn
                sleep(0.3)

                sleep(0.5)

        except KeyboardInterrupt:
            print("\nCtrl+C pressed...")

        finally:
            crawler.do_step('sit', 40)  # Sit down before exit
            sleep(1.0)

    if __name__ == "__main__":
        main()

**Come funziona?**

#. Importazione e inizializzazione

   .. code-block:: python

      from picrawler import Picrawler
      from time import sleep

      crawler = Picrawler()

   Lo script importa i moduli necessari e crea un oggetto
   ``Picrawler``, che viene utilizzato per controllare tutti i movimenti del robot.

#. Funzione principale e configurazione

   .. code-block:: python

      def main():
          speed = 80
          crawler.do_step('stand', 40)
          sleep(1.0)

   La funzione ``main()`` definisce la velocità di movimento.
   Prima di avviare il ciclo, il robot si alza e si stabilizza.

#. Ciclo continuo di movimento

   .. code-block:: python

      while True:
          crawler.do_action('forward', 1, speed)
          crawler.do_action('backward', 1, speed)
          crawler.do_action('turn left', 1, speed)
          crawler.do_action('turn right', 1, speed)
          crawler.do_action('turn left angle', 1, speed)
          crawler.do_action('turn right angle', 1, speed)

   Il robot esegue continuamente una sequenza predefinita di
   azioni di movimento all'interno di un ciclo infinito.
   Brevi pause tra le azioni aiutano a rendere il movimento più fluido.

#. Gestione dell'uscita sicura

   .. code-block:: python

      except KeyboardInterrupt:
          print("\nCtrl+C pressed...")
      finally:
          crawler.do_step('sit', 40)

   La struttura ``try / except / finally`` garantisce:
   - Ctrl+C interrompe il ciclo in modo sicuro.
   - Il robot si siede prima che il programma termini.

#. Avvio del programma

   .. code-block:: python

      if __name__ == "__main__":
          main()

   Questo assicura che ``main()`` venga eseguita solo quando lo script
   viene avviato direttamente.