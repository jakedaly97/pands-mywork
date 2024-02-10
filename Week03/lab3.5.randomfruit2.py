# lab3.5.randomfruit2.py
# Author: Jake Daly
# This program prints out random fruit

import random
fruits = ('Apple', 'Orange', 'Banana', 'Pear')
# we want a random number between 0 and lenght-1
index = random.randint(0,len(fruits)-1)
fruit = fruits[index]
print("A Random Fruit:{}".format(fruit))