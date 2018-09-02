'''
We can use "else" with "try & catch"
if "try" section is TRUE "else" section executes.
'''


def divide(x, y):

    try:
        result = x / y

    except Exception as e:
        return 'Error!!', e

    else:
        return result


print(divide(10, 3))
print(divide(23, 0))
print(divide(32, 13))
print(divide('2', '2'))
