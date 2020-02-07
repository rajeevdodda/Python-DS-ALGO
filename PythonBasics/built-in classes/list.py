# list, tuple, strings are sequence types
# list is mutable

# list constructor produces empty list by default==> []
new_list = list()
print(new_list)


# list() constructor accepts iterable and produces a new list. Iterables ==> strings, list, tuples, set, dictionaries

# string ==> list
print(list("rajeev"))

# list ==> list
print(list([1, 2, 3]))

# tuple ==> list
print(list((1, 2, 3)))

# set ==> list
print(list({1, 2, 3, 2}))

# dict ==> list --> returns keys of dictionary as tuple
print(list(
    {
        "a": 1,
        "b": 2,
        "c": 3
    }
))

