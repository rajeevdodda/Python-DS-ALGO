# Example 5-6. Sum of integers up to 99 performed with reduce and sum

from functools import reduce
from operator import add

s = reduce(add, range(100))

print(s)

print(sum(range(100)))

