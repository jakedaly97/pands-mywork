# plottask.py
# Author: Jake Daly
# Histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
# and a plot of the function  h(x)=x^3 in the range 0 to 10, on the one set of axes.

import numpy
import matplotlib.pyplot as plt
# importing the numpy and matplotlib.pyplot modules

x = numpy.random.normal(5.0, 2.0, 1000) # mean value = 5.0, standard deviation = 2.0, values = 1000

plt.hist(x,100) # histogram of x with 10 bars

xpoints = numpy.array(range(0, 10)) # array of x values from 0 to 9
ypoints = xpoints * xpoints * xpoints # function h(x)=x^3

plt.plot(xpoints, ypoints, color='r', label = "x cubed") # plots function h(x)=x^3
plt.title("Normal distribution") # gives title to plot
plt.xlabel("X axis") # labels x axis
plt.ylabel("Y axis") # labels y axis
plt.legend() # adds a legend to the plot
plt.show() # displays the plot

# Resources
# https://www.w3schools.com/python/python_ml_normal_data_distribution.asp