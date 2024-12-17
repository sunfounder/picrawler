.. note:: 

    こんにちは！SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32に関心のある仲間と一緒にさらに深く学びましょう。

    **参加する理由**

    - **専門家のサポート**: 購入後の問題や技術的な課題を、コミュニティやチームのサポートで解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換して、スキルを向上させましょう。
    - **特別なプレビュー**: 新製品の発表や先行公開に早期アクセスできます。
    - **特別割引**: 新製品に対して限定割引を楽しめます。
    - **祝祭プロモーションとプレゼント**: プレゼントや祝祭プロモーションに参加できます。

    👉 私たちと一緒に探求し、創造する準備はできましたか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _py_pose:

ポーズ
=============

PiCrawlerは座標の配列を記述することで特定のポーズを取ることができます。ここでは、右後足を上げたポーズを取らせています。

.. image:: img/4cood.A.png

**コードの実行**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 do_step.py


**コード**

.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep

    crawler = Picrawler() 

    ## [右前足], [左前足], [左後足], [右後足]
    new_step=[[45, 45, -75], [45, 0, -75], [45, 0, -30], [45, 45, -75]]
    stand_step = crawler.move_list['stand'][0]

    def main():  
        while True:
            speed = 80

            print(f"stand step: {stand_step}")
            crawler.do_step(stand_step, speed)
            sleep(3)
            print(f"new step: {new_step}")
            crawler.do_step(new_step,speed)
            sleep(3)

    
    if __name__ == "__main__":
        main()

**仕組みは？**

このコードで注目すべき部分は ``crawler.do_step()`` です。

``do_action()`` と似ていますが、 ``do_step()`` もPiCrawlerの動作を制御できます。
違いは、前者が「前進」のような連続的な動作を行うのに対し、後者は「立つ」や「座る」などの個別の動作を実行するために使われます。


このメソッドには2つの使い方があります。

1つ目: 文字列を記述し、 ``picrawler`` ライブラリ内の ``step_list`` 辞書を直接利用できます。

.. code-block:: python

    crawler.do_step('stand',speed) 
    # "speed"はステップの速度を示し、範囲は0～100です。

2つ目: 4つの座標値を含む配列を記述できます。

.. code-block:: python

    new_step=[[45, 45, -75], [45, 0, -75], [45, 0, -30], [45, 45, -75]]
    # これらの4つの座標は、右前足、左前足、左後足、右後足をそれぞれ制御するために使用します。

各足には独立した座標系があります。以下の図のように表示されます。

.. image:: img/4cood.png

各つま先の座標を個別に測定する必要があります。以下の図のように表示されます。

.. image:: img/1cood.png


ちなみに、最初の方法で呼び出す ``step_list`` も4つの座標値を含む配列で構成されています。

.. code-block:: python

    step_list = {

        "stand":[
            [45, 45, -50], 
            [45, 45, -50], 
            [45, 45, -50], 
            [45, 45, -50]
        ],
        "sit":[
            [45, 45, -30], 
            [45, 45, -30], 
            [45, 45, -30], 
            [45, 45, -30]
        ],
              
    }





