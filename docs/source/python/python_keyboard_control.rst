.. note:: 

    こんにちは！SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32に関心のある仲間とともに、さらに深く学びましょう。

    **参加する理由**

    - **専門家のサポート**: 購入後の問題や技術的な課題を、コミュニティやチームのサポートで解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換して、スキルを向上させましょう。
    - **特別なプレビュー**: 新製品の発表や先行公開に早期アクセスできます。
    - **特別割引**: 新製品に対して限定割引を楽しめます。
    - **祝祭プロモーションとプレゼント**: プレゼントや祝祭プロモーションに参加できます。

    👉 私たちと一緒に探求し、創造する準備はできましたか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _py_keyboard:

キーボード操作
=======================

このプロジェクトでは、キーボードを使用してPiCrawlerをリモートで制御する方法を学びます。PiCrawlerを前進、後退、左旋回、右旋回させることができます。

**コードの実行**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 keyboard_control.py

プログラムが開始されると、PiCrawler が初期化され、ターミナルにキーボード操作インターフェースが表示されます。

キーボードのキーを押して PiCrawler を操作できます！

* ``w``：前進
* ``a``：左に旋回
* ``s``：後退
* ``d``：右に旋回
* ``Ctrl+C``：終了

現在の速度が表示され、以下のキーで調整できます：

- + / ]：速度を上げる
- - / [：速度を下げる

各動作の後には、安定性を保つために短い待機時間が入ります。

Ctrl+C を押すと終了します。  
終了前に、PiCrawler は安全に「座る」動作を行います。

**コード**

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

**仕組みは？**

#. ロボットオブジェクトの作成

   .. code-block:: python

      crawler = Picrawler()

   この行では ``Picrawler`` オブジェクトを作成します。  
   これにより、プログラムからロボットの動作を制御できるようになります。

#. 安全な速度範囲の定義

   .. code-block:: python

      SPEED_MIN = 20
      SPEED_MAX = 70
      speed = 60

   これらの変数は、許可される速度範囲を定義します。  
   ``speed`` には現在の移動速度が保存されます。  
   ロボットは最大値を超える速度では動作しません。

#. clamp() による速度制限

   .. code-block:: python

      def clamp(value, min_value, max_value):
          return max(min_value, min(max_value, value))

   この関数は、速度が安全な範囲内に収まるようにします。  
   極端な値による不安定な動作を防ぎます。

#. 動作の実行

   .. code-block:: python

      def do_move(action_name):
          crawler.do_action(action_name, STEP, speed)
          sleep(ACTION_GAP)

   この関数は、ロボットに動作コマンドを送ります。  
   ``ACTION_GAP`` は短い待機時間を追加し、動作の安定性を高めます。

#. キーボード入力の読み取り

   .. code-block:: python

      key = readchar.readkey()
      k = key.lower()

   プログラムはキー入力を待機します。  
   キーは統一性を保つため、小文字に変換されます。

#. 動作制御ロジック

   .. code-block:: python

      if k == "w":
          do_move("forward")
      elif k == "s":
          do_move("backward")

   キーが押されると、対応する動作がすぐに実行されます。  
   Enter キーを押す必要はありません。

#. 安全な終了

   .. code-block:: python

      finally:
          safe_sit()

   プログラム終了前に、ロボットは安全に「座る」動作を行います。  
   これにより、不安定な姿勢や突然のシャットダウンを防ぎます。