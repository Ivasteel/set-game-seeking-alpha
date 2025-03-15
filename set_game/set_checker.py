from typing import List
from .card import Card

def is_set(cards: List[Card]) -> bool:
    """
    Checks if the given three cards form a valid set based on the game's rules.

    A valid set satisfies all four conditions:
      - The three cards have the same or all different numbers.
      - The three cards have the same or all different shapes.
      - The three cards have the same or all different shadings.
      - The three cards have the same or all different colors.

    Time Complexity: O(1)
    Space Complexity: O(1)

    Parameters:
        cards (List[Card]): A list of exactly three `Card` objects.

    Returns:
        bool: True if the three cards form a valid set, False otherwise.
    """
    if len(cards) != 3:
        return False

    attributes = ["number", "shape", "shading", "color"]

    return all(len({getattr(card, attr) for card in cards}) in {1, 3} for attr in attributes)