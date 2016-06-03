#!/usr/bin/env python

import curses
from curses import KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT
from snake import Snake
from apple import Apple
from astar import Astar
from grid import Grid

# Initialization
curses.initscr()
window = curses.newwin(Grid.HEIGHT, Grid.WIDTH, 0, 0)
window.keypad(1)
curses.curs_set(0)

speed = 100
auto = False
snake = Snake()
apple = Apple()

def reset():
    """Reset game"""
    apple.reset()
    snake.reset()

while True:
    window.clear()
    window.border(0)
    window.addstr(0, 18, ' Snake Solver ')
    window.addstr(Grid.HEIGHT - 1, 1, '(Q)uit, (R)eset, (A)uto, (M)anual')
    window.timeout(speed)

    grid = Grid(snake, apple)
    grid.display(window)

    # Snake eat apple
    if snake.head == apple.position:
        snake.eat(apple, grid)

    # A* Algorithm
    if auto:
        path = Astar(tuple(snake.head), tuple(apple.position), grid.grid)
        move = path[0] if path else False

        if not move:
            move = snake.any_possible_move(grid)

        if move:
            snake.automove(move)
        else:
            reset()

    key = window.getch()

    # (M)anual
    if not auto:
        if snake.is_collide():
            reset()

        if key in [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT]:
            snake.move(key)
        else:
            snake.move(snake.last_direction)

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
