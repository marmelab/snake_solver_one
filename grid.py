class Grid(object):
    WIDTH = 50
    HEIGHT = 10
    MAX_WIDTH = WIDTH - 2
    MAX_HEIGHT = HEIGHT - 2

    def __init__(self, snake, apple):
        self.snake = snake
        self.apple = apple
        self.grid = []

        # Create grid
        for line in range(self.HEIGHT):
            self.grid.append([])
            for column in range(self.WIDTH):
                if column == 0 or line == 0 or column == self.WIDTH - 1 or line == self.HEIGHT - 1:
                    self.grid[line].append(1)
                else:
                    self.grid[line].append(0)

        # Add snake
        for line, column in snake.position:
            self.grid[line][column] = 1

    def display(self, window):
        line, column = self.apple.position
        window.addstr(line, column, 'a')

        for line, column in self.snake.position:
            window.addstr(line, column, 's')
