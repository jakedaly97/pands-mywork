# lab4.2.guess2.py
# Author: Jake Daly
# Program that prompts the user to guess a number then tells the user if they are too high or too low,
# Untill the right answer is guessed

numberToGuess = 30

guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    if guess < numberToGuess:
        print("too low")
        guess = int(input("Please guess again:"))
    else:
        print("too high")
        guess = int(input("Please guess again:"))

print("Well done! Yes the number was ", numberToGuess)