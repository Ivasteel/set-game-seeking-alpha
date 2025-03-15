from set_game.deck import Deck
from set_game.set_checker import is_set

def play_set():
    """
    Runs the Set game, drawing three cards at a time until a valid set is found or the deck is empty.
    """
    deck = Deck()  # Initialize and shuffle the deck
    print("Starting the game...")

    while len(deck) >= 3:  # Ensure there are enough cards to draw
        cards = [deck.draw() for _ in range(3)]  # Draw three cards
        print(f"Drawn cards: {', '.join(map(str, cards))}")  # Cleaner print format

        if is_set(cards):  # Check if the drawn cards form a valid set
            print("\nFound a valid set! :)")
            return cards  # Exit the function after finding a set

        print("Not a set, drawing again...")

    print("\nDeck is empty, no valid set found :(")  # End of the game
    return None  # Exit when no set is found

if __name__ == "__main__":
    """
    Entry point for the script.
    Runs the game once and exits.
    """
    play_set()  # Start the game
