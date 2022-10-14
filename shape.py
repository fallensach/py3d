import numpy as np
from math import cos, sin
from copy import deepcopy


class Shape:
    AXIS_Y = 0
    AXIS_X = 1
    AXIS_Z = 2
    trans_matrix = np.matrix([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ])

    AXES = {"X": AXIS_X, "Y": AXIS_Y, "Z": AXIS_Z}

    def __init__(self, shape_matrix, pos):
        self.hit_box = set()
        self.x = pos[0]
        self.y = pos[1]
        self.points_3d = deepcopy(shape_matrix)
        self.points_2d = [n for n in range(len(self.points_3d))]
        self.update_2d_projection()

    def rotate(self, axis, alpha):
        """
        Rotates the shape on the given axis and degree

        axis: The axis to rotate on
        alpha: The degree to rotate
        """
        if axis == self.AXIS_X:
            rotation_matrix = np.matrix([
                [cos(alpha), 0, sin(alpha), 0],
                [0, 1, 0, 0],
                [-sin(alpha), 0, cos(alpha), 0],
                [0, 0, 0, 0]
            ])
        elif axis == self.AXIS_Y:
            rotation_matrix = np.matrix([
                [1, 0, 0, 0],
                [0, cos(alpha), -sin(alpha), 0],
                [0, sin(alpha), cos(alpha), 0],
                [0, 0, 0, 0]
            ])
        elif axis == self.AXIS_Z:
            rotation_matrix = np.matrix([
                [cos(alpha), -sin(alpha), 0, 0],
                [sin(alpha), cos(alpha), 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 0]
            ])
        else:
            assert "Axis not found"
            return "ERROR"

        # Rotate the point and put it back into the shape matrix
        for i, point in enumerate(self.points_3d):
            rotated_point = np.dot(rotation_matrix, point.reshape(4, 1))
            self.points_3d[i] = rotated_point.reshape(1, 4)

        self.update_2d_projection()

    def move_x(self, step):
        for i, point in enumerate(self.points_3d):
            self.points_3d[i][0, 0] += step

        self.update_2d_projection()

    def update_2d_projection(self, rescale=False):
        """
        Must be called each time the 3d points are transformed in any way
        """
        if rescale:
            for i, point in enumerate(self.points_3d):
                self.points_3d[i] *= 20

        for i, point in enumerate(self.points_3d):
            self.points_2d[i] = (np.dot(self.trans_matrix, point.reshape(4, 1)))

    def update_3d(self, camera):
        for i, point in enumerate(self.points_3d):
            self.points_3d[i] = np.dot(camera, point.reshape(4, 1)).reshape(1, 4)
            if self.points_3d[i][0, 3] != 0:
                self.points_3d[i][0, 0] /= self.points_3d[i][0, 3]
                self.points_3d[i][0, 1] /= self.points_3d[i][0, 3]
                self.points_3d[i][0, 2] /= self.points_3d[i][0, 3]

        self.update_2d_projection(False)

