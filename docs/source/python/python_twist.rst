.. note:: 

    こんにちは！SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32に興味がある仲間たちと一緒に、さらに深く学びましょう。

    **なぜ参加するのか？**

    - **専門家のサポート**: 購入後の問題や技術的な課題を、コミュニティやチームのサポートを通じて解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換し、スキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表に早期アクセスし、先行して情報を得ることができます。
    - **特別割引**: 最新の製品に対して、限定の割引を享受できます。
    - **祝祭プロモーションとプレゼント**: プレゼント企画や祝祭プロモーションに参加できます。

    👉 私たちと一緒に探求し、創造する準備はできましたか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _py_twist:

Twist
==============

これまでに、PiCrawlerが特定のポーズをとる方法を学びました。次のステップは、それらのポーズを組み合わせて連続的な動作を作成することです。

ここでは、PiCrawlerの4つの足がペアで上下し、音楽に合わせてジャンプします。

**コードを実行する**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 twist.py

**コード**

.. note::
    下記のコードは **修正/リセット/コピー/実行/停止** できますが、その前に ``picrawler\examples`` のようなソースコードのパスに移動する必要があります。コードを修正した後は、直接実行して効果を確認できます。

.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from robot_hat import Music

    music = Music()
    crawler = Picrawler()


    def twist(speed):
        new_step=[[50, 50, -80], [50, 50, -80],[50, 50, -80], [50, 50, -80]]
        for i in range(4):
            for inc in range(30, 60, 5): 
                rise = [50,50,(-80+inc*0.5)]
                drop = [50,50,(-80-inc)]

                new_step[i]=rise
                new_step[(i+2)%4] = drop
                new_step[(i+1)%4] = rise
                new_step[(i-1)%4] = drop
                # print(new_step)
                crawler.do_step(new_step,speed)


    def main():  

        music.music_play('./musics/sports-Ahjay_Stelino.mp3')
        music.music_set_volume(20)

        while True:
            twist(speed=100) 

    
    if __name__ == "__main__":
        main()

**仕組みは？**

このコードで注目すべき部分は以下です：

.. code-block:: python

    def twist(speed):
        ## [右前],[左前],[左後],[右後]
        new_step=[[50, 50, -80], [50, 50, -80],[50, 50, -80], [50, 50, -80]]
        for i in range(4):
            for inc in range(30,60,5):  
                rise = [50,50,(-80+inc*0.5)]
                drop = [50,50,(-80-inc)]

                new_step[i]=rise
                new_step[(i+2)%4] = drop
                new_step[(i+1)%4] = rise
                new_step[(i-1)%4] = drop
                crawler.do_step(new_step,speed)

簡単に言うと、このコードは2重のforループを使って、 `new_step` 配列が連続的かつ規則的に変化するようにしており、その間に ``crawler.do_step()`` がポーズを実行し、連続的な動作を作り出します。

各ポーズに対応する座標値の配列は、:ref:`py_posture` から直感的に取得できます。


さらに、この例ではバックグラウンド音楽も再生されます。その実装方法は以下の通りです。

音楽を再生するために以下のライブラリをインポートします。

.. code-block:: python

    from robot_hat import Music

次に、Musicオブジェクトを宣言します。

.. code-block:: python

    music = Music()

次に、 ``picrawler/examples/musics`` ディレクトリ内の音楽を再生し、音量を20に設定します。また、音楽を ``musics`` フォルダに追加することもできます。フォルダには、:ref:`filezilla` を通じて音楽を追加できます。

.. code-block:: python

    music.music_play('./musics/sports-Ahjay_Stelino.mp3')
    music.music_set_volume(20)

.. note::

    異なる効果音や音楽を ``musics`` または ``sounds`` フォルダに追加することができます。これも:ref:`filezilla` を通じて行えます。
