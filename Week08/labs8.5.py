# labs8.5.py
# Author: Jake Daly
# Plotting

import matplotlib.pyplot as plt

import numpy as np

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints #multiply each entry by itself

plt.plot(xpoints, ypoints)
plt.show()