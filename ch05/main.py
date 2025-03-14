#import my_module
from my_module import c_to_f

celsius = float(input("Enter a temperature in Celsius: "))
fahrenheit = c_to_f(celsius)
print("That's", fahrenheit, "degrees Fahrenheit")

