# Enter the code here
from random import shuffle
from collections import namedtuple

Card = namedtuple('Card', ['rank', 'suit'])

class Deck:
    ranks = ''.join([str(r) for r in range(2, 11)] + list('JQKA'))
    suits = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self):
        self.cards = List(Card(rank, suit) for suit in self.suits for rank in self.ranks)

    def shuffle(self):
        self.cards.shuffle()

    def deal(self, num_cards):
        return self.cards.pop_many(num_cards)

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = List()

    def draw(self, deck, num_cards):
        self.hand.extend(deck.deal(num_cards))

    def discard(self, num_cards):
        return self.hand.pop_many(num_cards)

class List:
    def __init__(self, items=None):
        self.items = list(items) if items else []

    def is_empty(self):
        return not self.items

    def append(self, item):
        self.items.append(item)

    def extend(self, items):
        self.items.extend(items)

    def pop(self):
        return self.items.pop()

    def pop_many(self, n):
        return [self.items.pop() for _ in range(n)]

    def shuffle(self):
        shuffle(self.items)

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)

    def __str__(self):
        return str(self.items)

# Example usage
deck = Deck()
deck.shuffle()

player1 = Player("Alice")
player2 = Player("Bob")

player1.draw(deck, 5)
player2.draw(deck, 5)

print(f"{player1.name}'s hand: {player1.hand}")
print(f"{player2.name}'s hand: {player2.hand}")

discarded_cards = player1.discard(2) + player2.discard(3)
print(f"Discarded cards: {discarded_cards}")

print(f"{player1.name}'s hand: {player1.hand}")
print(f"{player2.name}'s hand: {player2.hand}")
