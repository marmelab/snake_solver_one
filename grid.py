class Grid(object):
    def __init__(self, width, height, snake):
        self.width = width
        self.height = height
        self.grid = []

        # Create grid
        for line in range(self.height):
            self.grid.append([])
            for column in range(self.width):
                if column == 0 or line == 0 or column == self.width - 1 or line == self.height - 1:
                    self.grid[line].append(1)
                else:
                    self.grid[line].append(0)

        # Add snake
        for line,column in snake.position:
            self.grid[line][column] = 1
