# -----_______________-----
# -----|-------------|-----
# -----|  Exception  |-----
# -----|_____________|-----
# _____---------------_____


def div(x, y):
    '''
    This function divide two numbers
    '''
    try:
        return x/y
    except Exception as e:
        return e


print(div(4, 2))
print(div(3, '2'))
print(div(32, 0))
print(div(23, 3))
