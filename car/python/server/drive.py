from lib import motor

class Drive:
    def __init__(self, speed):
        motor.setup()
        motor.setSpeed(speed)
