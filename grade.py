import math
# Create a program that will ask for grade percentage
# Display equivalent grade/mark and description
# Grading System
# Grade/Mark    Percentage      Description
# 1.0           97-100          Excellent
# 1.25          94-96           Excellent
# 1.5           91-93           Very Good
# 1.75          88-90           Very Good
# 2.0           85-87           Good
# 2.25          82-84           Good
# 2.50          79-81           Satisfactory
# 2.75          76-78           Satisfactory
# 3.0           75              Passing
# 5.0           65-74           Failure
# Inc.                          Incomplete
# W                             Withdrawn
# D                             Dropped


Percentage = input("Grade Percentage: ")

if Percentage == "Inc.":
    print("Description: Incomplete")
elif Percentage == "W":
    print("Description: Withdrawn")
elif Percentage == "D":
    print("Description: Dropped")
else:
    percentage = int(Percentage)
    if percentage >= 97 and percentage <= 100:
        print("Grade/Mark: 1.0")
        print("Description: Excellent")
    elif percentage >= 94 and percentage <= 96:
        print("Grade/Mark: 1.25")
        print("Description: Excellent")
    elif percentage >= 91 and percentage <= 93:
        print("Grade/Mark: 1.50")
        print("Description: Very Good")
    elif percentage >= 88 and percentage <= 90:
        print("Grade/Mark: 1.75")
        print("Description: Very Good")
    elif percentage >= 85 and percentage <= 87:
        print("Grade/Mark: 2.0")
        print("Description: Good")
    elif percentage >= 82 and percentage <= 84:
        print("Grade/Mark: 2.25")
        print("Description: Good")
    elif percentage >= 79 and percentage <= 81:
        print("Grade/Mark: 2.50")
        print("Description: Satisfactory")
    elif percentage >= 76 and percentage <= 78:
        print("Grade/Mark: 2.75")
        print("Description: Satisfactory")
    elif percentage >= 75 and percentage <= 75:
        print("Grade/Mark: 3.00")
        print("Description: Passing")
    elif percentage >= 65 and percentage <= 74:
        print("Grade/Mark: 5.00")
        print("Description: Failure")
    elif percentage <= 64.9:
        pass