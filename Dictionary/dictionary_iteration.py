'''
Dictionary iteration is different form
list or tuple iteration.
In dictionary we have *key and *value pair.

If we try to iterate a dictionary like list
with on variable. It returns only the *key items.

'''
shop_itmes = {
    'rice': 50,
    'flour': 40,
    'milk': 30,
    'oil': 57,
    'fish': 210,
}

# iteration using for loop
for key, value in shop_itmes.items():
    print(key, value, sep=' -> ')

print()

# iteration with one variable
for key in shop_itmes:
    print(key)

print()

# dictionary value iteration
for value in shop_itmes.values():
    print(value)

print()

# dictionary key iteration
for key in shop_itmes.keys():
    print(key)
