import random
def guess_word():

    words = ['python', 'java', 'ruby', 'javascript', 'c++']
    word = random.choice(words)

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

        if guess in word:
            guessed_letters.append(guess)
            print("Correct!")
        else:
            attempts -= 1
            print(f"Wrong guess. Attempts left: {attempts}")

    if attempts == 0:
        print("You lost! The word was:", word)

guess_word()