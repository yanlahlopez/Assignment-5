import math
# Create a program that will ask for 3 numbers
# Find lowest number

number1, number2, number3 = map(float,input("Enter three numbers: ").split(" "))

if number1 < number2 and number1 < number3:
    print("{} is the lowest number.".format(number1))
elif (number2 < number3):
    print("{} is the lowest number.".format(number2))
else:
    print("{} is the lowest number.".format(number3))