import unittest
from set_game.card import Card
from set_game.set_checker import is_set

class TestSetGame(unittest.TestCase):
    """
    Unit tests for the Set game logic.

    This test suite verifies the correctness of the is_set function
    by checking different combinations of three cards.
    """

    def test_valid_sets(self):
        """
        Test cases for valid sets where all attributes are either the same or different.
        """
        valid_cases = [
            ([Card(2, "oval", "striped", "green"),
              Card(2, "oval", "striped", "green"),
              Card(2, "oval", "striped", "green")], True),
            ([Card(1, "diamond", "solid", "red"),
              Card(2, "squiggle", "striped", "green"),
              Card(3, "oval", "open", "purple")], True)
        ]
        for cards, expected in valid_cases:
            with self.subTest(cards=cards):
                self.assertEqual(is_set(cards), expected)

    def test_invalid_sets(self):
        """
        Test cases for invalid sets where attributes do not meet the Set game criteria.
        """
        invalid_cases = [
            ([Card(1, "diamond", "solid", "red"),
              Card(1, "oval", "striped", "red"),
              Card(3, "diamond", "solid", "red")], False),
            ([Card(1, "diamond", "solid", "red"),
              Card(1, "diamond", "solid", "green"),
              Card(1, "diamond", "striped", "red")], False)
        ]
        for cards, expected in invalid_cases:
            with self.subTest(cards=cards):
                self.assertEqual(is_set(cards), expected)

    def test_invalid_card_count(self):
        """
        Test cases where the number of cards is not exactly three.
        """
        invalid_counts = [
            ([Card(1, "diamond", "solid", "red"), Card(2, "oval", "striped", "green")], False),
            ([Card(1, "diamond", "solid", "red"),
              Card(2, "oval", "striped", "green"),
              Card(3, "squiggle", "open", "purple"),
              Card(2, "diamond", "solid", "red")], False)
        ]
        for cards, expected in invalid_counts:
            with self.subTest(cards=cards):
                self.assertEqual(is_set(cards), expected)

if __name__ == "__main__":
    unittest.main()