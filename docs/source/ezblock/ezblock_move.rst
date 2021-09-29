Move — Ezblock
=================


This is PiCrawler's first project. Perform its most basic function - move.


.. note:: 

    If you are not yet familiar with the use of Ezblock, please refer to the `Quick User Guide <https://docs.sunfounder.com/projects/ezblock3/en/latest/quick_user_guide_for_ezblock3.html#>`_. You need to know **How to connect the product and Ezblock Studio?** and **How to Open and Run examples?** to proceed with this project smoothly.

**Program**

After opening the example, you can see the following code block.

.. image:: media/move.png

Click the Upload & Run button at the bottom right of the screen, and PiCrawler will execute "forward" and "backward" actions in sequence.


**How it works?**

First, you need to understand the program framework of Ezblock. as follows:

.. image:: media/sp210927_162828.png
    :width: 200

All Ezblock projects contain these two blocks. The **Start** block runs at the beginning of the program and is executed only once, and is often used to set variables; the **Forever** block runs after **Start**, and will be executed repeatedly, and is often used to implement main functions.
If you delete these two blocks, you can drag them back from the **Basic** category on the left.

Next you need to understand the following blocks.

.. image:: media/sp210927_165133.png

**do action** allows PiCrawler to perform basic actions. You can modify the options in the first groove. For example, select "Turn Left", "Back" and so on.
The second groove can set the number of executions of the action, and only integer numbers greater than 0 can be written.
The third groove can set the speed of the action, and only integers within 0~100 can be written.

.. image:: media/sp210927_170717.png
    :width: 500

**do step** is similar to **do action**, but it is not an action but a static posture. Such as "stand", "sit".

Both blocks can be dragged from the **PiCrawler** category on the left.