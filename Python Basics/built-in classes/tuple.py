# tuple is immutable

# tuple constructor produces empty list by default==> []
new_tuple = tuple()
print(new_tuple)

new_tuple = 17 # this returns a int object
print(type(new_tuple))

# to create a tuple of length, keep a trailing comma
new_tuple = 17,
print(new_tuple, type(new_tuple))


# tuple() constructor accepts iterable and produces a new tuple. Iterables ==> strings, list, tuples, set, dictionaries

# string ==> tuple
print(tuple("rajeev"))

# list ==> tuple
print(tuple([1, 2, 3]))

# tuple ==> tuple
print(tuple((1, 2, 3)))

# set ==> tuple
print(tuple({1, 2, 3, 2}))

# dict ==> tuple --> returns keys of dictionary as tuple
print(tuple(
    {
        "a": 1,
        "b": 2,
        "c": 3
    }
))

