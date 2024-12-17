.. note:: 

    こんにちは！SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32に関心のある仲間たちとともに、さらに深く学びましょう。

    **参加する理由**

    - **専門家のサポート**: 購入後の問題や技術的な課題を、コミュニティやチームのサポートで解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換して、スキルを向上させましょう。
    - **特別なプレビュー**: 新製品の発表や先行公開に早期アクセスできます。
    - **特別割引**: 新製品に対して限定割引を楽しめます。
    - **祝祭プロモーションとプレゼント**: プレゼントや祝祭プロモーションに参加できます。

    👉 私たちと一緒に探求し、創造する準備はできましたか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _py_video:

ビデオ録画
==================

この例では、録画機能の使い方を紹介します。

**コードの実行**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 record_video.py


コードが実行された後、ブラウザに ``http://<your IP>:9000/mjpg`` と入力すると、ビデオ画面が表示されます。例： ``http://192.168.18.113:9000/mjpg`` 

.. image:: img/display.png

録画は、キーボードのキーを押すことで開始、停止、再開できます。

* ``q`` を押して録画を開始、または一時停止/再開します。 ``e`` を押して録画を停止または保存します。
* プログラムを終了するには、 ``Ctrl+C`` を押してください。

**コード**

.. code-block:: python

    from time import sleep,strftime,localtime
    from vilib import Vilib
    import readchar 
    from os import getlogin
    
    USERNAME = getlogin()
    VIDEO_PATH = f"/home/{USERNAME}/Videos/"
    
    MANUAL = '''
    Press keys on keyboard to control recording:
        Q: record/pause/continue
        E: stop
        Ctrl^C: Quit
    '''
    
    def print_overwrite(msg,  end='', flush=True):
        print('\r\033[2K', end='',flush=True)
        print(msg, end=end, flush=True)
    
    def main():
        rec_flag = 'stop' # start, pause, stop
        vname = None
        Vilib.rec_video_set["path"] = VIDEO_PATH
    
        Vilib.camera_start(vflip=False,hflip=False) 
        Vilib.display(local=True,web=True)
        sleep(0.8)  # スタートアップを待機
    
        print(MANUAL)
        while True:
            # キーボード入力を読み取る
            key = readchar.readkey()
            key = key.lower()
            # 録画開始、一時停止
            if key == 'q':
                key = None
                if rec_flag == 'stop':            
                    rec_flag = 'start'
                    # 名前を設定
                    vname = strftime("%Y-%m-%d-%H.%M.%S", localtime())
                    Vilib.rec_video_set["name"] = vname
                    # 録画を開始
                    Vilib.rec_video_run()
                    Vilib.rec_video_start()
                    print_overwrite('rec start ...')
                elif rec_flag == 'start':
                    rec_flag = 'pause'
                    Vilib.rec_video_pause()
                    print_overwrite('pause')
                elif rec_flag == 'pause':
                    rec_flag = 'start'
                    Vilib.rec_video_start()
                    print_overwrite('continue')
            # 停止       
            elif key == 'e' and rec_flag != 'stop':
                key = None
                rec_flag = 'stop'
                Vilib.rec_video_stop()
                print_overwrite("ビデオは%s%s.aviとして保存されました"%(Vilib.rec_video_set["path"],vname),end='\n')  
            # 終了
            elif key == readchar.key.CTRL_C:
                Vilib.camera_close()
                print('\nquit')
                break 
    
            sleep(0.1)
    
    if __name__ == "__main__":
        main()

**仕組みは？**


録画に関連する機能は以下の通りです：


* ``Vilib.rec_video_run(video_name)`` : 録画スレッドを開始します。 ``video_name`` はビデオファイルの名前で、文字列で指定する必要があります。
* ``Vilib.rec_video_start()`` : 録画を開始または再開します。
* ``Vilib.rec_video_pause()`` : 録画を一時停止します。
* ``Vilib.rec_video_stop()`` : 録画を停止します。

``Vilib.rec_video_set["path"] = "~/video/test/"`` は、ビデオファイルの保存先を設定します。
