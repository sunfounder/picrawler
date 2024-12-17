.. note:: 

    こんにちは！SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者と共にさらに深く学びましょう。

    **参加する理由は？**

    - **専門的なサポート**: コミュニティやチームのサポートを受けて、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換して、スキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表や先行情報にいち早くアクセスできます。
    - **特別割引**: 最新製品の特別割引をお楽しみいただけます。
    - **イベントやプレゼント**: プレゼント企画や祝祭プロモーションに参加できます。

    👉 探求と創造の準備はできましたか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

For Linux/Unix Users
==========================

#. お使いのLinux/Unixシステムで **ターミナル** を開きます。

#. Raspberry Piが同じネットワークに接続されていることを確認します。以下のコマンドで確認できます：

    .. code-block::

        ping raspberrypi.local

    Raspberry Piがネットワークに接続されていれば、IPアドレスが表示されるはずです。

    * もし ``Ping request could not find host pi.local. Please check the name and try again.`` というメッセージが表示された場合は、入力したホスト名を再確認してください。
    * IPアドレスを取得できない場合は、Raspberry Piのネットワーク設定やWiFi設定を確認してください。

#. SSH接続を開始するには、以下のコマンドを入力します。 ``<username>`` にはRaspberry Piのユーザー名、 ``<hostname>`` または ``<IP address>`` にはRaspberry Piのホスト名またはIPアドレスを入力します：

    .. code-block::

        ssh pi@raspberrypi.local

#. 初回ログイン時にセキュリティ警告が表示されます。接続を続けるには ``yes`` と入力します。

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. 以前に設定したパスワードを入力します。セキュリティのため、パスワードは入力中に表示されませんのでご注意ください。

    .. note::
        パスワードがターミナルに表示されないのは正常です。正しいパスワードを入力してください。

#. ログインに成功すると、Raspberry Piに接続され、次のステップに進む準備が整いました。
