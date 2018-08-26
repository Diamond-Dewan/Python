'''
we can import a module in many ways
each way works differently

'''

# import the module
import math

'''
In this type of import
we always have to access 
resources inside math module 
using dot( . ) operator

math.sum(3, 4)

'''

# import specific fucntion or class from a module
from math import sum, sub, divide

'''
We can dirctly call these function without any reference

sum(2, 3)
sub(8, 2)
divide(12, 3)

'''
# import all
from math import *
sum(2, 3)
sub(8, 2)
divide(12, 3)

'''
if we need to access all resources 
we can access module just like 
this

'''
sum(2, 3)
sub(8, 2)
divide(12, 3)
