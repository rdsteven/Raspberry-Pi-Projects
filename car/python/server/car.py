#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

# Car
from stearing import Stearing
from drive import Drive
from display import Display

# Sensors
from gamma import Gamma
from ping import Ping
from temperature import Temperature

# This class pretty much just puts all the cars controllers into a single
# component
class Car:
    def __init__(self, front, right, back, left, debug):
        self.debug = debug;

        self.stearing = Stearing()
        self.drive = Drive(defaultSpeed)

        self.location = Location(front, right, back, left)
        self.temp = Temperature()
        self.gamma = Gamma()
        self.display = Display()

    def getPosition(self):
        return self.location.getLocation()

    def forward(self, speed):
        print "Forward" if self.debug
        self.drive.forward(speed)

    def stop(self):
        print "Stop" if self.debug
        self.drive.stop()

    def reverse(self, speed):
        print "Reverse" if self.debug
        self.drive.backward(speed)

    def turn(self, angle):
        if angle > 50 || angle < -50:
            print "turn angle not between -50 and 50" if self.debug
            return

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
