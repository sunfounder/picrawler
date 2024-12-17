.. note:: 

    こんにちは！SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者と共にさらに深く学びましょう。

    **参加する理由は？**

    - **専門的なサポート**: コミュニティやチームのサポートを受けて、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換して、スキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表や先行情報にいち早くアクセスできます。
    - **特別割引**: 最新製品の特別割引をお楽しみいただけます。
    - **イベントやプレゼント**: プレゼント企画や祝祭プロモーションに参加できます。

    👉 探求と創造の準備はできましたか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

For Mac OS X Users
==========================

Mac OS Xをお使いの方は、SSH（Secure Shell）を利用することで、Raspberry Piに安全で便利にリモートアクセスし、制御することができます。特にRaspberry Piがモニターに接続されていない場合や、リモートで作業する際に非常に便利です。Macのターミナルアプリケーションを使用して、この安全な接続を確立します。接続時には、Raspberry Piのユーザー名とホスト名を含むSSHコマンドを使用し、最初の接続時にRaspberry Piの認証確認を行います。

#. Raspberry Piに接続するには、以下のSSHコマンドを入力します：

    .. code-block::

        ssh pi@raspberrypi.local

    .. image:: img/mac-ping.png

#. 初回ログイン時にセキュリティメッセージが表示されます。接続を続けるには **yes** と入力してください。

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Raspberry Piのパスワードを入力します。セキュリティ上の理由から、パスワードは入力中に表示されませんのでご注意ください。

    .. code-block::

        pi@raspberrypi.local's password: 
        Linux raspberrypi 5.15.61-v8+ #1579 SMP PREEMPT Fri Aug 26 11:16:44 BST 2022 aarch64

        The programs included with the Debian GNU/Linux system are free software;
        the exact distribution terms for each program are described in the
        individual files in /usr/share/doc/*/copyright.

        Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
        permitted by applicable law.
        Last login: Thu Sep 22 12:18:22 2022
        pi@raspberrypi:~ $ 

