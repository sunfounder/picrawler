Record Video
==================

This example will guide you how to use the recording function.

**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picrawler/examples
    sudo python3 record_video.py


After the code runs, the recording function will start. You can input ``q`` to start/pause/continue recording, and input ``e`` to stop recording.

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

Then you can enter ``http://<your IP>:9000/mjpg`` in the browser to view the video screen. such as:  ``http://192.168.18.113:9000/mjpg``

.. image:: image/display.png


**Code** 

.. code-block:: python

	from time import sleep,strftime,localtime
	from vilib import Vilib
	import readchar 

	manual = '''
	Press keys on keyboard to control recording:
		Q: record/pause/continue
		E: stop
		ESC: Quit
	'''

	def print_overwrite(msg,  end='', flush=True):
		print('\r\033[2K', end='',flush=True)
		print(msg, end=end, flush=True)

	def main():
		rec_flag = 'stop' # start,pause,stop
		vname = None
		Vilib.rec_video_set["path"] = "/home/pi/Videos/" # set path

		Vilib.camera_start(vflip=False,hflip=False) 
		Vilib.display(local=True,web=True)
		sleep(0.8)  # wait for startup

		print(manual)
		while True:
			# read keyboard
			key = readchar.readkey()
			key = key.lower()
			# start,pause
			if key == 'q':
				key = None
				if rec_flag == 'stop':            
					rec_flag = 'start'
					# set name
					vname = strftime("%Y-%m-%d-%H.%M.%S", localtime())
					Vilib.rec_video_set["name"] = vname
					# start record
					Vilib.rec_video_run()
					print_overwrite('rec start ...')
				elif rec_flag == 'start':
					rec_flag = 'pause'
					Vilib.rec_video_pause()
					print_overwrite('pause')
				elif rec_flag == 'pause':
					rec_flag = 'start'
					Vilib.rec_video_start()
					print_overwrite('continue')
			# stop       
			elif key == 'e' and rec_flag != 'stop':
				key = None
				rec_flag = 'stop'
				Vilib.rec_video_stop()
				print_overwrite("The video saved as %s%s.avi"%(Vilib.rec_video_set["path"],vname),end='\n')  
			# quit
			elif key == readchar.key.CTRL_C or key in readchar.key.ESCAPE_SEQUENCES:
				Vilib.camera_close()
				print('\nquit')
				break 

			sleep(0.1)

	if __name__ == "__main__":
		main()


**How it works?**

Functions related to recording include the following:

* ``Vilib.rec_video_run(video_name)`` : Started the thread to record the video. ``video_name`` is the name of the video file, it should be a string.
* ``Vilib.rec_video_start()`` : Start or continue video recording.
* ``Vilib.rec_video_pause()`` : Pause recording.
* ``Vilib.rec_video_stop()`` : Stop recording.

``Vilib.rec_video_set["path"] = "/home/pi/video/test/"`` sets the storage location of video files.