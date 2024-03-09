# lab6.4functions.py
# Author: Jake Daly
# function that prints out a menu of commands we can perform.

students= []
def readModules():
 return []
def doAdd(students):
  currentStudent = {}
  currentStudent["name"]=input("enter name :")
  currentStudent["modules"]= readModules()
  
  students.append(currentStudent)
#test
doAdd(students)
doAdd(students)
print (students)