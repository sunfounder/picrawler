.. note:: 

    こんにちは！SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32に関心のある仲間とともに、さらに深く学びましょう。

    **参加する理由**

    - **専門家のサポート**: 購入後の問題や技術的な課題を、コミュニティやチームのサポートで解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換して、スキルを向上させましょう。
    - **特別なプレビュー**: 新製品の発表や先行公開に早期アクセスできます。
    - **特別割引**: 新製品に対して限定割引を楽しめます。
    - **祝祭プロモーションとプレゼント**: プレゼントや祝祭プロモーションに参加できます。

    👉 私たちと一緒に探求し、創造する準備はできましたか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _py_move:

移動
==============

これはPiCrawlerの最初のプロジェクトです。最も基本的な機能である「移動」を実行します。

.. .. image:: img/move.png

**コードを実行する**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 move.py

プログラムが開始されると、PiCrawler は立ち上がり、短時間待機します。

その後、以下の動作サイクルを継続的に実行します：
前進、後退、左旋回、右旋回、
小さな左旋回、小さな右旋回。

各動作の間には短い待機時間が設けられており、
より滑らかな動きになるようにしています。

Ctrl+C を押すとプログラムが停止します。
終了前に、PiCrawler は安全に座る姿勢に戻ります。

**コード**

.. note::
    以下のコードは **修正/リセット/コピー/実行/停止** できます。ですが、実行する前にソースコードパス（例： ``picrawler\examples`` ）に移動する必要があります。コードを修正した後は、そのまま実行して効果を確認できます。

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


**仕組みは？**

#. インポートと初期化

   .. code-block:: python

      from picrawler import Picrawler
      from time import sleep

      crawler = Picrawler()

   このスクリプトでは、必要なモジュールをインポートし、
   ``Picrawler`` オブジェクトを作成します。  
   このオブジェクトは、ロボットのすべての動作を制御するために使用されます。

#. メイン関数と初期設定

   .. code-block:: python

      def main():
          speed = 80
          crawler.do_step('stand', 40)
          sleep(1.0)

   ``main()`` 関数では移動速度を設定します。  
   ループを開始する前に、ロボットは立ち上がり、姿勢を安定させます。

#. 連続動作ループ

   .. code-block:: python

      while True:
          crawler.do_action('forward', 1, speed)
          crawler.do_action('backward', 1, speed)
          crawler.do_action('turn left', 1, speed)
          crawler.do_action('turn right', 1, speed)
          crawler.do_action('turn left angle', 1, speed)
          crawler.do_action('turn right angle', 1, speed)

   ロボットは無限ループの中で、事前に定義された一連の
   動作を繰り返し実行します。  
   各動作の間に短い待機時間を入れることで、動きがより滑らかになります。

#. 安全な終了処理

   .. code-block:: python

      except KeyboardInterrupt:
          print("\nCtrl+C pressed...")
      finally:
          crawler.do_step('sit', 40)

   ``try / except / finally`` 構造により、以下を保証します：
   - Ctrl+C によってループを安全に停止できます。
   - プログラム終了前にロボットが座る動作を行います。

#. プログラムエントリ

   .. code-block:: python

      if __name__ == "__main__":
          main()

   これにより、スクリプトが直接実行された場合のみ
   ``main()`` が実行されます。