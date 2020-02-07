#  Basic container types, such as list, tuple, and set, qualify as iterable types.
from collections.abc import Iterable

data = [1, 2, 3, 4]
iterable_object = iter(data)
print(type(iterable_object), iterable_object)

for i in iterable_object:
    print(i)
iterable_object2 = iter(data)

try:
    print(next(iterable_object2))
    print(next(iterable_object2))
    print(next(iterable_object2))
    print(next(iterable_object2))
    print(next(iterable_object2))
    print(next(iterable_object2))
except StopIteration as error:
    print(error)

# once used iterable object can be used to get data from it
print(list(iterable_object))  # return empty list

# if the contents of the original list
# are modified after the iterator is constructed, but before the iteration is complete,
# the iterator will be reporting the updated contents of the list
iterable_object3 = iter(data)

# to check if an object is iterable
print(isinstance(iterable_object3, Iterable))

print(next(iterable_object3))
data.append(10)
print(next(iterable_object3))
data.pop(-3)
print(next(iterable_object3))

# returns a range object that is iterable
range_object = range(100)
print(isinstance(range_object, range), isinstance(range_object, Iterable))

sample_dict = {"a": 1,
               "b": 2,
               "c": 2}
# keys(), values(), items() returns iterator object
print(sample_dict.keys(), isinstance(sample_dict.keys(), Iterable), isinstance(sample_dict.keys(), list))
print(sample_dict.values(), isinstance(sample_dict.values(), Iterable), isinstance(sample_dict.values(), list))
print(sample_dict.items(), isinstance(sample_dict.items(), Iterable), isinstance(sample_dict.items(), list))

print(list(range(10)))

print(list(sample_dict.items()), tuple(sample_dict.items()), set(sample_dict.items()))
print(set(sample_dict.values()))