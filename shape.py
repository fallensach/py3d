import numpy as np
from math import cos, sin
from copy import deepcopy
class Shape:
    AXIS_Y = 0
    AXIS_X = 1
    AXIS_Z = 2
    trans_matrix = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ])

    AXES = {"X": AXIS_X, "Y": AXIS_Y, "Z": AXIS_Z}

    def __init__(self, shape_matrix, pos):
        self.hit_box = set()
        self.x = pos[0]
        self.y = pos[1]
        self.points_3d = deepcopy(shape_matrix)
        self.points_2d = [n for n in range(len(self.points_3d))]
        self.update_2d_projection(self.points_3d)

    def move_x(self, step):
        for i, point in enumerate(self.points_3d):
            self.points_3d[i][0, 0] += step

        self.update_2d_projection()

    def update_2d_projection(self, new_points):
        """
        Must be called each time the 3d points are transformed in any way
        """
        for i, point in enumerate(new_points):
            self.points_2d[i] = np.dot(self.trans_matrix, point.reshape(4, 1))



