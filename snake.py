#!/usr/bin/env python

from random import randint
from os import system
from time import sleep

WIDTH = 20
HEIGHT = 10
SPEED = 0.2
grid = []
snake = [[2,1], [2,2], [2,3], [2,4]]
apple = [2, 11]

# Create a 2 dimentional array
def init_grid():
    grid[:] = []
    for row in range(HEIGHT):
        grid.append([])
        for column in range(WIDTH):
            if column == 0 or row == 0 or column == WIDTH - 1 or row == HEIGHT - 1:
                grid[row].append('x')
            else:
                grid[row].append(' ')

def run_snake(event):
    head_row, head_column = snake[len(snake) -1]

    if [head_row, head_column] == apple:
        row = randint(1, HEIGHT - 2)
        column = randint(1, WIDTH - 2)
        apple[:] = [row, column]
    else:
        snake.pop(0)

    if event == 'up':
        snake.append([head_row - 1, head_column])
    elif event == 'down':
        snake.append([head_row + 1, head_column])
    elif event == 'left':
        snake.append([head_row, head_column - 1])
    elif event == 'right':
        snake.append([head_row, head_column + 1])

# Print grid
def print_grid():
    row, column = apple
    grid[row][column] = 'a'
    for row,column in snake:
        grid[row][column] = 's'
    for row in grid:
        print(" ".join(row))

# Initialization
init_grid()
print_grid()

while True:
    system('clear')
    init_grid()
    print_grid()
    run_snake('right')
    sleep(SPEED)
