# the most convenient technique for creating iterators in Python is through the use of generators.

# all factors of a positive integer using traditional function.

from collections.abc import Iterable


def factors(n):
    results = []
    for k in range(1, n + 1):
        if n % k == 0:
            results.append(k)
    return results


print(factors(100))


# on calling the below function returns iterable object

def factors_generator(n):
    for k in range(1, n + 1):
        if n % k == 0:
            yield k


print(next(factors_generator(100)))
print(next(factors_generator(100)))

factors_generator_iterable_object = factors_generator(100)
print(isinstance(factors_generator_iterable_object, Iterable))  # returns true
print("using object : ", next(factors_generator_iterable_object))
print("using object : ", next(factors_generator_iterable_object))

for factor in factors_generator(100):
    print(factor)


# generator can produce infinite number of values


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fibonacci_object = fibonacci()
print(isinstance(fibonacci_object, Iterable))
for i in range(10):
    print(next(fibonacci_object), end=" ")