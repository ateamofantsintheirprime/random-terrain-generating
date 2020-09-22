import pygame
import random

pygame.init()
dimensions = (800,800)
screen = pygame.display.set_mode(dimensions)

blue = (100,100,255)
green = (25,125,25)

def generate_y_values(deviation, start_point, num_points):
    points_list = [None] * (num_points + 1)

    points_list[0] = start_point + random.uniform(-deviation, deviation)

    for i in range(1, len(points_list)):
        points_list[i] = points_list[i-1] + random.uniform(-deviation, deviation)

    return points_list


def generate_coords(y_values):
    step_size = dimensions[0]/(len(y_values)-1)
    points_coords = zip([x*step_size for x in range(len(y_values))],y_values)
    return list(points_coords)


def draw_points(points):
    point_list = [(round(x[0]), round(x[1])) for x in points]
    point_list.append(dimensions)
    point_list.append((0,dimensions[1]))
    pygame.draw.polygon(screen, green, point_list)

point_list = generate_coords(generate_y_values(5, dimensions[1]/2, 150))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                point_list = generate_coords(generate_y_values(5, dimensions[1]/2, 150))

    screen.fill(blue)
    draw_points(point_list)
    pygame.display.update()
