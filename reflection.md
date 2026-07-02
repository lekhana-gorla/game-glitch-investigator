# Reflection

## Bugs Identified

1. The game accepted invalid guesses such as 0 and numbers greater than 10.
2. The game did not have a dedicated input validation function.
3. The project initially did not contain automated tests.

## How I Reproduced the Bugs

I ran the game several times and entered invalid inputs such as letters, 0, and numbers greater than 10. This helped identify issues with input validation and gameplay.

## Fixes Applied

- Added an `is_valid_guess()` function.
- Prevented invalid guesses from affecting gameplay.
- Improved error handling for non-numeric input.
- Added automated pytest tests to verify the game logic.

## AI Collaboration

I used ChatGPT to help explain debugging concepts, improve the game logic, generate pytest test cases, and verify my fixes. I tested every AI suggestion before accepting it.

## What I Learned

This project taught me how to debug Python programs, write unit tests using pytest, and verify AI-generated code instead of accepting it without testing.