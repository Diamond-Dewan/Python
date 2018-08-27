# import to use with namespace
from mypack import math
# import to use without namespace
from mypack.math import *

x = int(input('Enter first number: '))
y = int(input('Enter second number: '))

cal = math.Mathclass(x, y)   # Mathclass object

print(cal.sum())    # class method
print(math.sum(x, y))   # function

print(sum(x, y))    # function called without namespace
