# lab4.1.grade_extra2.py
# Author: Jake Daly
# Program that read a students percentage and prints out the grade
# will keep prompting the user until the user eneters -1

while True:
    percentage = float(input("Please enter a percentage (Enter -1 to exit): "))
    
    if percentage == -1:
        break
    
    if percentage < 0 or percentage > 100:
        print("Please enter a number between 0 and 100")
    elif percentage < 40:
        print("Fail")
    elif percentage < 50: 
        print("Pass")
    elif percentage < 60: 
        print("Merit1")
    elif percentage < 70:
        print("Merit2")
    else:
        print("Distinction")