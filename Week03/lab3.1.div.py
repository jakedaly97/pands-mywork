# lab3.1.div.py
# Author: Jake Dal
# Program that reads two numbers and divides the first by the second number

x = int(input("Enter first number: "))
y = int(input("Enter the number you want to divide by: "))
answer = int(x//y) # // gives the int division
remainder = x%y # % gives the remainder
print("{} divided by {} is {} with remainder {}".format( x, y, answer, remainder))