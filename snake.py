from curses import KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT

class Snake(object):
    def __init__(self, window):
        self.position = [[2,1], [2,2], [2,3], [2,4]]
        self.head = self.position[len(self.position) -1]
        self.window = window
        self.is_eating = False
        self.direction = KEY_RIGHT

    def display(self):
        for line,column in self.position:
            self.window.addstr(line, column, 's')

    def move(self, direction):
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

        self.head = self.position[len(self.position) -1]

    def automove(self, position):
        if not self.is_eating:
            self.position.pop(0)

        self.is_eating = False
        self.position.append(position)
        self.head = self.position[len(self.position) -1]

    def eat(self, apple, grid):
        self.is_eating = True
        apple.random(grid)

    def reset(self):
        self.__init__(self.window)
