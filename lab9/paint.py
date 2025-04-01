import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 15
    mode = 'blue'
    points = []
    drawing = False
    erasing = False
    shape = 'circle'

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_e:
                    erasing = True
                elif event.key == pygame.K_c:
                    shape = 'circle'
                elif event.key == pygame.K_v:
                    shape = 'rectangle'
                elif event.key == pygame.K_s:
                    shape = 'square'
                elif event.key == pygame.K_t:
                    shape = 'right_triangle'
                elif event.key == pygame.K_q:
                    shape = 'equilateral_triangle'
                elif event.key == pygame.K_h:
                    shape = 'rhombus'
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_e:
                    erasing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    drawing = True
                elif event.button == 3:
                    radius = max(1, radius - 1)
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drawing = False
            if event.type == pygame.MOUSEMOTION and drawing:
                points.append((event.pos, erasing, shape))

        screen.fill((0, 0, 0))
        for pos, erase, shape in points:
            color = (0, 0, 0) if erase else get_color(mode)
            if shape == 'circle':
                pygame.draw.circle(screen, color, pos, radius)
            elif shape == 'rectangle':
                pygame.draw.rect(screen, color, (pos[0] - radius, pos[1] - radius, radius * 2, radius * 2))
            elif shape == 'square':
                pygame.draw.rect(screen, color, (pos[0] - radius, pos[1] - radius, radius * 2, radius * 2))
            elif shape == 'right_triangle':
                draw_right_triangle(screen, color, pos, radius)
            elif shape == 'equilateral_triangle':
                draw_equilateral_triangle(screen, color, pos, radius)
            elif shape == 'rhombus':
                draw_rhombus(screen, color, pos, radius)

        pygame.display.flip()
        clock.tick(60)

def get_color(mode):
    colors = {'blue': (0, 0, 255), 'red': (255, 0, 0), 'green': (0, 255, 0)}
    return colors.get(mode, (255, 255, 255))

# Draw a right triangle
def draw_right_triangle(screen, color, pos, size):
    points = [
        (pos[0], pos[1] - size),
        (pos[0] - size, pos[1] + size),
        (pos[0] + size, pos[1] + size)
    ]
    pygame.draw.polygon(screen, color, points)

# Draw an equilateral triangle
def draw_equilateral_triangle(screen, color, pos, size):
    height = math.sqrt(3) * size / 2
    points = [
        (pos[0], pos[1] - height),
        (pos[0] - size, pos[1] + height),
        (pos[0] + size, pos[1] + height)
    ]
    pygame.draw.polygon(screen, color, points)

# Draw a rhombus
def draw_rhombus(screen, color, pos, size):
    points = [
        (pos[0], pos[1] - size),
        (pos[0] - size, pos[1]),
        (pos[0], pos[1] + size),
        (pos[0] + size, pos[1])
    ]
    pygame.draw.polygon(screen, color, points)

main()
