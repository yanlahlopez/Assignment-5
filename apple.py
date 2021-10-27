money = int(input("Amount of money you have: "))
print("An apple is 20 pesos.")
apple = 20
appletotal = money // apple
total = appletotal * apple
change = money - total
print(f"You can buy {appletotal} apples and your change is {change} pesos.")