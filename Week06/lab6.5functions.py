# lab6.5functions.py
# Author: Jake Daly
# function that prints out a menu of commands we can perform.

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
