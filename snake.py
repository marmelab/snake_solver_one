class Snake(object):
    def __init__(self, window):
        self.position = [[2,1], [2,2], [2,3], [2,4]]
        self.head = self.position[len(self.position) -1]
        self.window = window
        self.is_eating = False

    def display(self):
        for line,column in self.position:
            self.window.addstr(line, column, 's')

    def move(self, position):
        head_line, head_column = self.head
        print(position)

        if not self.is_eating:
            self.position.pop(0)

        self.is_eating = False

        if position == [head_line - 1, head_column]:
            self.position.append([head_line - 1, head_column])
        elif position == [head_line + 1, head_column]:
            self.position.append([head_line + 1, head_column])
        elif position == [head_line, head_column - 1]:
            self.position.append([head_line, head_column - 1])
        elif position == [head_line, head_column + 1]:
            self.position.append([head_line, head_column + 1])

        self.head = self.position[len(self.position) -1]

    def eat(self, apple):
        self.is_eating = True
        apple.random()

    def reset(self):
        self.__init__(self.window)
