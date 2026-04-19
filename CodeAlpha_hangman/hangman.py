import random

# A small collection of words for the game
WORD_LIST = ["python", "guitar", "jungle", "rocket", "bridge"]

HANGMAN_STAGES = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]


def display_word(word, guessed_letters):
    """Show the current state of the word with blanks for unguessed letters."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def play_hangman():
    print("\n" + "="*40)
    print("       Welcome to Hangman!")
    print("="*40)

    word = random.choice(WORD_LIST)
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = 6

    print(f"\nI'm thinking of a word with {len(word)} letters.")
    print("You have 6 chances before the man is hanged!\n")

    while wrong_guesses < max_wrong:
        print(HANGMAN_STAGES[wrong_guesses])
        print(f"Word: {display_word(word, guessed_letters)}")
        print(f"Wrong guesses left: {max_wrong - wrong_guesses}")

        if guessed_letters:
            print(f"Letters guessed: {', '.join(sorted(guessed_letters))}")

        # Check if the player has won
        if all(letter in guessed_letters for letter in word):
            print(f"\n🎉 Congratulations! You guessed the word: '{word}'")
            break

        guess = input("\nEnter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter only.")
            continue

        if guess in guessed_letters:
            print(f"You already tried '{guess}'. Pick a different letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Nice! '{guess}' is in the word.")
        else:
            wrong_guesses += 1
            print(f"Oops! '{guess}' is not in the word.")

    else:
        print(HANGMAN_STAGES[max_wrong])
        print(f"\n💀 Game over! The word was: '{word}'")

    play_again = input("\nWant to play again? (yes/no): ").lower().strip()
    if play_again in ("yes", "y"):
        play_hangman()
    else:
        print("\nThanks for playing! See you next time. 👋\n")


if __name__ == "__main__":
    play_hangman()
