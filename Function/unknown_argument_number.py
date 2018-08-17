'''
If we don't know how many number of arguments 
a function should take we can use this python feature.

'''

'''
single star (*) argument makes a tuple of arguments

double star (**) makes a dictionary of arguments
'''


# Arbitrary number of arguments

def students(*student_name):
    print(student_name, type(student_name), end='\n\n')


# Positional & Arbitrary argument mix

def ship(captain, *crue):
    print('Captain: ', captain, end='\n\n')
    print('Crues: ', crue, end='\n\n')


# Key based Arbitrary argument
def userName(**user):
    print(type(user), end='\n\n')
    print(user, end='\n\n')


students('Bill', 'Jack', 'Stive', 'Jhon', 'Smit')

ship('Drue', 'Will', 'Cj', 'Eile', 'Mipu')

userName(first_user='Bill', second_user='Jack',
         third_user='Stive', fourth_user='Jhone')

# Lets call the function with Empty argument
students()

# call with single argument
students('Biku')
ship('Kloas')
