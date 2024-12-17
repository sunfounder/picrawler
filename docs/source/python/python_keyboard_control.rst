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

キーボードのキーを押してPiCrawlerを操作してください！

* ``w``: 前進
* ``a``: 左旋回
* ``s``: 後退
* ``d``: 右旋回
* ``Ctrl+C``: 終了

**コード**

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep
    import readchar

    crawler = Picrawler() 
    speed = 90

    manual = '''
    Press keys on keyboard to control PiCrawler!
        W: Forward
        A: Turn left
        S: Backward
        D: Turn right

        Ctrl^C: Quit
    '''

    def show_info():
        print("\033[H\033[J", end='')  # ターミナルウィンドウをクリア 
        print(manual)


    def main(): 
        show_info()   
        while True:
            key = readchar.readkey()
            key = key.lower()
            if key in('wsad'):
                if 'w' == key:
                    crawler.do_action('forward',1,speed)     
                elif 's' == key:
                    crawler.do_action('backward',1,speed)          
                elif 'a' == key:
                    crawler.do_action('turn left',1,speed)           
                elif 'd' == key:
                    crawler.do_action('turn right',1,speed)
                sleep(0.05)
                show_info()  
            elif key == readchar.key.CTRL_C:
                print("\n Quit") 
                break    

            sleep(0.02)          

    
    if __name__ == "__main__":
        main()

**仕組みは？**

PiCrawlerは、読み取ったキーボードの文字に基づいて適切な動作を実行します。 ``lower()`` 関数は、大文字を小文字に変換するため、大文字・小文字に関係なく文字が有効になります。

.. code-block:: python

    def main(): 
        show_info()   
        while True:
            key = readchar.readkey()
            key = key.lower()
            if key in('wsad'):
                if 'w' == key:
                    crawler.do_action('forward',1,speed)     
                elif 's' == key:
                    crawler.do_action('backward',1,speed)          
                elif 'a' == key:
                    crawler.do_action('turn left',1,speed)           
                elif 'd' == key:
                    crawler.do_action('turn right',1,speed)
                sleep(0.05)
                show_info()  
            elif key == readchar.key.CTRL_C:
                print("\n Quit") 
                break    
            
            sleep(0.02)  
