#!/usr/bin/python3
import sys
sys.path.append(r'/opt/ezblock')
from ezblock import __reset_mcu__
import time
__reset_mcu__()
time.sleep(0.01)
from vilib import Vilib
from ezblock import WiFi
from ezblock import delay
from spider import Spider
__SPIDER__ = Spider([10,11,12,4,5,6,1,2,3,7,8,9])

xAxis = None
width = None
speed = None

Vilib.camera_start(True)
Vilib.color_detect_switch(True)
Vilib.detect_color_name('red')
WiFi().write('CN', 'MakerStarsHall', 'sunfounder')
speed = 100


def forever():
  global xAxis, width, speed
  xAxis = Vilib.color_detect_object('x')
  width = Vilib.color_detect_object('width')
  delay(5)
  if width > 50:
    if xAxis == -1:
      __SPIDER__.do_action('turn left', 1, speed)
    elif xAxis == 0:
      __SPIDER__.do_action('forward', 1, speed)
    elif xAxis == 1:
      __SPIDER__.do_action('turn right', 1, speed)
  else:
    __SPIDER__.do_action('stand', 1, speed)

if __name__ == "__main__":
    while True:
        forever()  