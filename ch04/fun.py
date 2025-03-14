#def print_my_address():
#    print("Ethan")
#    print("123 Main Street")
#    print("Xicheng, Beijing")
#    print("China")
#    print()
#
#print_my_address()
#print_my_address()

def print_my_address(name):
    print(name)
    print("123 Main Street")
    print("Xicheng, Beijing")
    print("China")
    print()
print_my_address("Ethan")
print_my_address("Alice")

def calculate_area(length, width):
    area = length * width
    return area

room1 = calculate_area(10, 20)
room2 = calculate_area(20.4, 30.3)
#print(length)
print("room1:", room1, "room2:", room2)

def calculate_tax(price, tax_rate):
    total = price + (price * tax_rate)
    #global my_price
    my_price = 1_000
    print(my_price)
    return total

my_price = float(input("Enter a price: "))

total_price = calculate_tax(my_price, 0.06)
print("price = ", my_price, " Total price = ", total_price)