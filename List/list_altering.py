'''
list are mutable

which means we can make change  

anything inside a list

'''

# define an empty List
nums = []

print(nums)

# add itmes to the list
'''
The append() method always add items at the end of 
the list.
'''
nums.append(0)
nums.append(1)
nums.append(2)
nums.append(3)
nums.append(4)

print(nums)


# insert() method
'''
* The insert() method is similar to appaend().

* But it alows us to insert new items at any position in the list.

* Note: It does not replace an item it just insert the new item to the index
        though pre
* Syntex:

    list.insert(index, object)

'''

# define a new list here
words = ['I', 'learning', 'Python']

index = 1
obj = 'am'

words.insert(index, obj)

print(words)
