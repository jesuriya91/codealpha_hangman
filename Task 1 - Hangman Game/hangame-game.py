import random

# List of predefined words
words = ["python", "computer", "program", "student", "college"]

# Select a random word
word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("=== HANGMAN GAME ===")

while incorrect_guesses < max_attempts:
    # Display current progress
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses left:", max_attempts - incorrect_guesses)

    # Check if word is completely guessed
    if "_" not in display_word:
        print("\nCongratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")
    else:
        print("Wrong guess!")
        incorrect_guesses += 1

# Game over if attempts exhausted
if incorrect_guesses == max_attempts:
    print("\nGame Over!")
    print("The word was:", word