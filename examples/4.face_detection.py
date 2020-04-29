#!/usr/bin/python3
import sys
sys.path.append(r'/opt/ezblock')
from vilib import Vilib
from ezblock import WiFi
from ezblock import print
from ezblock import delay

Vilib.camera_start(True)
Vilib.human_detect_switch(True)
WiFi().write('CN', 'MakerStarsHall', 'sunfounder')


def forever():
  print("%s"%(''.join([str(x) for x in ['There are ', Vilib.human_detect_object(('number')), ' face in the camera']])))
  delay(100)

if __name__ == "__main__":
    while True:
        forever()  