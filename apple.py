from random import randint

class Apple(object):
    def __init__(self, window):
        self.position = [2, 35]
        self.window = window

    def display(self):
        line, column = self.position
        self.window.addstr(line, column, 'a')

    def random(self):
        height, width = self.window.getmaxyx()
        line = randint(1, height - 2)
        column = randint(1, width - 2)
        self.position = [line, column]

    def reset(self):
        self.__init__(self.window)
