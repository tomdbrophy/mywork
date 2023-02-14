# random_generator.py
# prints a random number between 1 and 10
# Author: Tom Brophy

import random

lower = int(input('Enter the lower bound for number range: '))
upper = int(input('Enter the upper bound for number range: '))
number = random.randint(lower,upper)
print('Here is a random number: {}'.format(number))
