import numpy as np
from math import cos, sin
from copy import deepcopy


class Shape:
    AXIS_Y = 0
    AXIS_X = 1
    AXIS_Z = 2
    trans_matrix = np.matrix([
        [1, 0, 0],
        [0, 1, 0],
    ])

    def __init__(self, shape_matrix, pos):
        self.hit_box = set()
        self.x = pos[0]
        self.y = pos[1]
        self.points_3d = deepcopy(shape_matrix)
        self.points_2d = [n for n in range(len(self.points_3d))]
        self.update_2d_projection()

    def rotate(self, axis, alpha):
        if axis == self.AXIS_X:
            rotation_matrix = np.matrix([
                [cos(alpha), 0, sin(alpha)],
                [0, 1, 0],
                [-sin(alpha), 0, cos(alpha)]
            ])
        elif axis == self.AXIS_Y:
            rotation_matrix = np.matrix([
                [1, 0, 0],
                [0, cos(alpha), -sin(alpha)],
                [0, sin(alpha), cos(alpha)]
            ])
        elif axis == self.AXIS_Z:
            rotation_matrix = np.matrix([
                [cos(alpha), -sin(alpha), 0],
                [sin(alpha), cos(alpha), 0],
                [0, 0, 1]
            ])
        else:
            assert "Axis not found"
            return "ERROR"

        # Rotate the point and put it back into the shape matrix
        for i, point in enumerate(self.points_3d):
            rotated_point = np.dot(rotation_matrix, point.reshape(3, 1))
            self.points_3d[i] = rotated_point.reshape(1, 3)

        self.update_2d_projection()

    def move_x(self, step):
        for i, point in enumerate(self.points_3d):
            self.points_3d[i][0, 0] += step

        self.update_2d_projection()

    def update_2d_projection(self):
        for i, point in enumerate(self.points_3d):
            self.points_2d[i] = (np.dot(self.trans_matrix, point.reshape(3, 1)))
