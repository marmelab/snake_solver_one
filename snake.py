#!/usr/bin/env python

WIDTH = 10
HEIGHT = 10
grid = []

# Create a 2 dimentional array
for row in range(WIDTH):
    grid.append([])
    for column in range(HEIGHT):
        if column == 0 or row == 0 or column == HEIGHT - 1 or row == WIDTH - 1:
            grid[row].append('x')
        else:
            grid[row].append(' ')

# Print grid
def print_grid(grid):
    for row in grid:
        print(" ".join(row))

print_grid(grid)
