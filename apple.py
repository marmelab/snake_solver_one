from random import randint

class Apple(object):
    def __init__(self, grid):
        self.position = [2, 8]
        self.grid = grid

    def display(self):
        row, column = self.position
        self.grid.grid[row][column] = 'a'

    def reset(self):
        row = randint(1, self.grid.height - 2)
        column = randint(1, self.grid.width - 2)
        self.position = [row, column]
