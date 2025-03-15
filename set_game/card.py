from enum import Enum
from dataclasses import dataclass

class Shape(Enum):
    DIAMOND = "diamond"
    SQUIGGLE = "squiggle"
    OVAL = "oval"

class Shading(Enum):
    SOLID = "solid"
    STRIPED = "striped"
    OPEN = "open"

class Color(Enum):
    RED = "red"
    GREEN = "green"
    PURPLE = "purple"

@dataclass(frozen=True)
class Card:
    """
    Represents a single Set card with four attributes (number, shape, shading, and color).

    Attributes:
        number (int): The number of shapes on the card (1, 2, or 3).
        shape (Shape): The shape type (DIAMOND, SQUIGGLE, or OVAL).
        shading (Shading): The fill type (SOLID, STRIPED, or OPEN).
        color (Color): The color of the shape (RED, GREEN, or PURPLE).

    Example:
        >>> card = Card(3, Shape.DIAMOND, Shading.STRIPED, Color.GREEN)
        >>> print(card)
        Card(3, DIAMOND, STRIPED, GREEN)
    """
    number: int  # 1, 2, or 3
    shape: Shape
    shading: Shading
    color: Color

    def __repr__(self) -> str:
        """
        Returns a string representation of the card.
        """
        return f"Card({self.number}, {self.shape.name}, {self.shading.name}, {self.color.name})"