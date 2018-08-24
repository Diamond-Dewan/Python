class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age, sep=' | ')


people_list = []

for x in range(0, 3):
    person = Person("Person "+str(x), 30+x)
    people_list += [person]

for x in people_list:
    x.info()


print(people_list)
