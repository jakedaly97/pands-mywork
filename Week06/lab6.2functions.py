# lab6.2functions.py
# Author: Jake Daly
# function that prints out a menu of commands we can perform.

def displayMenu():
 print("What would you like to do?")
 print("\t(a) Add new student")
 print("\t(v) View students")
 print("\t(q) Quit")
 choice = input("Type one letter (a/v/q):").strip()
 return choice
#test the function
choice = displayMenu()
print(f"you chose { choice }")
