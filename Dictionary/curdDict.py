# Syntax

'''
dict = {key : value}
'''

shop_itmes = {
    'rice': 50,
    'flour': 40,
    'milk': 30,
    'oil': 57,

}

print(shop_itmes)

# Add new item

shop_itmes['fish'] = 200
print(shop_itmes)

# Delete item
del shop_itmes['oil']
print(shop_itmes)

# Update
shop_itmes['flour'] = 30
print(shop_itmes)
