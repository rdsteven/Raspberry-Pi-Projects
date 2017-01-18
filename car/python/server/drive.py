from lib import motor

class Drive:
    def __init__(self):
        motor.setup()

    def forward(self, speed = 50):
	motor.forwardWithSpeed(speed)
	#motor.setSpeed(speed)
	#motor.motor0(True)
	#motor.motor1(True)

    def stop(self):
        motor.stop()

    def reverse(self, speed = 50):
        #motor.setSpeed(speed)
	motor.backwardWithSpeed(speed)
	#motor.motor0(False)
	#motor.motor1(False)
