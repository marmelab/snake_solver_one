#!/usr/bin/env python

import curses
from config import WIDTH, HEIGHT
from game import Game

curses.initscr()
window = curses.newwin(HEIGHT, WIDTH, 0, 0)
window.keypad(1)
curses.curs_set(0)

auto = True
speed = 50
game = Game(window)

while True:
    window.erase()
    window.border(0)
    window.addstr(0, 12, ' Snake Solver (score: ' + str(game.score) + ') ')
    window.addstr(HEIGHT - 1, 1, '(Q)uit, (R)eset, (A)uto, (M)anual')
    window.timeout(speed)

    # Draw
    game.display()

    # Keys events
    key = window.getch()

    if auto:
        game.automove()

    if not auto:
        game.move_snake(key)

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
        game.reset()

    # (Q)uit
    if key == 113 or key == 81:
        break

curses.endwin()
