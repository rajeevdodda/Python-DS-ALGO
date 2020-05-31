# Example 5-2. Use function through a different name, and pass function as argument


def factorial(n):
    """ returns n!"""
    return 1 if n < 2 else n * factorial(n - 1)


fact = factorial

print(type(fact))

m = map(fact, range(10))
print(m)
print(list(m))
