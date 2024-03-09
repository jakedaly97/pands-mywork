# squareroot.py
# Author: Jake Daly
# program that asks the user to input a positive floating number,
# program will then give an estimate of the square root of the inputted number using the Newton Method.

def square_root(number): # this funtion will be the Newton Method fo calculating
    guess = number / 2  # Initial guess, can be any value closer to the actual square root
    
    while True:
        print("Calculating new guess using Newton's Method.")
        new_guess = (guess + (number / guess)) / 2 # this is the newton method for calculating sqaure root
        
        print("The current guess is:", guess)
        
        if abs(new_guess - guess) < 0.000001:  # Check if the difference between the new and old guess is small
            print("Found the square root!", new_guess)
            return new_guess  # Return the square root once it's found
            
        print("New guess is:", new_guess)
        
        # Update guess for the next iteration
        guess = new_guess

number = float(input("Please enter a positive number: "))
print(square_root(number))

# Resources
# https://patrickwalls.github.io/mathematicalpython/root-finding/newton/
# https://www.instructables.com/Python-Programming-calculating-Newtons-Method/