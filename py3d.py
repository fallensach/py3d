import pygame
import numpy as np
from math import cos, sin, atan, pi
from rectangle import Rectangle
from copy import deepcopy


def mult_matrix(m1, m2):
    new_m2 = np.array([0., 0., 0.])

    for i in range(3):
        for x in range(3):
            new_m2[i] += m2[x] * m1[x][i]

        new_m2[i] += m1[3][i]

    w = (m2[0] * m1[0][3]) + (m2[1] * m1[1][3]) + (m2[2] * m1[2][3]) + m1[3][3]

    if w != 0.0:
        new_m2[0] /= w
        new_m2[1] /= w
        new_m2[2] /= w

    return new_m2

class Py3d:
    AXIS_Y = 0
    AXIS_X = 1
    AXIS_Z = 2
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    trans_matrix = np.matrix([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ])

    # FOR DEBUG ONLY
    point_size = 1

    def __init__(self, width, height, pygame, screen):
        self.game = pygame
        self.screen = screen
        self.polygons = []
        self.width = width
        self.height = height
        self.aspect_ratio = height/width
        self.fov = atan((pi/2)/2)
        self.z_far = 1000
        self.z_near = 0.1
        self.projection_matrix = np.array([
            [self.aspect_ratio*self.fov, 0, 0, 0],
            [0, self.fov, 0, 0],
            [0, 0, self.z_far/(self.z_far-self.z_near), 1],
            [0, 0, (-self.z_far*self.z_near)/(self.z_far-self.z_near), 0]
        ])

    def create_rectangle(self, width, height, depth, pos):
        """
        Creates a Rectangle object and adds it to the world's polygon list

        width: width of the rectangle
        height: height of the rectangle
        depth: depth of the rectangle
        pos: position as a tuple (x, y)
        return: Rectangle object
        """
        assert width != isinstance(width, float), "Given width is not an integer"
        assert height != isinstance(height, float), "Given height is not an integer"
        assert depth != isinstance(depth, float), "Given depth is not an integer"
        assert pos != isinstance(pos, tuple()), "Given position is not a float tuple"
        poly = Rectangle(width, height, depth, pos)
        self.polygons.append(poly)
        return poly

    def connect_triangle(self, t_points):
        self.game.draw.line(self.screen, self.WHITE, (t_points[0][0], t_points[0][1]), (t_points[1][0], t_points[1][1]))
        self.game.draw.line(self.screen, self.WHITE, (t_points[1][0], t_points[1][1]), (t_points[2][0], t_points[2][1]))
        self.game.draw.line(self.screen, self.WHITE, (t_points[2][0], t_points[2][1]), (t_points[0][0], t_points[0][1]))

    def draw_lines(self, points):
        triangle = []
        i = 0
        for point in points:
            if i == 3:
                i = 0
                self.connect_triangle(triangle)
                triangle.clear()
            triangle.append(point)
            i += 1

    def render_polygons(self):
        self.clear_screen()
        for polygon in self.polygons:
            self.draw_poly(polygon)

    def draw_poly(self, poly):
        """
        Renders a polygon to the screen

        poly: polygon to draw
        """
        vertices = []
        for tri in poly.world_space:
            for vertex in tri:
                x = vertex[0]  # + poly.x
                y = vertex[1]  # + poly.y
                vertices.append((x, y))
                self.game.draw.circle(self.screen, self.WHITE, (x, y), self.point_size)
        self.draw_lines(vertices)

    def rotate_test(self, poly, alpha):
        rotation_matrix_y = np.array([
            [cos(alpha), 0, sin(alpha), 0],
            [0, 1, 0, 0],
            [-sin(alpha), 0, cos(alpha), 0],
            [0, 0, 0, 1]
        ])
        rotation_matrix_x = np.array([
            [1, 0, 0, 0],
            [0, cos(alpha), -sin(alpha), 0],
            [0, sin(alpha), cos(alpha), 0],
            [0, 0, 0, 1]
        ])
        rotation_matrix_z = np.array([
            [cos(alpha), -sin(alpha), 0, 0],
            [sin(alpha), cos(alpha), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

        new_points = []
        for tri in poly.mesh_space:
            proj_triangle = []
            for i in range(len(tri.points)):
                rotated_point_z = mult_matrix(rotation_matrix_z, tri.points[i])
                proj_triangle.append(rotated_point_z)
                rotated_point_zx = mult_matrix(rotation_matrix_x, proj_triangle[i])
                rotated_point_zx[2] += 2
                proj_triangle[i] = rotated_point_zx

            for i, point in enumerate(proj_triangle):
                projection = mult_matrix(self.projection_matrix, point)
                projection[0] += 1
                projection[1] += 1

                projection[0] *= 0.5 * self.width
                projection[1] *= 0.5 * self.height
                proj_triangle[i] = projection

            new_points.append(proj_triangle)

        poly.update_world(new_points)

    def rotate(self, degree):
        for poly in self.polygons:
            self.rotate_test(poly, degree)

    def move_x(self, step):
        for poly in self.polygons:
            poly.move_x(step)

    def clear_screen(self):
        self.screen.fill(self.BLACK)

    def flip(self, axis):
        for poly in self.polygons:
            poly.flip(axis)

    def update(self):
        for poly in self.polygons:
            poly.update_3d(self.projection_matrix)