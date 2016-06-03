from random import choice

class Apple(object):
    """Apple object"""

    def __init__(self):
        """Initialize apple"""
        self.position = [2, 35]

    def random(self, grid):
        """Generate random position of apple"""
        nodes = []
        for line in range(grid.HEIGHT):
            for column in range(grid.WIDTH):
                if grid.grid[line][column] != 1:
                    nodes.append([line, column])
        self.position = choice(nodes)

    def reset(self):
        """Reset position apple"""
        self.__init__()
