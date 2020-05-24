# https://docs.python.org/3/reference/datamodel.html#id8

# 3.1. Objects, values and types
# Every object has an identity, a type and a value. An object’s identity never changes once it has been created;
# you may think of it as the object’s address in memory. The ‘is’ operator compares the identity of two objects;
# the id() function returns an integer representing its identity.

# immutable
a = 1
b = 1
# a and b may or may not refer to the same object with the value "1", depending on the implementation
print("id of a = ", id(a))
print("id of b = ", id(b))

# mutable
c = []
d = []
# c and d are guaranteed to refer to two different, unique, newly created empty lists
print("id of c = ", id(c))
print("id of d = ", id(d))

# 3.2. The standard type hierarchy

# None
# This type has a single value | built-in name = None | Its truth value is false
print(type(None), "id of None = ", id(None))

# NotImplemented
# This type has a single value | built-in name = NotImplemented | Its truth value is true
print(type(NotImplemented), "id of None = ", id(NotImplemented))

# Ellipsis
# This type has a single value | built-in name = Ellipsis | Its truth value is true
print(type(...))

from numbers import Number, Integral
import inspect

print(inspect.getmro(int))
print(inspect.getmro(Integral))