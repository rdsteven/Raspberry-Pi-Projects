import RPi.GPIO as GPIO
from car import Car
import time

GPIO.setmode(GPIO.BOARD)  # set gpio mode.  can only be done onces so it's here

car = Car() # create car instance in debug mode
car.forward(35) # tell the car to drive foreward at 35 speed

stop = 0
reset = 0
count = 0

while (stop < 4):
    # Get the cars current position
    forward = car.getFront() 
    right = car.getRight()
    
    print "Front: ", forward, " Right: ", right

    # Should the car stop
    if (forward < 60):
        stop = stop + 1
    else:
        stop = 0

    # Correct cars course
    if count % 5 == 0:
        if reset:
            car.turn(0)
            reset = 0
        else:
            if (right > 30):
                car.turn(25)
            else:
                car.turn(-25)
            reset = 1

    count = count + 1
    time.sleep(0.1)

car.turn(0)
car.stop()
GPIO.cleanup()
