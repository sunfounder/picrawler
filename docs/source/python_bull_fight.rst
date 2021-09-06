Bull Fight
==========

让PiCrawler化身一头愤怒的牛牛！用它的摄像头追踪红色，随着前方的红色色块发起冲锋！

**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picrawler/examples
    sudo python3 bull_fight.py


**View the Image**

代码运行后，terminal会显示以下提示：

.. code-block::

    No desktop !
    * Serving Flask app "vilib.vilib" (lazy loading)
    * Environment: production
    WARNING: Do not use the development server in a production environment.
    Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)

随后你可以在浏览器中输入 ``http://<your IP>:9000/mjpg`` 来查看视频画面。

如： "https://192.168.18.113:9000/mjpg"

.. image:: image/display.png

**Code**

.. code-block:: python



**How it works?**

总的来说，这个项目结合了 :ref:`Keyboard Control` ， :ref:`Computer Vision` 和 :ref:`Sound Effect` 的知识点。

它的流程如下图所示

.. image:: image/flow_bullfight.png

