# labs8.11.py
# Author: Jake Daly
# Pie chart

import numpy as np
import matplotlib.pyplot as plt
# make the array of occurences
possibleCounties = ['mayo', 'Galway', 'Rosommon', 'DirtyDublin','Donegal']
# pick 100 randomly from possible counties with the frequence set in p
counties = np.random.choice(
possibleCounties ,
p=[0.1, 0.3, 0.2, 0.12, 0.28 ],
size=(100)
)
# right now we need the number of occurences of each county
# this returns a tuple of the unique values and how many times they appear
unique, counts = np.unique(counties, return_counts=True)
# we can now put this into a pie plot
plt.bar(unique, counts)
plt.show()