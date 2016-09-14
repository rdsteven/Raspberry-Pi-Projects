#!/usr/bin/python
import os
import time
import datetime
from picamera import PiCamera
from time import sleep
go = True

camera = PiCamera()

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)
GPIO.setup(10, GPIO.IN)
GPIO.setup(9, GPIO.IN)
GPIO.setup(11, GPIO.IN)

print("------------------")
print(" Button + GPIO ")
print("------------------")

print GPIO.input(10)
while (go == True):
   if ( GPIO.input(10) == False ):
      print("Button Pressed")
      os.system('date')
      print GPIO.input(10)
      camera.start_preview()

   if ( GPIO.input(9) == False ):
	camera.stop_preview()
	go = True

   if (GPIO.input(11) == False ):
	camera.capture ('/home/pi/Desktop/{:%Y-%m-%d %H:%M:%S}.jpg'.format(datetime.datetime.now()))
        go = False
      
   else:
      os.system('clear')
      print ("Waiting for you to press a button")
time.sleep(1)
