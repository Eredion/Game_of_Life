#! /usr/bin/env python3

import pygame
from pygame.locals import *

SCREEN_WIDTH = 200
SCREEN_HEIGHT = 200
BOX_SIZE = 20
MARGIN = 5
BOX_N = SCREEN_HEIGHT * SCREEN_HEIGHT / BOX_SIZE ** 2
white = [255, 255, 255]
red = [255, 0, 0]
black = [0, 0, 0]

def draw_table(screen):
    for row in range (int(SCREEN_WIDTH / BOX_SIZE)):
        for column in range (int(SCREEN_HEIGHT / BOX_SIZE)):
            rect = (MARGIN + BOX_SIZE) * (column), (MARGIN + BOX_SIZE) * row, BOX_SIZE, BOX_SIZE
            pygame.draw.rect(screen, white, rect)


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
