"""

Dictionary data type, which is known as 
'HashMap' in Java.

In python a Dictionary is a collection
of (key, value) pairs & is mutable


"""

# Syntex

'''
dict = {key : value}
'''

# create a Dictionary

dict = {}  # empty dictionary

# assign key & value

dict['firstName'] = "Diamond"
dict['lastName'] = "Dewan"
dict['age'] = 21
dict[0] = 'Default'     # integer key

print(dict['firstName'], dict['lastName'],
      dict['age'], sep=(' '), end=('\n\n'))


# define key & value on create

dic = {
    'name': "Diamond Dewan",
    'roll': "ASH1501063M",
    'session': "2014 - 2015",
    'address': "Maijdee",
}

print(
    " Name: {name} \n Roll: {roll} \n Session: {session} \n Address: {address}\n".format(
        name=dic['name'], roll=dic['roll'], session=dic['session'], address=dic['address'])
)
