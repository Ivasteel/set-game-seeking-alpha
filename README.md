# 🃏 Set Game - Python Implementation

A Python implementation of the **Set** card game, where the program:
- **Draws three unique cards** from a deck of 81 unique cards.
- **Checks if the cards form a valid set** based on the game rules.
- **Repeats the process until a set is found** or the deck is empty.

---

## 📖 Table of Contents
- [📌 How to Play](#-how-to-play)
- [🛠️ Installation & Setup](#️-installation--setup)
- [🚀 Running the Game](#-running-the-game)
- [🎯 Game Rules](#-game-rules)
- [✅ Running Tests](#-running-tests)
- [📌 Author](#-author)
- [📜 License](#-license)

---

## 📌 How to Play
1. The program **shuffles the deck** and starts drawing three cards.
2. It checks if the drawn cards **form a valid set** based on the game rules.
3. If a valid set is found, the game **stops and displays the set**.
4. If not, it **continues drawing new cards** until the deck is empty.

---

## 🛠️ Installation & Setup

### 🔹 Prerequisites
- Python **3.8+** installed on your system.

### 🔹 Clone the Repository
```bash
git clone https://github.com/ivasteel/set-game-python.git
cd set-game-python

### 🔹 Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 🔹 Install Dependencies
```bash
pip install -r requirements.txt
```

### 🚀 Running the Game
To start the game, run:
```bash
python -m set_game.game
```

### 🏗️ Project Structure
```bash
set_game_project/
│── set_game/
│   ├── __init__.py       # Marks this as a package
│   ├── card.py           # Defines the Card class
│   ├── deck.py           # Manages the Deck of cards
│   ├── set_checker.py    # Validates if a set is correct
│   ├── game.py           # Runs the game logic
│── set_tests/            # Unit tests for the game logic
│   ├── test_set.py        # Unit tests for the game logic
│── set_ui/               # Future UI implementation
│   ├── __init__.py       # Placeholder for UI components
│── .gitignore            # Ignore unnecessary files
│── requirements.txt      # Python dependencies (if needed)
│── README.md             # Documentation
```

### 🎯 Game Rules

A **Set** consists of **three cards** that satisfy **all** of the following conditions:

1. They **all have the same number** or **all have different numbers**.
2. They **all have the same shape** or **all have different shapes**.
3. They **all have the same shading** or **all have different shadings**.
4. They **all have the same color** or **all have different colors**.

Example of a **valid set**:
```python
Card(1, "diamond", "solid", "red")
Card(2, "diamond", "solid", "red")
Card(3, "diamond", "solid", "red")
```
All cards share the **same shape, shading, and color** but have **different numbers**, making them a **valid set**.

### ✅ Running Tests

To run unit tests, execute:
```bash
pytest set_tests/
```
or
```bash
python -m pytest set_tests/
```

### 📌 Author

* Vasyl Ivchyk – Lead Data Engineer & AI Enthusiast
* 💼 LinkedIn: [Vasyl Ivchyk](https://www.linkedin.com/in/vasyl-ivchyk-1a0b1358/)
* 📧 Email: [ivasteel@gmail.com]()

### 📜 License

This project is **MIT Licensed** – feel free to use and modify it! :)
