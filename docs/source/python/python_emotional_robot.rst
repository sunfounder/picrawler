.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti Speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a promozioni e concorsi durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_emotional:

Robot Emotivo
================

Questo esempio mostra diverse azioni personalizzate e divertenti di PiCrawler.

**Esegui il Codice**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 emotional_robot.py

After running the program, the robot first stands up slowly to reach a stable posture.

It then performs a series of motions, including swimming-like movements, push-ups, waving gestures with the front legs, and a twisting dance. These actions are executed sequentially, creating a dynamic and expressive behavior.

If **Ctrl+C** is pressed, the program exits safely and the robot returns to a sitting position.

**Codice**

.. note::
    Puoi **Modificare/Reimpostare/Copiare/Eseguire/Interrompere** il codice qui sotto. Prima di farlo, devi accedere al percorso del codice sorgente come ``picrawler\examples``. Dopo aver modificato il codice, puoi eseguirlo direttamente per vedere il risultato.

.. raw:: html

    <run></run>


.. code-block:: python

    from picrawler import Picrawler
    from time import sleep

    crawler = Picrawler()


    def get_sit_step():
        # Get a valid sit step used as the base pose for hand actions
        try:
            return crawler.move_list['sit'][0]
        except Exception:
            return None


    def handwork(speed):
        base = get_sit_step()

        # If a valid sit step cannot be retrieved, just perform a sit action
        if not base or len(base) < 4:
            crawler.do_step('sit', speed)
            sleep(0.6)
            return

        # Generate hand poses by modifying the sit step
        left_hand = crawler.mix_step(base, 0, [0, 50, 80])
        right_hand = crawler.mix_step(base, 1, [0, 50, 80])
        two_hand = crawler.mix_step(left_hand, 1, [0, 50, 80])

        crawler.do_step('sit', speed)
        sleep(0.6)

        crawler.do_step(left_hand, speed)
        sleep(0.6)

        crawler.do_step(two_hand, speed)
        sleep(0.6)

        crawler.do_step(right_hand, speed)
        sleep(0.6)

        crawler.do_step('sit', speed)
        sleep(0.6)

    def twist(speed):
        # Initialize the base position for all four legs
        new_step = [[50, 50, -80], [50, 50, -80], [50, 50, -80], [50, 50, -80]]

        # Create a twisting motion by alternating rise and drop movements
        for i in range(4):
            for inc in range(30, 60, 5):
                rise = [50, 50, (-80 + inc * 0.5)]
                drop = [50, 50, (-80 - inc)]

                new_step[i] = rise
                new_step[(i + 2) % 4] = drop
                new_step[(i + 1) % 4] = rise
                new_step[(i - 1) % 4] = drop

                crawler.do_step(new_step, speed)
                sleep(0.02)

    def pushup(speed):
        # Two poses used to simulate a push-up motion
        up = [[80, 0, -100], [80, 0, -100], [0, 120, -60], [0, 120, -60]]
        down = [[80, 0, -30], [80, 0, -30], [0, 120, -60], [0, 120, -60]]

        crawler.do_step(up, speed)
        sleep(0.6)

        crawler.do_step(down, speed)
        sleep(0.6)

    def swimming(speed, loops=100):
        # Simulate a swimming-like motion by gradually adjusting leg coordinates
        for i in range(loops):
            crawler.do_step(
                [
                    [100 - i, i, 0],
                    [100 - i, i, 0],
                    [0, 120, -60 + i / 5],
                    [0, 100, -40 - i / 5]
                ],
                speed
            )
            sleep(0.01)

    def main():
        speed = 100

        try:
            # Stand up slowly before performing actions
            crawler.do_step('stand', 40)
            sleep(1.0)

            swimming(speed)
            pushup(speed)
            handwork(speed)
            twist(speed)

        except KeyboardInterrupt:
            print("\nCtrl+C detected, exiting...")

        finally:
            # Return to a sitting posture before exiting
            try:
                crawler.do_step('sit', 40)
                sleep(1.0)
            except Exception:
                pass

    if __name__ == "__main__":
        main()

**Come funziona?**

#. Quando il programma si avvia, il robot si alza lentamente per raggiungere una postura stabile.

   .. code-block:: python
   
      crawler.do_step('stand', 40)
      sleep(1.0)

   Dopo essersi alzato, il programma esegue in sequenza diversi movimenti predefiniti.

#. Movimento di nuoto

   Il robot esegue un movimento simile al nuoto regolando gradualmente le coordinate delle gambe.

   .. code-block:: python

      for i in range(loops):
          crawler.do_step([
              [100-i, i, 0],
              [100-i, i, 0],
              [0,120,-60+i/5],
              [0,100,-40-i/5]
          ], speed)

#. Movimento di flessioni

   Vengono definite due pose per simulare un movimento di flessioni.

   .. code-block:: python

      up = [[80,0,-100],[80,0,-100],[0,120,-60],[0,120,-60]]
      down = [[80,0,-30],[80,0,-30],[0,120,-60],[0,120,-60]]

      crawler.do_step(up, speed)
      crawler.do_step(down, speed)

#. Movimento di saluto con le zampe

   Il programma modifica le coordinate delle zampe anteriori usando ``mix_step()`` per creare un gesto di saluto.

   .. code-block:: python

      left_hand = crawler.mix_step(base,0,[0,50,80])
      right_hand = crawler.mix_step(base,1,[0,50,80])

#. Movimento di torsione

   Il robot ruota il corpo sollevando e abbassando le zampe diagonali.

   .. code-block:: python

      rise = [50,50,(-80+inc*0.5)]
      drop = [50,50,(-80-inc)]
      crawler.do_step(new_step, speed)

#. Se si preme **Ctrl+C**, il programma termina in modo sicuro e il robot torna alla posizione seduta.

   .. code-block:: python
   
      crawler.do_step('sit', 40)
    
 
