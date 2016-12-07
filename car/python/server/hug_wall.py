#!/usr/bin/env python
import RPi.GPIO as GPIO
import car_dir
import motor
import time   

car_dir.setup()
motor.setup()
car_dir.home()
motor.setSpeed(100)
motor.forward()
time.sleep(3)
motor.stop()

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

