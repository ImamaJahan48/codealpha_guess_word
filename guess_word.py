import random
import requests

def guess_word():
    # Get a list of English words
    response = requests.get("https://raw.githubusercontent.com/dwyl/english-words/master/words.txt")
    words = response.text.splitlines()
    word = random.choice(words).lower()

    guessed_letters = []
    attempts = 6

    print("Welcome to the Guess the Word Game!")
    print("Guess the word letter by letter.")

    while attempts > 0:
        display = ""

        for letter in word:
            if letter in guessed_letters:
                display += letter
            else:
                display += "_"

        print("Word:", display)

        if "_" not in display:
            print("Congratulations! You guessed the word!")
            break

        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            print("Correct!")
        else:
            guessed_letters.append(guess)
            attempts -= 1
            print(f"Wrong guess. Attempts left: {attempts}")

    if attempts == 0:
        print("You lost! The word was:", word)

# Start the game
guess_word()
