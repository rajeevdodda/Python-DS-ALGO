import collections.abc


def square_root(x):
    if not isinstance(x, (int, float)):
        raise TypeError('x must be numeric')
    if x < 0:
        raise ValueError('x cannot be negative')


try:
    square_root('a')
except TypeError as error:
    print(error)

try:
    square_root(-10)
except ValueError as error:
    print(error)


def sum_of_iterable(values):
    if not isinstance(values, collections.abc.Iterable):
        raise TypeError("parameter must be iterable type")
    total = 0
    for i in values:
        if not isinstance(i, (int, float)):
            raise TypeError("elements must be numeric")
        total += i
    return total


try:
    sum_of_iterable([1, 3, "a"])
except TypeError as error:
    print(error)
    raise Exception("re raise exception")
