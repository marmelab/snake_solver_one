#!/usr/bin/env python

import curses
import logging as log
from curses import KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT
from snake import Snake
from apple import Apple
from astar import Astar
from grid import Grid

log.basicConfig(filename='debug.log', level=log.DEBUG)

WIDTH = 50
HEIGHT = 10
MAX_WIDTH = WIDTH - 2
MAX_HEIGHT = HEIGHT - 2
speed = 100
auto = True

# Initialization
curses.initscr()
window = curses.newwin(HEIGHT, WIDTH, 0, 0)
window.keypad(1)
curses.curs_set(0)

snake = Snake(window)
apple = Apple(window)

def reset():
    """Reset game"""
    apple.reset()
    snake.reset()

while True:
    window.clear()
    window.border(0)
    window.addstr(0, 18, 'Snake Solver')
    window.addstr(HEIGHT - 1, 1, '(Q)uit, (R)eset, (A)uto, (M)anual')
    window.timeout(speed)

    apple.display()
    snake.display()

    grid = Grid(WIDTH, HEIGHT, snake)

    # Snake eat apple
    if snake.head == apple.position:
        snake.eat(apple, grid)

    # A* Algorithm
    if auto:
        path = Astar(tuple(snake.head), tuple(apple.position), grid.grid)
        move = path[0] if path else False

        if not move:
            log.debug('test any possible move')
            move = snake.any_possible_move(grid)

        if move:
            snake.automove(move)
        else:
            log.debug('dead')
            reset()

    key = window.getch()

    # (M)anual
    if not auto:
        # If snake out of the window
        head_line, head_column = snake.head
        if head_line > MAX_HEIGHT or head_line == 0 or head_column > MAX_WIDTH or head_column == 0:
            reset()

        if key in [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT]:
            snake.move(key)
        else:
            snake.move(snake.direction)

    # Speed +
    if key == 43:
        speed -= 10

    # Speed -
    if key == 45:
        speed += 10

    # (A)uto
    if key == 65 or key == 97:
        auto = True

    # (M)anuel
    if key == 77 or key == 109:
        auto = False

    # (R)eset
    if key == 114 or key == 82:
        reset()

    # (Q)uit
    if key == 113 or key == 81:
        break

curses.endwin()
