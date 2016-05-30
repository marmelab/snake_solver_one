from random import choice

class Apple(object):
    def __init__(self, window):
        self.position = [2, 35]
        self.window = window

    def display(self):
        line, column = self.position
        self.window.addstr(line, column, 'a')

    def random(self, grid):
        nodes = []
        for line in range(grid.height):
            for column in range(grid.width):
                if grid.grid[line][column] != 1:
                    nodes.append([line, column])
        self.position = choice(nodes)

    def reset(self):
        self.__init__(self.window)
