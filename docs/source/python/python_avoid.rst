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

.. image:: img/avoid1.png

**コードを実行する**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 avoid.py

コードを実行すると、PiCrawlerは前進を開始します。もし障害物までの距離が10cm未満であると検出した場合、警告音を鳴らして停止し、左に回転して停止します。左に回転後、障害物がなければまたは障害物までの距離が10cm以上であれば、前進を続けます。

**コード**

.. note::
    下記のコードは **修正/リセット/コピー/実行/停止** できます。ただし、まずはソースコードのパス（例えば ``picrawler\examples`` ）に移動してください。コードを修正した後、直接実行して効果を確認できます。

.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from robot_hat import TTS, Music
    from robot_hat import Ultrasonic
    from robot_hat import Pin
    import time

    tts = TTS()
    music = Music()

    crawler = Picrawler() 
    sonar = Ultrasonic(Pin("D2") ,Pin("D3"))
    music.music_set_volume(100)

    alert_distance = 15
    speed = 80

    def main():
        distance = sonar.read()
        print(distance)
        if distance < 0:
            pass
        elif distance <= alert_distance:
            try:
                music.sound_play_threading('./sounds/sign.wav', volume=100)
            except Exception as e:
                print(e)
            crawler.do_action('turn left angle',3,speed)
            time.sleep(0.2)
        else :
            crawler.do_action('forward', 1,speed)
            time.sleep(0.2)

    if __name__ == "__main__":
        while True:
            main()

**動作の仕組み**

``Ultrasonic`` クラスをインポートすることで、距離を取得できます。

.. code-block:: python

    from robot_hat import Ultrasonic

次に、超音波のピンを初期化します。

.. code-block:: python

    sonar = Ultrasonic(Pin("D2") ,Pin("D3"))

こちらがメインのプログラムです。

* 超音波モジュールで検出した ``distance``を読み取り、0未満の値を除外します（超音波モジュールが障害物から遠すぎるか、データが正しく読み取れない場合に ``distance<0`` が表示されます）。
* ``distance`` が ``alert_distance`` （事前に設定した閾値、ここでは10）以下の場合、 ``sign.wav`` の効果音を再生し、PiCrawlerは ``turn left angle`` の動作を行います。
* ``distance`` が ``alert_distance`` より大きければ、PiCrawlerは ``forward`` の動作を続けます。

.. code-block:: python

    distance = sonar.read()
    print(distance)
    if distance < 0:
        pass
    elif distance <= alert_distance:
        try:
            music.sound_play_threading('./sounds/sign.wav', volume=100)
        except Exception as e:
            print(e)
        crawler.do_action('turn left angle',3,speed)
        time.sleep(0.2)
    else :
        crawler.do_action('forward', 1,speed)
        time.sleep(0.2)

.. note::

    ``musics`` や ``sounds`` フォルダにさまざまな効果音や音楽を追加することができます。詳細は:ref:`filezilla` をご参照ください。
