#!/usr/bin/env python
import RPi.GPIO as GPIO
import car_dir
import motor
import time

TRIG = 16
ECHO = 18

class Ping:
    def __init__(self, trig, echo):
        self.trig = trig
        self.echo = echo

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(trig, GPIO.OUT)
        GPIO.setup(echo, GPIO.IN)

    def measure():
        GPIO.output(TRIG, 0)
        time.sleep(0.000002)

        GPIO.output(TRIG, 1)
        time.sleep(0.00001)
        GPIO.output(TRIG, 0)

        while GPIO.input(ECHO) == 0:
        	a = 0
        time1 = time.time()
        while GPIO.input(ECHO) == 1:
        	a = 1
        time2 = time.time()

        during = time2 - time1
        return during * 340 / 2 * 100

car_dir.setup()
#motor.setup()
car_dir.home()
setupPing()
#motor.setSpeed(50)

forwardPing = Ping(16,18)
rightPing = Ping(29, 31)

#motor.backward()

stop = 0
reset = 0

while (stop < 4):
    # stop
    f = forward.measure()
    print "Forward: " + f + " cm"

    if (f < 60):
        stop = stop + 1
    else:
        stop = 0

    # course correct
    r = right.measure()
    print "Right: " + r + " cm"

    if reset:
        car_dir.home()
        reset = 0
    else:
        car_dir.turn_right() if r > 30 else car_dir.turn_left()
        reset = 1

    time.sleep(.05)

print "stop"
#motor.stop()
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
