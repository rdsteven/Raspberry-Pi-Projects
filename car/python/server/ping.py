import RPi.GPIO as GPIO
import time

class Ping:
    def __init__(self, trig, echo):
        self.trig = trig
        self.echo = echo

        GPIO.setup(trig, GPIO.OUT)
        GPIO.setup(echo, GPIO.IN)

    def read(self):
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

    def measure(self, sample):
        sum = 0

        for val in range(sample):
            sum = sum + self.read()

        return sum / sample
