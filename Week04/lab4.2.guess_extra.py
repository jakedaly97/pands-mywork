# lab4.2.guess_extra.py
# Author: Jake Daly
# Program that prompts the user to guess a RANDOM number between 1 and 100,
#then tells the user if they are too high or too low,
# Untill the right answer is guessed

from random import randint

numberToGuess = randint(1,100) # pythonspot.com, producing a random integer between 1 and 100

guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    if guess < numberToGuess:
        print("too low")
        guess = int(input("Please guess again:"))
    else:
        print("too high")
        guess = int(input("Please guess again:"))

print("Well done! Yes the number was ", numberToGuess)