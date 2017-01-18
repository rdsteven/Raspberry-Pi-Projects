from ping import Ping

# this class combines all of the cars ping sensors into a single component.
# will return a dict with front, right, left, and back measurements and a shift
# amount that gives you the delta of the right measurement between this and the
# lookup
class Location:
    def __init__(self, sample):
        self.sample = sample

        self.front = Ping(33, 35)
        self.right = Ping(29, 31)
        self.back = Ping(38, 40)
        self.left = Ping(23, 24)

    def getLocation(self):
        right = self.right.measure(self.sample)
        shift = right - self.previous['right']

        self.previous = {
            'front': self.front.measure(self.sample),
            'right': right,
            'back': self.back.measure(self.sample),
            'left': self.left.measure(self.sample),
            'shift': shift
        }

        return self.previous
