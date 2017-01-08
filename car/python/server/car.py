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

class Car:
    def __init__(self, logFile):
        GPIO.setmode(GPIO.BOARD)
        self.logFile = logFile

        self.stearing = Stearing()
        self.drive = Drive(35)

        self.front = Ping(16, 18)
        self.right = Ping(29, 31)
        self.back = Ping(33, 35)
        self.left = Ping(34, 38)

        self.temp = Temperature()
        self.gamma = Gamma()
        self.display = Display()

    def start():

    def stop():


class Gamma:
    def __init__(self):

class Temperature:
    def __init__(self):

class Ping:
    def __init__(self, trig, echo):
        self.trig = trig
        self.echo = echo

        GPIO.setup(trig, GPIO.OUT)
        GPIO.setup(echo, GPIO.IN)

    def measure(self):
        GPIO.output(self.trig, 0)
        time.sleep(0.000002)

        GPIO.output(self.trig, 1)
        time.sleep(0.00001)
        GPIO.output(self.trig, 0)

        while GPIO.input(self.echo) == 0:
        	a = 0
        time1 = time.time()
        while GPIO.input(self.echo) == 1:
        	a = 1
        time2 = time.time()

        during = time2 - time1
        return during * 340 / 2 * 100


forwardPing = Ping(16, 18)
rightPing = Ping(29, 31)

motor.backward()

stop = 0
reset = 0
count = 0

while (stop < 4):
    # stop
    f = forwardPing.measure()
    print "Forward: ", f, " cm"

    if (f < 60):
        stop = stop + 1
    else:
        stop = 0

    # course correct
    if count % 5 == 0:
        r = rightPing.measure()
        print "Right: ", r, " cm"

        if reset:
            car_dir.home()
            reset = 0
        else:
            car_dir.turn_right() if r > 30 else car_dir.turn_left()
            reset = 1

    count = count + 1
    time.sleep(.05)

print "stop"
motor.stop()
GPIO.cleanup()

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
