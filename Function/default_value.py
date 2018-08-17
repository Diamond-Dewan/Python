'''
In a function we can set default value of a parameter.

non-default arguments must define before the arguments with default values

'''


def user_details(name, age, address, country='Bangladesh'):
    print(name, age, country)


# Error function example
'''
def test(name='', age, country = 'Bangladesh')

'''


user_details('Kaey', 32, 'Gweey', country='us')
user_details(age=21, name='Edee', address='Ewrex')
user_details('Sid', 24, 'Dhaka')
