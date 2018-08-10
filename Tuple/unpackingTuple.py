# Unpacking tuple

tup = 5, 2, 12

x, y, z = tup

print(x, y, z, sep=' | ')


# Skiping items

"""
Use Underscore( _ ) to skip an item from unpacking

x, y = tup  >>> this will be an error

Using an UnderScore( _ ) is just a programming trend
which means we are skipping this value.

"""

x, y, _ = tup

print(x, y, sep=" | ")
