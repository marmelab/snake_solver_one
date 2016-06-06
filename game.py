from config import WIDTH, HEIGHT
from snake import Snake
from apple import Apple
from curses import KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT
from astar import find_path

class Game(object):
    def __init__(self, window):
        self.snake = Snake()
        self.apple = Apple()
        self.window = window
        self.grid = []
        self.score = 0

    def move_snake(self, key):
        """Manual move of snake"""
        if key in [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT]:
            self.snake.move(key)
        else:
            self.snake.move(self.snake.last_direction)

        if self.snake.head == self.apple.position:
            self.snake.eat(self.apple, self.grid)
            self.score += 1

        if self.snake.is_collide():
            self.reset()

    def automove(self):
        """Deplace position of the snake with A* algorithm"""
        path = find_path(tuple(self.snake.head), tuple(self.apple.position), self.grid)
        move = path[0] if path else False

        if not move:
            move = self.any_possible_move()

        if move:
            if not self.snake.is_eating:
                self.snake.position.pop(0)

            self.snake.is_eating = False
            self.snake.position.append(move)
            self.snake.head = self.snake.position[-1]
            self.snake.tail = self.snake.position[0]

        if self.snake.head == self.apple.position:
            self.snake.eat(self.apple, self.grid)
            self.score += 1

        if self.snake.is_collide() or not move:
            self.reset()

    def any_possible_move(self):
        """Return any possible position"""
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i, j in neighbors:
            neighbor = self.snake.head[0] + i, self.snake.head[1] + j
            if self.grid[neighbor[0]][neighbor[1]] == 0:
                return [neighbor[0], neighbor[1]]
        return False

    def display(self):
        """display game"""
        self.grid[:] = []
        for line in range(HEIGHT):
            self.grid.append([])
            for column in range(WIDTH):
                if column == 0 or line == 0 or column == WIDTH - 1 or line == HEIGHT - 1:
                    self.grid[line].append(1)
                else:
                    self.grid[line].append(0)

        for line, column in self.snake.position:
            self.grid[line][column] = 1
            self.window.addstr(line, column, 's')

        line, column = self.apple.position
        self.window.addstr(line, column, 'a')

    def reset(self):
        """Reset game"""
        self.apple.reset()
        self.snake.reset()
        self.score = 0
