from lib import motor

class Drive:
    def __init__(self):
        motor.setup()

    def forward(speed):
        motor.setSpeed(speed)
        motor.backward()

    def stop():
        motor.stop()

    def reverse(speed):
        motor.setSpeed(speed)
        motor.forward()
