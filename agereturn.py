import math

def insert():
    name = input("Name: ")
    age = int(input('Age: '))
    address = input("Address: ")
    return name, age, address
name, age, address=insert()


print(f"Hi, my name is {name}. I am {age} years old and I live in {address}.")