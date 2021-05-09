#! /usr/bin/env python3

import pygame
from pygame.locals import *

SCREEN_WIDTH = 200
SCREEN_HEIGHT = 200
BOX_SIZE = 20
BOX_N = SCREEN_HEIGHT * SCREEN_HEIGHT / BOX_SIZE ** 2
white = [255, 255, 255]
red = [255, 0, 0]
black = [0, 0, 0]


class box:
    def __init__(self, px, py, state = 0):
        self.px = px
        self.py = py
        self.state = state
        self.future = 0

    def update_state(self):
        self.state = self.future
        self.future = 0

def draw_table(screen):
    i = 1
    while i < SCREEN_HEIGHT:
        i += BOX_SIZE
        pygame.draw.line(screen, white, (0, i), (SCREEN_WIDTH, i))
    i = 1
    while i < SCREEN_WIDTH:
        i += BOX_SIZE
        pygame.draw.line(screen, white, (i, 0), (i, SCREEN_HEIGHT))


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Amo a ve")

    screen.fill(black)
    draw_table(screen)
    pygame.display.flip()
    print(BOX_N)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                exit()

if __name__ == "__main__":
    main()
