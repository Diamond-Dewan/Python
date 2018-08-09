# define a tuple

"""
Two ways to create a tuple
    
    1. With parentheses ()
    
    2. Without parentheses 

Note: tuple are immutable. That means once a tuple is created its items can't be changed

"""

tup = 1, 34, 'Hello', 2.23, 5, True

tupl = (23.23, 34, 'Hi', False, 0)

# print(type(tup))
# print(type(tupl))

# Access tuple
print(tup[0], tup[2], tup[5])

# Iteration

for t in tup:
    print(t, end=' ')
