from random import choice

class Apple(object):
    """Apple object"""

    def __init__(self, window):
        """Initialize apple"""
        self.position = [2, 35]
        self.window = window

    def display(self):
        """Display apple on curses window"""
        line, column = self.position
        self.window.addstr(line, column, 'a')

    def random(self, grid):
        """Generate random position of apple"""
        nodes = []
        for line in range(grid.height):
            for column in range(grid.width):
                if grid.grid[line][column] != 1:
                    nodes.append([line, column])
        self.position = choice(nodes)

    def reset(self):
        """Reset position apple"""
        self.__init__(self.window)
