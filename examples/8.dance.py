#!/usr/bin/python3
from Music import *
from ezblock import delay
from spider import Spider
__SPIDER__ = Spider([10,11,12,4,5,6,1,2,3,7,8,9])

speed = None

background_music('angry.mp3')
music_set_volume(50)
delay(2000)
speed = 100


def forever():
  global speed
  __SPIDER__.do_action('forward', 2, speed)
  __SPIDER__.do_action('look_left', 1, speed)
  __SPIDER__.do_action('look_right', 1, speed)
  for count in range(2):
    __SPIDER__.do_action('look_left', 1, speed)
    __SPIDER__.do_action('look_right', 1, speed)
  for count2 in range(3):
    __SPIDER__.do_action('sit', 1, speed)
    __SPIDER__.do_action('stand', 1, speed)
  __SPIDER__.do_action('push up', 1, speed)
  __SPIDER__.do_action('backward', 2, speed)
  __SPIDER__.do_action('dance', 1, speed)

if __name__ == "__main__":
    while True:
        forever()  