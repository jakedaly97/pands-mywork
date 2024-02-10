# lab3.2.sub.py
# Author: Jake Daly
# program that read two numbers and subtracts the first one by the second one

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
answer= x-y
print("{} minus {} is {} ".format(x, y, answer))

# if the input we put in for the first or second number is not an integer, the program will give an error, this is because the input needs to be an integer as shown in the code "int()"