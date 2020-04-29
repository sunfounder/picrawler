#!/usr/bin/python3
import sys
sys.path.append(r'/opt/ezblock')
from spider import Spider
from ezblock import delay

__SPIDER__ = Spider([10,11,12,4,5,6,1,2,3,7,8,9])


def forever():
  __SPIDER__.do_action('forward', 1, 80)
  delay(1000)
  __SPIDER__.do_action('backward', 1, 80)
  delay(1000)
  __SPIDER__.do_action('turn left', 1, 80)
  delay(1000)
  __SPIDER__.do_action('turn right', 1, 80)
  delay(1000)
  __SPIDER__.do_action('sit', 1, 80)
  delay(1000)
  __SPIDER__.do_action('stand', 1, 80)
  delay(2000)

if __name__ == "__main__":
    while True:
        forever()  