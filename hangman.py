import random

def play_hangman():
    # Step 1: Predefined word list
    words = ["python", "intern", "code", "alpha", "project"]

    # Step 2: Choose a random word
    secret_word = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    # Initial display of underscores
    display = ["_" for _ in secret_word]
    print(" ".join(display))

    # Step 3 & 4: Game loop
    while incorrect_guesses < max_incorrect_guesses and "_" in display:
        guess = input("Guess a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        # Step 5: Check guess and update display
        if guess in secret_word:
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    display[i] = guess
            print("Correct! The word is now: " + " ".join(display))
        else:
            incorrect_guesses += 1
            print(f"Incorrect guess. You have {max_incorrect_guesses - incorrect_guesses} guesses left.")

    # Step 6: End game and display result
    if "_" not in display:
        print(f"Congratulations! You guessed the word: {secret_word}")
    else:
        print(f"Game over! The word was: {secret_word}")

# ✅ Run the game
play_hangman()
