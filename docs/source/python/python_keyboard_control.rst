.. note::

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein und verbinden Sie sich mit anderen Technikbegeisterten.

    **Warum mitmachen?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitig Zugriff auf neue Produktankündigungen und Einblicke.
    - **Exklusive Rabatte**: Genießen Sie besondere Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und saisonalen Aktionen teil.

    👉 Bereit für spannende Projekte? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _py_keyboard:

Tastatursteuerung
====================

In diesem Projekt lernen wir, wie man den PiCrawler mit der Tastatur fernsteuert. Sie können den PiCrawler vorwärts, rückwärts, nach links und nach rechts bewegen.

**Code ausführen**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 keyboard_control.py

Wenn das Programm startet, wird der PiCrawler initialisiert und eine Tastatur-Steueroberfläche im Terminal angezeigt.

Drücken Sie Tasten auf der Tastatur, um den PiCrawler zu steuern!

* ``w``: Vorwärts
* ``a``: Nach links drehen
* ``s``: Rückwärts
* ``d``: Nach rechts drehen
* ``Ctrl+C``: Beenden

Die aktuelle Geschwindigkeit wird angezeigt und kann angepasst werden mit:

- + / ] zum Erhöhen der Geschwindigkeit
- - / [ zum Verringern der Geschwindigkeit

Nach jeder Aktion wird eine kurze Verzögerung eingefügt, um die Stabilität zu verbessern.

Drücken Sie Ctrl+C zum Beenden.
Vor dem Herunterfahren führt der Crawler eine sichere „Sitzen“-Aktion aus.

**Code**

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

**Wie funktioniert das?**

#. Erstellen des Roboter-Objekts

   .. code-block:: python

      crawler = Picrawler()

   Diese Zeile erstellt ein ``Picrawler``-Objekt.  
   Dadurch kann das Programm die Bewegungen des Roboters steuern.

#. Definieren eines sicheren Geschwindigkeitsbereichs

   .. code-block:: python

      SPEED_MIN = 20
      SPEED_MAX = 70
      speed = 60

   Diese Variablen definieren den erlaubten Geschwindigkeitsbereich.  
   ``speed`` speichert die aktuelle Bewegungsgeschwindigkeit.  
   Der Roboter bewegt sich nicht schneller als der maximale Wert.

#. Begrenzen der Geschwindigkeit mit clamp()

   .. code-block:: python

      def clamp(value, min_value, max_value):
          return max(min_value, min(max_value, value))

   Diese Funktion stellt sicher, dass die Geschwindigkeit im sicheren Bereich bleibt.  
   Dadurch werden instabile Bewegungen durch extreme Werte verhindert.

#. Ausführen einer Bewegung

   .. code-block:: python

      def do_move(action_name):
          crawler.do_action(action_name, STEP, speed)
          sleep(ACTION_GAP)

   Diese Funktion sendet einen Bewegungsbefehl an den Roboter.  
   ``ACTION_GAP`` fügt eine kurze Verzögerung hinzu, um die Stabilität zu verbessern.

#. Tastatureingaben lesen

   .. code-block:: python

      key = readchar.readkey()
      k = key.lower()

   Das Programm wartet auf eine Tasteneingabe.  
   Die Taste wird zur Einheitlichkeit in Kleinbuchstaben umgewandelt.

#. Bewegungssteuerungslogik

   .. code-block:: python

      if k == "w":
          do_move("forward")
      elif k == "s":
          do_move("backward")

   Wenn eine Taste gedrückt wird, wird die entsprechende Bewegung sofort ausgeführt.  
   Das Drücken der Enter-Taste ist nicht erforderlich.

#. Sicheres Beenden

   .. code-block:: python

      finally:
          safe_sit()

   Bevor das Programm beendet wird, führt der Roboter eine sichere „Sitzen“-Aktion aus.  
   Dadurch werden eine instabile Haltung oder ein abruptes Herunterfahren verhindert. 
