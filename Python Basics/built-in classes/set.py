# list, tuple, strings are sequence types
# set is mutable, it can have only immutable types as elements ==> int, float, string, tuple, frozenset

# list constructor produces empty list by default==> []
new_set = set()
print(new_set)

# {} represents empty dictionary not set

# set() constructor accepts iterable and produces a new list. Iterables ==> strings, list, tuples, set, dictionaries

# string ==> list
print(set("rajeev"))

# list ==> set
print(set([1, 2, 3, 3]))

# tuple ==> set
print(set((1, 2, 3, 3)))

# set ==> set
print(set({1, 2, 3, 2}))

# dict ==> set --> returns keys of dictionary as set
print(set(
    {
        "a": 1,
        "b": 2,
        "c": 3
    }
))


try:
    new_set.add([1,2])
except TypeError as error:
    print(error)

try:
    new_set.add({1,2})
except TypeError as error:
    print(error)


try:
    new_set.add({1: 2, 2: 3})
except TypeError as error:
    print(error)

# A set have immutable types as its elements
try:
    new_set.add((1, 2, 2, 3))
except TypeError as error:
    print(error)
print(new_set)