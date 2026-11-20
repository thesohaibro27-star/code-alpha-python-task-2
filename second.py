import random

# List of 5 predefined words
words = ["python", "apple", "chair", "robot", "tiger"]

# Pick a random word
word = random.choice(words)

guessed_letters = []   # all letters the player has tried
wrong_guesses = 0
max_wrong = 6

print("Welcome to Hangman!")
print("Guess the word one letter at a time. You can make 6 wrong guesses.")

while wrong_guesses < max_wrong:
    # Build the display string, e.g. "p _ t _ o _"
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Guessed letters:", " ".join(guessed_letters))
    print("Wrong guesses left:", max_wrong - wrong_guesses)

    # Check for a win
    if "_" not in display:
        print("\nCongratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
    elif guess in guessed_letters:
        print("You already guessed that letter.")
    else:
        guessed_letters.append(guess)
        if guess in word:
            print("Good guess!")
        else:
            wrong_guesses += 1
            print("Wrong guess!")
else:
    print("\nGame over! The word was:", word)