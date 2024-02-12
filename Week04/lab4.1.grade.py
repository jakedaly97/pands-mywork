# lab4.1.grade.py
# Author: Jake Daly
# Program that read a students percentage and prints out the grade

percentage = float(input("Please enter a percentage: "))


if percentage <0 or percentage >100:
    print("Please enter a number between 0 and 100")
elif percentage < 40:
    print("Fail")
elif percentage < 50: 
 print ("Pass")
elif percentage < 60: 
 print ("Merit1")
elif percentage < 70:
 print ("Merit2")
else: # the only option left is between 70 and 100
 print ("Distinction")
