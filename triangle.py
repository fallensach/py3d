import numpy as np


class Triangle:
    def __init__(self, p1, p2, p3):
        #print((p1, p2, p3))
        self.points = np.array([p1, p2, p3])
        print(self.points)
        self.x = self.points[0]
        self.y = self.points[1]
        self.z = self.points[2]

    def __str__(self):
        for point in self.points:
            print(point)
