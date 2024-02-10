# lab3.3.weeklytask.py
# Author: Jake Daly
# program that reads in a 10 character account number,
# outputs the account number with only the last 4 digits showing,
# The first 6 digits replaced are replaced with Xs

account_number = str(input("Please enter your 10 digit account number:"))
censor = "XXXXXX"

print(censor + account_number[6:])
