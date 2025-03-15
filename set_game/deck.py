import random
from itertools import product
from .card import Card, Shape, Shading, Color

class Deck:
    def __init__(self):
        """
        Initializes a deck containing all 81 unique Set cards and shuffles it.
        """
        self.cards = [Card(n, s, sh, c) for n, s, sh, c in product([1, 2, 3], Shape, Shading, Color)]
        self.shuffle()

    def shuffle(self):
        """Shuffles the deck randomly."""
        random.shuffle(self.cards)

    def draw(self):
        """Draws a card from the deck, returning None if empty but logging a warning."""
        if not self.cards:
            print("Warning: Attempted to draw from an empty deck.")
            return None
        return self.cards.pop()

    def __len__(self):
        """Returns the number of remaining cards in the deck."""
        return len(self.cards)