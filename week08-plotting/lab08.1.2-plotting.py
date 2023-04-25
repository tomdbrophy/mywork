# Program for learning to plot with matplotlib
# Author: Tom Brophy

import matplotlib.pyplot as plt 
import numpy as np

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints)
plt.show()
