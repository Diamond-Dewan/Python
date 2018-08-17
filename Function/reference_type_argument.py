# Reference type argument
# List & Dictionary

user = {
    "name": 'Diamond Dewan',
    "user_id": 1,
    "admin_access": True,
    "email": 'diamond@mail.com'
}

print('Main dict: {d}'.format(d=user))

# modify dict


def update_user(user_dict):
    user_dict['admin_access'] = False
    print('Updated dict: {d}'.format(d=user_dict))


update_user(user)
print('Main dict: {d}'.format(d=user))
