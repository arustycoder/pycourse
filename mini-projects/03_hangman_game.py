# Description: A simple hangman game

import random
from collections import Counter

some_words = """apple papaya banana orange mango strawberry pineapple
grapefruit watermelon blueberry raspberry blackberry
kiwi lemon lime peach apricot nectarine"""

some_words = some_words.split(" ")
word = random.choice(some_words)

if __name__ == "__main__":
    print("Welcome to the Hangman Game!")

    for i in word:
        print("_", end=" ")
    print()

    letters_guessed = ""
    chances = len(word) + 2
    flag = 0  # indicates if the player has guessed the word

    try:
        while chances != 0 and flag == 0:
            chances -= 1

            try:
                guess = str(input("\nGuess a letter: "))
            except ValueError:
                print("Please enter only a letter.")
                continue

            if not guess.isalpha():
                print("Invalid input! Please enter a letter.")
                continue
            elif len(guess) != 1:
                print("Invalid input! Please enter a single letter.")
                continue
            elif guess in letters_guessed:
                print("You already guessed this letter.")
                continue

            # if letter is guessed correctly
            if guess in word:
                k = word.count(guess)
                for _ in range(k):
                    letters_guessed += guess

            for ch in word:
                if ch in letters_guessed and (
                    Counter(letters_guessed) != Counter(word)
                ):
                    print(ch, end=" ")
                # check if the word is guessed
                elif Counter(letters_guessed) == Counter(word):
                    print("\nYou won! The word is: ", word)
                    flag = 1
                    break
                else:
                    print("_", end=" ")

        if chances <= 0 and flag == 0:
            print("\nYou lost! The word was:", word)

    except KeyboardInterrupt:
        print("\nBye! See you next time.")
        exit()
