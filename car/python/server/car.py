#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

# Car
from stearing import Stearing
from drive import Drive
from display import Display

# Sensors
#from gamma import Gamma
from location import Location
#from temperature import Temperature

# This class pretty much just puts all the cars controllers into a single
# component
class Car:
    def __init__(self):
        self.stearing = Stearing()
        self.drive = Drive()

        self.location = Location(3)
        #self.temp = Temperature()
        #self.gamma = Gamma()
        self.display = Display()

    def getPosition(self):
        return self.location.getLocation()

    def forward(self, speed):
	print "Forward"
        self.drive.forward(speed)

    def stop(self):
        self.drive.stop()

    def reverse(self, speed):
        self.drive.backward(speed)

    def turn(self, angle):
        self.stearing.turn(angle)


#motor.forward()
#time.sleep(3)
#motor.stop()

#while True:
#			motor.forward()
#			motor.backward()
#			car_dir.turn_left()
#			car_dir.turn_right()
#			car_dir.home()
#			motor.ctrl(0)
#			temp = cpu_temp.read()
#			numLen = len(data) - len('speed')
#			if numLen == 1 or numLen == 2 or numLen == 3:
#				tmp = data[-numLen:]
#				print 'tmp(str) = %s' % tmp
#				spd = int(tmp)
#				print 'spd(int) = %d' % spd
#				if spd < 24:
#					spd = 24
#				motor.setSpeed(spd)
#			angle = data.split('=')[1]
#			try:
#				angle = int(angle)
#				car_dir.turn(angle)
#			spd = data[8:]
#			try:
#				spd = int(spd)
#				motor.forward(spd)
#                       spd = data.split('=')[1]
#			try:
#				spd = int(spd)
#	                        motor.backward(spd)
