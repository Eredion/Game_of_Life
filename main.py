#! /usr/bin/env python3

import pygame
from pygame.locals import *

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BOX_SIZE = 20
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

def draw_tableable(screen):
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
    drawTable(screen)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

if __name__ == "__main__":
    main()
