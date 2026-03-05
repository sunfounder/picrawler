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

    from time import sleep, strftime, localtime
    from vilib import Vilib
    import readchar
    from os import getlogin
    import os

    USERNAME = getlogin()
    VIDEO_PATH = f"/home/{USERNAME}/Videos/"

    MANUAL = '''
    Press keys on keyboard to control recording:
        Q: record/pause/continue
        E: stop
        Ctrl+C: Quit
    '''

    def print_overwrite(msg, end='', flush=True):
        """Overwrite the current terminal line."""
        print('\r\033[2K', end='', flush=True)
        print(msg, end=end, flush=True)

    def safe_stop_recording():
        """Stop recording safely (avoid exceptions during exit)."""
        try:
            Vilib.rec_video_stop()
        except Exception:
            pass

    def safe_close_camera():
        """Close camera safely (avoid exceptions during exit)."""
        try:
            Vilib.camera_close()
        except Exception:
            pass

    def main():
        rec_flag = 'stop'  # Possible states: start, pause, stop
        vname = None

        # Ensure the video directory exists
        os.makedirs(VIDEO_PATH, exist_ok=True)

        # Set save path for recorded videos
        Vilib.rec_video_set["path"] = VIDEO_PATH

        # Start camera and preview
        Vilib.camera_start(vflip=False, hflip=False)
        Vilib.display(local=False, web=True)
        sleep(0.8)  # Wait for camera startup

        print(MANUAL)

        try:
            while True:
                # Read keyboard input (no Enter needed)
                key = readchar.readkey().lower()

                # Q: start / pause / continue
                if key == 'q':
                    if rec_flag == 'stop':
                        rec_flag = 'start'

                        # Generate filename based on timestamp
                        vname = strftime("%Y-%m-%d-%H.%M.%S", localtime())
                        Vilib.rec_video_set["name"] = vname

                        # Start recording
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

                # E: stop recording
                elif key == 'e' and rec_flag != 'stop':
                    rec_flag = 'stop'
                    safe_stop_recording()
                    print_overwrite(
                        "The video saved as %s%s.avi" % (Vilib.rec_video_set["path"], vname),
                        end='\n'
                    )

                # Ctrl+C (readchar special key): quit
                elif key == readchar.key.CTRL_C:
                    print('\nquit')
                    break

                sleep(0.1)

        except KeyboardInterrupt:
            # Handle Ctrl+C from terminal as well
            print('\nquit')

        finally:
            # If recording is still active, stop it before closing camera
            if rec_flag != 'stop':
                safe_stop_recording()
            safe_close_camera()
            sleep(0.1)

    if __name__ == "__main__":
        main()

**仕組みは？**

#. このプログラムの概要

   このプログラムでは、キーボードを使用して動画録画を制御できます。

   • Q → 録画開始 / 一時停止 / 再開  
   • E → 録画停止  
   • Ctrl+C → プログラム終了  

   録画された動画は Videos フォルダに保存されます。

#. 動画フォルダの準備

   .. code-block:: python

      USERNAME = getlogin()
      VIDEO_PATH = f"/home/{USERNAME}/Videos/"
      os.makedirs(VIDEO_PATH, exist_ok=True)

   プログラムは現在のユーザー名を取得し、  
   Videos フォルダが存在しない場合は自動的に作成します。

   すべての録画動画はこのフォルダに保存されます。

#. カメラの起動

   .. code-block:: python

      Vilib.camera_start(vflip=False, hflip=False)
      Vilib.display(local=False, web=True)
      sleep(0.8)

   カメラを起動します。  
   Web プレビューが有効になり、ブラウザからライブ映像を確認できます。

   短い待機時間を入れることで、カメラが正しく起動するのを待ちます。

#. 録画状態の設定

   .. code-block:: python

      rec_flag = 'stop'
      vname = None

   プログラムでは ``rec_flag`` という変数を使用して、  
   現在の録画状態を管理します。

   • stop  → 録画していない状態  
   • start → 録画中  
   • pause → 一時停止中  

#. キーボード入力の待機

   .. code-block:: python

      key = readchar.readkey().lower()

   プログラムはキー入力を待機します。

#. Qキーで録画開始

   .. code-block:: python

      if rec_flag == 'stop':
          vname = strftime("%Y-%m-%d-%H.%M.%S", localtime())
          Vilib.rec_video_set["name"] = vname
          Vilib.rec_video_run()
          Vilib.rec_video_start()

   Q を最初に押すと：

   • 現在の日付と時刻を使ってファイル名が生成されます  
   • 録画がすぐに開始されます  

   例のファイル名：  
   2026-03-03-15.30.21.avi

#. もう一度Qキーで一時停止

   .. code-block:: python

      elif rec_flag == 'start':
          Vilib.rec_video_pause()

   すでに録画が開始されている場合、  
   Q を押すと録画が一時停止します。

#. さらにQキーで録画再開

   .. code-block:: python

      elif rec_flag == 'pause':
          Vilib.rec_video_start()

   録画が一時停止状態のときに、  
   再度 Q を押すと録画が再開されます。

#. Eキーで録画停止

   .. code-block:: python

      elif key == 'e' and rec_flag != 'stop':
          Vilib.rec_video_stop()

   E を押すと録画が完全に停止します。

   動画ファイルは次の場所に保存されます：  
   ``/home/your_username/Videos/``

#. プログラムの安全な終了

   .. code-block:: python

      finally:
          if rec_flag != 'stop':
              Vilib.rec_video_stop()
          Vilib.camera_close()

   プログラムが終了する際：

   • 録画が継続している場合は停止します  
   • カメラを安全に閉じます  

   これにより、動画ファイルの破損やカメラエラーを防ぎます。