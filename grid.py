class Grid(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = []

        # Create a 2 dimentional array
        for row in range(self.height):
            self.grid.append([])
            for column in range(self.width):
                if column == 0 or row == 0 or column == self.width - 1 or row == self.height - 1:
                    self.grid[row].append('x')
                else:
                    self.grid[row].append(' ')

    def display(self):
        for row in self.grid:
            print(" ".join(row))

    def reset(self):
        self.__init__(self.width, self.height)
