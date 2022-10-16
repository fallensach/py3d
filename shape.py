import numpy as np
from math import cos, sin
from copy import deepcopy
from triangle import Triangle
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
        self.points_3d = self.triangularize(shape_matrix)
        self.points_2d = [n for n in range(len(self.points_3d)*3)]
        self.update_2d_projection(self.points_3d)

    def move_x(self, step):
        for i, point in enumerate(self.points_3d):
            self.points_3d[i][0, 0] += step

        self.update_2d_projection()

    def triangularize(self, points):
        """
        Divides the shape into triangles
        """
        i = 0
        triangles = []
        triangle_vertices = []
        for point in points:
            if i == 3:
                i = 0
                triangle = Triangle(triangle_vertices[0], triangle_vertices[1], triangle_vertices[2])
                triangles.append(triangle)
                triangle_vertices = []
            triangle_vertices.append(point)
            i += 1

        return triangles

    def update_2d_projection(self, new_points):
        """
        Must be called each time the 3d points are transformed in any way
        """
        for i, point in enumerate(new_points):
            self.points_2d[i] = np.dot(self.trans_matrix, point.reshape(4, 1))



