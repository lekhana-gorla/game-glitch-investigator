# Game Glitch Investigator

## Project Overview

This project is a Python Number Guessing Game created to practice debugging AI-generated code. The game allows the player to guess a random number between 1 and 10, provides hints, tracks the score, validates user input, and includes automated tests using pytest.

## Features

- Random number generation
- Score tracking
- Input validation
- Helpful hints
- Error handling
- Automated testing with pytest

## How to Run

Open a terminal and run:

```bash
py game.py
```

## Running the Tests

```bash
py -m pytest -v
```

Expected output:

```
7 passed
```

## Demo Walkthrough

1. Start the game.
2. Guess a number between 1 and 10.
3. Receive hints after incorrect guesses.
4. Win by guessing the correct number or lose after three incorrect attempts.
5. Invalid input is handled without crashing the game.

## Technologies Used

- Python
- pytest
- Visual Studio Code