"""
set package

This package contains the core logic for the Set card game, including:
- `Card`: Defines the structure of a single Set card.
- `Deck`: Manages the deck of 81 unique cards and handles drawing.
- `set_checker`: Contains logic to check if three selected cards form a valid set.

Modules:
- card.py: Represents an individual Set card.
- deck.py: Implements the deck and drawing mechanism.
- set_checker.py: Implements the rules for determining a valid set.

Usage:
    from set.card import Card
    from set.deck import Deck
    from set.set_checker import is_set
"""

from .card import Card
from .deck import Deck
from .set_checker import is_set
