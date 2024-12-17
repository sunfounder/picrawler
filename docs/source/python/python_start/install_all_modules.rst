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


5. すべてのモジュールをインストールする（重要）
===============================================================

インターネットに接続されていることを確認し、システムを更新します：

.. raw:: html

    <run></run>

.. code-block::

    sudo apt update
    sudo apt upgrade

.. note::

    Python3関連のパッケージは、LiteバージョンのOSをインストールしている場合に必須です。

    .. raw:: html

        <run></run>

    .. code-block::

        sudo apt install git python3-pip python3-setuptools python3-smbus


``robot-hat`` モジュールをインストールします。

.. raw:: html

    <run></run>

.. code-block::

    cd ~/
    git clone -b v2.0 https://github.com/sunfounder/robot-hat.git
    cd robot-hat
    sudo python3 setup.py install

次に、コードをダウンロードして ``vilib`` モジュールをインストールします。

.. raw:: html

    <run></run>

.. code-block::

    cd ~/
    git clone -b picamera2 https://github.com/sunfounder/vilib.git
    cd vilib
    sudo python3 install.py

次に、コードをダウンロードして ``picrawler`` モジュールをインストールします。

.. raw:: html

    <run></run>

.. code-block::

    cd ~/
    git clone https://github.com/sunfounder/picrawler.git
    cd picrawler
    sudo python3 setup.py install

この手順は少し時間がかかりますので、少々お待ちください。

最後に、 ``i2samp.sh`` スクリプトを実行してi2sアンプに必要なコンポーネントをインストールします。これを行わないと、ピースロットから音が出ません。

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler
    sudo bash i2samp.sh
	
.. image:: img/i2s.png

``y`` と入力して、 **Enter** キーを押してスクリプトを実行します。

.. image:: img/i2s2.png

``y`` と入力して、 **Enter** キーを押してバックグラウンドで ``/dev/zero`` を実行します。

.. image:: img/i2s3.png

``y`` と入力して、 **Enter** キーを押してマシンを再起動します。

.. note::

    再起動後に音が出ない場合は、 ``i2samp.sh`` スクリプトを複数回実行する必要があるかもしれません。
