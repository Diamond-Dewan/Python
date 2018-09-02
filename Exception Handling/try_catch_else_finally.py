'''
In exception handling the finally clause always executed.
'''


def div(x, y):
    try:
        result = x / y
    except Exception as e:
        print("Error:", e)
    else:
        print('Result: ', result)
    finally:
        print('Finally executed.')


div(32, 0)
div('23', '3')
