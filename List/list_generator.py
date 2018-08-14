'''
In Python it is posible to generate 
a list of sequential numbers.

'''
# range function
'''
The range returns a range object
and we need to convert this to list object
'''
print(type(range(3)))

# range with one argument
print(list(range(10)), end='\n')

# range with two argument
'''
sequence start from first argument
up to the second argument.
'''
print(list(range(5, 10)))

# range with three argument
'''
The third argument determines the 
interval of the sequence.
'''
print(list(range(0, 10, 2)))
