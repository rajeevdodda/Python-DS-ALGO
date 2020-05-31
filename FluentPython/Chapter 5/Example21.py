# Example 5-21. Factorial implemented with reduce and an anonymous function

from functools import reduce


def factorial(n):
    return reduce(lambda a, b: a * b, range(1, n + 1))

print(factorial(10))
