.. note:: 

    こんにちは！SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32に関心のある仲間とともに、さらに深く学びましょう。

    **参加する理由**

    - **専門家のサポート**: 購入後の問題や技術的な課題を、コミュニティやチームのサポートで解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換して、スキルを向上させましょう。
    - **特別なプレビュー**: 新製品の発表や先行公開に早期アクセスできます。
    - **特別割引**: 新製品に対して限定割引を楽しめます。
    - **祝祭プロモーションとプレゼント**: プレゼントや祝祭プロモーションに参加できます。

    👉 私たちと一緒に探求し、創造する準備はできましたか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _py_emotional:

感情的なロボット
====================

この例では、PiCrawlerのいくつかの興味深いカスタムアクションを紹介します。

**コードの実行**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 emotional_robot.py

プログラムを実行すると、ロボットはまずゆっくりと立ち上がり、安定した姿勢になります。

その後、泳ぐような動き、腕立て伏せ、前脚を使った手振り動作、そしてツイストダンスなど、複数の動作を順番に実行します。これらの動作が連続して行われることで、ダイナミックで表現力のある動きを演出します。

**Ctrl+C** を押すと、プログラムは安全に終了し、ロボットは座る姿勢に戻ります。

**コード**

.. note:: 
    以下のコードは **変更/リセット/コピー/実行/停止** が可能です。ただし、最初にソースコードのパス（例: ``picrawler\examples`` ）に移動する必要があります。コードを変更した後は、直接実行してその効果を確認できます。

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
    
**どのように動作するのか？**

#. プログラムが開始されると、ロボットはまずゆっくりと立ち上がり、安定した姿勢になります。

   .. code-block:: python
   
      crawler.do_step('stand', 40)
      sleep(1.0)

   立ち上がった後、プログラムは複数の事前定義された動作を順番に実行します。

#. スイミング動作

   脚の座標を徐々に調整することで、ロボットは泳ぐような動きを行います。

   .. code-block:: python

      for i in range(loops):
          crawler.do_step([
              [100-i, i, 0],
              [100-i, i, 0],
              [0,120,-60+i/5],
              [0,100,-40-i/5]
          ], speed)

#. 腕立て伏せ動作

   腕立て伏せの動きを表現するために、2つの姿勢が定義されています。

   .. code-block:: python

      up = [[80,0,-100],[80,0,-100],[0,120,-60],[0,120,-60]]
      down = [[80,0,-30],[80,0,-30],[0,120,-60],[0,120,-60]]

      crawler.do_step(up, speed)
      crawler.do_step(down, speed)

#. ハンドワーク動作

   ``mix_step()`` を使用して前脚の座標を変更し、手を振るようなジェスチャーを作ります。

   .. code-block:: python

      left_hand = crawler.mix_step(base,0,[0,50,80])
      right_hand = crawler.mix_step(base,1,[0,50,80])

#. ツイスト動作

   対角線上の脚を上げ下げすることで、ロボットが体をひねる動きを行います。

   .. code-block:: python

      rise = [50,50,(-80+inc*0.5)]
      drop = [50,50,(-80-inc)]
      crawler.do_step(new_step, speed)

#. **Ctrl+C** が押されると、プログラムは安全に終了し、ロボットは座る姿勢に戻ります。

   .. code-block:: python
   
      crawler.do_step('sit', 40)
