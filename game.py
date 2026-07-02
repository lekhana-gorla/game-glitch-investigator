import random


def calculate_score(score, guess, secret):
    if guess == secret:
        score += 10
    else:
        score -= 2
    return score


def give_hint(secret):
    if secret > 5:
        return "The number is greater than 5."
    return "The number is 5 or less."


def is_valid_guess(guess):
    return 1 <= guess <= 10


def play_game():
    print("🎮 Welcome to the Guessing Game!")

    secret = random.randint(1, 10)
    score = 0
    attempts = 3

    while attempts > 0:
        try:
            guess = int(input("Guess a number (1-10): "))

            if not is_valid_guess(guess):
                print("Please enter a number between 1 and 10.")
                continue

        except ValueError:
            print("Please enter a valid number.")
            continue

        score = calculate_score(score, guess, secret)

        if guess == secret:
            print("🎉 Congratulations! You guessed correctly!")
            print("Final Score:", score)
            return

        attempts -= 1
        print("❌ Incorrect guess.")
        print(give_hint(secret))
        print("Attempts left:", attempts)

    print("\n😢 Game Over!")
    print("The correct number was:", secret)
    print("Final Score:", score)


if __name__ == "__main__":
    play_game()