mix_list = ['Honda', 4.3, False, 23, 23]

# list are mutable

# add items to list
mix_list.append('Audi')
print(mix_list)

mix_list += ['BMW']
print(mix_list)

mix_list.insert(2, 'Suzuki')
print(mix_list)

# deleting items

del mix_list[0]
print(mix_list)

# Using pop() method
lastItem = mix_list.pop()  # it removes last item by default

print("Poped item: " + lastItem)
print(mix_list)

# Using remove() method

mix_list.remove(23)  # first matched value will be removed
print(mix_list)
