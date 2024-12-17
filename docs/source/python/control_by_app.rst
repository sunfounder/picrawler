.. note::

    こんにちは！SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者と共にさらに深く学びましょう。

    **参加する理由**

    - **専門家のサポート**: 購入後の問題や技術的な課題を、コミュニティやチームのサポートで解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換して、スキルを向上させましょう。
    - **特別なプレビュー**: 新製品の発表や先行公開に早期アクセスできます。
    - **特別割引**: 新しい製品に対する限定割引をお楽しみください。
    - **祝祭プロモーションとプレゼント**: プレゼントや祝祭プロモーションに参加できます。

    👉 私たちと一緒に探求し、創造する準備はできましたか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！


.. _control_by_app:

アプリによる制御
=======================

SunFounderコントローラーは、Raspberry Pi/Picoベースのロボットを制御するために使用されます。

このアプリには、ボタン、スイッチ、ジョイスティック、D-pad、スライダー、スロットルスライダーなどのウィジェットが統合されています。また、デジタルディスプレイ、超音波レーダー、グレースケール検出、スピードメーター入力ウィジェットも含まれています。

17のエリアA〜Qがあり、ここに異なるウィジェットを配置して、独自のコントローラーをカスタマイズできます。

さらに、このアプリはライブビデオストリーミング機能も提供しています。

このアプリを使ってPiCrawlerコントローラーをカスタマイズしてみましょう。

**手順**

#. ``sunfounder-controller`` モジュールをインストールします。

    最初に ``robot-hat`` 、 ``vilib`` 、 ``picrawler`` モジュールをインストールする必要があります。詳細については、:ref:`install_all_modules` をご覧ください。

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~
        git clone https://github.com/sunfounder/sunfounder-controller.git
        cd ~/sunfounder-controller
        sudo python3 setup.py install

#. コードを実行します。

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/sunfounder-controller/examples
        sudo python3 picrawler_control.py

#. `SunFounder Controller <https://docs.sunfounder.com/projects/sf-controller/en/latest/>`_  を **APP Store（iOS）** または **Google Play（Android）** からインストールします。


#. 新しいコントローラーを作成します。

    SunFounder Controllerアプリで、+アイコンをクリックして新しいコントローラーを作成します。

    .. image:: img/app1.PNG

    プリセットセクションには、いくつかの製品用のプリセットコントローラーがあります。ここではPiCrawlerを選択します。

    .. image:: img/app_control1.jpg

    コントローラーに名前を付け、コントローラーの種類を選択します。

    .. image:: img/app_control2.jpg

    このプリセットコントローラーに入ると、すでにいくつかのウィジェットが配置されているのがわかります。変更する項目がなければ、|app_save| ボタンをクリックします。

    .. image:: img/app_control3.jpg

#. PiCrawlerに接続します。

    **接続** ボタンをクリックすると、自動的に近くのロボットが検索されます。その名前は ``picrawler_control.py`` で定義されており、常に実行している必要があります。

    .. image:: img/app_control6.jpg

    製品名をクリックすると、「接続成功」のメッセージが表示され、製品名が右上に表示されます。

    .. image:: img/app_control7.jpg

    .. note::

        * モバイルデバイスがPiCrawlerと同じLANに接続されていることを確認する必要があります。
        * 自動で検索されない場合は、手動でIPを入力して接続することもできます。

        .. image:: img/app11.PNG

#. このコントローラーを実行します。

    **実行** ボタンをクリックすると、車の映像が表示され、これらのウィジェットを使ってPiCrawlerを制御できるようになります。

    .. image:: img/app_control8.jpg

    ここではウィジェットの機能を紹介します。

    * **A**: PiCrawlerの電源を設定します。
    * **B**: ロボットの移動速度を表示します。
    * **C**: Bウィジェットと同じ機能です。
    * **D**: 検出された障害物を赤い点で表示します。
    * **G**: 音声認識、ウィジェットを押し続けて話すと、話した内容が認識され、放すと認識された音声が表示されます。コード内で、車を制御するために ``forward`` 、 ``backward`` 、 ``left`` 、 ``right`` の4つのコマンドが設定されています。
    * **K**: 車の前進、後退、左折、右折を制御します。
    * **Q**: カメラ（頭部）の上下左右を制御します。
    * **N**: 色認識機能をオンにします。
    * **O**: 顔認識機能をオンにします。
    * **P**: 物体認識機能をオンにします。約90種類の物体を認識でき、モデルのリストについては以下のリンクを参照してください: https://github.com/sunfounder/vilib/blob/master/workspace/coco_labels.txt
