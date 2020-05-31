# Example 5-26. Using partial to use a two-argument function where a one-argument
# callable is required

from operator import mul
from functools import partial


triple = partial(mul, 3)
print(triple(7))

print(list(map(triple, range(1, 10))))