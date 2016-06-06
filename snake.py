from config import MAX_WIDTH, MAX_HEIGHT
from curses import KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT

class Snake(object):
    """Snake object"""

    reverse_move = {
        KEY_UP: KEY_DOWN,
        KEY_DOWN: KEY_UP,
        KEY_LEFT: KEY_RIGHT,
        KEY_RIGHT: KEY_LEFT,
    }

    def __init__(self):
        """Initialize position of the snake"""
        self.position = [[2, 1], [2, 2]]
        self.head = self.position[-1]
        self.tail = self.position[0]
        self.is_eating = False
        self.last_direction = KEY_RIGHT

    def is_collide(self):
        head_line, head_column = self.head
        if head_line > MAX_HEIGHT or head_line == 0 or head_column > MAX_WIDTH or head_column == 0:
            self.reset()

    def move(self, direction):
        """Manual move of snake"""
        head_line, head_column = self.head

        if direction == self.reverse_move[self.last_direction]:
            direction = self.last_direction

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

        self.last_direction = direction
        self.head = self.position[-1]

    def eat(self, apple, grid):
        """Snake eat apple and regenerate apple position"""
        self.is_eating = True
        apple.random(grid)

    def reset(self):
        """Reset position of the snake"""
        self.__init__()
