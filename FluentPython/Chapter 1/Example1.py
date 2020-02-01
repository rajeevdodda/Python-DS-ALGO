import collections
from random import choice


Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(i) for i in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]
        self._name = "rajeev"

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


beer_card = Card("A", "diamonds")
print(beer_card)


deck = FrenchDeck()
print(len(deck))

# This works only if class has __getitem__ method
print(choice(deck))

# __getitem__ delegates to the [] operator of self._cards, our deck automatically supports slicing.
print(deck[1:10])

# Just by implementing the __getitem__ special method, our deck is also iterable
for card in deck:
    print(card)

for card in reversed(deck):
    print(card)