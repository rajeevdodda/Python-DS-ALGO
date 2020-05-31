# Example 5-8 implements a BingoCage class. An instance is built from any iterable, and
# stores an internal list of items, in random order. Calling the instance pops an item.

import random


class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self, *args, **kwargs):
        return self.pick()


bingo = BingoCage(range(3))

print(bingo.pick())
print(bingo())
print(bingo())
print(bingo())

