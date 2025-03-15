from set_game.deck import Deck
from set_game.set_checker import is_set

def play_set():
    """
    Runs the Set game, drawing three cards at a time until a valid set is found or the deck is empty.

    The game proceeds as follows:
      - A shuffled deck of 81 unique cards is created.
      - Three cards are drawn at a time.
      - The drawn cards are checked to determine whether they form a valid set.
      - If a valid set is found, the game stops and returns the set.
      - If the drawn cards do not form a set, three new cards are drawn.
      - The game continues until a valid set is found or the deck is empty.

    Time Complexity: O(1) per iteration (since the deck has a fixed maximum of 81 cards)
    Space Complexity: O(1) (small fixed storage for selected cards)

    Returns:
    - List[Card] | None: The valid set of three cards if found, otherwise None.
    """
    deck = Deck()  # Initialize and shuffle the deck

    while len(deck) >= 3:  # Ensure there are enough cards to draw
        cards = [deck.draw() for _ in range(3)]  # Draw three cards
        print(f"Drawn cards: {', '.join(map(str, cards))}")  # Cleaner print format

        if is_set(cards):  # Check if the drawn cards form a valid set
            print("\nFound a valid set! :)")
            return cards  # Return the valid set
        else:
            print("Not a set, drawing again...")  # Continue drawing

    print("\nDeck is empty, no valid set found :(")  # No more possible sets
    return None  # No valid set was found

if __name__ == "__main__":
    """
    Entry point for the script. 
    
    - Initializes the deck.
    - Repeatedly draws three cards.
    - Checks if they form a valid set.
    - Stops when a set is found or the deck is empty.
    """
    play_set()  # Start the game