'''
Sometime we need to perform code on each item in a list
this is called iteration, and it can be accomplished 
with a loop and a counter variable.
'''

# while loop syntex
'''
while(condition):
    statements
    statements
    ..........
    ..........
'''
words = ['Hello', 'world', 'spam', 'eggs', 'good']
counter = 0
max_index = len(words)

while counter < max_index:
    print(words[counter])
    counter = counter + 1
