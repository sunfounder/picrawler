.. note:: 

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者と一緒にさらに深く学んでいきましょう。

    **なぜ参加するべきか？**

    - **専門家によるサポート**：購入後の問題や技術的な課題を、コミュニティやチームの支援を通じて解決できます。
    - **学びと共有**：スキルを向上させるためのヒントやチュートリアルを交換できます。
    - **限定プレビュー**：新製品の発表やプレビューをいち早く見ることができます。
    - **特別割引**：最新製品に対する専用割引を享受できます。
    - **季節のプロモーションとプレゼント企画**：プレゼント企画やホリデープロモーションに参加できます。

    👉 一緒に探求し、創造を楽しみたいですか？ [|link_sf_facebook|] をクリックして、今すぐ参加しましょう！

.. _filezilla:

Filezillaソフトウェア
==========================

.. image:: img/filezilla_icon.png

File Transfer Protocol（FTP）は、コンピューターネットワーク上でサーバーからクライアントにファイルを転送するための標準的な通信プロトコルです。

Filezillaは、FTPだけでなく、TLSを使用したFTP（FTPS）およびSFTPもサポートするオープンソースのソフトウェアです。これを使用して、ローカルのファイル（画像や音声など）をRaspberry Piにアップロードしたり、Raspberry Piからローカルにファイルをダウンロードしたりできます。

**ステップ 1**: Filezillaのダウンロード。

`Filezillaの公式ウェブサイト <https://filezilla-project.org/>` からクライアントをダウンロードしてください。Filezillaには非常に良いチュートリアルがありますので、こちらを参照してください: `Documentation - Filezilla <https://wiki.filezilla-project.org/Documentation>`。

**ステップ 2**: Raspberry Piに接続する。

インストール後、Filezillaを開き、 `FTPサーバーへの接続方法 <https://wiki.filezilla-project.org/Using#Connecting_to_an_FTP_server>` を参照して接続します。接続方法は3種類ありますが、ここでは **Quick Connect** バーを使用します。 **ホスト名/IPアドレス** 、 **ユーザー名** 、 **パスワード** 、 **ポート（22）** を入力し、 **Quick Connect** をクリックするか、 **Enter** を押してサーバーに接続します。

.. image:: img/filezilla_connect.png

.. note::

    Quick Connectは、ログイン情報をテストするための便利な方法です。恒久的な接続を作成したい場合は、Quick Connectが成功した後、 **File** -> **Copy Current Connection to Site Manager** を選択し、名前を入力して **OK** をクリックします。次回は、 **File** -> **Site Manager** から保存したサイトを選択することで接続できます。

    .. image:: img/ftp_site.png

**ステップ 3**: ファイルのアップロード/ダウンロード。

ローカルのファイルをRaspberry Piにドラッグ＆ドロップしてアップロードするか、Raspberry Pi内のファイルをローカルにダウンロードできます。

.. image:: img/upload_ftp.png
