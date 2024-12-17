.. note:: 

    こんにちは！SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32に関心のある仲間と一緒にさらに深く学びましょう。

    **参加する理由**

    - **専門家のサポート**: 購入後の問題や技術的な課題を、コミュニティやチームのサポートで解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換して、スキルを向上させましょう。
    - **特別なプレビュー**: 新製品の発表や先行公開に早期アクセスできます。
    - **特別割引**: 新製品に対して限定割引を楽しめます。
    - **祝祭プロモーションとプレゼント**: プレゼントや祝祭プロモーションに参加できます。

    👉 私たちと一緒に探求し、創造する準備はできましたか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _py_posture:

姿勢調整
=====================

この例では、キーボードを使ってPiCrawlerの各足を個別に操作し、希望する姿勢を取らせます。

スペースバーを押すと、現在の座標値が表示されます。この座標値は、PiCrawlerの独自のアクションを作成する際に役立ちます。

.. image:: img/1cood.A.png

**コードの実行**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 do_single_leg.py

コードが実行された後、ターミナルに表示されるプロンプトに従って操作を行ってください。

* ``1234``キーで足を個別に選択します。 ``1`` : 右前足、 ``2`` : 左前足、 ``3`` : 左後足、 ``4`` : 右後足
* ``w`` , ``a`` , ``s`` , ``d`` , ``r`` , ``f`` キーでPiCrawlerの座標値をゆっくりと制御できます。
* ``Ctrl+C`` で終了します。

**コード**

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep
    import readchar

    crawler = Picrawler()
    speed = 80


    manual = '''
    -------- PiCrawler Controller --------- 
           .......          .......
        <=|   2   |┌-┌┐┌┐-┐|   1   |=>
           ``````` ├      ┤ ```````
           ....... ├      ┤ .......
        <=|   3   |└------┘|   4   |=>
           ```````          ```````
        1: Select right front leg
        2: Select left front leg
        3: Select left rear leg
        4: Select right rear leg

        W: Y++          R: Z++             
        A: X--          F: Z-- 
        S: Y-- 
        D: X++          Ctrl+C: Quit
    '''
    legs_list = ['right front', 'left front', 'left rear', 'right rear']

    def main():  
        leg = 0
        speed = 80
        step = 2
        print(manual)
        crawler.do_step('stand', speed)
        sleep(0.2)
        coordinate=crawler.current_step_all_leg_value()  

        def show_info():
            print("\033[H\033[J", end='')  # ターミナルの画面をクリア
            print(manual)   
            print('%s : %s'%(leg+1, legs_list[leg])) 
            print('coordinate: %s'%(coordinate))  

        show_info()

        while True:
            # キー入力を読み取る
            key = readchar.readkey()
            key = key.lower()
            # 足を選択
            if key in ('1234'):
                leg = int(key) - 1
                show_info()
            # 移動
            elif key in ('wsadrf'):         
                if 'w' == key:
                    coordinate[leg][1]=coordinate[leg][1] + step    
                elif 's' == key:
                    coordinate[leg][1]=coordinate[leg][1] - step           
                elif 'a' == key:
                    coordinate[leg][0]=coordinate[leg][0] - step         
                elif 'd' == key:
                    coordinate[leg][0]=coordinate[leg][0] + step   
                elif 'r' == key:
                    coordinate[leg][2]=coordinate[leg][2] + step         
                elif 'f' == key:
                    coordinate[leg][2]=coordinate[leg][2] - step 

                crawler.do_single_leg(leg,coordinate[leg],speed) 
                sleep(0.1)  
                # coordinate=crawler.current_step_all_leg_value()
                show_info()

            sleep(0.05)

    
    if __name__ == "__main__":
        main()

* ``current_step_all_leg_value()``: すべての足の座標値を返します。
* ``do_single_leg(leg,coordinate[leg],speed)``: 特定の足の座標値を個別に変更します。
