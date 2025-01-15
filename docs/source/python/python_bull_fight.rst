.. note::

    こんにちは！SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者と一緒にさらに深く学びましょう。

    **参加する理由**

    - **専門家のサポート**: 購入後の問題や技術的な課題を、コミュニティやチームのサポートで解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換して、スキルを向上させましょう。
    - **特別なプレビュー**: 新製品の発表や先行公開に早期アクセスできます。
    - **特別割引**: 新製品に対して限定割引を楽しめます。
    - **祝祭プロモーションとプレゼント**: プレゼントや祝祭プロモーションに参加できます。

    👉 私たちと一緒に探求し、創造する準備はできましたか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！


.. _py_bull:

ブルファイト
==============

PiCrawlerを怒った雄牛に変身させましょう！そのカメラを使って赤い布を追跡し、突進させます！

.. image:: img/bullfight.png

**コードを実行する**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 bull_fight.py


**画像の表示**

コードが実行されると、ターミナルには以下のようなプロンプトが表示されます：

.. code-block::

    No desktop !
    * Serving Flask app "vilib.vilib" (lazy loading)
    * Environment: production
    WARNING: Do not use the development server in a production environment.
    Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)

その後、ブラウザで ``http://<your IP>:9000/mjpg`` を入力して、ビデオ画面を表示できます。例: ``https://192.168.18.113:9000/mjpg``

.. image:: img/display.png

**コード**

.. note::
    以下のコードは **修正/リセット/コピー/実行/停止** できます。ただし、まずソースコードのパス（例: ``picrawler/examples`` ）に移動する必要があります。コードを修正した後、直接実行して効果を確認できます。

.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep
    from robot_hat import Music
    from vilib import Vilib
    
    
    crawler = Picrawler() 
    
    music = Music()
    
    def main():
        Vilib.camera_start()
        Vilib.display()
        Vilib.color_detect("red") 
        speed = 80
    
        while True:
            if Vilib.detect_obj_parameter['color_n']!=0:
                coordinate_x = Vilib.detect_obj_parameter['color_x']
                music.sound_play_threading('./sounds/talk1.wav')
    
                if coordinate_x < 100:
                    crawler.do_action('turn left',1,speed)
                    sleep(0.05) 
                elif coordinate_x > 220:
                    crawler.do_action('turn right',1,speed)
                    sleep(0.05) 
                else :
                    crawler.do_action('forward',2,speed)
                    sleep(0.05)    
            else :
                crawler.do_step('stand',speed)
                sleep(0.05)
    
    
    if __name__ == "__main__":
        main()


**仕組み**

このプロジェクトは、:ref:`py_move` 、:ref:`py_vision` 、および:ref:`py_sound` の知識ポイントを組み合わせています。

その流れは以下の図に示されています：

.. image:: img/bull_fight-f.png
