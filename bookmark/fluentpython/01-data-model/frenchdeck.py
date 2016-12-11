import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11) + list('JQKA')]
    # better way to creat a string list
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    deck = FrenchDeck()
    print(deck, type(deck))
    print(len(deck))
    print(deck[0], type(deck[0]))
    print(deck[-1], deck[-1].rank, type(deck[-1].rank))

    from random import choice
    print(choice(deck))
    print(choice(deck))
    print(deck[:3])
    
