# Define a list called cars

cars = ['Toyota', 'Honda', 'BMW', 'Audi', 'Lada',
        'Datsun', 'Porsche', 'Mercedes-Benz', 'Volkswagen']

print("Original List: \n\t{cars}".format(cars=cars), end='\n\n')

# Sort the list
# Sort items using sorted() function
''' 
As this is a function, it just return a sorted list.
But it doesn't actually change the object 
'''
print("Sorted List: \n\t{cars}".format(cars=sorted(cars)), end="\n\n")

# print(type(sorted(cars)))

# Sort items using sort() method

cars.sort()
"""
Note: usign this sort() method changes the structure of original object(variable)
"""
print("Sorted List: \n\t{cars}".format(cars=cars), end="\n\n")

# Two way to reverse sort
# One is passing reverse is True as parameter through sort() method

cars.sort(reverse=True)
print("Reversly Sorted List: \n\t{cars}".format(cars=cars), end='\n\n')

# another is the reverse() method
cars.sort()

cars.reverse()
print("Reversly Sorted List: \n\t{cars}".format(cars=cars), end='\n\n')
