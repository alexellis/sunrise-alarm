#!/usr/bin/env python

from blinkt import set_brightness, set_pixel, show
import time

def splash():
   set_brightness(0.3)
   for x in range(0, 8):
       set_pixel(x, 255, 0, 0)
       show()
       time.sleep(0.1)

   time.sleep(0.1)
   for y in range(0, 8):
       set_pixel(y, 0, 0, 0)
       show()
       time.sleep(0.1)

splash()

