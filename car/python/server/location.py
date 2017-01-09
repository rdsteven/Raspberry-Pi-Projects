from ping import Ping

class Location:
    def __init__(self, sample):
        self.sample = sample
        self.front = Ping(16, 18)
        self.right = Ping(29, 31)
        self.back = Ping(33, 35)
        self.left = Ping(34, 38)

    def getLocation(self):
        right = self.right.measure(self.sample)
        shift = right - self.previous['right']

        self.previous = {
            'front': self.front.measure(3),
            'right': right,
            'back': self.back.measure(3),
            'left': self.left.measure(3),
            'shift': shift
        }

        return self.previous
