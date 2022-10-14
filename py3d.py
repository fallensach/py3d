import pygame
import numpy as np
from math import cos, sin, tan, pi
from rectangle import Rectangle

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
    point_size = 5

    def __init__(self, width, height, pygame, screen):
        self.game = pygame
        self.screen = screen
        self.polygons = []
        self.width = width
        self.height = height
        self.aspect_ratio = height/width
        self.f_fov = 90
        self.fov = 1/tan((pi/2)/2)
        self.z_far = 1000
        self.z_near = 0.1
        self.camera_matrix = np.matrix([
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
        """
        assert width != isinstance(width, float), "Given width is not an integer"
        assert height != isinstance(height, float), "Given height is not an integer"
        assert depth != isinstance(depth, float), "Given depth is not an integer"
        assert pos != isinstance(pos, tuple()), "Given position is not a float tuple"

        self.polygons.append(Rectangle(width, height, depth, pos))

    def connect_triangle(self, t_points):
        self.game.draw.line(self.screen, self.WHITE, (t_points[0][0], t_points[0][1]), (t_points[1][0], t_points[1][1]))
        self.game.draw.line(self.screen, self.WHITE, (t_points[1][0], t_points[1][1]), (t_points[2][0], t_points[2][1]))
        self.game.draw.line(self.screen, self.WHITE, (t_points[2][0], t_points[2][1]), (t_points[0][0], t_points[0][1]))
        #self.game.draw.line(self.screen, self.WHITE, (t_points[2][0], t_points[2][1]), (t_points[0][0], t_points[0][1]))

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
            vertices = []
            for i, point in enumerate(polygon.points_2d):
                #polygon.points_3d[i] = np.dot(self.trans_matrix, point.reshape(4, 1)).reshape(1, 4)
                x = float(point[0][0, 0]) + polygon.x
                y = float(point[1][0, 0]) + polygon.y
                vertices.append((x, y))
                self.game.draw.circle(self.screen, self.WHITE, (x, y), self.point_size)
            self.draw_lines(vertices)

    def rotate(self, axis, degree):
        for poly in self.polygons:
            poly.rotate(axis, degree)

    def move_x(self, step):
        for poly in self.polygons:
            poly.move_x(step)

    def clear_screen(self):
        self.screen.fill(self.BLACK)

    def flip(self, axis):
        for poly in self.polygons:
            poly.flip(axis)

    def update_3d(self):
        for poly in self.polygons:
            poly.update_3d(self.camera_matrix)