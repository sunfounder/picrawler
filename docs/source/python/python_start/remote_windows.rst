.. note:: 

    こんにちは！SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者と共にさらに深く学びましょう。

    **参加する理由は？**

    - **専門的なサポート**: コミュニティやチームのサポートを受けて、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換して、スキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表や先行情報にいち早くアクセスできます。
    - **特別割引**: 最新製品の特別割引をお楽しみいただけます。
    - **イベントやプレゼント**: プレゼント企画や祝祭プロモーションに参加できます。

    👉 探求と創造の準備はできましたか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

For Windows Users
=======================

Windows 10以降のユーザーは、以下の手順でRaspberry Piにリモートログインできます。

#. Windowsの検索ボックスに「 ``powershell`` 」を入力し、「 ``Windows PowerShell`` 」を右クリックして「 ``管理者として実行`` 」を選択します。

    .. image:: img/powershell_ssh.png
        :align: center

#. PowerShellで「 ``ping -4 <hostname>.local`` 」と入力して、Raspberry PiのIPアドレスを確認します。

    .. code-block::

        ping -4 raspberrypi.local

    .. image:: img/sp221221_145225.png
        :width: 550
        :align: center

    Raspberry Piがネットワークに接続されている場合、そのIPアドレスが表示されます。

    * もし「 ``Ping request could not find host pi.local. Please check the name and try again.`` 」と表示された場合、入力したホスト名が正しいか確認してください。
    * IPアドレスが取得できない場合は、Raspberry Piのネットワーク設定またはWi-Fi設定を確認してください。

#. IPアドレスが確認できたら、「 ``ssh <username>@<hostname>.local`` 」または「 ``ssh <username>@<IP address>`` 」を使用してRaspberry Piにログインします。

    .. code-block::

        ssh pi@raspberrypi.local

    .. warning::

        「 ``The term 'ssh' is not recognized as the name of a cmdlet...`` 」というエラーが表示された場合、システムにSSHツールがインストールされていない可能性があります。この場合、:ref:`openssh_powershell` に従ってOpenSSHを手動でインストールするか、PuTTYのようなサードパーティ製ツールを使用してください。

#. 初回ログイン時にセキュリティメッセージが表示されます。「 ``yes`` 」と入力して接続を続けます。

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. 以前に設定したRaspberry Piのパスワードを入力します。パスワードはセキュリティ上の理由で画面に表示されませんので、正しく入力されていることを確認してください。

    .. note::

        パスワードを入力しても、文字が表示されないのは通常の動作です。正しいパスワードを入力してください。

#. 接続が成功すると、Raspberry Piがリモート操作可能になります。

    .. image:: img/sp221221_140628.png
        :width: 550
        :align: center
