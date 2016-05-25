#!/usr/bin/env python

from random import randint
from os import system
from time import sleep

WIDTH = 10
HEIGHT = 10
SPEED = 1
grid = []

# Create a 2 dimentional array
def init_grid():
    grid[:] = []
    for row in range(WIDTH):
        grid.append([])
        for column in range(HEIGHT):
            if column == 0 or row == 0 or column == HEIGHT - 1 or row == WIDTH - 1:
                grid[row].append('x')
            else:
                grid[row].append(' ')

# Init apple
def init_apple():
    x = randint(1, WIDTH - 2)
    y = randint(1, HEIGHT - 2)
    grid[x][y] = 'a'

# Print grid
def print_grid():
    for row in grid:
        print(" ".join(row))

while True:
    system('clear')
    init_grid()
    init_apple()
    print_grid()
    sleep(SPEED)
