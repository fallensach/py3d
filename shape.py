import numpy as np
from math import cos, sin
from copy import deepcopy
from triangle import Triangle
class Shape:
    AXIS_Y = 0
    AXIS_X = 1
    AXIS_Z = 2
    trans_matrix = np.array([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ])

    AXES = {"X": AXIS_X, "Y": AXIS_Y, "Z": AXIS_Z}

    def __init__(self, shape_matrix, pos):
        self.hit_box = set()
        self.length = len(shape_matrix)
        self.x = pos[0]
        self.y = pos[1]
        self.mesh_space = self.triangularize(shape_matrix)
        self.world_space = [n for n in range((len(self.mesh_space)))]
        #self.update_world(self.mesh_space)
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.mesh_space):
            self.index = -1
            raise StopIteration

        return self.mesh_space[self.index]


    def triangularize(self, points):
        """
        Divides the shape into triangles
        """
        i = 0
        triangles = []
        triangle_vertices = []
        for count, point in enumerate(points):
            triangle_vertices.append(point)
            if i == 2 or count == self.length-1:
                i = -1
                triangle = Triangle(triangle_vertices[0], triangle_vertices[1], triangle_vertices[2])
                triangles.append(triangle)
                triangle_vertices = []
            i += 1

        return triangles

    def update_world(self, new_tris):
        """
        Must be called each time the 3d points are transformed in any way
        """

        for i, tri in enumerate(new_tris):
            self.world_space[i] = tri



