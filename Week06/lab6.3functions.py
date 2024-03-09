# lab6.3functions.py
# Author: Jake Daly
# function that prints out a menu of commands we can perform.

def displayMenu():
  print("What would you like to do?")
  print("\t(a) Add new student")
  print("\t(v) View students")
  print("\t(q) Quit")
  choice = input("Type one letter (a/v/q):").strip()
  return choice

def doAdd():
 # we fill this in later
 print("in adding")
 
def doView():
 # we fill this in later
 print("in viewing")
 
#main program
choice = displayMenu()
while choice != 'q':
    if choice == 'a':
        doAdd()
    elif choice == 'v':
        doView()
    elif choice != 'q':
        print("\n\nPlease select either 'a', 'v', or 'q'")
    choice = displayMenu()