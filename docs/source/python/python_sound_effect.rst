.. note:: 

    こんにちは！SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32に関心のある仲間たちと一緒に、さらに深く学んでいきましょう。

    **なぜ参加するのか？**

    - **専門家のサポート**: 購入後の問題や技術的な課題を、コミュニティやチームのサポートを通じて解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換して、スキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表に早期アクセスし、先行して情報を得られます。
    - **特別割引**: 最新の製品に対して、限定の割引を楽しむことができます。
    - **祝祭プロモーションとプレゼント**: プレゼント企画や祝祭プロモーションに参加できます。

    👉 私たちと一緒に探求し、創造する準備はできましたか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _py_sound:

音声効果
=====================

この例では、PiCrawler（正確にはRobot HAT）の音声効果を使用します。音声効果は、 **音楽** 、 **サウンド** 、 **テキスト読み上げ** の3つの部分で構成されています。

.. .. image:: img/tts.png

**i2sampのインストール**

これらの機能を使用する前に、まずスピーカーを有効にして、音を出せるようにする必要があります。

``i2samp.sh`` を実行して、このスクリプトを使ってi2sアンプを使用するために必要なすべての設定を行います。

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/
    sudo bash i2samp.sh 

いくつかの確認メッセージが表示されるので、すべてのプロンプトに **Y** で答えてください。Raspberry Piの設定が変更された後、これらの変更が有効になるためには、コンピュータを再起動する必要があります。

再起動後、再度 ``i2samp.sh`` スクリプトを実行して、アンプをテストします。スピーカーから音が正常に再生されれば、設定は完了です。

**コードの実行**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 sound_effect.py

プログラムが開始されると、ターミナルに操作メニューが表示されます。

キーを押すと、対応する機能がすぐに実行されます。

* ``q``：バックグラウンド音楽の再生 / 停止を切り替えます。
* ``1``：複数の効果音を順番に再生します（ブロッキングモード）。
* ``2``：同じ効果音をスレッドを使用して再生します（ノンブロッキング）。
* ``t``：テキスト読み上げ（TTS）機能を使って「Hello」と発話します。

プログラムは継続して実行され、キー入力を待機します。

Ctrl+C を押すとプログラムが停止します。  
終了前に、再生中のバックグラウンド音楽は自動的に停止します。


**コード**

.. code-block:: python

    from time import sleep
    import readchar
    from robot_hat import Music, TTS

    music = Music()
    tts = TTS()

    manual = '''
    Press a key to trigger actions (no Enter needed):
        q: Play/Stop background music
        1: Play sound effect (blocking)
        2: Play sound effect (threading)
        t: Text to speak

        Ctrl^C: quit
    '''

    def main():
        print(manual)

        flag_bgm = False
        music.music_set_volume(20)
        tts.lang("en-US")

        try:
            while True:
                # Real-time key input (no Enter required)
                key = readchar.readkey().lower()

                if key == "q":
                    flag_bgm = not flag_bgm
                    if flag_bgm:
                        music.music_play('./musics/sports-Ahjay_Stelino.mp3')
                    else:
                        music.music_stop()

                elif key == "1":
                    music.sound_play('./sounds/talk1.wav')
                    sleep(0.05)
                    music.sound_play('./sounds/talk3.wav')
                    sleep(0.05)
                    music.sound_play('./sounds/sign.wav')
                    sleep(0.5)

                elif key == "2":
                    music.sound_play_threading('./sounds/talk1.wav')
                    sleep(0.05)
                    music.sound_play_threading('./sounds/talk3.wav')
                    sleep(0.05)
                    music.sound_play_threading('./sounds/sign.wav')
                    sleep(0.5)

                elif key == "t":
                    tts.say("Hello")

        except KeyboardInterrupt:
            print("\nquit")

        finally:
            # Stop music before exit to reduce error messages
            try:
                music.music_stop()
            except Exception:
                pass

    if __name__ == "__main__":
        main()


**仕組みは？**

背景音楽に関連する機能は以下の通りです：

* ``music = Music()`` : オブジェクトを宣言します。
* ``music.music_set_volume(20)`` : 音量を設定します。範囲は0~100です。
* ``music.music_play(./musics/sports-Ahjay_Stelino.mp3)`` : 音楽ファイルを再生します。ここでは、 ``./musics`` パスにある **sports-Ahjay_Stelino.mp3** ファイルを再生します。
* ``music.music_stop()`` : 背景音楽の再生を停止します。

.. note::

    異なる音楽や効果音を ``musics`` または ``sounds`` フォルダに追加できます。追加方法は:ref:`filezilla` を参照してください。

サウンドエフェクトに関連する機能は以下の通りです：

* ``music = Music()``
* ``music.sound_play('./sounds/talk1.wav')`` : サウンドエフェクトファイルを再生します。ここでは、 ``./musics`` パスにある **talk1.wav** ファイルを再生します。
* ``music.sound_play_threading('./sounds/talk1.wav')`` : サウンドエフェクトファイルを新しいスレッドで再生し、メインスレッドを停止しません。

テキスト読み上げに関連する機能は以下の通りです：

* ``tts = TTS()``
* ``tts.say(words)`` : テキストを音声に変換して読み上げます。
* ``tts.lang("en-US")`` : 言語を設定します。

.. note:: 

    言語は、 ``lang("")`` パラメータで次のような文字列を設定することで指定できます。

.. list-table:: Language
    :widths: 15 50

    *   - zh-CN 
        - 中国語（普通話）
    *   - en-US 
        - 英語（アメリカ）
    *   - en-GB     
        - 英語（イギリス）
    *   - de-DE     
        - ドイツ語（Deutsch）
    *   - es-ES     
        - スペイン語（España）
    *   - fr-FR  
        - フランス語（フランス）
    *   - it-IT  
        - イタリア語（Italia）
