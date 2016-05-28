#!/usr/bin/env python

import curses
from curses import KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT
from snake import Snake
from apple import Apple

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

    # Snake eat apple
    if snake.head == apple.position:
        snake.eat(apple)

    # If snake out of the window
    head_line, head_column = snake.head
    if head_line > MAX_HEIGHT or head_line == 0 or head_column > MAX_WIDTH or head_column == 0:
        reset()

    # Snake move
    key = window.getch()
    if key in [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT]:
        snake.move(key)
    else:
        snake.move(snake.direction)

    # (R)eset
    if key == 114 or key == 82:
        reset()

    # (Q)uit
    if key == 113 or key == 81:
        break

curses.endwin()
