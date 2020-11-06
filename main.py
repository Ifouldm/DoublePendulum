import math

import pygame

width = 600
height = 600

white = (255, 255, 255)
black = (0, 0, 0)

r1 = 125
r2 = 175
m1 = 10
m2 = 4
a1 = 0
a2 = 0
a1_v = 0
a2_v = 0
g = 1
cx = 0
cy = 0

line_buffer = []

px2 = -1
py2 = -1

pygame.init()
display = pygame.display.set_mode((width, height))


def setup():
    global a1, a2, cx, cy
    a1 = math.pi / 2
    a2 = math.pi / 2
    cx = int(width / 2)
    cy = 200
    display.fill(white)


def translate(x, y):
    return x + cx, y + cy


def draw():
    display.fill(white)
    global a2_v, a1_v, a1, a2, line_buffer, px2, py2
    num1 = -g * (2 * m1 + m2) * math.sin(a1)
    num2 = -m2 * g * math.sin(a1 - 2 * a2)
    num3 = -2 * math.sin(a1 - a2) * m2
    num4 = a2_v * a2_v * r2 + a1_v * a1_v * r1 * math.cos(a1 - a2)
    den = r1 * (2 * m1 + m2 - m2 * math.cos(2 * a1 - 2 * a2))
    a1_a = (num1 + num2 + num3 * num4) / den

    num1 = 2 * math.sin(a1 - a2)
    num2 = a1_v * a1_v * r1 * (m1 + m2)
    num3 = g * (m1 + m2) * math.cos(a1)
    num4 = a2_v * a2_v * r2 * m2 * math.cos(a1 - a2)
    den = r2 * (2 * m1 + m2 - m2 * math.cos(2 * a1 - 2 * a2))
    a2_a = (num1 * (num2 + num3 + num4)) / den

    x1 = int(r1 * math.sin(a1))
    y1 = int(r1 * math.cos(a1))

    x2 = int(x1 + r2 * math.sin(a2))
    y2 = int(y1 + r2 * math.cos(a2))

    pygame.draw.line(display, black, translate(0, 0), translate(x1, y1))
    pygame.draw.circle(display, black, translate(x1, y1), m1)
    pygame.draw.line(display, black, translate(x1, y1), translate(x2, y2))
    pygame.draw.circle(display, black, translate(x2, y2), m2)

    a1_v += a1_a
    a2_v += a2_a
    a1 += a1_v
    a2 += a2_v

    # a1_v *= 0.999
    # a2_v *= 0.999

    line_buffer.append(translate(x2, y2))
    if px2 != -1:
        pygame.draw.lines(display, black, False, line_buffer)

    # buffer.stroke(0)
    # if (frameCount > 1):
    #    buffer.line(px2, py2, x2, y2)

    px2 = x2
    py2 = y2


setup()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    draw()
    pygame.time.wait(20)
    pygame.display.update()
