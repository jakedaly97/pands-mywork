# lab3.2.convert.py
# Author: Jake Daly
# Program that takes in a float amount of dollars and returns that absolute amount in cent.

number = float(input("Please enter the amount:"))
absoluteValue = abs(number*100)
print('The absolute value of {} is {} cents'.format(number, int(absoluteValue)))

# for the absolute value i multiplied the floating number by 100 which will give the value in cents,
# I made the code print the absoluteValue as an integer so it wouldnt give decimals places for the cents