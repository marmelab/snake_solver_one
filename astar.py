#!/usr/bin/env python

from math import sqrt

def neighbors(node):
    neighbors = []
    for i, j in [(-1,0), (0,1), (1,0), (0,-1)]:
        if node[0] + i < 5 and node[0] + i >= 0 and node[1] + j < 5 and node[1] + j >= 0:
            neighbors.append([node[0] + i, node[1] + j])
    return neighbors

def h(start, end):
    ya, xa = start
    yb, xb = end
    return sqrt((xb - xa)**2 + (yb - ya)**2)

def astar(start, end, grid):
    open_list = []
    close_list = []
    finalPath = []

    gscore = 0
    hscore = h(start, end)
    fscore = hscore + gscore

grid = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [1,1,1,1,0],
    [0,1,0,0,0],
    [0,0,0,0,0],
]

astar((4,0), (1,1), grid)
