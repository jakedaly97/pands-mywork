# weekday.py
# Author: Jake Daly
# Program that tells you if the current day of the week is a weekday or weekend

# https://www.w3schools.com/python/python_datetime.asp
# this page was used as a resource for writing this program.

import datetime # datetime module is to work with dates

x = datetime.datetime.now() # variable gives the current date

# The Strftime() function is used to convert date and time objects to their string representation,
# %w = Weekday as a number 0-6, 0 is Sunday,
# x.strftime("%w") is the current day represented as a string.

if x.strftime("%w") in ("6", "0"): # line checks if the current day of the week is found in touple ("6", "0"). i.e Saturday = 6, Sunday = 0
    print("It is the weekend, yay!")
else:
    print("Yes, unfortunately today is a weekday.")
