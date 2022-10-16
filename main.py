import pygame
from py3d import Py3d
import numpy as np
from math import pi

running = True
WIDTH = 1280
HEIGHT = 960
pygame.display.set_caption("Cube")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
py3d = Py3d(WIDTH, HEIGHT, pygame, screen)

clock = pygame.time.Clock()


zoom = 100
move_x = 100

py3d.create_rectangle(1, 1, 1, (WIDTH/2, HEIGHT/2))

#py3d.create_rectangle(10, 10, 20, ((WIDTH/2)+200, HEIGHT/2))


step_3d = 0.02
start = True
degree = 0
while running:
    degree += 0.01
    if start:
        #py3d.update_3d()
        start = False

    clock.tick(60)
    screen.fill((0, 0, 0))
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                py3d.update_3d(py3d.polygons[0])

    if keys[pygame.K_UP]:
        py3d.rotate(py3d.AXIS_Y, step_3d)

    if keys[pygame.K_DOWN]:
        py3d.rotate(py3d.AXIS_Y, -step_3d)

    if keys[pygame.K_LEFT]:
        degree += 0.01

    if keys[pygame.K_RIGHT]:
        py3d.rotate(py3d.AXIS_X, step_3d)

    if keys[pygame.K_w]:
        py3d.rotate(py3d.AXIS_Z, step_3d)

    if keys[pygame.K_s]:
        py3d.rotate(py3d.AXIS_Z, step_3d)

    if keys[pygame.K_a]:
        py3d.move_x(1)

    if keys[pygame.K_d]:

        py3d.move_x(-1)

    py3d.rotate(degree)
    py3d.render_polygons()

    pygame.display.update()