# lab6.7functions.py
# Author: Jake Daly
# function that prints out a menu of commands we can perform.

def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q): ").strip()
    return choice

def readModules():
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit): ").strip()

    while moduleName != "":
        module = {}
        module["name"] = moduleName
        # No error handling here for simplicity, you might want to add it
        module["grade"] = int(input("\t\tEnter grade: "))
        modules.append(module)
        # Now read the next module name
        moduleName = input("\tEnter next module name (blank to quit): ").strip()

    return modules

def displayModules(modules):
    print("\tName \tGrade")
    for module in modules:
        print(f"\t{module['name']} \t{module['grade']}")

def doAdd(students):
    currentStudent = {}
    currentStudent["name"] = input("Enter name: ")
    currentStudent["modules"] = readModules()
  
    students.append(currentStudent)

def doView(students):
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"])

# Main program
students = []  # Initialize the list of students
choice = displayMenu()
while choice != 'q':
    if choice == 'a':
        doAdd(students)
    elif choice == 'v':
        doView(students)
    elif choice != 'q':
        print("\n\nPlease select either 'a', 'v', or 'q'")
    choice = displayMenu()