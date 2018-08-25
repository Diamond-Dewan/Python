# ---|---------------|---
# ---|- Python OOP  -|---
# ---|---------------|---
# ---|    Method     |---
# ---|  Overriding   |---
# ---|---------------|---

'''
note: Python does not support overloading
'''


class Math():   # parent class
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self):
        print("Sum: ", self.x + self.y)


class MathExtended(Math):   # child class
    def __init__(self, x, y):
        super().__init__(x, y)

    # override method
    def sum(self):
        return self.x + self.y


cal = MathExtended(2, 3)
print(cal.sum())
