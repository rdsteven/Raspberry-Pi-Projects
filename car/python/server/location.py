from ping import Ping

# this class combines all of the cars ping sensors into a single component.
# will return a dict with front, right, left, and back measurements and a shift
# amount that gives you the delta of the right measurement between this and the
# lookup
class Location:
    def __init__(self, front, right, back, left, sample):
        self.sample = sample
        self.front = Ping(front[0], front[1])
        self.right = Ping(right[0], right[1])
        self.back = Ping(back[0], back[1])
        self.left = Ping(left[0], left[1])

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
