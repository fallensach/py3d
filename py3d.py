import pygame
import numpy as np
from math import cos, sin
from rectangle import Rectangle

class Py3d:
    AXIS_Y = 0
    AXIS_X = 1
    AXIS_Z = 2
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    def __init__(self, width, height, pygame, screen):
        self.game = pygame
        self.screen = screen
        self.polygons = []
        self.width = width
        self.height = height

    def create_rectangle(self, width, height, depth, pos):
        self.polygons.append(Rectangle(width, height, depth, pos))

    def draw_line(self, x, y, points):
        self.game.draw.line(self.screen, self.WHITE, (points[x][0], points[x][1]), (points[y][0], points[y][1]))

    def draw_lines(self, points):
        for p in range(4):
            self.draw_line(p, (p+1) % 4, points)
            self.draw_line(p+4, ((p + 1) % 4) + 4, points)
            self.draw_line(p, (p + 4), points)

    def render_polygons(self):
        self.clear_screen()
        for polygon in self.polygons:
            points_to_draw = [n for n in range(len(polygon.points_2d))]
            for i, point in enumerate(polygon.points_2d):
                x = int(point[0][0]) + polygon.x
                y = int(point[1][0]) + polygon.y
                points_to_draw[i] = (x, y)
                self.game.draw.circle(self.screen, self.WHITE, (x, y), 0.1)
            self.draw_lines(points_to_draw)


    def rotate(self, axis, degree):
        for poly in self.polygons:
            poly.rotate(axis, degree)

    def move_x(self, step):
        for poly in self.polygons:
            poly.move_x(step)

    def clear_screen(self):
        self.screen.fill(self.BLACK)