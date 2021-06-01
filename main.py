#! /usr/bin/env python3

import pygame
import numpy as np
from pygame.locals import *
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
BOX_SIZE = 5
MARGIN = 1
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

def sumNeighbors(M, x ,y):
    l = []
    for i in range(max(0,x-1),x+2): # max(0,x-1), such that no negative values in range()
        for j in range(max(0,y-1),y+2):
            try:
                t = M[i][j]
                l.append(t)
            except IndexError: # if entry doesn't exist
                pass
    return sum(l)-M[x][y] # exclude the entry itself


def calc_state(arr):
    #Add border to array
   # old = np.pad(arr, pad_width=1, mode='constant', constant_values=0)
    old = np.copy(arr)
    alives = 0
    for y in range (0, ROWS):
        for x in range (0, COLS):
            alives = 0
            alives = sumNeighbors(old, y, x)
            if old[y][x] == 0 and alives == 3:
                arr[y][x] = 1
            elif old[y][x] == 1 and(alives >= 2 and alives <= 3):
                arr[y][x] = 1
            else:
                arr[y][x] = 0
    return arr


def main():
    pygame.init()
    adjust_screen()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Amo a ve")

    arr = np.random.randint(2, size=(int(ROWS), int(COLS)))
    # arr = np.zeros((ROWS,COLS), dtype=int)
    # arr[3][3] = 0
    # arr[3][4] = 1
    # arr[4][5] = 1
    # arr[5][3] = 1
    # arr[5][4] = 1
    # arr[5][5] = 1

    screen.fill(black)
   # draw_table(screen)
    draw_table(screen, arr)

    while True:
        arr = calc_state(arr)
        draw_table(screen, arr)
        pygame.display.flip()
        time.sleep(0.1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                exit()


if __name__ == "__main__":
    main()
