'''
In function we always have to pass 
all the arguments that we defined in the function.

But sometime we don't want to use all the arguments 
supplied by function. 

This situation can be handle using  --Optional argument 
'''

# Example


def name(firstName, lastName, middleName=''):

    fullName = firstName

    if middleName:
        fullName += ' ' + middleName

    fullName += ' ' + lastName

    return fullName


print(name('Diamond', 'Dewan'))
print(name('Diamond', 'Dewan', 'D'))
