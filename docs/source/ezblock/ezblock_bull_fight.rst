.. note:: 

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者と一緒にさらに深く学んでいきましょう。

    **なぜ参加するべきか？**

    - **専門家によるサポート**：購入後の問題や技術的な課題を、コミュニティやチームの支援を通じて解決できます。
    - **学びと共有**：スキルを向上させるためのヒントやチュートリアルを交換できます。
    - **限定プレビュー**：新製品の発表やプレビューをいち早く見ることができます。
    - **特別割引**：最新製品に対する専用割引を享受できます。
    - **季節のプロモーションとプレゼント企画**：プレゼント企画やホリデープロモーションに参加できます。

    👉 一緒に探求し、創造を楽しみたいですか？ [|link_sf_facebook|] をクリックして、今すぐ参加しましょう！

.. _ezb_bull:

闘牛
======================

PiCrawlerを怒った牛に変身させましょう！カメラを使って赤い布を追跡し、突進させます！

.. .. image:: ../python/img/bullfight.png

.. note:: カラーチェックには、以下のPDFカラーカードをダウンロードして印刷できます: :download:`PDFカラーカード <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>`。

**プログラム**

.. note::

    * 以下の画像に従ってプログラムを書くことができます。詳細なチュートリアルについては、:ref:`ezblock:create_project_latest` をご参照ください。
    * あるいは、EzBlock Studioの **Examples** ページで同名のコードを見つけて、 **実行** または **編集** を直接クリックすることができます。

.. image:: img/sp210928_175806.png
    :width: 800


リモートコントロールインターフェースに切り替えると、以下の画面が表示されます。

.. image:: img/sp21aa.png


**仕組みは？**

このプロジェクトは、:ref:`ezb_move` 、:ref:`ezb_vision` 、および:ref:`ezb_sound` の知識を組み合わせたものです。

そのフローは、以下の図に示されています。

.. image:: ../python/img/bull_fight-f.png
    :width: 600
