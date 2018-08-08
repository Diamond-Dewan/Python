

# Spliting a String into a List

import re

cars = "Toyota, Honda, BMW, Audi, Lada, Datsun, Porsche, Mercedes-Benz, Volkswagen"

car_list = re.split(',', cars)
print(cars)
print(car_list)


# List to String

l = ['love', 'is', 'blind']
print(l)
quote = ' '.join(l)

print(quote)
