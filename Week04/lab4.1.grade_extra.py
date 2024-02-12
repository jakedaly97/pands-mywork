# lab4.1.grade_extra.py
# Author: Jake Daly
# Program that read a students percentage and prints out the grade

percentage = float(input("Please enter a percentage: "))

# In practice percentage points are rounded so 69.5 = distinction,
# How would you modify the program to account for this?

if percentage <0 or percentage >100:
    print("Please enter a number between 0 and 100")
elif percentage < 39.5: # I change the grade scores for each grade to account for the rounding.
    print("Fail")
elif percentage < 49.5: 
 print ("Pass")
elif percentage < 59.5: 
 print ("Merit1")
elif percentage < 69.5:
 print ("Merit2")
else: 
 print ("Distinction")