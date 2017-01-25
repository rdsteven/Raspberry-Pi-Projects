from lib import motor

class Drive:
    def __init__(self):
        motor.setup()

    def forward(self, speed = 50):
	motor.forwardWithSpeed(speed)

    def stop(self):
        motor.stop()

    def reverse(self, speed = 50):
	motor.backwardWithSpeed(speed)
