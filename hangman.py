import random

# List of words
words = ["apple", "tiger", "house", "plant", "music"]

# Choose a random word
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("Welcome to Hangman!")

while wrong_guesses < max_wrong:

    # Display current progress
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if player has won
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    # Get player's guess
    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess in word:
        print("✅ Correct!")
    else:
        wrong_guesses += 1
        print("❌ Wrong!")
        print("Remaining chances:", max_wrong - wrong_guesses)

# Lose condition
if wrong_guesses == max_wrong:
    print("\n💀 Game Over!")
    print("The word was:", word)
