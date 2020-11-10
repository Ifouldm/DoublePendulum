import math

import pygame

width = 600
height = 600

white = (255, 255, 255)
blue = (50, 50, 200)
black = (0, 0, 0)

r1 = 100
r2 = 175
m1 = 10
m2 = 10
a1 = 0
a2 = 0
a1_v = 0
a2_v = 0
g = 1
cx = 0
cy = 0

line_buffer = []
toolbar = []

px2 = -1
py2 = -1

pygame.init()
display = pygame.display.set_mode((width, height))


class Button:
    def __init__(self, x, y, w, h, text, colour):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
        self.colour = colour

    def contains(self, pos):
        return self.x < pos[0] < (self.x + self.w) and self.y < pos[1] < (self.y + self.h)

    def show(self):
        pygame.draw.rect(display, self.colour, (self.x, self.y, self.w, self.h), 1)
        text = pygame.font.Font("freesansbold.ttf", 20)
        text.render(self.text, True, black)

class Slider:
    def __init__(self, start_val, x, y, w):
        self.w = w
        self.y = y
        self.x = x
        self.current_val = int(w * start_val)
        self.h = 20

    def contains(self, pos):
        return self.x < pos[0] < (self.x + self.w) and self.y < pos[1] < (self.y + self.h)

    def click(self, pos):
        self.current_val = (pos[0] - self.x) / self.w

    def show(self):
        pygame.draw.rect(display, blue, (self.x, self.y, self.w, self.h), 1)
        pygame.draw.circle(display,
                           blue,
                           (int(self.x + (self.w * self.current_val)),
                                int(self.y + self.h / 2)),
                           int(self.h / 2),
                           1)

def setup():
    global a1, a2, cx, cy
    a1 = math.pi / 2
    a2 = math.pi / 2
    cx = int(width / 2)
    cy = 200
    display.fill(white)
    clear_button = Button(100, 500, 120, 40, "Clear", blue)
    toolbar.append(clear_button)
    slider1 = Slider(0.5, 300, 500, 120)
    toolbar.append(slider1)



def translate(x, y):
    return x + cx, y + cy


def draw():
    display.fill(white)
    global a2_v, a1_v, a1, a2, line_buffer, px2, py2
    for item in toolbar:
        item.show()
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
    pygame.draw.circle(display, blue, translate(x2, y2), m2)

    a1_v += a1_a
    a2_v += a2_a
    a1 += a1_v
    a2 += a2_v

    #a1_v *= 0.999
    #a2_v *= 0.999

    line_buffer.append(translate(x2, y2))
    if px2 != -1:
        pygame.draw.lines(display, blue, False, line_buffer, 2)

    # buffer.stroke(0)
    # if (frameCount > 1):
    #    buffer.line(px2, py2, x2, y2)

    px2 = x2
    py2 = y2


setup()
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if toolbar[0].contains(pygame.mouse.get_pos()):
                line_buffer = [line_buffer[-1]]
            if toolbar[1].contains(pygame.mouse.get_pos()):
                toolbar[1].click(pygame.mouse.get_pos())
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    draw()
    pygame.time.wait(20)
    pygame.display.update()
