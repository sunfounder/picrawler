Bull Fight
==========

Make PiCrawler an angry bull! Use its camera to track and rush the red cloth!

.. image:: image/bullfight.png

**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picrawler/examples
    sudo python3 bull_fight.py


**View the Image**

After the code runs, the terminal will display the following prompt:

.. code-block::

    No desktop !
    * Serving Flask app "vilib.vilib" (lazy loading)
    * Environment: production
    WARNING: Do not use the development server in a production environment.
    Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)

Then you can enter ``http://<your IP>:9000/mjpg`` in the browser to view the video screen. such as:  ``https://192.168.18.113:9000/mjpg``

.. image:: image/display.png

**Code**

.. note::
    You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you need to go to source code path like ``picrawler\examples``. After modifying the code, you can run it directly to see the effect.


.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler import Picrawler
    from time import sleep
    from robot_hat import Music
    from vilib import Vilib


    crawler = Picrawler([10,11,12,4,5,6,1,2,3,7,8,9]) 
    #crawler.set_offset([0,0,0,0,0,0,0,0,0,0,0,0])

    music = Music()

    def main():
        Vilib.camera_start()
        Vilib.display()
        Vilib.color_detect("red") 
        speed = 100

        while True:
            if Vilib.detect_obj_parameter['color_n']!=0:
                coordinate_x = Vilib.detect_obj_parameter['color_x']
                music.sound_effect_threading('./sounds/talk1.wav')

                if coordinate_x < 100:
                    crawler.do_action('turn left',1,speed)
                    sleep(0.05) 
                elif coordinate_x > 220:
                    crawler.do_action('turn right',1,speed)
                    sleep(0.05) 
                else :
                    crawler.do_action('forward',2,speed)
                    sleep(0.05)    
            else :
                crawler.do_step('stand',speed)
                sleep(0.05)


    if __name__ == "__main__":
        main()


**How it works?**

In general, this project combines the knowledge points of :ref:`Move`, :ref:`Computer Vision` and :ref:`Sound Effect`.

Its flow is shown in the figure below:

.. image:: image/bull_fight-f.png

