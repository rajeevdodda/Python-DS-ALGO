# {} creates empty dictionary
new_dict = dict()
print(new_dict)

# the constructor accepts a sequence of key-value pairs as a parameter, at least 2 parameters are required.
print(dict([(1, 2), ('a', 4), [5, 4]]))
print(dict([[1, 2], [2, 4]]))
# keys should be type of immutable
print(dict([((1, 2, 4), 5)]))

try:
    print(dict([[[1, 2], 2]]))
except TypeError as error:
    print(error)
