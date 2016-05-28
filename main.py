#!/usr/bin/env python

import curses
from snake import Snake
from apple import Apple
# from astar import astar
from grid import Grid

WIDTH = 50
HEIGHT = 10
MAX_WIDTH = WIDTH - 2
MAX_HEIGHT = HEIGHT - 2
SPEED = 100

# Initialization
curses.initscr()
window = curses.newwin(HEIGHT, WIDTH, 0, 0)
window.timeout(SPEED)
window.keypad(1)
curses.curs_set(0)

snake = Snake(window)
apple = Apple(window)

def reset():
    apple.reset()
    snake.reset()

while True:
    window.clear()
    window.border(0)
    window.addstr(0, 18, 'Snake Solver')
    window.addstr(HEIGHT - 1, 5, '(Q)uit, (R)eset')

    apple.display()
    snake.display()

    grid = Grid(WIDTH, HEIGHT, snake)

    # Snake eat apple
    if snake.head == apple.position:
        snake.eat(apple)

    # A* Algorithm
    # next_position = astar(snake.head, apple.position, grid)
    # snake.move(next_position)

    # (R)eset
    key = window.getch()
    if key == 114 or key == 82:
        reset()

    # (Q)uit
    if key == 113 or key == 81:
        break

curses.endwin()
