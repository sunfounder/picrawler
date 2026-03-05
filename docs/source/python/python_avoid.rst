.. note::

    こんにちは！SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者と一緒にさらに深く学んでいきましょう。

    **参加する理由**

    - **専門家のサポート**: 購入後の問題や技術的な課題を、コミュニティやチームのサポートを通じて解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換し、スキルを向上させましょう。
    - **特別なプレビュー**: 新製品の発表や先行公開に早期アクセスできます。
    - **特別割引**: 新しい製品に対して限定割引をお楽しみください。
    - **祝祭プロモーションとプレゼント**: プレゼントや祝祭プロモーションに参加できます。

    👉 私たちと一緒に探求し、創造する準備はできましたか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！


.. _py_avoid:

障害物回避
=====================

このプロジェクトでは、PiCrawlerが超音波モジュールを使用して前方の障害物を検出します。
PiCrawlerが障害物を検出すると、信号を送信し、別の方向に進むために方向転換を行います。

.. .. image:: img/avoid1.png

**コードを実行する**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 avoid.py

プログラムが開始されると、PiCrawler は立ち上がります。

超音波センサーを使用して距離を継続的に測定し、
その値をターミナルに表示します。

15 cm以内に障害物が検出された場合：
- 警告音が再生されます。
- ロボットは小さく左に旋回します。

進行方向に障害物がない場合：
- ロボットは前進します。

Ctrl+C を押すまで、ロボットは自動的に障害物回避を続けます。

終了する前に、安全に座る姿勢に戻ります。

**コード**

.. note::
    下記のコードは **修正/リセット/コピー/実行/停止** できます。ただし、まずはソースコードのパス（例えば ``picrawler\examples`` ）に移動してください。コードを修正した後、直接実行して効果を確認できます。

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

**どのように動作するのか？**

#. 初期化ブロック

   .. code-block:: python

      music = Music()
      crawler = Picrawler()
      sonar = Ultrasonic(Pin("D2"), Pin("D3"))

      music.music_set_volume(100)
      alert_distance = 15
      speed = 80

   このブロックでは、3つの主要モジュールを初期化します：
   - ``music``：音声の再生を制御します。
   - ``crawler``：PiCrawler の動作を制御します。
   - ``sonar``：超音波センサーを使用して距離を読み取ります。

   また、スピーカーの音量、障害物検出のしきい値（cm）、
   および移動速度を設定します。

#. タイムアウト設定ブロック（``sonar.read()`` が停止するのを防ぐ）

   .. code-block:: python

      class Timeout(Exception):
          pass

      def _alarm_handler(signum, frame):
          raise Timeout()

      signal.signal(signal.SIGALRM, _alarm_handler)

   超音波センサーのドライバは、エコー信号を待つ間に
   処理がブロックされる可能性があります。  
   このブロックではシグナルハンドラを設定し、停止した
   ``sonar.read()`` の呼び出しをプログラム側で中断できるようにします。

#. 関数：safe_read_once()

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

   この関数は、タイムアウト保護付きで超音波センサーを1回読み取ります。  
   - 読み取りが成功した場合は、距離の値を返します。  
   - タイムアウトまたはエラーが発生した場合は、処理が停止する代わりに ``None`` を返します。

#. 関数：read_distance_filtered()

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

   この関数は、複数回のサンプルを取得することで信頼性を向上させます：
   - 無効な値（``None`` または ``<= 0``）は無視されます。
   - 残った値をソートします。
   - ノイズの影響を減らすために中央値を返します。

#. 関数：main()（主要な判断と動作）

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

   これはメインの制御ロジックです：

   - フィルタ処理された距離値を読み取ります。
   - 読み取りに失敗した場合、このサイクルはスキップされます。
   - 障害物が ``alert_distance`` より近い場合、警告音を再生し、左に旋回します。
   - それ以外の場合は前進します。

#. プログラムエントリーブロック（連続ループ + 安全終了）

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

   このブロックは、プログラム全体の動作フローを制御します：
   - 開始前に PiCrawler を立ち上がらせます。
   - プログラムは無限ループで ``main()`` を繰り返し実行します。
   - Ctrl+C を押すとループが停止します。
   - プログラム終了前に、PiCrawler は座る姿勢に戻ります。