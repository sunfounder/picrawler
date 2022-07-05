.. _ezb_record:

Record New Step
==============================

We use the remote function to control PiCrawler to make several poses in turn, and record these poses. Replay them later.


**Program**

.. note::

    * You can write the program according to the following picture, please refer to the tutorial: :ref:`ezblock:create_project_latest`.
    * Or find the code with the same name on the **Examples** page of the EzBlock Studio and click **Run** or **Edit** directly.

.. image:: img/record.png
    :width: 800

Switch to the Remote Control interface, and you will see the following widgets.

.. image:: img/sp210928_164343-1.png
    :width: 600

**How it works?**


This project was born out of :ref:`ezb_posture`. Added recording and replay functions.

The recording function is implemented by the following code.

.. image:: img/sp210928_164449.png

The replay function is implemented by the following code.

.. image:: img/sp210928_164500.png