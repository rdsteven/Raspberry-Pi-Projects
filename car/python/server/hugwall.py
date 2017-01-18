import RPi.GPIO as GPIO
import car

GPIO.setmode(GPIO.BOARD)  # set gpio mode.  can only be done onces so it's here

car = Car(true) # create car instance in debug mode
car.forward(35) # tell the car to drive foreward at 35 speed

stop = 0
reset = 0
count = 0

while (stop < 4):
    # Get the cars current position
    position = car.getPosition()
    forward = position['front']
    right = position['right']

    # Should the car stop
    if (forward < 60):
        stop = stop + 1
    else:
        stop = 0

    # Correct cars course
    if count % 5 == 0:
        print "Right: ", right, " cm"

        if reset:
            car.turn(0)
            reset = 0
        else:
            car.turn(5) if right > 30 else car.turn(-5)
            reset = 1

    count = count + 1
    time.sleep(.05)

car.stop()
GPIO.cleanup()
