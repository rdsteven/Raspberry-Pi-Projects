from lib import car_dir

class Stearing:
    def __init__(self):
        car_dir.setup()
        car_dir.home()

    def turn(self, angle):
        if angle > 50 or angle < -50:
	    print "Fuck off"
            return

        car_dir.turn(450 + angle)
