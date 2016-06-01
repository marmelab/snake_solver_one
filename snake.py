from curses import KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT

neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Snake(object):
    """Snake object"""

    def __init__(self, window):
        """Initialize position of the snake"""
        self.position = [[2, 1], [2, 2], [2, 3], [2, 4]]
        self.head = self.position[-1]
        self.window = window
        self.is_eating = False
        self.direction = KEY_RIGHT

    def display(self):
        """Display snake on curses window"""
        for line, column in self.position:
            self.window.addstr(line, column, 's')

    def move(self, direction):
        """Manual move of snake"""
        self.direction = direction
        head_line, head_column = self.head

        if not self.is_eating:
            self.position.pop(0)

        self.is_eating = False

        if direction == KEY_UP:
            self.position.append([head_line - 1, head_column])
        elif direction == KEY_DOWN:
            self.position.append([head_line + 1, head_column])
        elif direction == KEY_LEFT:
            self.position.append([head_line, head_column - 1])
        elif direction == KEY_RIGHT:
            self.position.append([head_line, head_column + 1])

        self.head = self.position[-1]

    def automove(self, position):
        """Deplace position of the snake with A* algorithm"""
        if not self.is_eating:
            self.position.pop(0)

        self.is_eating = False
        self.position.append(position)
        self.head = self.position[-1]

    def futur_move_is_possible(self, position, grid):
        """Return if futur move is possible"""
        if not position:
            return False

        for i, j in neighbors:
            neighbor = position[0] + i, position[1] + j
            if grid.grid[neighbor[0]][neighbor[1]] == 0:
                return True
        return False

    def any_possible_move(self, grid):
        """Return any possible position"""
        for i, j in neighbors:
            neighbor = self.head[0] + i, self.head[1] + j
            if grid.grid[neighbor[0]][neighbor[1]] == 0 and self.futur_move_is_possible(neighbor, grid):
                return [neighbor[0], neighbor[1]]
        return False

    def eat(self, apple, grid):
        """Snake eat apple and regenerate apple position"""
        self.is_eating = True
        apple.random(grid)

    def reset(self):
        """Reset position of the snake"""
        self.__init__(self.window)
