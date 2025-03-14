import random

name = input("What is your name?")
print(f"Hello, {name}! Welcome to the word guessing game!")

words = [
    "apple",
    "banana",
    "cherry",
    "date",
    "elderberry",
    "fig",
    "grape",
    "honeydew",
    "kiwi",
    "lemon",
    "mango",
    "nectarine",
    "orange",
    "papaya",
    "quince",
    "raspberry",
    "strawberry",
    "tangerine",
    "watermelon",
]

word = random.choice(words)
print("Guess the characters of the word.")

guesses = ""
turns = 12

while turns > 0:
    failed = 0
    for ch in word:
        if ch in guesses:
            print(ch, end=" ")
        else:
            print("_", end=" ")
            failed += 1

    if failed == 0:
        print("\nCongratulations! You win!")
        print("The word is:", word)
        break

    guess = input("\nGuess a character:")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong!")
        print(f"You have {turns} more guesses.")

        if turns == 0:
            print("You lose!")
            print(f"The word is {word}.")
            break
