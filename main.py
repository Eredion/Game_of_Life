#! /usr/bin/env python3

import pygame
import numpy as np
from pygame.locals import *
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
BOX_SIZE = 20
MARGIN = 3
BOX_N = SCREEN_HEIGHT * SCREEN_HEIGHT / BOX_SIZE ** 2

ROWS = 0
COLS = 0
white = [255, 255, 255]
red = [255, 0, 0]
black = [0, 0, 0]


def adjust_screen():
    global SCREEN_HEIGHT, SCREEN_WIDTH, MARGIN, ROWS, COLS
    while ((SCREEN_HEIGHT) % (BOX_SIZE + MARGIN) != 0):
        SCREEN_HEIGHT += 1
    while ((SCREEN_WIDTH) % (BOX_SIZE + MARGIN) != 0):
        SCREEN_WIDTH += 1
    SCREEN_WIDTH += MARGIN
    SCREEN_HEIGHT += MARGIN
    ROWS = int((SCREEN_HEIGHT - MARGIN) / (BOX_SIZE + MARGIN))
    COLS = int((SCREEN_WIDTH - MARGIN) / (BOX_SIZE + MARGIN))


def draw_table2(screen):
    for row in range(int(SCREEN_WIDTH / BOX_SIZE + MARGIN)):
        for column in range(int(SCREEN_HEIGHT / (BOX_SIZE + MARGIN))):
            rect = (MARGIN + BOX_SIZE) * column + MARGIN, (MARGIN +
                                                           BOX_SIZE) * row + MARGIN, BOX_SIZE, BOX_SIZE
            pygame.draw.rect(screen, white, rect)


def draw_table(screen, arr):
    py = MARGIN
    for x in arr:
        px = MARGIN
        for y in x:
            rect = ((px, py), (BOX_SIZE, BOX_SIZE))
            if y == 1:
                pygame.draw.rect(screen, white, rect)
            else:
                pygame.draw.rect(screen, black, rect)
            px += MARGIN + BOX_SIZE
        py += MARGIN + BOX_SIZE

def calc_state(arr):
    #Add border to array
    old = np.pad(arr, pad_width=1, mode='constant', constant_values=0)
    alives = 0
    for y in range (0, COLS):
        for x in range (0, ROWS):
            for i in range(-1,1):
                for j in range(-1,1):
                    if (j == 0 and i == 0):
                        continue
                    alives+=old[y+i][x+j]
            if alives == 3:
                print("entro")
                arr[y][x] = 1
            elif old[y][x] == 1 & (alives != 2 & alives != 3):
                arr[y][x] = 0
            alives = 0
    return arr


def main():
    pygame.init()
    adjust_screen()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Amo a ve")

    arr = np.random.randint(2, size=(int(ROWS), int(COLS)))
    print(str(arr))
    screen.fill(black)
   # draw_table(screen)
    draw_table(screen, arr)
    calc_state(arr)

    while True:
        arr = calc_state(arr)
        draw_table(screen, arr)
        pygame.display.flip()
        time.sleep(1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                exit()


if __name__ == "__main__":
    main()
