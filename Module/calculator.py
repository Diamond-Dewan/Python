'''
if we want to access any resource
of math module we need to import 
this file first.
'''


import math

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

sum = math.sum(x, y)
sub = math.sub(x, y)
divide = math.divide(x, y)
multiply = math.multi(x, y)


print("\nSum: ", sum, "\nSubstruct: ", sub,
      "\nDivide: ", divide, "\nMultiply: ", multiply)
