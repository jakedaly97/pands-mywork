# labs8.1.py
# Author: Jake Dalyu
# List of salries

import numpy as np

np.random.seed(1)
# it is a good idea to have your absolute values set into variables at the beginning of your program

minSalary= 20000
maxSalary = 80000
numberOfEntries = 10

salaries = np.random.randint(minSalary, maxSalary,numberOfEntries)

salaries_mult = salaries * 1.05

newSalaries = salaries_mult.astype(int)

print(newSalaries)