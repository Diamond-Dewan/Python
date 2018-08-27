def sum(x, y):
    return x+y


def sub(x, y):
    return x-y


def divide(x, y):
    return x/y


def multi(x, y):
    return x*y


def modulo(x, y):
    return x % y


class Mathclass:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self):
        return self.x + self.y

    def sub(self):
        return self.x-self.y

    def divide(self):
        return self.x/self.y

    def multi(self):
        return self.x*self.y

    def modulo(self):
        return self.x % self.y
