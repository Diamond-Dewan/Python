# 2D List or Matrix

'''
1 2 3 4 5
4 5 6 7 8
1 0 3 8 9
4 8 3 2 1
'''

matrix = [
    [1, 2, 3, 4, 5],
    [4, 5, 6, 7, 8],
    [1, 0, 3, 8, 9],
    [4, 8, 3, 2, 1],
]

for lists in matrix:
    for items in lists:
        print(items, end=' ')
    print()
