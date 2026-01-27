.. note:: 

    こんにちは！SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32に関心のある仲間たちと一緒に、さらに深く学んでいきましょう。

    **参加する理由は？**

    - **専門サポート**: コミュニティやチームの支援を受けて、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換して、スキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表や先行情報にいち早くアクセスできます。
    - **特別割引**: 最新製品の限定割引をお楽しみいただけます。
    - **イベントやプレゼント**: プレゼント企画や祝祭プロモーションに参加できます。

    👉 探求と創造の準備はできましたか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _install_all_modules:

すべてのモジュールをインストールする（重要）
===============================================================

#. **システムを準備する**

   Raspberry Pi がインターネットに接続されていることを確認し、システムを更新します：

   .. raw:: html

      <run></run>

   .. code-block::

      sudo apt update
      sudo apt upgrade

   .. note::
      
      Raspberry Pi OS Lite を使用している場合は、まず必要な Python 3 パッケージをインストールしてください：

   .. raw:: html

      <run></run>

   .. code-block::

         sudo apt install git python3-pip python3-setuptools python3-smbus

#. **robot-hat をインストールする**

   ``robot-hat`` モジュールをダウンロードしてインストールします：

   .. raw:: html

      <run></run>

   .. code-block::

      cd ~/
      git clone -b v2.0 https://github.com/sunfounder/robot-hat.git --depth 1
      cd robot-hat
      sudo python3 install.py

#. **vilib をインストールする**

   ``vilib`` モジュールをダウンロードしてインストールします：

   .. raw:: html

      <run></run>

   .. code-block::

      cd ~/
      git clone https://github.com/sunfounder/vilib.git --depth 1
      cd vilib
      sudo python3 install.py


#. **picrawler をインストールする**

   次に、コードをダウンロードして ``picrawler`` モジュールをインストールします。
   
   .. raw:: html
   
       <run></run>
   
   .. code-block::
   
       cd ~/
       git clone https://github.com/sunfounder/picrawler.git --depth 1
       cd picrawler
       sudo python3 setup.py install
   
   このステップには少し時間がかかるため、しばらくお待ちください。

#. **サウンドを有効にする（I2S アンプ）**

   オーディオ出力を有効にするには、``i2samp.sh`` スクリプトを実行して必要な I2S アンプ関連コンポーネントをインストールします：

   .. raw:: html

      <run></run>

   .. code-block::

      cd ~/robot-hat
      sudo bash i2samp.sh

   画面の指示に従って ``y`` と入力して Enter を押し、続行してください。その後、``/dev/zero`` をバックグラウンドで実行し、Picar-X を再起動します。

   .. note::
      再起動後に音が出ない場合は、``i2samp.sh`` スクリプトを数回実行してみてください。
