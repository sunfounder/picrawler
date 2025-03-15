#!/usr/bin/env python3
"""
Flask Camera Server for PiCrawler
---------------------------------
This script creates a simple web server to display the camera feed from picamera2
when vilib is not available. Run it in a separate terminal window:

sudo python3 flask_camera_server.py

Then access the feed at: http://your_pi_ip:9001/

Press Ctrl+C to stop the server.
"""

import cv2
import time
import threading
import argparse
from flask import Flask, Response, render_template_string

# Default camera to None, will be set by main script
camera = None
latest_frame = None
frame_lock = threading.Lock()
is_running = True

# Add frame processor variable - can be set by main script to process frames
frame_processor = None

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>PiCrawler Camera Feed</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            text-align: center;
            background-color: #f5f5f5;
        }
        h1 {
            color: #333;
        }
        img {
            max-width: 100%;
            border: 2px solid #ddd;
            border-radius: 6px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>PiCrawler Camera Feed</h1>
        <img src="{{ url_for('video_feed') }}" />
        <p>
            This feed is provided by the picamera2 module.
        </p>
    </div>
</body>
</html>
"""


def capture_frames():
    """Continuously capture frames from the camera"""
    global camera, latest_frame, is_running, frame_processor

    while is_running:
        if camera is not None:
            try:
                frame = camera.capture_array()

                # Apply frame processing if a processor is available
                if frame_processor is not None:
                    try:
                        frame = frame_processor(frame)
                    except Exception as e:
                        print(f"Error in frame processor: {e}")

                with frame_lock:
                    latest_frame = frame
            except Exception as e:
                print(f"Error capturing frame: {e}")
        time.sleep(0.033)  # ~30 fps


def generate_frames():
    """Generate frames for the MJPEG stream"""
    global latest_frame

    while True:
        with frame_lock:
            if latest_frame is not None:
                # Convert to jpeg
                _, jpeg = cv2.imencode(".jpg", latest_frame)
                frame_bytes = jpeg.tobytes()
                yield (
                    b"--frame\r\n"
                    b"Content-Type: image/jpeg\r\n\r\n" + frame_bytes + b"\r\n"
                )
        time.sleep(0.033)  # ~30 fps


@app.route("/")
def index():
    """Render the main page"""
    return render_template_string(HTML_TEMPLATE)


@app.route("/video_feed")
def video_feed():
    """Provide the video stream"""
    return Response(
        generate_frames(), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


def set_camera(cam):
    """Set the camera object from the main script"""
    global camera
    camera = cam
    print(f"Camera set to: {camera}")


def start_server(port=9001, host="0.0.0.0"):
    """Start the Flask server in a separate thread"""
    # Start the frame capture thread
    capture_thread = threading.Thread(target=capture_frames)
    capture_thread.daemon = True
    capture_thread.start()

    # Start the Flask server
    try:
        print(f"Starting camera web server at http://{host}:{port}/")
        app.run(host=host, port=port, debug=False, threaded=True)
    except Exception as e:
        print(f"Error starting Flask server: {e}")
    finally:
        global is_running
        is_running = False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flask Camera Server for PiCrawler")
    parser.add_argument(
        "--port", type=int, default=9001, help="Port for the web server"
    )
    args = parser.parse_args()

    # Initialize a test camera if running stand-alone
    try:
        from picamera2 import Picamera2

        test_camera = Picamera2()
        test_camera.start()
        set_camera(test_camera)
        start_server(port=args.port)
    except Exception as e:
        print(f"Error initializing camera: {e}")
        print("Please run this script from the main PiCrawler script.")
