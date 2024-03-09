# lab6.6functions.py
# Author: Jake Daly
# function that prints out a menu of commands we can perform.

def displayModules(modules):
    print("\tName \tGrade")
    for module in modules:
        print(f"\t{module['name']} \t{module['grade']}") 

def doView(students):
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"])
