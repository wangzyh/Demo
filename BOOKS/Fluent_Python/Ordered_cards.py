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

# 前三张牌
print(deck[:3])

# 只看A 第12张 每13个
print(deck[12::13])

# 实现了 __getitem__ 方法，这一摞牌就变成可迭代的了
for card in deck:
    print(card)
# 反向迭代
for card in reversed(deck):
    print(card)

# in 方法
print(Card('Q', 'hearts') in deck)
print(Card('7', 'beasts') in deck)

# 排序 ： 用点数来判定扑克牌的大小，2 最小、A 最大；同时还要加上对花色的判定，黑桃最大、红桃次之、方块再次、梅花最小
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):
    print(card)

