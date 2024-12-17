.. note:: 

    こんにちは！SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者と共にさらに深く学びましょう。

    **参加する理由は？**

    - **専門的なサポート**: コミュニティやチームのサポートを受けて、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換して、スキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表や先行情報にいち早くアクセスできます。
    - **特別割引**: 最新製品の特別割引をお楽しみいただけます。
    - **イベントやプレゼント**: プレゼント企画や祝祭プロモーションに参加できます。

    👉 探求と創造の準備はできましたか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _remote_desktop:

Raspberry Piのリモートデスクトップアクセス
==================================================

コマンドラインアクセスよりもグラフィカルユーザーインターフェース（GUI）を好む方には、Raspberry Piはリモートデスクトップ機能をサポートしています。このガイドでは、リモートアクセス用にVNC（Virtual Network Computing）を設定し、使用する方法を説明します。

この目的には、 `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ の使用をお勧めします。

**Raspberry PiでのVNCサービスの有効化**

VNCサービスはRaspberry Pi OSに標準でインストールされていますが、初期設定では無効になっています。以下の手順で有効化できます：

#. Raspberry Piターミナルで以下のコマンドを入力します：

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. 下矢印キーを使って **Interfacing Options** に移動し、 **Enter** を押します。

    .. image:: img/config_interface.png
        :align: center

#. オプションから **VNC** を選択します。

    .. image:: img/vnc.png
        :align: center

#. 矢印キーで **<Yes>** -> **<OK>** -> **<Finish>** を選択し、VNCサービスを有効化します。

    .. image:: img/vnc_yes.png
        :align: center

**VNC Viewerでのログイン**

#. ご自身のパソコンに `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ をダウンロードしてインストールします。

#. インストール後、VNC Viewerを起動します。Raspberry Piのホスト名またはIPアドレスを入力し、Enterキーを押します。

    .. image:: img/vnc_viewer1.png
        :align: center

#. プロンプトが表示されたら、Raspberry Piのユーザー名とパスワードを入力し、 **OK** をクリックします。

    .. image:: img/vnc_viewer2.png
        :align: center

#. 数秒後、Raspberry Pi OSのデスクトップが表示されます。これでターミナルを開き、コマンドを入力する準備が整いました。

    .. image:: img/bookwarm.png
        :align: center
