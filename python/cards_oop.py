import random

class Card(object):

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print(f"{self.value} of {self.suit}")

class Deck(object):

    def __init__(self, Joker=False):
        self.suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
        self.cards = []
        self.build(Joker)

    def build(self, joker=False):
        for suit in self.suits:
            self.add_to_deck(suit, 14)
        if joker:
            self.add_to_deck("Joker", 3)

    def add_to_deck(self, suit, r):
        for value in range(1, r):
            self.cards.append(Card(suit, value))

    def show(self):
        for card in self.cards:
            card.show()

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw_card(self):
        return self.cards.pop()

class Player(object):

    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.draw_card())
        return self

    def discard(self):
        # can add additonal logic, can check for a certain suit of value etc.
        return self.hand.pop()

    def show_hand(self):
        for card in self.hand:
            card.show()