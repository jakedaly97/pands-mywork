# lab4.2.guess1.py
# Author: Jake Daly
# Program the prompts the user to guess a number till it gets the right one

numberToGuess = 30
guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    print ("Wrong")
    guess = int(input("Please guess again:"))
print ("Well done! Yes the number was ", numberToGuess)