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

コードが実行されると、PiCrawlerは以下の動作を順番に実行します：前進、後退、左旋回、右旋回、立つ。

**コード**

.. note::
    以下のコードは **修正/リセット/コピー/実行/停止** できます。ですが、実行する前にソースコードパス（例： ``pisloth\examples`` ）に移動する必要があります。コードを修正した後は、そのまま実行して効果を確認できます。

.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep
    
    crawler = Picrawler() 
    
    def main():  
        
        speed = 80
              
        while True:
           
            crawler.do_action('forward',2,speed)
            sleep(0.05)     
            crawler.do_action('backward',2,speed)
            sleep(0.05)          
            crawler.do_action('turn left',2,speed)
            sleep(0.05)           
            crawler.do_action('turn right',2,speed)
            sleep(0.05)  
            crawler.do_action('turn left angle',2,speed)
            sleep(0.05)  
            crawler.do_action('turn right angle',2,speed)
            sleep(0.05) 
            crawler.do_step('stand',speed)
            sleep(1)
    
    if __name__ == "__main__":
        main()


**仕組みは？**

まず、インストールした ``picrawler`` ライブラリから ``Picrawler`` クラスをインポートします。このクラスには、PiCrawlerのすべての動作と、それを実現する関数が含まれています。

.. code-block:: python

    from picrawler import Picrawler

次に、 ``crawler`` クラスをインスタンス化します。

.. code-block:: python

    crawler = Picrawler() 

最後に、 ``crawler.do_action()`` 関数を使用して、PiCrawlerを動かします。

.. code-block:: python
    
    crawler.do_action('forward',2,speed)    
    crawler.do_action('backward',2,speed)         
    crawler.do_action('turn left',2,speed)          
    crawler.do_action('turn right',2,speed) 
    crawler.do_action('turn left angle',2,speed) 
    crawler.do_action('turn right angle',2,speed)

一般的に、PiCrawlerのすべての移動は ``do_action()`` 関数で実行できます。この関数には3つのパラメータがあります：

* ``motion_name`` は特定の動作名で、以下のような動作を含みます： ``forward`` 、 ``turn right``、 ``turn left`` 、 ``backward`` 、 ``turn left angle`` 、 ``turn right angle`` 。
* ``step`` は各動作が実行される回数で、デフォルトは1です。
* ``speed`` は動作の速度を指定し、デフォルトは50で、範囲は0〜100です。

また、 ``crawler.do_step('stand',speed)`` もここで使用されており、PiCrawlerを立たせることができます。この関数の使い方については、次の例で説明します。
