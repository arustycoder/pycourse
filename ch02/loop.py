for num in [1,2,3,4,5]:
    print(num)

num = 5
while num > 0:
    print(num)
    num = num - 1

print("range")
for num in range(5):
    print(num)

for num in range(1,10):
    i = 1
    while i<=num:
        print (i,"x",num, "=", i*num, end="\t")
        i = i + 1
    print()

for letter in "I love playing MineCraft!":
    if letter == "l":
        print("l found")
