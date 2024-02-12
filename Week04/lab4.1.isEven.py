# lab4.1.isEven.py
# Author: Jake Daly
# Program that asks you to input a number and tells you if it is odd or even

number = int(input("Enter an integer:"))

if(number % 2) == 0:
    print(f"{number} is an even number ")
else:
    print(f"{number} is an odd number")
