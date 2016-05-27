#!/usr/bin/env python

from os import system
from time import sleep
from grid import Grid
from snake import Snake
from apple import Apple

WIDTH = 20
HEIGHT = 10
SPEED = 1

# Initialization
grid = Grid(WIDTH, HEIGHT)
snake = Snake(grid)
apple = Apple(grid)

while True:
    system('clear')
    grid.reset()

    snake.move('right')
    snake.display()

    if snake.head == apple.position:
        snake.eat(apple)

    apple.display()
    grid.display()

    sleep(SPEED)
