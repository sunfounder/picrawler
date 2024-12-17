.. note:: 

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者と一緒にさらに深く学んでいきましょう。

    **なぜ参加するべきか？**

    - **専門家によるサポート**：購入後の問題や技術的な課題を、コミュニティやチームの支援を通じて解決できます。
    - **学びと共有**：スキルを向上させるためのヒントやチュートリアルを交換できます。
    - **限定プレビュー**：新製品の発表やプレビューをいち早く見ることができます。
    - **特別割引**：最新製品に対する専用割引を享受できます。
    - **季節のプロモーションとプレゼント企画**：プレゼント企画やホリデープロモーションに参加できます。

    👉 一緒に探求し、創造を楽しみたいですか？ [|link_sf_facebook|] をクリックして、今すぐ参加しましょう！

.. _openssh_powershell:

PowerShell経由でOpenSSHをインストール
======================================

``ssh <username>@<hostname>.local``（または ``ssh <username>@<IP address>``）を使用してRaspberry Piに接続しようとしたときに、次のエラーメッセージが表示される場合があります。

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.


これは、使用しているコンピューターのシステムが古く、 `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ が事前にインストールされていないことを意味します。以下の手順に従って、手動でインストールする必要があります。

#. Windowsデスクトップの検索ボックスに ``powershell`` と入力し、 ``Windows PowerShell`` を右クリックして、表示されるメニューから ``管理者として実行`` を選択します。

    .. image:: img/powershell_ssh.png
        :align: center

#. 次のコマンドを使用して、 ``OpenSSH.Client`` をインストールします。

    .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. インストールが完了すると、以下の出力が表示されます。

    .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. 次のコマンドを使用してインストールを確認します。

    .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. これで、 ``OpenSSH.Client`` が正常にインストールされたことが確認できます。

    .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

    .. warning:: 
        上記のメッセージが表示されない場合は、使用しているWindowsシステムが依然として古いため、PuTTYのようなサードパーティ製SSHツールのインストールをお勧めします。

#. PowerShellを再起動し、再度管理者として実行します。この時点で、 ``ssh`` コマンドを使用してRaspberry Piにログインできるようになります。ログイン時に、以前設定したパスワードの入力を求められます。

    .. image:: img/powershell_login.png