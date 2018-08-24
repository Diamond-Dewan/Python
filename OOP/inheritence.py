# ---|---------------|---
# ---|- Python OOP  -|---
# ---|---------------|---
# ---|- Inheritence -|---
# ---|---------------|---


class Math():   # Parent class
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self):
        return self.x + self.y

    def substruct(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y

    def divide(self):
        return self.x / self.y

    def modulo(self):
        return self.x % self.y


class Cal(Math):    # Child class
    def __init__(self, x, y):
        super().__init__(x, y)


'''
Note: Why we dont write like this [ super().__init__(self.x, self.y) ]

** self.x & self.y reffer to class variable.
** Since we didn't create any class variable it is error.

'''

# Create child class Object
obj = Cal(4, 5)
obj2 = Cal(5, 6)

print('Sum: {s}'.format(s=obj.sum()))
print("Substruct: {s}".format(s=obj.substruct()))
print("Divide: {s}". format(s=obj.divide()))
print('Multiply: {s}'.format(s=obj.multiply()))
