.. note:: 

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者と共にさらに深く学んでいきましょう。

    **なぜ参加するべきか？**

    - **専門家によるサポート**：購入後の問題や技術的な課題を、コミュニティやチームの支援を通じて解決できます。
    - **学びと共有**：スキルを向上させるためのヒントやチュートリアルを交換できます。
    - **限定プレビュー**：新製品の発表やプレビューをいち早く見ることができます。
    - **特別割引**：最新製品に対する専用割引を享受できます。
    - **季節のプロモーションとプレゼント企画**：プレゼント企画やホリデープロモーションに参加できます。

    👉 一緒に探求し、創造を楽しみたいですか？ [|link_sf_facebook|] をクリックして、今すぐ参加しましょう！

.. _ezb_treasure:

宝探し
============================

部屋に迷路を作り、6つの異なる色のカードを6つの隅に配置します。そして、PiCrawlerを操作して、これらの色カードを1つずつ探し出しましょう！

.. note:: カラーチェック用のPDFカードを:download:`こちらからダウンロードして印刷できます <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>`。

**プログラム**

.. note::

    * 以下の画像を参考にしてプログラムを書くことができます。詳細なチュートリアルについては、:ref:`ezblock:create_project_latest` をご参照ください。
    * または、EzBlock Studioの **Examples** ページで同名のコードを見つけ、 **実行** または **編集** をクリックすることができます。

.. image:: img/sp210928_181036.png
    :width: 800

リモートコントロールインターフェースに切り替えると、次のウィジェットが表示されます。

.. image:: img/sp210928_181134.png
    :width: 800


**動作の仕組み**

このプロジェクトは、:ref:`ezb_remote` 、:ref:`ezb_vision` 、および:ref:`ezb_sound` の知識を組み合わせたものです。

その流れは以下の図のようになります：

.. image:: ../python/img/treasure_hunt-f.png
    :width: 600