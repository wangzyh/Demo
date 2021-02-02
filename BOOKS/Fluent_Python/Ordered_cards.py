import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


# beer_card = Card('7', 'diamonds')
# print(beer_card)

deck = FrenchDeck()
print(deck)
print(len(deck))
# 抽取特定的一张纸牌
print(deck[0])
print(deck[-1])
# 随机抽取一张纸牌
from random import choice

print(choice(deck))
