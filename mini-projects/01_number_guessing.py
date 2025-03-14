# Description: A simple number guessing game

import random, math

def chances(start, end):
    return math.ceil(math.log2(end - start + 1))

user_range = input("Input number range:")
[start, end] = user_range.split(sep=",", maxsplit=2)
start, end = int(start), int(end)
answer = random.randint(start, end)
max_chances = chances(start, end)
print(f"You have {max_chances} chances to guess the number.")

tries = 1
while True:
    guess = input(f"Guess the number in [{start}, {end}]:")
    if int(guess) == answer:
        print(f"Congratulations! You got it with {tries} tries!")
        break
    elif tries == max_chances:
        print(f"Sorry, you have used up all the chances. The answer is {answer}.")
        break
    elif int(guess) < answer:
        tries += 1
        print("Too small!")
    else:
        tries += 1
        print("Too large!")

