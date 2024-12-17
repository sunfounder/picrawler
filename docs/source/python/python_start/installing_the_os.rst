.. note:: 

    こんにちは！SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者と一緒にさらに深く学んでいきましょう。

    **参加する理由は？**

    - **専門的なサポート**: コミュニティやチームのサポートを受けて、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換して、スキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表や先行情報にいち早くアクセスできます。
    - **特別割引**: 最新製品の特別割引をお楽しみいただけます。
    - **イベントやプレゼント**: プレゼント企画や祝祭プロモーションに参加できます。

    👉 探求と創造の準備はできましたか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _install_os_sd:

2. OSのインストール
============================================================


**必要なコンポーネント**

* パソコン
* マイクロSDカードとカードリーダー

1. Raspberry Pi Imagerのインストール
--------------------------------------

#. `Raspberry Pi Imager <https://www.raspberrypi.org/software/>`_ のソフトウェアダウンロードページにアクセスします。お使いのOSに適したImagerバージョンを選択し、ダウンロードしてファイルを開き、インストールを開始します。

    .. image:: img/os_install_imager.png
        :align: center

#. インストール中にセキュリティの警告が表示される場合があります。たとえば、Windowsでは警告メッセージが表示されることがあります。その場合は、 **詳細情報** を選択し、次に **実行** を選んでインストールを続行します。画面の指示に従って、Raspberry Pi Imagerのインストールを完了させます。

    .. image:: img/os_info.png
        :align: center

#. Raspberry Pi Imagerアプリケーションを起動します。アイコンをクリックするか、ターミナルで ``rpi-imager`` と入力します。

    .. image:: img/os_open_imager.png
        :align: center

2. OSをマイクロSDカードにインストール
-------------------------------------

#. SDカードリーダーを使用して、SDカードをコンピュータやラップトップに挿入します。

#. Imager内で、 **Raspberry Pi Device** をクリックし、ドロップダウンリストからRaspberry Piモデルを選択します。

    .. image:: img/os_choose_device.png
        :align: center

#. **Operating System** を選択し、推奨されるOSバージョンを選択します。

    .. image:: img/os_choose_os.png
        :align: center

#. **Choose Storage** をクリックし、インストールするストレージデバイスを選択します。

    .. note::

        正しいストレージデバイスを選択してください。複数のストレージデバイスが接続されている場合は、誤って選ばないように、他のデバイスを切り離しておくことをお勧めします。

    .. image:: img/os_choose_sd.png
        :align: center

#. **NEXT** をクリックし、次に **EDIT SETTINGS** をクリックして、OS設定をカスタマイズします。

    .. note::

        Raspberry Piにモニターが接続されている場合は、次の手順をスキップして、「はい」をクリックしてインストールを開始できます。モニター上で他の設定を後で調整できます。

    .. image:: img/os_enter_setting.png
        :align: center

#. Raspberry Piの **ホスト名** を定義します。

    .. note::

        ホスト名はRaspberry Piのネットワーク識別子です。 ``<hostname>.local`` または ``<hostname>.lan`` を使用して、Piにアクセスできます。

    .. image:: img/os_set_hostname.png
        :align: center

#. Raspberry Piの管理者アカウントの **ユーザー名** と **パスワード** を作成します。

    .. note::

        Raspberry Piにはデフォルトのパスワードがないため、セキュリティを確保するために固有のユーザー名とパスワードを設定することが重要です。

    .. image:: img/os_set_username.png
        :align: center

#. ワイヤレスLANを構成し、ネットワークの **SSID** と **パスワード** を入力します。

    .. note::

        **Wireless LAN country** を、あなたの地域に対応する2文字の `ISO/IEC alpha2コード <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ に設定してください。

    .. image:: img/os_set_wifi.png
        :align: center

#. Raspberry Piにリモートで接続するために、サービスタブでSSHを有効にします。

    * **パスワード認証**の場合、 **一般** タブからユーザー名とパスワードを使用します。
    * 公開鍵認証の場合、「公開鍵認証のみ許可」を選択します。RSAキーがある場合、それが使用されます。ない場合は、「Run SSH-keygen」をクリックして新しい鍵ペアを生成します。

    .. image:: img/os_enable_ssh.png
        :align: center

#. **Options** メニューでは、書き込み中にImagerの動作を設定できます。完了時に音を鳴らす、書き込み後にメディアを排出する、テレメトリを有効にするなどの設定が可能です。

    .. image:: img/os_options.png
        :align: center

#. OSカスタマイズ設定が完了したら、 **Save** をクリックしてカスタマイズを保存します。次に、書き込み時にそれらを適用するために **Yes** をクリックします。

    .. image:: img/os_click_yes.png
        :align: center

#. SDカードに既存のデータが含まれている場合は、データ損失を防ぐためにバックアップを取ることをお勧めします。バックアップが不要な場合は、 **Yes** をクリックして進みます。

    .. image:: img/os_continue.png
        :align: center

#. 「書き込み成功」のポップアップが表示されたら、画像の書き込みと検証が完了しました。これで、Micro SDカードからRaspberry Piを起動できる準備が整いました！

    .. image:: img/os_finish.png
        :align: center

#. Raspberry Piの下部にあるマイクロSDカードスロットに、Raspberry Pi OSがインストールされたSDカードを挿入します。

    .. image:: img/insert_sd_card.png
        :width: 500
        :align: center