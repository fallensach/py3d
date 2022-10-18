import numpy as np


class Triangle:
    def __init__(self, p1, p2, p3):
        self.points = np.array([p1, p2, p3])
        self.x = self.points[0]
        self.y = self.points[1]
        self.z = self.points[2]
        self.index = -1

    def __str__(self):
        self.index += 1
        if self.index > len(self.points):
            self.index = -1
            return 0

        return str(self.points)
