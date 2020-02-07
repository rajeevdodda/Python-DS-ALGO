# Logical Operators ==> and, or, not

# and returns first occurred false
print(1 and 1 and [] and 0)

# or returns first occurred true
print(0 or [] or 1 or 2)

# Equality Operators ==> is, is not, ==, !=
a = 1
b = 1
# is returns true only if id() are equal same pointing to one object
# == checks values of identifiers
print(a is b)  # returns true
print(a == b)  # return true

a = [1]
b = [1]

print(a is b)  # returns false
print(a == b)  # return true

a = (1,)
b = (1,)
print(a is b)  # returns true
print(a == b)  # return true

# Comparision Operators ==> <, >, <=, >= ,

# works normal for numbers
print(1 < 1)  # returns false
print(2 < 3)  # returns true

# works lexicographically for strings
print('ab' < 'aba')  # returns true
print('A' < 'a')  # returns false
print('1' > '02')  # returns True


try:
    print("2" > 3)
except TypeError as error:
    print(error)

