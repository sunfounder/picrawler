.. note:: 

    こんにちは！SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32に興味を持つ仲間たちと一緒に、さらに深く学んでいきましょう。

    **参加する理由は？**

    - **専門サポート**: コミュニティやチームの支援を受けて、購入後の問題や技術的な課題を解決します。
    - **学びと共有**: チュートリアルやヒントを交換して、スキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表や先行情報にいち早くアクセスできます。
    - **特別割引**: 最新製品の限定割引をお楽しみいただけます。
    - **イベントやプレゼント**: プレゼント企画や祝祭プロモーションに参加できます。

    👉 探求と創造の準備はできましたか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _i2c_spi_config:

6. I2Cインターフェースの確認
========================================

Raspberry PiのI2Cインターフェースを使用します。このインターフェースは、先ほど ``robot-hat`` モジュールをインストールする際に有効化されています。すべてが正しく設定されているか確認してみましょう。

#. 次のコマンドを入力します。

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. キーボードの下矢印キーを使用して **Interfacing Options** を選択し、 **Enter** キーを押します。

    .. image:: img/image282.png
        :align: center

#. 次に、 **I2C** を選択します。

    .. image:: img/image283.png
        :align: center

#. キーボードの矢印キーで **<Yes>** を選択し、 **<OK>** を押してI2Cの設定を完了します。

    .. image:: img/image284.png
        :align: center