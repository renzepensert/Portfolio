"""cardgame.py: A program that implements a game of cards."""

__author__ = "Rens Groot"
__studentNumber__ = "13122304"


import random


class Card:

    # initializer
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value


    # description of the card
    def description(self):
        return(f"{self.value} of {self.suit}")


class Deck:

    # initializer
    def __init__(self):

        # hardcoded declarations of suits and values
        self._suits = ['Hearts','Diamonds','Clubs','Spades']
        self._values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

        # create a list to store the deck of cards in
        self._cards = []

        # create cards and add them to the deck of cards
        for i in self._suits:
            for j in self._values:
                makecard = Card(i, j)
                self._cards.append(makecard)


    # description with the number of cards in deck
    def description(self):
        return(f"{len(self._cards)} cards in the deck")


    # randomly shuffle the deck of cards
    def shuffle(self):
        return random.shuffle(self._cards)


    # remove the top card from the deck and return its value
    def deal(self):
        return self._cards.pop(-1)
