import numpy as np
from shape import Shape


class Rectangle(Shape):
    RECTANGLE = [
            np.matrix([-1, -1, 1]), np.matrix([1, -1, 1]),
            np.matrix([1, 1, 1]), np.matrix([-1, 1, 1]),
            np.matrix([-1, -1, -1]), np.matrix([1, -1, -1]),
            np.matrix([1, 1, -1]), np.matrix([-1, 1, -1])
        ]

    DIMENSION = 3

    def __init__(self, width, height, depth, pos):
        super().__init__(self.RECTANGLE, pos)
        self.width = width
        self.height = height
        self.depth = depth
        self.init_rectangle()

    def init_rectangle(self):
        for i in range(len(self.points_3d)):
            for x in range(self.DIMENSION):
                if x == 0:
                    self.points_3d[i][0, 0] *= self.width
                elif x == 1:
                    self.points_3d[i][0, 1] *= self.height
                elif x == 2:
                    self.points_3d[i][0, 2] *= self.depth
        self.update_2d_projection()


