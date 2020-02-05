# first-class objects are instances of a type that can be assigned to an identifier, passed as a parameter,
# or returned by a function.

scream = print  # assign name ’scream’ to the function denoted as ’print’
scream("hello world")  # call that function

from math import pi, sqrt

print(vars())

# pseudo random number generation

import random

print(random.random())
