# Description: A simple hangman game

import random

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

    playing = True
    letters_guessed = ""
    chances = len(word) + 2
    flag = 0

    while chances != 0 and flag == 0:
        chances -= 1

        guess = input("Guess a letter: ")

        # if letter is guessed correctly
        if guess in word:
            letters_guessed += guess

        flag = 1
        for ch in word:
            if ch in letters_guessed:
                print(ch, end=" ")
            else:
                flag = 0
                print("_", end=" ")

    if flag == 1:
        print("\nYou won!")
    elif chances <= 0:
        print("\nYou lost! The word was:", word)
