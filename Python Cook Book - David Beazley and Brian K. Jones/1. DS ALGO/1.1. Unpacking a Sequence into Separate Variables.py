p = 4, 5

# Any sequence (or iterable) can be unpacked into variables using a simple assignment operation.
x, y = p
print(x, y)

# Unpacking actually works with any object that happens to be iterable, not just tuples or
# lists. This includes strings, files, iterators, and generators.

data = ('ACME', 50, 91.1, (2012, 12, 21), 10)

name, shares, price, (a, b, c), _ = data
print(name, a, b, c)

try:
    p, q, r = 4, 5
except ValueError as e:
    print(e)

s = "hello"
a, b, c, *d = s
print(a, b, c, d)

a, b = range(2)
print(a, b)
