#! /usr/bin/env python3

import pygame
from pygame.locals import *

SCREEN_WIDTH = 180
SCREEN_HEIGHT = 180
BOX_SIZE = 21
MARGIN = 5
BOX_N = SCREEN_HEIGHT * SCREEN_HEIGHT / BOX_SIZE ** 2
white = [255, 255, 255]
red = [255, 0, 0]
black = [0, 0, 0]

def adjust_screen():
    global SCREEN_HEIGHT, SCREEN_WIDTH, MARGIN
    while ((SCREEN_HEIGHT) % (BOX_SIZE + MARGIN) != 0):
        SCREEN_HEIGHT += 1
    while ((SCREEN_WIDTH) % (BOX_SIZE + MARGIN) != 0):
        SCREEN_WIDTH += 1



def draw_table(screen):
    for row in range (int(SCREEN_WIDTH / BOX_SIZE + MARGIN)):
        for column in range (int(SCREEN_HEIGHT / (BOX_SIZE + MARGIN))):
            rect = (MARGIN + BOX_SIZE) * column + MARGIN, (MARGIN + BOX_SIZE) * row + MARGIN, BOX_SIZE, BOX_SIZE
            pygame.draw.rect(screen, white, rect)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Amo a ve")


    adjust_screen()
    print(f"altura = {SCREEN_HEIGHT}")
    print(f"gordura = {SCREEN_WIDTH}")
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
