# Makes a pie chart of number of times counties are selected randomly.
# Author: Tom Brophy

import numpy as np
import matplotlib.pyplot as plt

possible_counties = ['Tipperary', 'Limerick', 'Clare', 'Kerry', 'Cork']

counties = np.random.choice(
    possible_counties,
    p=[0.1, 0.3, 0.2, 0.12, 0.28],
    size = (100)
)

unique, counts = np.unique(counties, return_counts=True)

plt.bar(unique, counts)

plt.show()