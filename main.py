import pygame
from py3d import Py3d
from math import pi

running = True
WIDTH = 1280
HEIGHT = 960
pygame.display.set_caption("Cube")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
py3d = Py3d(WIDTH, HEIGHT, pygame, screen)

clock = pygame.time.Clock()
degree = 0.01

zoom = 100
move_x = 100

py3d.create_rectangle(100, 50, 20, (WIDTH/2 + 100, HEIGHT/2))
py3d.create_rectangle(100, 50, 20, (WIDTH/2, HEIGHT/2))
py3d.polygons[1].rotate(py3d.AXIS_X, -pi/2)

step_3d = 0.05

while running:
    clock.tick(60)
    screen.fill((0,0,0))
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if keys[pygame.K_UP]:
        py3d.rotate(py3d.AXIS_Y, step_3d)

    if keys[pygame.K_DOWN]:
        py3d.rotate(py3d.AXIS_Y, -step_3d)

    if keys[pygame.K_LEFT]:
        py3d.rotate(py3d.AXIS_X, -step_3d)

    if keys[pygame.K_RIGHT]:
        py3d.rotate(py3d.AXIS_X, step_3d)

    if keys[pygame.K_w]:
        zoom += 0.1

    if keys[pygame.K_s]:
        zoom -= 0.1

    if keys[pygame.K_a]:
        py3d.move_x(1)

    if keys[pygame.K_d]:
        py3d.move_x(-1)

    py3d.render_polygons()
    """
    for i, point in enumerate(rect.points_2d):
        x = int(point[0][0] * zoom) + move_x
        y = int(point[1][0] * zoom) + 200

        projected_points[i] = [x, y]
        pygame.draw.circle(screen, (255,255,255), (x, y), 5)
        i += 1
    """

    pygame.display.update()