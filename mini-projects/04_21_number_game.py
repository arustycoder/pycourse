# Description:
import random


def lose():
    print("\n\nYOU LOSE!")
    print("Better luck next time!")
    exit(0)


def win():
    print("\n\nYOU WIN!")
    print("Congratulations!")
    exit(0)


def check(nums):
    i = 1
    while i < len(nums):
        if nums[i] != nums[i - 1] + 1:
            return False
        i += 1
    return True


def start():
    xyz = []
    last = 0
    while True:
        print("Enter 'F' to take the First chance, Or 'S' for Second.")
        chance = input(">")

        if chance == "F":
            while True:
                if last == 20:
                    lose()
                else:
                    print("\nYour turn.")
                    while True:
                        print("Enter no more than THREE numbers: ")
                        num = input(">")
                        num = num.split(maxsplit=4)
                        if len(num) < 1:
                            print("Enter at least one number.")
                        elif len(num) <= 3:
                            nums = [int(i) for i in num]
                            comp = 4 - len(nums)
                            xyz.extend(nums)
                            break

                    last = xyz[-1]

                    if check(xyz):
                        if last == 21:
                            lose()
                        else:
                            for i in range(comp):
                                last += 1
                                xyz.append(last)
                            print("Order of numbers after Computer's turn is:\n", xyz)
                            last = xyz[-1]
                    else:
                        print("\n You did not input consecutive integers.")
                        lose()

        elif chance == "S":
            last = 0
            while last < 20:
                max_comp = min(4, 21 - last)
                comp = random.choice(range(1, max_comp))
                for i in range(comp):
                    last += 1
                    xyz.append(last)
                print("Order of numbers after Computer's turn is:\n", xyz)
                if xyz[-1] == 20:
                    lose()
                else:
                    print("\nYour turn.")
                    while True:
                        print("Enter no more than THREE numbers: ")
                        num = input(">")
                        num = num.split(maxsplit=4)
                        if len(num) < 1:
                            print("Enter at least one number.")
                        elif len(num) <= 3:
                            nums = [int(i) for i in num]
                            xyz.extend(nums)
                            break

                    if check(xyz):
                        # set last to 20 to break the loop
                        last = min(20, xyz[-1])
                    else:
                        print("\nYou did not input consecutive integers.")
                        lose()
            win()

        else:
            print("Wrong choice. Try again.")


while True:
    print("Welcome to 21 number game!")
    print("Player 2 is computer.")
    print("Ready to play? (yes/no)")
    ans = input(">")
    if ans.lower() == "yes":
        start()
    else:
        print("Input 'yes' to confirm.")
        nex = input(">")
        if nex.lower() == "yes":
            print("Quiting game now...")
            exit(0)
        else:
            print("Continuing...")
