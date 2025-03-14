# Description: A simple hangman game using tkinter

import random
import tkinter as tk

from IPython.core.display_functions import update_display

# List of words to guess
words = ["apple", "papaya", "banana", "orange", "mango", "strawberry"]

# Select a random word from the list
word = random.choice(words)
guessed = ["_" for _ in word]


def guess(letter):
    global guessed
    if letter in word:
        update_guessed(letter)
    update_display()


def update_guessed(letter):
    for i, ch in enumerate(word):
        if ch == letter:
            guessed[i] = letter


def update_display():
    label.config(text=" ".join(guessed))
    if "_" not in guessed:
        label.config(text="You won!")


# Create the main window
root = tk.Tk()
root.title("Hangman Game")

# Create a label to display the word to guess
label = tk.Label(root, text=" ".join(guessed), font=("Arial", 24))
label.pack(pady=20)

# Create a frame to hold the buttons
frame = tk.Frame(root)
frame.pack()

# Create buttons for each letter
for ascii_code in range(97, 123):  # ASCII codes for a-z
    letter = chr(ascii_code)
    btn = tk.Button(frame, text=letter.upper(), command=lambda l=letter: guess(l))
    btn.pack(side="left")

# Run the game
root.mainloop()
