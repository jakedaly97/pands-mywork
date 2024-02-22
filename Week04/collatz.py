# collatz.py
# Author: Jake Daly
# program that asks the user to input a positive integer,
# program will output succesive values of the following calculations,
# at each step calculate the next value by taking the current value and,
# if it is even, divide it by two, but if it is odd, multiply it by three and add one.
# program will end when value is 1

number = int(input("Please enter a positive integer: ")) # prompts user for positive integer, same as in lab 4.1 isEven program
number_end = 1 

while number != number_end: # while statement pretty much the same as lab 4.2 guess program
    if number % 2 == 0: # if statement the same as found in lab 4.1 isEven program
        number = number // 2 # divide number by 2
    else:
        number = number * 3 + 1 # if number is not even the program will multiply by 3 and add 1
        
    print(number)

# I found this weekly task easier than the other ones I have done so far as all the code could
# be found in this weeks (Week 04) lab content.
