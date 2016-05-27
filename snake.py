class Snake(object):
    def __init__(self, grid):
        self.position = [[2,1], [2,2], [2,3], [2,4]]
        self.head = self.position[len(self.position) -1]
        self.grid = grid
        self.is_eating = False

    def display(self):
        for row,column in self.position:
            self.grid.grid[row][column] = 's'

    def move(self, direction):
        head_row, head_column = self.head

        if not self.is_eating:
            self.position.pop(0)

        self.is_eating = False

        if direction == 'up':
            self.position.append([head_row - 1, head_column])
        elif direction == 'down':
            self.position.append([head_row + 1, head_column])
        elif direction == 'left':
            self.position.append([head_row, head_column - 1])
        elif direction == 'right':
            self.position.append([head_row, head_column + 1])

        self.head = self.position[len(self.position) -1]

    def eat(self, apple):
        self.is_eating = True
        apple.reset()
