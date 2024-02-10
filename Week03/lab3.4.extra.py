# lab3.4.extra.py
# Author: Jake Daly
# trying to modify the program lab3.4.randomGenerator.py so that the user inputs the range of number generated

import random

number = random.randint(int(input("Enter first number: ")),int(input("Enter secoond number: ")))
print("here is a random number {}".format(number))