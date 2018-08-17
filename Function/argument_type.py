'''
in function we have two types of arguments
positional and key based arguments

'''


def info(name, phone, address):
    print(name, phone, address)


# positional argument
# in this type argument passing we need to maintain the order
info('Cruw', '013334923', 'New Helsing')

'''
In positional argument passing the order is very important.
Where in key based passing order of arguments does not matter.

'''

# key based argument
info(name='Perly', phone='023432232', address='Waylonge')

# positional & key based mix argument passing
info('Swift', '203288434', address='Boston')

'''
Note: In mix argument passing the **Positional arguments must be passed before **Key based argument
'''
