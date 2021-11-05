import math
money = float(input("Amount of money you have: "))
print("An apple is 20 pesos.")
apple = 20
appletotal = money // apple
appletotal1 = math.floor(appletotal)
total = appletotal * apple
change = money - total
print(f"You can buy {appletotal1} apples and your change is {change:.2f} pesos.")