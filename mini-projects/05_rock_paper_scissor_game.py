import random

# Print multiline instruction
print(
    "Winning rules of the game 石头 布 剪刀 are:\n"
    + "石头 vs 布 -> 布 wins \n"
    + "石头 vs 剪刀 -> 石头 wins \n"
    + "布 vs 剪刀 -> 剪刀 wins \n"
)

while True:

    print("Enter your choice \n 1 - 石头 \n 2 - 布 \n 3 - 剪刀 \n")

    # Take the input from user
    choice = int(input("Enter your choice: "))

    # Looping until user enters valid input
    while choice > 3 or choice < 1:
        choice = int(input("Enter a valid choice please : "))

    # Initialize value of choice_name variable corresponding to the choice value
    if choice == 1:
        choice_name = "石头"
    elif choice == 2:
        choice_name = "布"
    else:
        choice_name = "剪刀"

    # Print user choice
    print("User choice is:", choice_name)
    print("Now it's Computer's Turn...")

    # Computer chooses randomly any number among 1, 2, and 3
    comp_choice = random.randint(1, 3)

    # Initialize value of comp_choice_name variable corresponding to the choice value
    if comp_choice == 1:
        comp_choice_name = "石头"
    elif comp_choice == 2:
        comp_choice_name = "布"
    else:
        comp_choice_name = "剪刀"

    print("Computer choice is:", comp_choice_name)
    print(choice_name, "vs", comp_choice_name)

    # Determine the winner
    if choice == comp_choice:
        result = "DRAW"
    elif (choice == 1 and comp_choice == 2) or (comp_choice == 1 and choice == 2):
        result = "布"
    elif (choice == 1 and comp_choice == 3) or (comp_choice == 1 and choice == 3):
        result = "石头"
    elif (choice == 2 and comp_choice == 3) or (comp_choice == 2 and choice == 3):
        result = "剪刀"

    # Print the result
    if result == "DRAW":
        print("<== It's a tie! ==>")
    elif result == choice_name:
        print("<== You wins! ==>")
    else:
        print("<== Computer wins! ==>")

    # Ask if the user wants to play again
    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == "n":
        break

# After coming out of the while loop, print thanks for playing
print("Thanks for playing!")
