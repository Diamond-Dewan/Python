'''
Python supports Value type & Reference type arguments
'''

# value type
num = 10


def square(num):
    num = num * num
    print("Inside function: {n}".format(n=num))


square(num)
print("Outer: {n}".format(n=num))
