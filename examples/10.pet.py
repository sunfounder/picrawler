#!/usr/bin/python3
from spider import Spider
__SPIDER__ = Spider([10,11,12,4,5,6,1,2,3,7,8,9])
from Music import *
from ezblock import Pin
from ezblock import Ultrasonic

maxDistance = None
distance = None
minDistance = None
actionFlag = None
outDistance = None
errorValue = None
findFlag = None
speed = None

"""Describe this function...
"""
def lookAround():
  global maxDistance, distance, minDistance, actionFlag, outDistance, errorValue, findFlag
  if actionFlag != 'Left' and actionFlag != 'Right':
    __SPIDER__.do_action('turn left', 1, speed)
    actionFlag = 'Left'
  elif actionFlag == 'Left':
    __SPIDER__.do_action('turn right', 2, speed)
    actionFlag = 'Right'
  elif actionFlag == 'Right':
    __SPIDER__.do_action('turn left', 1, speed)
    actionFlag = 'Left'
    findFlag = 'Lost'

maxDistance = 70
minDistance = 30
outDistance = 20000
errorValue = 0
speed = 100
actionFlag = 'Stand'
findFlag = 'Get'
background_music('spry.mp3')
music_set_volume(100)

pin_D0=Pin("D0")

pin_D1=Pin("D1")

"""Describe this function...
"""
def stayingAlive():
  global maxDistance, distance, minDistance, actionFlag, outDistance, errorValue, findFlag
  if distance <= errorValue:
    return
  if distance <= minDistance:
    __SPIDER__.do_action('stand', 1, speed)
    actionFlag = 'Stand'
    findFlag = 'Get'
  elif distance <= maxDistance:
    __SPIDER__.do_action('forward', 1, speed)
    actionFlag = 'Forward'
    findFlag = 'Get'
  else:
    __SPIDER__.do_action('sit', 1, speed)
    actionFlag = 'Sit'
    findFlag = 'Lost'


def forever():
  global maxDistance, distance, minDistance, actionFlag, outDistance, errorValue, findFlag
  distance = Ultrasonic(pin_D0, pin_D1).read()
  if distance > outDistance:
    distance = errorValue
  if findFlag == 'Get':
    music_pause()
    if distance > maxDistance:
      lookAround()
    else:
      stayingAlive()
  elif findFlag == 'Lost':
    music_unpause()
    stayingAlive()

if __name__ == "__main__":
    while True:
        forever()  